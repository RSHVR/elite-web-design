# Recording — ScreenCaptureKit Master + Camera-Clean URL

Two recording rigs exist. The in-driver `C`-key MediaRecorder capture (getDisplayMedia,
"This Tab" + tab audio → auto-downloaded MP4) is the quick fallback: convenient,
realtime-lossy (~8 Mbps, 30fps, tab resolution). The master rig below is what ships.

## Why window-scoped ScreenCaptureKit

- **Window capture contains no desktop, no dock, no menu bar** — the exact requirement for
  compositing the app over a chosen background later.
- **Alpha channel** (ProRes 4444 / HEVC-with-alpha): the window's rounded corners
  composite cleanly. Disable the window shadow in capture; add a shadow in the edit if
  wanted.
- **System encoder at native Retina resolution** — the window's point size × scale factor.
  Window size = capture size; a full-screen browser window ≈ a 4K-ish master.
- **Tab audio** (the app's sfx) captured via `capturesAudio` and muxed in.
- `showsCursor = false` — the driver draws its own cursor; the OS pointer never appears.

## The recorder (small Swift CLI, compiled with `swiftc`)

Shape: find the target window from `SCShareableContent` (match app name + title substring),
build `SCContentFilter(desktopIndependentWindow:)`, configure
`SCStreamConfiguration` (BGRA, fps 60, `ignoreShadowsSingleWindow`, `capturesAudio`,
48kHz stereo, `showsCursor=false`), stream into an `AVAssetWriter` (.mov; ProRes 4444 for
the alpha master — ~10–12GB per 3 min at 4K60 — or `hevcWithAlpha` @ ~40 Mbps for ~1.5GB),
finalize on SIGINT.

**Gotchas that cost real debugging time:**
1. **TCC**: first run fails until the *terminal app* is granted Screen Recording in System
   Settings → Privacy; the grant requires relaunching the terminal.
2. **`CGS_REQUIRE_INIT` assertion abort**: CLI tools must touch CoreGraphics before any
   SCK call — `_ = CGMainDisplayID()` at the top of main fixes an intermittent crash.
3. **Spaces**: query shareable content with `onScreenWindowsOnly: false` — a browser on
   another Space is invisible to the on-screen-only query, but window capture records it
   fine once found. Prefer on-screen matches; fall back to any-Space.
4. SCK output is **VFR** (frames only when pixels change, ceiling = configured fps).
   Editors handle it; don't panic at a "41fps" readout.
5. **The demo still needs the tab visible**: capture works across Spaces, but the page
   freezes (rAF) if Chrome isn't actually displayed. During a take: browser frontmost on
   the active Space; the terminal running the recorder can sit behind or on another
   display.

**Take workflow**: start recorder → click into the browser → press `R` (clean driver
restart) → let it play through the outro → Ctrl-C the recorder (finalizes the .mov).

## Camera-clean URL

The address bar is in frame, so it must read as production. Chrome cannot fake the bar —
build real infrastructure:

1. `/etc/hosts`: point the display domain at `127.0.0.1`.
2. **Caddy with `tls internal`** serving the frontend on 443 — locally-trusted cert means
   no port, no "Not Secure" chip. One-time: `sudo caddy trust` ("certificate installed in
   macOS keychain" is the success line; the `certutil`/NSS warning only matters for
   Firefox).
3. **Serve the app at the domain ROOT** so the bar reads bare-domain. Path fallback for a
   subdirectory app: rewrite `/` to the app's index, then
   `try_files {path} /<appdir>{path}` so same-directory assets resolve while
   parent-relative ones hit the real root.
4. **Gate the driver on the hostname** (`location.hostname === '<display domain>'` →
   autorun) so no `?demo=1` clutters the bar; everywhere else stays opt-in.

**Choose a domain that is NOT a real deployed property.** A demo rig on
`app.realcompany.com` collides the moment someone needs the real site (this happened).
Prefer reserved-TLD space (`product.demo.test`) unless the owner explicitly wants a real
(but unused) subdomain on camera — and then plan the teardown.

**Teardown checklist** (in order):
1. `sudo caddy untrust` **while Caddy is still running** (it needs the admin API), or
   remove trust directly: `sudo security remove-trusted-cert -d <root.crt>` then
   `sudo security delete-certificate -c "<CA common name>"` (delete-by-`-Z` wants a SHA-1
   hash and no-ops silently on SHA-256 — delete by name).
2. `caddy stop`.
3. Remove the hosts line; flush DNS (`dscacheutil -flushcache; killall -HUP mDNSResponder`).
4. Verify: hosts grep is empty, `security dump-trust-settings -d` has no entry, the real
   domain resolves publicly, and a no-`-k` curl shows the genuine certificate issuer.

## Master hygiene

Verify every take before importing: codec (ProRes 4444 + AAC), resolution, duration
(`mdls` on macOS). Name takes and keep them all — owners compare takes.

# The Edit — Palmier Pro Pipeline

The edit turns a raw window-capture take + generated VO into the shipped video. Palmier
Pro is MCP-driven, so the whole assembly is scriptable — but the OWNER edits too, in
parallel, in the same project. Re-read the timeline before every mutation batch; it will
have changed under you (real occurrence: a split failed because the owner had already
re-cut the clip; the muted track and trimmed music were theirs too). Their changes are
signal, not interference — read them (see pacing-canon.md).

## Project assembly

- **Import**: `import_media` takes a whole directory in one call (mirrors folder
  structure) — generate VO into a local folder, import the folder. Takes go in a `Takes`
  media folder, named per take.
- **Track discipline**: never place onto the owner's tracks. Auto-created tracks for the
  take (video + its linked audio) and a dedicated track for VO. Background image on a new
  bottom video track (index-0-renders-on-top — reorder after adding).
- **Same-track overlap = overwrite.** Placing a clip over an existing one on the same
  track trims/splits it, exactly like dragging in the UI. Compute placements so nothing
  on the same track overlaps, ever.

## Ground truth extraction (before any keyframing)

Two analysis passes over the take give exact event times/positions; never eyeball them:

Bundled tools do both passes deterministically — run them, don't re-derive them:

1. **Audio onsets are the event log** — `scripts/audio_events.py` (extract mono WAV with
   `afconvert` first). 10ms energy envelope, rise >12dB, classified by duration/spectral
   centroid; pass a beats TSV (from `scripts/clock_lint.py --beats-out`) and every click
   sfx, send-whoosh, and notification chime labels itself against the shot clock to the
   centisecond. A full match also validates the take.
2. **Cursor tracking by self-bootstrapped template** — `scripts/track_cursor.py`.
   Hand-rasterized templates fail (anti-aliasing, shadows) and masked `TM_CCORR_NORMED`
   is NaN-prone; the script frame-differences a glide-over-static segment (`--boot-at`)
   to capture the cursor's real rendered appearance, then tracks with masked `TM_SQDIFF`.
   Full-bleed brand-color frames (`--card-color`) segment the take and sync video time to
   the driver clock.
3. If the take starts at the hook card, video time ≈ shot-clock time; chapter-card spans
   confirm the offset.

## Attention keyframes FIRST, length cuts SECOND

Zoom/pan keyframes are configured on the UNCUT take, before anyone trims a frame. Two
reasons this ordering is law:
1. **Timing is free while the take is uncut.** Video time ≈ driver-clock time (verify
   with the chapter-card spans), so every keyframe timestamp comes straight from the
   shotlist's `until()` values — no eyeballing, no re-derivation. After cuts, every
   timestamp needs the piece-mapping transform (`scripts/timeline_map.py`) and precision
   degrades.
2. **Keyframes are clip-relative** — they travel with the pieces through every later
   split, trim, and speed change the owner makes. Keyframed-then-cut survives; cut-then-
   keyframed means redoing the work per piece.

The attention PLAN comes from interaction-design-and-flows.md, not from taste: punch in
on interruptions (notification banners), the one or two hero cause→click→consequence
beats, and rough-human→polished-product payoffs — nothing else. Build the plan as a JSON
of `{name, t (driver seconds), focus_px, zoom, ease_in/hold/out}` and run
`scripts/keyframe_zooms.py` to get the exact scale/position keyframe rows (it holds the
focus point fixed through the zoom and warns with the minimum covering zoom if the frame
would expose the background). Focus positions come from the cursor track
(`scripts/track_cursor.py`) or fixed UI regions (a banner corner); verify the timing
against audio onsets (`scripts/audio_events.py`) — the chime IS the moment.

## Attention zooms (punch-ins)

- Keyframe `scale` + `position` on the take clip (clip-relative frames; keyframes travel
  with the clip). ~1.25–1.35×, ease in ~0.8s at the audio onset, hold through the action,
  ease out. Reserve for notifications and one or two hero clicks.
- **Focus-point math** (top-left position + normalized scale): with base scale `s0`,
  top-left `t0`, focus fraction `f` (focus px / source px per axis):
  `n = t0 + f·s0` (the focus point's canvas position) → zoomed top-left `t = n − f·s_zoom`.
  Verify the zoomed clip still covers the canvas (`t ≤ 0` and `t + s_zoom ≥ 1`).
- **Keyframes override the static transform.** Any resting-framing change (e.g. floating
  the window smaller) must be rewritten INTO every keyframe track's base rows, and zoom
  top-lefts re-aimed with the new base — otherwise the zooms drift toward stale
  coordinates.

## Background compositing (the alpha payoff)

- Background image on the bottom video track, spanning the full timeline, transform set
  to COVER the canvas (compute: matching aspect axis at 1.0, the other >1; never let it
  letterbox).
- Float the window take at ~0.88 scale, centered — the margin sells the composite. A
  drop shadow on the window helps it sit.
- Good background sources: the product's own brand imagery, or app-bundled wallpaper
  packs (e.g. Cap.app ships flat JPEGs in
  `Contents/Resources/assets/backgrounds/` — system macOS wallpapers are `.madesktop`
  manifests whose full-res assets are NOT on disk until selected).
- Match background mood to brand palette; a dusk/landscape image that shares the brand's
  hue family beats a generic gradient.

## Speed ramps

Speed is a clip property, not keyframable: **split the clip at the ramp point, set
`speed` on the tail piece**. Owners mark the spot themselves (a keyframe/playhead at the
frame). Splitting regroups linked audio correctly; keyframes before the split stay with
the head piece. After a 2× tail, re-check anything timed to the old ending (music fades,
background/track lengths, outro VO room).

## Laying the VO

The cue sheet's times are SOURCE times; the owner's edit changes the mapping. Use
`scripts/timeline_map.py` with the pieces read from the timeline (start/end/trimStart/
speed per take piece): it maps each cue to a timeline frame, flags cues that fall in
cut-out ranges, and snaps them to the next piece boundary. Doing this by hand is the
single most error-prone arithmetic in the pipeline — don't.

- One clip per script line (per pacing-canon.md, per-sentence stitching was rejected);
  keep the few deliberate seams ("Sent." on the send click; montage words one per cut).
- Anchor each line at its mapped beat; chain and cushion (~0.3–0.4s) when the owner's
  trims compressed the original spacing — and never overlap on the track.
- Expect spillover at a 2× tail (an 8s outro line over a 4s outro): surface it to the
  owner with options (slow the tail piece back, start the line over the montage, or let
  it play over the background after the window ends) rather than silently squeezing.

## The mix

Learned targets: music bed ~0.10 volume with a manual fade at picture end; app sfx track
at 0.5 or muted entirely (the sfx were shot-clock scaffolding — in the final mix VO +
music usually carry it, with at most the notification chimes surviving); VO at full on
its own track. The owner sets the final balance — apply their levels, don't argue dB.

## Export

Export from the editor (owner's call on preset). If asked whether the driver can export
"the animation" directly: yes via the in-browser recorder, but it's the lossy path — the
SCK master through the edit is the quality route.

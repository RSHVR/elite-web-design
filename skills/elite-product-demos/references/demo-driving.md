# Demo Driving — the Shot-Clock Autopilot

The driver is a single vanilla-JS file loaded by the frontend that plays the entire demo
deterministically: it draws its own cursor, clicks the real UI on an absolute clock, and
overlays only non-app chrome (hook/chapter/outro cards, watermark). Works on any DOM —
React, plain HTML, design-tool exports — because it finds elements by visible text and
drives them with real events.

## 0. Frontend intake (do this before promising anything)

The user provides the frontend; you inventory it:

1. **Surfaces**: list every screen/nav item. Which story beats map to existing surfaces?
2. **Wiring**: for each needed flow, is it functional, cosmetic, or absent? Click through
   or grep for handlers. Design-tool exports often keep INERT template copies of nodes in
   the DOM (real bounding boxes, no handlers) — see Finders below.
3. **Serving**: how does it run locally? Serve with `Cache-Control: no-store` (a tiny
   Python/Node server or Caddy) — browser memory-cache serving stale JS during iteration
   produces false "you didn't fix it" rounds.
4. **Seams**: where can demo data/flows be added without forking the app? (seed data
   files, a staged-response layer for AI features, CustomEvent hooks).
5. Output: a **gap list** (smallest → largest) the user approves. Typical gaps: staged AI
   conversation beats, a notification banner, seeded cast data, a missing screen.

## 1. Driver architecture

```
(function () {
  // gate: inert unless ?demo=1 (or a dedicated recording hostname — see recording.md)
  boot()        // overlay layer, drawn cursor, watermark, R/C hotkeys, visibility warn
  run()         // THE SHOT CLOCK — the whole film as a sequence of awaits
  // utilities: until, waitFor, clickFresh, glideTo, press, typeInto, card, chapter
})();
```

**Absolute clock.** `this.t0 = performance.now()` at the first meaningful frame; every
beat is `await this.until(seconds)`. Never chain relative sleeps — drift compounds and VO
can't be cued. Keep the clock monotonic (lint it: extract all `until()` values, assert
sorted).

**Non-fatal waits.** `waitFor(fn, timeout, label)` polls for an element and on timeout
LOGS AND RETURNS NULL — one flaky beat must degrade that beat, never freeze the take.
A frozen take wastes a full video-length rehearsal; a skipped beat is visible and fixable.

**Click pipeline** — the order matters, each stage exists because of a real failure:
```
clickFresh(find):
  el = waitFor(find)                 // re-resolvable finder, not a stale node
  ensureVisible(el)                  // scroll its own scrollable ancestor
  el = waitStable(find)              // WAIT until its rect stops moving (animating
                                     // lists/decks made the cursor chase & bob)
  glideTo(el)                        // eased cursor glide; SKIP if already within ~5px
                                     // (micro-glides between repeat clicks read as jitter)
  settle: re-measure; corrective 190ms glide if the target moved during the glide
  press(el)                          // click sfx + cursor dip, then el.click()
```

**Typing.** `typeInto` uses the native value setter + `input` events (framework state
updates correctly, cross-iframe too). Human pacing: ~38ms spaces / 48–70ms chars.

**Overlay cards.** `card()` = full-bleed brand-color div in the overlay layer (hook,
chapters, outro). Chapter cards ~2.1s (300ms fades). Get the brand color from the brand
package — a UI accent token that happens to share the color's name is usually NOT the
logo color.

**Hotkeys**: `R` reloads for a clean take; `C` arms a one-shot `getDisplayMedia`
MediaRecorder capture (the lightweight fallback recorder; the real rig is in
recording.md).

## 2. Finders — hard-won rules

- **Find by visible text, resolve at click time.** Finders are functions, re-run at every
  stage, because re-renders swap nodes underneath you.
- **Prefer wired nodes.** Filter candidates to `typeof el.onclick === 'function'` (or
  `cursor: pointer`), falling back to visible ones. Design-tool runtimes keep inert
  template copies with real bounding boxes — clicking one does nothing and the take
  silently degrades.
- **Length-cap text matches.** A regex text match MUST require the node's own text to be
  short (`textContent.length < 140`). Wrapper divs have few children but kilobytes of
  text; walking up from a wrapper hit lands on the WRONG handler. (Real bug: a card click
  silently hit "New chat" and wiped the scene.)
- **Walk up to the wired ancestor.** Labels usually aren't the clickable node; walk ≤6
  parents preferring onclick/pointer.
- **Style-attribute regexes need `\s*`.** Browsers normalize `width:44px` to
  `width: 44px`.
- **Keep finder strings in lockstep with app copy.** Renaming a title (or swapping an
  em dash for a middot) breaks the finder that quotes it — grep the driver whenever
  on-screen copy changes.

## 3. App ↔ driver contracts

Define every crossing in the cast sheet as exact CustomEvent / postMessage shapes, e.g.:
- `window.dispatchEvent(new CustomEvent('notify-message'))` → app shows banner + chime
- iframe context: parent forwards `{type: 'x', ...detail}` — beware **spread clobber**
  (a detail carrying its own `type` overwrites the envelope type; the receiver must accept
  both) and the **already-mounted case** (no remount → no "ready" handshake → post
  directly into the live frame).
- **State across remounts**: if a subview unmounts on navigation, on-camera state changes
  (a completed task) must persist (sessionStorage) or they'll visibly resurrect later in
  the take. The driver clears that storage on boot so `R` restarts stay clean.

## 4. Environment facts

- **Hidden tabs are frozen.** Chrome throttles timers to 1Hz and freezes rAF in hidden
  tabs. Rehearsals and takes REQUIRE the tab visible and frontmost. Make the driver warn
  (console + toast) on `visibilitychange`.
- Serve no-store (see intake). Cache-bust iframes (`?v=Date.now()`).
- Headless verification (browser MCP / Playwright) works for timer-driven logic but NOT
  rAF-driven motion — verify chains headlessly, verify feel in a visible run.

## 5. The iteration protocol

1. **Syntax gates on every change**: `node --check` the driver; parse every touched JSX
   (in-browser-Babel apps: `Babel.transform(src, {presets:['react']})` via node); run
   `scripts/clock_lint.py` (monotonic clock + beat TSV dump — that TSV is also the timing
   source for the edit's attention keyframes and audio-event labeling).
2. **Headless chain asserts**: for each beat, an element-based assertion (never
   `textContent.includes` on the whole body — templates and inline scripts pollute it).
3. **Visible rehearsal with the owner.** Their notes arrive as terse observations ("too
   slow on X", "that click did nothing"). Every note becomes: a driver retime (until()
   nudges — keep a constant offset when shifting a whole tail), an app change, or a doc
   update — all three stay in sync, changelog dated with the why.
4. Debug what the owner SAW, not what should have happened. A "nothing happened" click is
   usually a dead finder (silently skipped beat) — because waits are non-fatal, whole
   segments can vanish without an error. Trace the specific take.
5. Expect ~10 passes. Budget for it.

## 6. Worked-example timings (calibrated by an owner's edits — see pacing-canon.md)

- Silent brand hold before a typewriter hook: 2.0s
- Chapter card: ~2.1s total
- AI "thinking" before any staged response: ≥1.2s (staged planning beats: 1.5–2s stages)
- Reviewable card (email draft, etc.) before its send click: ≥2.5s
- Montage pages: 1.5–1.7s each
- Payoff holds (a KPI wall, a team view): 5–7s
- End-of-video: the last two beats compress — owners consistently run tails at 2×.

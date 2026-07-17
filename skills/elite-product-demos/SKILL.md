---
name: elite-product-demos
description: |
  End-to-end pipeline for producing recorded product demo videos from a frontend the user
  already has (a real app, staging build, or clickable mockup): positioning and story,
  script + shotlist authoring, building a shot-clock autopilot that drives the real UI,
  motion design and interaction polish, ScreenCaptureKit window recording with a
  camera-clean URL, AI voiceover generation, and finishing the edit in Palmier Pro
  (cursor/audio tracking, attention zooms, background compositing, VO layout). Use this
  skill whenever the user wants a product demo, demo video, product tour video, launch
  video, sales video, walkthrough recording, sizzle reel, or asks to "record the mockup",
  "drive the demo", "make a video of the app", "script a demo", write a shotlist or VO for
  a product video, automate UI clicks for a recording, or edit/pace a captured product
  take — even if they never say the word "demo". Also use it when a previous demo
  underperformed and needs a restructure. Load elite-copywriting alongside for VO lines and
  elite-ux-strategy for persuasion structure; brand colors come from the brand package
  (elite-brand-design), never from UI accent tokens.
---

# Elite Product Demos

A recorded product demo is a **film shot inside a working UI**. It has a screenplay (script +
shotlist), a camera operator (a deterministic autopilot driving the real interface), actors
(the app's own animations and a drawn cursor), a recording rig, and an edit. Every phase
below exists because skipping it produced a demo that flopped in front of real buyers.

## Inputs — what the user provides

This skill does not design a product UI from scratch. It turns an EXISTING frontend into a
film. Before starting, collect from the user:

1. **A runnable frontend** — a local mockup, staging build, or production app that renders
   in a browser. It does not need to be complete: demo-only flows, seeded data, and staged
   AI responses are normal and expected additions, but the surfaces being shown must exist
   or be explicitly scoped as builds. If the user has no frontend at all, route them to
   elite-web-design first — this skill starts where a clickable UI ends.
2. **Positioning context** — what the product does for whom, who will watch the video
   (archetypes), and any real sales-meeting signal about what lands. Interview for this;
   never invent it.
3. **Brand assets** — logo, the true brand colors (verify against the logo, not UI accent
   tokens), voice/tone constraints.
4. **Claim constraints** — what may legally/honestly be shown or said (data provenance,
   compliance, consent, roadmap-vs-shipped features).

## Quick Reference

| Phase | Reference file | Read when |
|-------|---------------|-----------|
| Story, positioning, script, shotlist, VO | [story-and-shotlist.md](references/story-and-shotlist.md) | Before writing a single beat |
| Interaction design + user flows | [interaction-design-and-flows.md](references/interaction-design-and-flows.md) | Designing what gets clicked and why; reviewing any shotlist draft |
| Shot-clock autopilot (demo driver) | [demo-driving.md](references/demo-driving.md) | Frontend intake; building or debugging the driver |
| Motion design + interaction polish | [motion-and-interactions.md](references/motion-and-interactions.md) | Making beats feel alive; timing any animation |
| Recording (ScreenCaptureKit, clean URL) | [recording.md](references/recording.md) | Setting up capture or the URL rig |
| The edit in Palmier Pro | [editing-palmier.md](references/editing-palmier.md) | Takes are recorded; assembling the video |
| Pacing canon (owner-edit ground truth) | [pacing-canon.md](references/pacing-canon.md) | ALWAYS — before scripting AND before driving |

## The Pipeline

```
0. INTAKE     Inventory the provided frontend: surfaces, wired vs. dead flows, how it's
              served, data seams. Map what the story needs against what exists; scope the
              gap as an explicit build list the user approves.
1. POSITION   Frame the story around what the product does for the buyer, in the buyer's
              words. Identify viewer archetypes. Weight beats by real sales-meeting
              signal, not copywriting instinct.
2. SCRIPT     Script + shotlist with hard timecodes, a causal-accounting rule, claim
              flags, and VO as pacing guides. One living document.
3. BUILD      Wire the demo flows into the frontend; write the shot-clock driver that
              clicks the real UI. Contracts between app and driver live in one cast sheet.
4. REHEARSE   Visible-tab runs with the owner watching. Every note becomes a driver or
              app change. Expect ~10 passes. The owner's cuts are the spec.
5. RECORD     Window-only ScreenCaptureKit capture with alpha, tab audio, and a
              camera-clean URL. ProRes master.
6. EDIT       Palmier Pro: ground-truth event extraction (cursor track + audio onsets),
              attention zooms, background float, speed ramps, VO, mix.
```

## Principles that are not optional

**Position before pixels.** A demo that shows features in product-menu order is a tour;
a demo that walks one believable person through one believable day is a story. Name the
frame the product sells (e.g. "Find, Close, Manage → Build, Develop, Scale") and SPEAK IT
ON SCREEN — chapter cards, outro line. Every viewer archetype (end user, management,
executive) must see their payoff *named*, and the archetypes with the shortest attention
must not be served last.

**Real sales signal beats craft instinct.** If live meetings show decision-makers lighting
up for three specific things, those three things get screen time and everything else gets
compressed — even when copywriting theory says otherwise. A beautifully argued beat about
a feature nobody asked about is dead weight.

**Causal accounting.** Every number spoken or shown must be *earned on camera*. If the
wrap-up says "six emails sent," the viewer watched six sends. If a reply arrives, the
viewer watched the email that provoked it. And the opening screen should be the video's
table of contents: everything queued there pays off in a later chapter. Audiences don't
consciously notice this; they subconsciously trust it.

**The demo is code.** Drive the real UI with a deterministic shot-clock autopilot — never
hand-mouse a take. Humans can't hit beats reproducibly and every retake costs the full
video length. The driver is ~600 lines you'll iterate ~30 times; the take is free after
that.

**Rehearse with the owner; their edits are the spec.** The person who will show this video
to buyers watches rehearsals and cuts the recorded take. Capture *every* cut they make and
*why*, then feed those numbers back into the next shot clock (see
[pacing-canon.md](references/pacing-canon.md)). Scripted pacing consistently runs ~25%
longer than what the owner ships.

**Claims are flagged, not assumed.** Any on-screen or spoken claim about data provenance,
compliance, recording/consent, or capability status gets an explicit flag (`F#`) in the
shotlist that the owner must resolve before recording. "It's on the roadmap" is a fine
answer; discovering the problem after shipping the video is not.

**One motion, one meaning.** Each beat gets one intentional animation and at most one
sound. Stacked animations split attention; stacked sounds (whoosh + chime + banner-chime
within seconds) read as noise. See
[motion-and-interactions.md](references/motion-and-interactions.md).

## Working loop

1. Read [pacing-canon.md](references/pacing-canon.md) first — it recalibrates every
   duration you're about to write.
2. Run frontend intake (top of [demo-driving.md](references/demo-driving.md)). Present the
   gap list — what the story needs that the frontend lacks — and get it approved before
   promising beats.
3. Author the script/shotlist doc per
   [story-and-shotlist.md](references/story-and-shotlist.md). Get the owner's sign-off on
   story and flags BEFORE building.
4. Create the cast sheet (single source of truth: names, numbers, integration contracts,
   banned strings) and build app flows + driver per
   [demo-driving.md](references/demo-driving.md), applying
   [motion-and-interactions.md](references/motion-and-interactions.md) to every new beat.
5. Verify headlessly (browser asserts for every chain), then rehearse with the owner in a
   visible tab. Fold every note back into driver/app/doc — keep all three in sync, with a
   dated changelog in the doc.
6. Record per [recording.md](references/recording.md). Import and finish per
   [editing-palmier.md](references/editing-palmier.md).
7. After the owner's edit ships, diff their cut against your take and append the new
   lessons to the pacing canon.

## Bundled scripts (use these — don't re-derive)

Deterministic utilities in `scripts/`; each replaces expensive, error-prone in-context
reasoning:

| Script | Does | When |
|---|---|---|
| `clock_lint.py` | Verifies the driver's `until()` clock is monotonic; dumps the beat list as TSV | Every driver change; TSV feeds the other tools |
| `track_cursor.py` | Tracks the drawn cursor in a take (self-bootstrapped template) + syncs video time to the shot clock via brand-color cards | After recording, before keyframing |
| `audio_events.py` | Onset-detects clicks/chimes/whooshes and labels them against the beat TSV — exact event times | After recording; timing source for zooms |
| `keyframe_zooms.py` | Turns an attention plan (driver-time + focus + zoom) into exact scale/position keyframe rows, focus-point-preserving, with canvas-coverage checks | Keyframing the UNCUT take, before any length cuts |
| `timeline_map.py` | Maps driver/source times → timeline frames through an edit's cuts and speed ramps | Laying VO after the owner has cut |

**Attention keyframes come BEFORE length cuts** — timings reference the demo-driver clock
(free while the take is uncut; clip-relative thereafter, so they survive the owner's
edits), and the plan of WHAT deserves a zoom comes from
[interaction-design-and-flows.md](references/interaction-design-and-flows.md), not taste.

## Cross-skill loading

- **elite-copywriting** — VO lines, hooks, objection pre-emption (collapse its phases for
  demo scale, but never skip the awareness/sophistication check).
- **elite-ux-strategy** — persuasion structure, social proof placement, CTA framing.
- **elite-brand-design / brand guidelines** — the brand's REAL colors for cards and
  outros. Never grab a UI accent token and assume it's the brand color; verify against
  the logo.
- **elite-web-design** — if the user has no frontend yet, that collection builds one;
  this skill starts where a clickable UI ends.

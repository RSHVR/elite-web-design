# Story, Script & Shotlist

The script is the product of three decisions made in order: what story frame the product
sells, who is watching, and only then what appears on screen. Getting these backwards is
how demos flop.

## 1. Positioning the story

**Extract the frame from the user, in their words.** Ask: "In one sentence, what does this
product do for the buyer?" A good frame is a verb chain the video can chapter itself around
(e.g. "helps advisors *Find, Close, and Manage* clients — and so *Build, Develop, and
Scale* their practice"). Then make the frame VISIBLE: full-bleed one-word chapter cards
between acts, and the outro restates it. A frame that lives only in your head is not a
story structure; it's a vibe.

**Identify archetypes and place their payoffs.** List who will actually watch (individual
user, management, executive...). Each archetype needs a *named* payoff beat. Rules learned
the hard way:
- Executives don't watch to the 84th percentile to find out the video is for them. Their
  payoff cannot be last-and-thinnest.
- Chapter cards double as a table of contents for people scrubbing the video.
- If archetype needs genuinely conflict, cut per-archetype versions rather than one bloated
  master.

**Weight beats by real sales signal.** Interview the user: "In live meetings, what did
decision-makers actually respond to?" Give those beats full screen time and compress
everything else — including beats that copywriting theory loves. Conversely, a feature the
team is proud of but buyers never ask about is a montage flash, not an act.

**Choose a story spine.** Two proven shapes:
- **Day-in-the-life**: one believable person, chronological, causality for free. Best for
  platforms with many surfaces. This is the shape that WORKED after a "wow-first" cut
  flopped.
- **Wow-first / do-the-last-thing-first**: open on the most impressive payoff, rewind.
  Best for single-killer-feature products. Warning from experience: a wow-first cut of a
  broad platform read as gimmick + all-end-user workflow, and lost the archetypes.

Whatever the spine: **no tension, no story**. Something must be at stake (a dropped
follow-up, a dormant client, money moving) or the demo is a screensaver of features.

## 2. Structural rules

**Causal accounting.** Every number in narration or on screen must be earned on camera
within the video. Wrap-up says "6 emails sent" → viewer watched 6 sends. A reply arrives →
the viewer watched the message that provoked it, earlier, with the same names. Break this
and attentive viewers feel lied to without knowing why. Keep a written ledger in the doc
(e.g. `6 emails = 4 invites + reply + reconnect`).

**Opening screen = table of contents.** Whatever the first meaningful screen shows (queued
tasks, signals, notifications) must each pay off in a later chapter. This turns the home
screen into a promise the video keeps.

**Claim flags.** Maintain `F#` flags in the doc for every claim needing owner sign-off:
data provenance ("verified against public records"), consent/recording features, social
data sourcing (often vetoed — prefer "from your own notes"-style internal sourcing),
roadmap-vs-shipped. Block the affected beats until resolved. Real example: a
"6 of your clients hold shares in X" beat was parked because nobody could say where the
product would know that from.

**Cast sheet (CAST.md).** One file that outrules everything else: every fictional name,
company, email, date, and number; the schedule of the fictional day; the causal-accounting
ledger; app↔driver integration contracts (exact event names and payload shapes); banned
strings (old personas, competitor names, unapproved claims — enforced by grep). Both the
app edits and the driver are built against it. Dates must be internally coherent (a "next
month" event is actually next month from the fictional today; "opened in March" is in the
past).

## 3. The shotlist document

One living markdown doc, kept in sync with the driver on every change, with a dated
changelog. Structure that works:

```
# <Product> Demo — Script & Shotlist (vN · "<title>")
**Deliverable:** ~M:SS video, audience, voice-track plan
**Built on:** <frontend path + how served> · **Orchestration:** <driver file + keys>
## 1 · The story        — one-paragraph spine + causal accounting + cast list
## 2 · Voice script     — TC | line table (~120wpm). TCs are PACING GUIDES;
                          the cue sheet is regenerated only after picture lock.
## 3 · Shotlist         — per-act tables: | # | TC | Driver action | On screen |
## 4 · Build gap list   — what the frontend lacks, smallest → largest
## 5 · Orchestration notes — D# numbered driver facts (finders, events, gotchas)
## 6 · Checklist & flags   — F# flags incl. claim checks, recording setup, captions
## 7 · Changelog           — dated, per rehearsal pass, WITH the why
```

The `| # | TC | Driver | On screen |` beat-table format matters: the Driver column is
transcribable straight into `until()` calls, and the On-screen column doubles as the QA
checklist and caption source.

## 4. Voiceover

- **Narrator-only by default.** In-app "AI voices" reading aloud is a gimmick tax; one
  warm narrator (~120 wpm, peer not announcer) survived every review round. If an in-app
  voice speaks, its spoken line must match the on-screen text EXACTLY (captions, audio,
  pixels agree).
- Write VO lines that comment on meaning, not UI ("The chase runs itself" beats "Sam now
  displays a follow-up card").
- **VO and on-screen text share the viewer's one language channel.** For any beat where
  the viewer must read, either make the VO point at the exact words ("Meera's mentions
  her March opening" — converting a full read into a cheap skim), make it redundant with
  them, or shut up. Run every beat through the reading math in pacing-canon.md while
  scripting: count the words the next beat depends on; dwell ≥ 0.5s + words ÷ 2.5.
- **Generate full-line reads, not per-sentence fragments.** A voiceover stitched from
  dozens of single-sentence clips was rejected as robotic even with prev/next-text
  conditioning. Generate one clip per script LINE; split only where the edit truly needs
  an alignable seam (a "Sent." that must land on a click; montage words landing one per
  cut) and note those seams in the cue sheet.
- Pronunciation traps go in the cue sheet: acronyms spelled phonetically ("CASL" →
  "Castle"), initialisms hyphenated to force letters ("R-S-V-P"), numbers pre-spelled for
  pacing.
- Mind the mix plan: app sfx (dings, chimes) come from tab audio — leave narrator space
  around them.
- **Never finalize the cue sheet before picture lock.** Every rehearsal pass moves the
  clock; regenerate TCs at the end, once.

## 5. Restructuring a flopped demo

When a demo underperforms, resist polishing it. Diagnose the failure mode first — it
determines everything:
- Confusion/too fast → calmer spine, same content.
- Bored decision-makers → wrong archetype weighting; the content itself must change.
- "It's a gimmick" → the hook over-promised relative to the beats.
Interview the owner about what actually happened in the room, then re-run positioning
(step 1) from scratch. Salvage surfaces and driver machinery; do not salvage structure.

# Pacing Canon — Owner Edits Are Ground Truth

This file encodes what a real owner actually cut from real takes, and why. It exists so
the NEXT demo's shot clock is written at shipped pace instead of scripted pace — every
second the owner has to cut in the edit is a second you mis-scripted. Read this before
writing any `until()` value or shotlist TC.

## The headline number

**Scripted demos run ~25% longer than what owners ship.** A 2:27 scripted take was
hand-edited to 1:49 (−26%). A later, tighter cut still lost ~8s of dwells plus a 2× tail.
Write the clock assuming your instinct for "comfortable" is a quarter too slow.

## The observed cuts (with inferred rules)

**Cut 1 — establishing tour trimmed ~4.5s.** A hover-tour of the home screen's queued
items (3 hovers × ~2.2s + settling) was cut nearly in half.
→ *Rule: establishing tours read at ≤1.5s per item. The viewer only needs to register
that items exist; the payoffs come later.*

**Cut 2 — post-read pre-click dwell trimmed ~3.8s.** After a results list rendered and
had clearly been "read," the take idled before the next click.
→ *Rule: once a surface has been on screen long enough to read its headline (~2s), act.
Waiting past comprehension reads as lag, not gravitas.*

**Cut 3 — the tail ran at 2× from the last payoff to the end.** The owner placed a marker
right after the final chapter's key beat and doubled everything after it (wrap-up dwell,
montage, outro).
→ *Rule: endings compress. Viewers who reach the ending are already convinced or already
gone. Script the wrap/montage/outro at what feels rushed — it will read as confident.
Corollary: give the outro VO less copy than feels complete.*

**Mix decisions.** Music bed at ~0.10 volume with a manual fade at picture end. The app's
own sfx track first halved, then muted entirely.
→ *Rule: in-app sfx are shot-clock scaffolding and rehearsal texture; the shipped mix is
VO + quiet music. Don't build story beats that only work if the viewer hears an app
sound.*

**VO rejection.** A voiceover generated as ~56 per-sentence clips (for alignment
flexibility) was deleted wholesale as "bad" despite prev/next-text conditioning.
→ *Rule: generate one clip per script LINE — prosody lives at line scope. Only split
where the edit needs an alignable seam, and decide those seams at script time.*

**Rehearsal-pass pattern.** Across ~10 passes, owner notes clustered as: pacing
(too-slow beats named explicitly, "then you speed through everything else"), dead
interactions ("that click did nothing" — usually a silently-skipped non-fatal beat),
redundant stimulus (a chime deleted, clock pills deleted, a green header strip deleted,
"consent on file" text deleted), and readability ("1 second minimum between sends so the
viewer can read them").
→ *Rule: when in doubt, remove the extra element rather than tune it. Every rehearsal
pass deleted more than it added.*

## Reading math — dwell times must survive arithmetic

The budgets below aren't taste; they're bounded by how fast humans read. Check every beat
against these numbers — if the viewer can't have read what the next beat depends on, the
demo stops making sense no matter how good it looks.

- Adults read ~240 wpm (≈4 words/s) silently under full focus. **On video, with motion
  and VO competing, plan for ~150 wpm (≈2.5 words/s)** — the same reason subtitle
  standards cap at ~17–20 characters/second.
- **Three levels of "reading," with different costs:**
  1. **Recognition** (nav labels, buttons, a card existing): 0.5–1s. The viewer registers
     *what it is*, not its content.
  2. **Skim-verify** (drafts, documents, result rows): the viewer reads only the words
     the VO points at. Budget = 0.5s orientation + pointed-words ÷ 2.5.
  3. **Full read** (hook lines, chapter words, any text carrying meaning the VO doesn't):
     0.5s + words ÷ 2.5, minimum 2s.
- **The VO-competition rule.** People cannot read one text while hearing different words.
  For any text the viewer must actually read: make the VO redundant with it, go
  VO-silent for the dwell, or double the budget. VO that *points* ("Meera's mentions her
  March opening") converts a full read into a cheap skim-verify — this is the single best
  pacing tool you have.
- **Orientation cost**: +0.3–0.5s after every cut or screen change before reading begins.
- **First-instance rule.** The first of a repeated element (first card of a deck, first
  notification) pays the full read cost; repeats pay only difference-verification
  (roughly half). This is why an owner-approved 2.5s-per-card send salvo works: card one
  arrived earlier with the deck fan (~4s total exposure), and cards two through four only
  need "it's different" confirmed.
- **Per-beat sanity check**: count the words the viewer must have read for the NEXT beat
  to make sense. If dwell < 0.5 + words ÷ 2.5 → cut words or add time. Prefer cutting
  words: on-screen copy in demos should be skimmable by design (front-load the
  distinguishing phrase into the first line).

## Feed-forward: write the next clock with these budgets

| Beat type | Budget | Reading-math basis |
|---|---|---|
| Silent brand hold before hook type | 2.0s | anticipation, no reading |
| Typewriter hook line | typing speed IS the read | guided full read |
| Establishing tour | ≤1.5s per item | recognition, not reading |
| Chapter/transition card | ~2.1s | full read of 1 word + orientation |
| AI thinking indicator | 1.2s (stages 1.5–2s) | none — builds credibility |
| Card render → its click | ~2s after fully readable | skim-verify w/ pointing VO |
| Reviewable document (draft/email) before send | 2.5s (first instance ~4s) | first-instance rule |
| Repeated sends in a salvo | ≥2.5s apart | difference-verification |
| Hero payoff hold (KPI wall, team view) | 5–7s | 3–5 numbers, full read, VO redundant |
| Montage page | 1.5–1.7s | recognition only — never put required reading in a montage |
| Wrap-up + outro combined | script at perceived-rushed; owner will 2× it anyway | wrap numbers must be VO-redundant to survive the 2× |

## The meta-rule

After every shipped demo, diff the owner's final cut against your recorded take: list
every trim, speed change, deletion, and mix decision, ask why once if unclear, and append
the generalized rule here. The canon compounds; the tenth demo should need almost no
editing.

# Interaction Design & User Flows

Motion (see motion-and-interactions.md) is how a beat *feels*; this file is about which
interactions to stage and how flows are constructed so a viewer can follow — and believe —
every action. In a demo, interaction design is narrative design: each click is a sentence
in an argument.

## Interaction design

**Every interaction is a cause→click→consequence chain.** The viewer must see (or hear in
VO) the *reason* for a click before it happens, and a visible *effect* within ~400ms
after. A click without a visible cause reads as scripted; one without a visible effect
reads as broken. When reviewing a shotlist, annotate every click with its cause and its
consequence — if either column is empty, redesign the beat.

**Let the product do the carrying.** Prefer interactions where the product moves the user:
click the notification banner's action button, the AI's suggested chip, the card's inline
CTA — not the nav rail. Nav-rail clicks say "the user must remember where things live";
in-flow affordances say "the product brings the work to you." A real rebuild happened for
exactly this: a nav click into the next act was replaced by a notification arriving *in
context* whose button carried the user there. Reserve nav clicks for the montage, where
they demonstrate breadth deliberately.

**The rough-human / polished-product contrast is the strongest beat archetype.** Stage
the user's input as minimal and imperfect — a lowercase "sounds good, does thursday
work?" — and let the product elevate it (one tap → a warm, signed, scheduled reply). The
roughness is not sloppiness; it's the setup. Same shape at larger scale: one click → four
individually-personalized drafts. Any beat of the form *small human act → large product
act* earns its screen time.

**Show outcomes, never configuration.** No settings screens, no forms filled field by
field, no empty states being populated. Defaults are pre-set; data is seeded. If
configuration IS the product, show the moment after it (the result) and let VO claim the
ease.

**Introduce each interaction concept once, then reuse it.** The second notification
banner, the second draft card, the second checklist must be visual twins of the first —
zero new learning cost. If two elements of the same kind look different, the viewer spends
their reading budget re-orienting instead of following the story.

**Demonstrated agency needs evidence.** If the product's value is background work
(auto-follow-ups, watching audiences, scheduled nudges), stage BOTH halves: the delegation
moment (the card that says what will happen) and later, on-camera evidence it happened
(the reply arriving, the badge ticking). Claiming background work without evidence is a
slideware smell; evidence without the delegation moment is unexplained magic.

**Dead interactions are catastrophic on camera.** Anything the cursor touches must
respond — hover states included (the driver dispatches real hover events for this
reason). In rehearsal, a "that click did nothing" note is a stop-the-line bug even when
the take recovers, because buyers assume the product, not the demo rig, is broken.

**Honesty boundary.** Demo-only staging (seeded data, scripted AI responses, simulated
notifications) is normal. Demo-only *interactions* that the product doesn't ship —
gestures, buttons, automations that don't exist — are claims, and go through the claim
flags (F#) like any other claim. Roadmap features may appear only with owner sign-off.

## User flows

**A flow is: signal → decision → action → confirmation → consequence.** Never start a
flow from nowhere ("now let's look at Reports"). Something on screen — a signal, a
notification, a queued item, a line of VO tension — must motivate entering the flow, and
the flow must end in a verifiable state change (sent-state, badge tick, list item
appearing, toast). The state change is the flow's proof of work.

**Enter flows where a real user would be.** From the home screen's queue, from a
notification, from a signal feed — not from a cold nav hunt. This is also why the opening
screen should be built as the video's table of contents: every flow's entry point is
planted there before any flow begins (see story-and-shotlist.md).

**Depth beats breadth — but only for hero flows.** One flow shown end-to-end (signal →
outreach → reply → close) is worth five half-flows. Give each chapter ONE hero flow at
full depth; everything else demonstrates breadth in the montage. If a flow can't justify
end-to-end treatment, it isn't a chapter — it's a montage page.

**Flow length: 3–7 interactions per chapter, with a payoff before any break.** Longer
chains need a mid-payoff (a completed sub-goal) or attention dies. If a hero flow
genuinely needs 10+ interactions, that is product feedback, not demo feedback — say so.

**Happy path only; tension comes from the world, not the software.** Nothing errors, no
retries, no loading failures on camera. Stakes come from the scenario (a dormant client,
money moving this week, a follow-up about to be dropped) so the product gets to be the
resolution every time.

**Close every loop you open.** Applied causal accounting: an email sent on camera gets
its reply on camera; a task queued at 8 a.m. completes by the wrap; the count shown in
the summary equals actions the viewer watched. Loops opened and abandoned are subliminal
broken promises.

**Cross-surface flows must persist their state.** If a flow leaves a surface and returns
later (queue item completed, then the queue shown again), the earlier change must still
be there — remount-safe state in the mockup (see demo-driving.md). A completed task
resurrecting on camera is a continuity error viewers can't articulate but do register.

## Attention plan (feeds the edit's zoom keyframes)

This file's hierarchy IS the edit's attention plan. While the shotlist is still being
written, tag the beats that will earn a punch-in zoom in the edit — interruptions
(notification banners), the one or two hero cause→click→consequence beats, and
rough-human→polished-product payoffs. Cap ~4 per video. Each tagged beat becomes an entry
in the zoom plan (`scripts/keyframe_zooms.py`): driver-clock time + focus region + zoom
level, applied to the UNCUT take before any length editing (see editing-palmier.md).
Deciding attention at script time, from flow logic, is what keeps the edit's camera moves
meaningful instead of decorative.

## Review checklist (run against every shotlist draft)

- [ ] Every click has a visible cause AND a ≤400ms visible consequence
- [ ] Product-carries-user affordances used everywhere except the montage
- [ ] At least one rough-human → polished-product beat per demo
- [ ] No configuration screens; no empty states
- [ ] Each interaction concept introduced once, reused as a twin thereafter
- [ ] Background-work claims have both a delegation moment and on-camera evidence
- [ ] Every flow: motivated entry → 3–7 interactions → verifiable state change
- [ ] One hero flow per chapter at full depth; breadth lives in the montage
- [ ] All opened loops close on camera; cross-surface state persists
- [ ] No demo-only interactions without an owner-approved claim flag

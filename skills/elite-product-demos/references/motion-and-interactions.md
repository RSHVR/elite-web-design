# Motion Design & Interactions

The camera never moves during a take — all cinematography inside the take IS the motion
design: what animates, when, how long, and what it sounds like. These patterns were tuned
across ~10 owner rehearsal passes; the timings are the surviving values, not first drafts.

## Philosophy

- **One motion, one meaning.** Each beat gets one intentional animation. If two things
  move at once, the viewer follows neither.
- **Sound is punctuation, not soundtrack.** One sound per moment, each with a fixed
  meaning (send = whoosh, arrival = ding, notification = chime, press = click). When two
  sounds stack within a few seconds, delete the less meaningful one — a task-complete
  chime died because it sat between a send-whoosh and a banner-chime.
- **Everything finishes before its consequence.** An animation must complete before the
  click that depends on it; the driver waits (`waitStable`), never talks over the UI.
- **Never animate what must be read.** Motion during required reading resets the
  viewer's eyes (each movement triggers a saccade back to it). Land the element, let it
  settle ~0.3–0.5s, THEN start the reading clock (budgets in pacing-canon.md's reading
  math). Typewriters are the one exception — they guide the read at typing speed.
- **The cursor is an actor.** Its stillness is as expressive as its motion.

## Text & typewriter moments

- **Typewriter hook**: hold the empty brand card ~2s (caret blinking) before typing.
  Pace: ~38ms per space, 48–70ms per character with jitter. The type–delete–retype
  pattern (type phrase A, beat ~750ms, delete in reverse at ~24ms/char, beat ~380ms, type
  phrase B) creates a "thought revision" moment worth more than any transition.
- **In-UI typewriters** (an AI rewriting a draft): hero moments get per-character typing
  at hook pace — a 200-char rewrite taking ~12 watchable seconds IS the feature demo.
  Non-hero text renders instantly. Never mid-speed: 7-chars-per-tick reads as a glitch,
  not typing.
- Scroll-pin the container to the newest text while it types.

## AI & response beats

- **Thinking indicators**: minimum 1.2s of typing-bubbles before any staged AI response.
  Instant answers read as fake precisely because they're instant.
- **Staged planning beats** for impressive moments: thinking → a status line
  ("Researching…") → the concept/decision → the payload card, at 1.5–2s per stage. This
  converts a data dump into visible reasoning.
- **Voice bubbles**: animated waveform bars + word-by-word transcript (~95ms/word) if an
  AI speaks; the spoken audio and on-screen words must match exactly.

## Cards, decks, lists

- **Card entrance**: 200ms fade+rise (`opacity + translateY(5px)`) is enough. Chat-style
  UIs: anchor the scroll to the FIRST message of a burst and DO NOT re-anchor follow-up
  messages — re-anchoring scrolls the first message off screen (real bug, caught by the
  owner on a take).
- **Carousel decks** (send-one-pull-next): fly-away ~340ms (up + scale + fade), then the
  strip slides the next card in. **Uniform card heights** — fix the content area height so
  the primary button sits in the same spot on every card; the cursor then doesn't move
  between repeated actions (stillness reads as competence).
- **Task/checklist completion theater**: checkbox tick → 360ms slide-out right at full
  height → the emptied slot collapses → rows below glide up → (optional) next item enters
  from below. No celebratory sfx when other audio is nearby.
- **Progress bars animate on entrance**: render at 0, wait ~450ms after the card lands,
  ease to the target over ~0.9s (cubic-bezier). A pre-filled bar is dead pixels; the fill
  is the story. Static label ("50%") beside an animating fill reads as "counting up".

## Notifications & interruptions

- **Banner pattern**: slide in from the right edge (translateX 24px + opacity, ~350ms
  ease-out) with a chime, action buttons inside, × to dismiss. All notification types
  share ONE visual language (a meeting alert and a message alert are twins with different
  copy) — the second occurrence then needs no explanation.
- The banner's action button IS the navigation for the next beat (click "Open message" /
  "Prep for meeting" rather than the nav rail) — interruptions that carry you somewhere
  demonstrate the product doing the carrying.
- Badge ticks (3→4) accompany the ding; the number changing on camera is the proof.

## Cursor choreography

- **Eased glides** (cubic ease-in-out, ~600–800ms for cross-screen, 400–500ms short).
- **Dispatch real hover events on arrival** (pointerover/mouseover/mouseenter, and leave
  events on the previous target) — CSS/JS hover states never fire from a drawn cursor's
  motion alone, and dead hovers make the UI look unfinished.
- **Press**: ~120ms scale-dip of the cursor + click sfx. No glow rings or ripples — they
  read as screen-recorder chrome, not product.
- **Stillness discipline**: skip glides under ~5px; wait for target-rect stability before
  gliding (animating layouts otherwise cause visible cursor bobbing); after the last
  interactive beat, hide the cursor entirely for montage/outro.
- The OS cursor is excluded from capture; the drawn cursor is the only one on film.

## Transitions & time

- **Chapter cards**: full-bleed brand color, one word, ~2.1s (300ms fades). They are the
  spoken frame made visible, and scrub-stops for viewers.
- **Montage**: cursorless hard cuts, 1.5–1.7s per page, ordered to match a visible
  structure (e.g. walking the nav top-to-bottom).
- **Time-skips**: prefer carrying them in VO ("Five minutes before the ten o'clock…").
  On-screen clock pills were tried and cut as clutter.
- **No screen-transition effects** (wipes/crossfades) inside the take — the app's own
  navigation is the transition. Cheap effects scream template.

## Edit-side motion (applied in the NLE, not the driver)

- **Attention punch-ins**: zoom ~1.25–1.35× toward a fixed focus point, ~0.8s ease in,
  hold through the action it highlights, ease back out. Reserve for interruptions
  (notifications) and one or two hero clicks — more than ~4 zooms per video reads as
  seasickness. Time them to the AUDIO event (chime/ding onset), not eyeballed frames.
- **Floating-window compositing**: capture the window with alpha, float it at ~0.88 scale
  over a background image; punch-ins keep their absolute zoomed size (recompute top-left
  so the focus point doesn't drift when the resting scale changes).
- **Speed ramps**: owners consistently run endings at 2×. Split the clip at the owner's
  marker and speed the tail rather than pre-animating a faster ending.

# Critical Rules

Rules that must pass before deployment. Failures in this category represent accessibility violations, performance blockers, or broken functionality.

## Table of Contents

1. [Contrast & Color](#contrast--color)
2. [Focus & Keyboard](#focus--keyboard)
3. [Touch Targets](#touch-targets)
4. [Reduced Motion](#reduced-motion)
5. [Core Web Vitals](#core-web-vitals)
6. [GPU Animation Properties](#gpu-animation-properties)
7. [GSAP Cleanup](#gsap-cleanup)
8. [Viewport & Zoom](#viewport--zoom)
9. [Ethics & Trust](#ethics--trust)

---

## Contrast & Color

### C-01: Normal text contrast ≥ 4.5:1

**Check:** All body text (< 18pt or < 14pt bold) meets 4.5:1 contrast ratio against its background
**Fix:** → `elite-accessibility` / wcag-contrast.md
**Test:** DevTools > CSS Overview > Colors, or WebAIM Contrast Checker

### C-02: Large text contrast ≥ 3:1

**Check:** Text ≥ 18pt (or ≥ 14pt bold) meets 3:1 contrast ratio
**Fix:** → `elite-accessibility` / wcag-contrast.md
**Test:** Measure font size, check contrast of headings and display text

### C-03: UI component contrast ≥ 3:1

**Check:** Buttons, inputs, icons meet 3:1 against adjacent backgrounds
**Fix:** → `elite-accessibility` / wcag-contrast.md
**Test:** Check interactive element borders/fills against their backgrounds

### C-04: Color not the sole indicator

**Check:** Information conveyed by color is also conveyed by icon, text, or pattern
**Fix:** → `elite-accessibility` / wcag-contrast.md
**Test:** View page in grayscale (DevTools > Rendering > Emulate vision deficiency); verify meaning preserved

### C-05: Link text distinguishable without color alone

**Check:** Links within body text are underlined or have non-color visual indicator
**Fix:** → `elite-accessibility` / wcag-contrast.md
**Test:** View page in grayscale; verify links are still identifiable

### C-06: Error states use icon + color

**Check:** Form error indicators use both red color and an icon/text label
**Fix:** → `elite-accessibility` / wcag-contrast.md
**Test:** Trigger validation error; verify icon accompanies color change

---

## Focus & Keyboard

### C-07: Focus ring visible on all interactive elements

**Check:** Every focusable element shows a visible focus indicator (≥ 2px outline, ≥ 2px offset)
**Fix:** → `elite-accessibility` / focus-keyboard.md
**Test:** Tab through entire page; verify every link, button, input shows focus state

### C-08: Focus ring contrast ≥ 3:1

**Check:** Focus indicator contrasts with both the element and surrounding background
**Fix:** → `elite-accessibility` / focus-keyboard.md
**Test:** Check outline color against page background

### C-09: Tab order matches visual order

**Check:** Tabbing follows the visual reading order (left→right, top→bottom)
**Fix:** → `elite-accessibility` / focus-keyboard.md
**Test:** Tab through page; verify sequence makes sense

### C-10: Modal focus trap

**Check:** When modal is open, Tab stays within modal; Escape dismisses
**Fix:** → `elite-accessibility` / focus-keyboard.md
**Test:** Open modal, Tab repeatedly; verify focus doesn't escape to background

### C-11: No keyboard traps

**Check:** No element traps focus permanently; user can always Tab away
**Fix:** → `elite-accessibility` / focus-keyboard.md
**Test:** Tab through all interactive elements; verify no dead-ends

### C-12: Custom controls keyboard-operable

**Check:** Custom dropdowns, sliders, tabs, accordions work with arrow keys, Enter, Space, Escape
**Fix:** → `elite-accessibility` / focus-keyboard.md
**Test:** Navigate each custom widget with keyboard only; verify full operability

---

## Touch Targets

### C-13: Touch target minimum 44×44px

**Check:** All interactive elements have at least 44×44px tap area (visual or extended via padding/pseudo-element)
**Fix:** → `elite-accessibility` / touch-interaction.md
**Test:** DevTools > Inspect element; check computed width/height ≥ 44px

### C-14: Touch target spacing ≥ 8px

**Check:** Adjacent touch targets have at least 8px gap
**Fix:** → `elite-accessibility` / touch-interaction.md
**Test:** Inspect gap between adjacent buttons/links

### C-15: Mobile form inputs ≥ 44px height

**Check:** Form inputs on mobile are at least 44px tall
**Fix:** → `elite-ux-strategy` / mobile-conversion.md
**Test:** DevTools responsive mode (375px); check input computed heights

---

## Reduced Motion

### C-16: Every animation has prefers-reduced-motion alternative

**Check:** No animation plays when prefers-reduced-motion: reduce is active
**Fix:** → `elite-accessibility` / reduced-motion.md
**Test:** DevTools > Rendering > Emulate CSS media feature > prefers-reduced-motion: reduce; navigate full page

### C-17: CSS global killswitch present

**Check:** Stylesheet includes `@media (prefers-reduced-motion: reduce) { * { animation-duration: 0.01ms !important; ... } }`
**Fix:** → `elite-accessibility` / reduced-motion.md
**Test:** Grep CSS for `prefers-reduced-motion`; verify global override exists

### C-18: GSAP uses matchMedia dual-branch

**Check:** Every GSAP animation has both `no-preference` and `reduce` branches via `gsap.matchMedia()`
**Fix:** → `elite-accessibility` / reduced-motion.md + `elite-gsap` / utility-library.md
**Test:** Grep JS for `gsap.matchMedia`; verify both branches exist

### C-19: CSS scroll-driven animations degrade without stranding content

**Check:** `animation-timeline: scroll()` and `animation-timeline: view()` appear inside `@media (prefers-reduced-motion: no-preference)`, AND any hidden initial state (`opacity: 0`, `visibility: hidden`, or a hiding transform) is safe when the reveal never runs — i.e. it is one of: (a) confined to `@keyframes { from }` over a visible base, (b) declared over a visible base and scoped to `no-preference`, or (c) additionally wrapped in `@supports (animation-timeline: view())`.
**Fix:** → `elite-css-animations` / scroll-driven-api.md + `elite-accessibility` / reduced-motion.md
**Test:** Grep CSS for `animation-timeline`; verify motion-query wrapping. Then, with reduced motion enabled AND in a browser without scroll-driven support (Firefox stable, 2026), confirm no element is stuck at `opacity: 0` / `visibility: hidden`.
**Fail if:** a base hidden state declared outside the reveal's guard can persist because the reveal animation never executes (reduced-motion users are the common victim — the reveal is gated behind `no-preference`, so nothing brings the content back).

### C-20: Auto-playing video/carousel respects motion preference

**Check:** Auto-playing media pauses when prefers-reduced-motion: reduce is active
**Fix:** → `elite-accessibility` / reduced-motion.md
**Test:** Enable reduced motion; verify auto-play stops

### C-21: Parallax disabled in reduced motion

**Check:** Parallax scrolling effects are removed (not just slowed) for reduced motion users
**Fix:** → `elite-accessibility` / reduced-motion.md
**Test:** Enable reduced motion; verify parallax layers are static

---

## Core Web Vitals

### C-22: LCP ≤ 2.5s

**Check:** Largest Contentful Paint loads within 2.5 seconds
**Fix:** → `elite-performance` / SKILL.md + asset-optimization.md
**Test:** Lighthouse > Performance > LCP

### C-23: INP ≤ 200ms

**Check:** Interaction to Next Paint response within 200ms
**Fix:** → `elite-performance` / SKILL.md
**Test:** Lighthouse > Performance > INP, or Chrome Web Vitals extension

### C-24: CLS ≤ 0.1

**Check:** Cumulative Layout Shift below 0.1
**Fix:** → `elite-performance` / asset-optimization.md
**Test:** Lighthouse > Performance > CLS

### C-25: TTFB ≤ 800ms

**Check:** Time to First Byte under 800ms on server response
**Fix:** → `elite-performance` / SKILL.md
**Test:** Lighthouse > Performance > TTFB, or Network tab timing

### C-26: Total blocking time ≤ 200ms

**Check:** Total Blocking Time (TBT) stays under 200ms
**Fix:** → `elite-performance` / SKILL.md
**Test:** Lighthouse > Performance > TBT

---

## GPU Animation Properties

### C-27: Only transform animated for position/size

**Check:** No animations on `width`, `height`, `top`, `left`, `right`, `bottom`, `margin`, `padding`
**Fix:** → `elite-performance` / animation-performance.md
**Test:** Grep for keyframes/transitions on banned properties; DevTools > Rendering > Paint flashing (nothing should flash during animations)

### C-28: Only opacity animated for visibility

**Check:** No animations on `display` or `visibility` for show/hide effects
**Fix:** → `elite-performance` / animation-performance.md
**Test:** Check animation code; verify opacity + transform only

### C-29: No font-size or border-width animations

**Check:** These properties are never animated (they trigger layout)
**Fix:** → `elite-performance` / animation-performance.md
**Test:** Grep animation/transition declarations for font-size, border-width

### C-30: will-change not applied globally

**Check:** No `* { will-change: ... }` or persistent will-change on many elements
**Fix:** → `elite-performance` / animation-performance.md
**Test:** Grep for will-change; verify only applied temporarily during animation

### C-31: No layout thrashing in animation loops

**Check:** requestAnimationFrame callbacks do not read then write DOM properties in a loop
**Fix:** → `elite-performance` / animation-performance.md
**Test:** DevTools > Performance > record interaction; check for forced reflows

---

## GSAP Cleanup

### C-32: gsap.context() wraps all animations

**Check:** Every animation initialization is wrapped in `gsap.context()`
**Fix:** → `elite-gsap` / utility-library.md
**Test:** Grep for `gsap.from`, `gsap.to`, `ScrollTrigger.create`; verify each is inside a context

### C-33: context.revert() called on unmount

**Check:** Component destruction/unmount calls `ctx.revert()`
**Fix:** → `elite-gsap` / utility-library.md
**Test:** Check framework lifecycle (Svelte destroy, React useEffect cleanup, Vue unmounted)

### C-34: SplitText.revert() called on cleanup

**Check:** SplitText instances are reverted before component destruction
**Fix:** → `elite-gsap` / utility-library.md
**Test:** Grep for `new SplitText`; verify corresponding `.revert()` call

### C-35: ScrollTrigger.kill() on route change

**Check:** SPA route transitions kill or refresh ScrollTrigger instances
**Fix:** → `elite-gsap` / utility-library.md
**Test:** Navigate between pages; check for orphaned ScrollTrigger warnings in console

---

## Viewport & Zoom

### C-36: Viewport meta tag present

**Check:** `<meta name="viewport" content="width=device-width, initial-scale=1">` exists in `<head>`
**Fix:** → `elite-layouts` / editorial-patterns.md
**Test:** View page source; check for viewport meta

### C-37: Zoom not disabled

**Check:** Viewport meta does NOT contain `user-scalable=no` or `maximum-scale=1`
**Fix:** → `elite-layouts` / editorial-patterns.md
**Test:** Grep for `user-scalable=no` or `maximum-scale=1`; must not exist

### C-38: Content readable at 400% zoom

**Check:** All content remains accessible at 400% browser zoom without loss of functionality
**Fix:** → `elite-accessibility` / wcag-contrast.md
**Test:** Zoom to 400%; verify all content reachable, no overlap

---

## Ethics & Trust

### C-39: Scarcity claims use real data

**Check:** "Only X left" badges reflect actual inventory, not fabricated urgency
**Fix:** → `elite-ux-strategy` / social-proof-trust.md + ethical-boundaries.md
**Test:** Verify scarcity numbers come from real-time data source

### C-40: Testimonials are authentic

**Check:** Testimonials from real customers with real names (not AI-generated or stock)
**Fix:** → `elite-ux-strategy` / social-proof-trust.md
**Test:** Verify testimonial sources; check for stock photo reverse image search

### C-41: Pricing is transparent

**Check:** All costs shown upfront; no hidden fees revealed at checkout
**Fix:** → `elite-ux-strategy` / ethical-boundaries.md
**Test:** Walk through purchase flow; verify no surprise charges

### C-42: No dark patterns

**Check:** Cancel/unsubscribe is as easy as signup; no confirmshaming
**Fix:** → `elite-ux-strategy` / ethical-boundaries.md
**Test:** Test cancel flow; verify it's straightforward

### C-43: Cookie consent not manipulative

**Check:** Cookie banner has equal-weight Accept/Reject buttons; no pre-checked boxes
**Fix:** → `elite-ux-strategy` / ethical-boundaries.md
**Test:** Check cookie banner; verify Reject is same size/prominence as Accept

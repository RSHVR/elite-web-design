# Elite Web Design - Skills Collection

A collection of specialized skills for producing premium, award-winning frontend designs with sophisticated animations and layouts.

## Skill Overview

| Skill | Triggers | Purpose |
|-------|----------|---------|
| `elite-design-core` | "elite design", "premium website", "design system" | Design philosophy, process, skill navigation |
| `elite-gsap` | "GSAP", "ScrollTrigger", "SplitText", "animation library" | Complete GSAP ecosystem |
| `elite-css-animations` | "CSS animation", "scroll-driven", "view transition" | CSS-native animations |
| `elite-layouts` | "bento grid", "horizontal scroll", "sticky section" | Layout patterns |
| `elite-performance` | "performance", "60fps", "Core Web Vitals", "Vite" | Build and optimization |
| `elite-accessibility` | "prefers-reduced-motion", "WCAG", "a11y" | Motion accessibility |
| `elite-inspiration` | "inspiration", "Awwwards", "FWA", "reference sites" | Curated site examples |
| `elite-ux-strategy` | "conversion", "CRO", "pricing page", "CTA", "copywriting" | Conversion optimization |
| `elite-brand-design` | "brand design", "visual identity", "logo", "brand guidelines", "tone of voice" | Brand identity creation |
| `elite-audit` | "audit", "review", "QA", "pre-launch", "check quality", "is this ready" | Quality verification & remediation |

## Code Style Guidelines

### Framework-Agnostic First

All code examples use vanilla HTML/CSS/JavaScript. Framework-specific patterns are in dedicated reference files.

```javascript
// GOOD: Framework-agnostic pattern
const ctx = gsap.context(() => {
  gsap.to('.element', { x: 100 });
});
// Cleanup: ctx.revert();

// Framework adaptation notes included where relevant
```

### Accessibility-First

Every animation pattern MUST include `prefers-reduced-motion` handling:

```javascript
// REQUIRED in every animation
gsap.matchMedia().add('(prefers-reduced-motion: reduce)', () => {
  gsap.set('.animated', { opacity: 1, y: 0 }); // Instant state
});

gsap.matchMedia().add('(prefers-reduced-motion: no-preference)', () => {
  gsap.from('.animated', { opacity: 0, y: 50 }); // Full animation
});
```

### GPU-Accelerated Properties Only

For 60fps performance, animate ONLY:
- `transform` (translate, scale, rotate)
- `opacity`

NEVER animate: `width`, `height`, `top`, `left`, `margin`, `padding`

### Copy-Paste Ready

Code examples should be complete and working. Include all necessary imports, setup, and cleanup.

## Cross-Skill Loading Rules

When a skill is loaded, also load its dependencies for complete coverage:

| When this skill loads | Also load | Why |
|-----------------------|-----------|-----|
| `elite-gsap` | `elite-accessibility` | Every animation needs reduced-motion handling |
| `elite-css-animations` | `elite-accessibility` | Every animation needs reduced-motion handling |
| `elite-design-core` | — | Foundation; loads standalone |
| `elite-layouts` | `elite-design-core` | Layouts depend on spacing/container tokens |
| `elite-performance` | — | Loads standalone |
| `elite-accessibility` | — | Loads standalone |
| `elite-inspiration` | `elite-design-core` | Archetypes reference design tokens and typography |
| `elite-ux-strategy` | `elite-design-core` | Conversion patterns depend on visual hierarchy |
| `elite-brand-design` | `elite-design-core` | Brand decisions map to design tokens |
| `elite-audit` | (triggers teaching skills on failure) | Orchestrates fixes via relevant skill |

When starting a new project, load `elite-design-core` first to establish foundations.
When building charts/dashboards, load `elite-design-core` (data-visualization reference).

## Design Philosophy

Elite web design is characterized by:

1. **Restraint over excess** - Every element earns its place
2. **Intentional motion** - Animations serve purpose, never decoration
3. **Whitespace confidence** - Empty space is a design element
4. **Typography hierarchy** - Type creates visual structure
5. **Performance parity** - Sophistication never sacrifices 60fps
6. **Accessible by default** - Reduced motion alternatives always provided
7. **Conversion-conscious** - Beautiful design that also converts

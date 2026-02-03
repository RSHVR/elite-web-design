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

## Cross-Skill References

When working on animations → also load `elite-accessibility`
When setting up a project → also load `elite-performance`
When choosing techniques → start with `elite-design-core` decision frameworks
When seeking direction → load `elite-inspiration`

## Design Philosophy

Elite web design is characterized by:

1. **Restraint over excess** - Every element earns its place
2. **Intentional motion** - Animations serve purpose, never decoration
3. **Whitespace confidence** - Empty space is a design element
4. **Typography hierarchy** - Type creates visual structure
5. **Performance parity** - Sophistication never sacrifices 60fps
6. **Accessible by default** - Reduced motion alternatives always provided

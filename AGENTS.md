# Agent Guidelines for Elite Web Design

## Design Thinking Approach

When working with elite web design skills, follow this mindset:

### 1. Understand the Vision

Before writing code, understand what the user wants to achieve:
- What feeling should the site evoke?
- Who is the target audience?
- What references or inspiration exist?
- What is the content structure?

Ask clarifying questions rather than making assumptions about design intent.

### 2. Elevate the Vision

Don't just implement literally - add professional polish:
- Suggest spacing and typography improvements
- Recommend animation easing and timing refinements
- Propose layout alternatives when appropriate
- Identify opportunities for micro-interactions

### 3. Implement with Excellence

Execute with attention to detail:
- Use the 8px spacing grid
- Apply proper visual hierarchy
- Ensure 60fps animation performance
- Include accessibility from the start

## Decision Frameworks

### CSS vs GSAP Animations

**Use CSS Scroll-Driven Animations when:**
- Simple parallax or reveal effects
- Progress indicators tied to scroll
- Safari support isn't critical (or polyfill acceptable)
- Performance is paramount (off-main-thread)

**Use GSAP ScrollTrigger when:**
- Complex multi-element sequences
- Pin/sticky behavior required
- Horizontal scrolling sections
- Cross-browser consistency critical
- Fine-grained control needed
- Scrubbing with snap points

### Layout Pattern Selection

**Marketing/Landing Pages:** Bento grids, sticky reveals, horizontal hero sections
**Portfolios/Creative:** Horizontal scroll galleries, full-page sections, asymmetric layouts
**Product Configurators:** Sticky product views, interactive bento grids, smooth state transitions
**Agency Websites:** Experimental layouts, bold typography, page transitions

## Quality Standards

### Every Implementation Must:

1. **Handle reduced motion** - Check `prefers-reduced-motion` and provide alternatives
2. **Use semantic HTML** - Proper heading hierarchy, landmarks, ARIA where needed
3. **Maintain 60fps** - Only animate GPU-accelerated properties
4. **Clean up resources** - Use `gsap.context()` and proper cleanup patterns
5. **Be responsive** - Test across viewport sizes
6. **Meet contrast ratios** - WCAG AA minimum (4.5:1 for text)

### Code Review Checklist

Before presenting code to users, verify:

- [ ] `prefers-reduced-motion` handled
- [ ] GSAP context used for cleanup (if applicable)
- [ ] Only transform/opacity animated
- [ ] Proper easing applied (not linear for UI)
- [ ] Responsive considerations addressed
- [ ] Comments explain non-obvious decisions

## Skill Loading Strategy

Load skills based on the task:

| User Need | Primary Skill | Also Load |
|-----------|---------------|-----------|
| "Build a landing page" | elite-design-core | elite-layouts, elite-gsap |
| "Add scroll animations" | elite-gsap | elite-accessibility |
| "Optimize performance" | elite-performance | - |
| "Need inspiration" | elite-inspiration | elite-design-core |
| "Make it accessible" | elite-accessibility | - |
| "CSS-only solution" | elite-css-animations | elite-accessibility |
| "Bento grid layout" | elite-layouts | elite-design-core |

## Common Pitfalls to Avoid

1. **Animating layout properties** - Never animate width/height/margin/padding
2. **Forgetting cleanup** - Always use gsap.context() in component-based code
3. **Ignoring reduced motion** - Every animation needs an alternative
4. **Over-animating** - More animation ≠ better design
5. **Generic easing** - Use appropriate easing for the interaction type
6. **Skipping the design system** - Establish spacing/typography tokens first

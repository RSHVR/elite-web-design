# Color Theory

Color establishes mood, creates hierarchy, and ensures accessibility. A systematic approach to color tokens creates consistency across all design decisions.

## Table of Contents

1. [Color Token Structure](#color-token-structure)
2. [Semantic Colors](#semantic-colors)
3. [Contrast & Accessibility](#contrast--accessibility)
4. [Dark Mode](#dark-mode)
5. [Color in UI](#color-in-ui)
6. [Tools & Resources](#tools--resources)

---

## Color Token Structure

### Primitive Colors (Base Palette)

Define raw color values first, then reference them semantically.

```css
:root {
  /* Primitive: Blue scale */
  --blue-50: #eff6ff;
  --blue-100: #dbeafe;
  --blue-200: #bfdbfe;
  --blue-300: #93c5fd;
  --blue-400: #60a5fa;
  --blue-500: #3b82f6;
  --blue-600: #2563eb;
  --blue-700: #1d4ed8;
  --blue-800: #1e40af;
  --blue-900: #1e3a8a;
  --blue-950: #172554;

  /* Primitive: Neutral scale */
  --neutral-50: #fafafa;
  --neutral-100: #f5f5f5;
  --neutral-200: #e5e5e5;
  --neutral-300: #d4d4d4;
  --neutral-400: #a3a3a3;
  --neutral-500: #737373;
  --neutral-600: #525252;
  --neutral-700: #404040;
  --neutral-800: #262626;
  --neutral-900: #171717;
  --neutral-950: #0a0a0a;

  /* Primitive: Additional colors */
  --red-500: #ef4444;
  --red-600: #dc2626;
  --green-500: #22c55e;
  --green-600: #16a34a;
  --amber-500: #f59e0b;
  --amber-600: #d97706;
}
```

### Why Scale from 50-950?

- **50-100**: Backgrounds, subtle fills
- **200-300**: Borders, dividers, disabled states
- **400-500**: Secondary text, icons
- **600-700**: Primary actions, links
- **800-900**: Text, high emphasis
- **950**: Maximum contrast

---

## Semantic Colors

Map primitives to semantic tokens for maintainability.

```css
:root {
  /* Text colors */
  --color-text-primary: var(--neutral-900);
  --color-text-secondary: var(--neutral-600);
  --color-text-muted: var(--neutral-500);
  --color-text-inverted: var(--neutral-50);

  /* Background colors */
  --color-bg-primary: var(--neutral-50);
  --color-bg-secondary: var(--neutral-100);
  --color-bg-tertiary: var(--neutral-200);
  --color-bg-inverted: var(--neutral-900);

  /* Border colors */
  --color-border: var(--neutral-200);
  --color-border-strong: var(--neutral-300);
  --color-border-focus: var(--blue-500);

  /* Interactive colors */
  --color-accent: var(--blue-600);
  --color-accent-hover: var(--blue-700);
  --color-accent-light: var(--blue-100);

  /* Feedback colors */
  --color-success: var(--green-600);
  --color-success-light: #dcfce7;
  --color-error: var(--red-600);
  --color-error-light: #fef2f2;
  --color-warning: var(--amber-600);
  --color-warning-light: #fffbeb;
}
```

### Using Semantic Tokens

```css
/* Always use semantic tokens in components */
.card {
  background: var(--color-bg-primary);
  border: 1px solid var(--color-border);
}

.card-title {
  color: var(--color-text-primary);
}

.card-description {
  color: var(--color-text-secondary);
}

.btn-primary {
  background: var(--color-accent);
  color: var(--color-text-inverted);
}

.btn-primary:hover {
  background: var(--color-accent-hover);
}
```

---

## Contrast & Accessibility

### WCAG Requirements

| Level | Normal Text | Large Text (18px+ or 14px+ bold) |
|-------|-------------|----------------------------------|
| AA | 4.5:1 | 3:1 |
| AAA | 7:1 | 4.5:1 |

### Testing Contrast

```css
/* PASSES AA for normal text (4.5:1+) */
.text-primary {
  color: #171717;      /* neutral-900 */
  background: #fafafa; /* neutral-50 */
  /* Contrast: 18.2:1 ✓ */
}

/* PASSES AA for normal text */
.text-secondary {
  color: #525252;      /* neutral-600 */
  background: #fafafa; /* neutral-50 */
  /* Contrast: 7.5:1 ✓ */
}

/* FAILS AA for normal text */
.text-muted {
  color: #a3a3a3;      /* neutral-400 */
  background: #fafafa; /* neutral-50 */
  /* Contrast: 3.0:1 ✗ - Only use for large text */
}
```

### Safe Combinations

```css
/* Light backgrounds */
--safe-text-on-light: var(--neutral-800);  /* 12.6:1 on white */
--safe-secondary-on-light: var(--neutral-600);  /* 7.5:1 on white */

/* Dark backgrounds */
--safe-text-on-dark: var(--neutral-100);  /* 15.9:1 on neutral-900 */
--safe-secondary-on-dark: var(--neutral-300);  /* 9.7:1 on neutral-900 */

/* Accent on light */
--safe-accent: var(--blue-700);  /* 4.6:1 on white - just passes AA */
```

### APCA (Advanced Perceptual Contrast Algorithm)

APCA is the emerging standard, more accurate for modern displays:

| Content Type | APCA Target |
|--------------|-------------|
| Body text | Lc 75-90 |
| Large headlines | Lc 45-60 |
| Placeholder text | Lc 60+ |

---

## Dark Mode

### Don't Just Invert

Dark mode isn't simply inverting colors. Key principles:

1. **Reduce contrast** - Pure white (#fff) on pure black (#000) is harsh
2. **Desaturate colors** - Vivid colors are too bright on dark
3. **Elevate with lightness** - Higher surfaces are lighter (not darker)
4. **Preserve hierarchy** - Primary text should still be most prominent

### Dark Mode Token Mapping

```css
/* Light mode (default) */
:root {
  --color-text-primary: var(--neutral-900);
  --color-text-secondary: var(--neutral-600);
  --color-bg-primary: var(--neutral-50);
  --color-bg-secondary: var(--neutral-100);
  --color-bg-elevated: white;
  --color-border: var(--neutral-200);
  --color-accent: var(--blue-600);
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  :root {
    --color-text-primary: var(--neutral-100);
    --color-text-secondary: var(--neutral-400);
    --color-bg-primary: var(--neutral-950);
    --color-bg-secondary: var(--neutral-900);
    --color-bg-elevated: var(--neutral-800);  /* Lighter = elevated */
    --color-border: var(--neutral-800);
    --color-accent: var(--blue-400);  /* Lighter accent for dark bg */
  }
}
```

### Manual Dark Mode Toggle

```css
/* System preference */
@media (prefers-color-scheme: dark) {
  :root { /* dark tokens */ }
}

/* Manual override via data attribute */
[data-theme="dark"] {
  --color-text-primary: var(--neutral-100);
  --color-bg-primary: var(--neutral-950);
  /* ... other dark tokens */
}

[data-theme="light"] {
  --color-text-primary: var(--neutral-900);
  --color-bg-primary: var(--neutral-50);
  /* ... other light tokens */
}
```

```javascript
// Toggle theme
function toggleTheme() {
  const current = document.documentElement.dataset.theme;
  document.documentElement.dataset.theme = current === 'dark' ? 'light' : 'dark';
}
```

### Dark Mode Surface Elevation

```css
/* Dark mode: lighter = higher elevation */
:root[data-theme="dark"] {
  --color-surface-0: var(--neutral-950);  /* Base layer */
  --color-surface-1: var(--neutral-900);  /* Cards, panels */
  --color-surface-2: var(--neutral-800);  /* Elevated cards, dropdowns */
  --color-surface-3: var(--neutral-700);  /* Modals, popovers */
}
```

---

## Color in UI

### The 60-30-10 Rule

- **60%**: Dominant color (background)
- **30%**: Secondary color (cards, surfaces)
- **10%**: Accent color (CTAs, highlights)

```css
body {
  background: var(--color-bg-primary);  /* 60% */
}

.card {
  background: var(--color-bg-secondary);  /* 30% */
}

.btn-primary {
  background: var(--color-accent);  /* 10% */
}
```

### Color for Hierarchy

```css
/* Primary content - full contrast */
.heading { color: var(--color-text-primary); }

/* Supporting content - reduced contrast */
.subheading { color: var(--color-text-secondary); }

/* Metadata - minimal contrast */
.meta { color: var(--color-text-muted); }
```

### Color for State

```css
/* Interactive states */
.link {
  color: var(--color-accent);
}

.link:hover {
  color: var(--color-accent-hover);
}

.link:focus-visible {
  outline: 2px solid var(--color-border-focus);
  outline-offset: 2px;
}

/* Feedback states */
.input-error {
  border-color: var(--color-error);
}

.message-success {
  background: var(--color-success-light);
  color: var(--color-success);
}
```

### Avoid Color-Only Communication

Never rely on color alone to convey meaning:

```html
<!-- BAD: Color only -->
<span class="status-dot red"></span>

<!-- GOOD: Color + icon/text -->
<span class="status-dot red">
  <svg aria-hidden="true"><!-- error icon --></svg>
  <span class="sr-only">Error</span>
</span>

<!-- Or -->
<span class="status-dot red" aria-label="Error status"></span>
```

---

## Tools & Resources

### Color Tools

- **[Realtime Colors](https://realtimecolors.com)** - Visualize palette on real UI
- **[Coolors](https://coolors.co)** - Palette generation
- **[Contrast Checker](https://webaim.org/resources/contrastchecker/)** - WCAG contrast testing
- **[APCA Contrast Calculator](https://www.myndex.com/APCA/)** - APCA testing
- **[Radix Colors](https://www.radix-ui.com/colors)** - Accessible color scales

### Generating Scales

Use tools like [Tailwind CSS Color Generator](https://uicolors.app/) or [Leonardo](https://leonardocolor.io/) to generate consistent scales from a base color.

### Quick Contrast Reference

```
White (#ffffff) background:
  neutral-900: 18.2:1 ✓ AAA
  neutral-800: 12.6:1 ✓ AAA
  neutral-700: 9.0:1  ✓ AAA
  neutral-600: 7.5:1  ✓ AAA
  neutral-500: 4.6:1  ✓ AA
  neutral-400: 3.0:1  ✓ Large text only

Black (#000000) background:
  neutral-100: 18.0:1 ✓ AAA
  neutral-200: 15.4:1 ✓ AAA
  neutral-300: 11.7:1 ✓ AAA
  neutral-400: 7.0:1  ✓ AAA
  neutral-500: 4.6:1  ✓ AA
```

---

## Quick Checklist

- [ ] Primitive color scales defined (50-950)
- [ ] Semantic tokens map to primitives
- [ ] All text meets WCAG AA contrast (4.5:1)
- [ ] Interactive elements have visible focus states
- [ ] Dark mode properly designed (not just inverted)
- [ ] Color is never the only indicator of meaning
- [ ] Accent color used sparingly (10% rule)

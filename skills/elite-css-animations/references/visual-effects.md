# Visual Effects

CSS visual effects for premium design: clip-path, masks, filters, and blend modes.

## Table of Contents

1. [Clip-Path Animations](#clip-path-animations)
2. [CSS Masks](#css-masks)
3. [Backdrop Filter](#backdrop-filter)
4. [Mix Blend Mode](#mix-blend-mode)
5. [Combined Effects](#combined-effects)

---

## Clip-Path Animations

### Basic Shapes

```css
/* Circle */
.circle-reveal {
  clip-path: circle(0% at 50% 50%);
  transition: clip-path 0.6s ease;
}
.circle-reveal.visible {
  clip-path: circle(100% at 50% 50%);
}

/* Ellipse */
.ellipse-reveal {
  clip-path: ellipse(0% 0% at 50% 50%);
  transition: clip-path 0.6s ease;
}
.ellipse-reveal.visible {
  clip-path: ellipse(100% 100% at 50% 50%);
}

/* Inset (Rectangle) */
.inset-reveal {
  clip-path: inset(0 100% 0 0);  /* Hidden from right */
  transition: clip-path 0.6s ease;
}
.inset-reveal.visible {
  clip-path: inset(0 0 0 0);
}
```

### Directional Reveals

```css
/* Left to right */
.reveal-ltr {
  clip-path: inset(0 100% 0 0);
}
.reveal-ltr.visible {
  clip-path: inset(0 0 0 0);
}

/* Right to left */
.reveal-rtl {
  clip-path: inset(0 0 0 100%);
}
.reveal-rtl.visible {
  clip-path: inset(0 0 0 0);
}

/* Top to bottom */
.reveal-ttb {
  clip-path: inset(0 0 100% 0);
}
.reveal-ttb.visible {
  clip-path: inset(0 0 0 0);
}

/* Bottom to top */
.reveal-btt {
  clip-path: inset(100% 0 0 0);
}
.reveal-btt.visible {
  clip-path: inset(0 0 0 0);
}
```

### Polygon Shapes

```css
/* Triangle */
.triangle {
  clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
}

/* Hexagon */
.hexagon {
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
}

/* Arrow */
.arrow {
  clip-path: polygon(0% 20%, 60% 20%, 60% 0%, 100% 50%, 60% 100%, 60% 80%, 0% 80%);
}

/* Animated polygon */
.morph-shape {
  clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);  /* Diamond */
  transition: clip-path 0.5s ease;
}
.morph-shape:hover {
  clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%);  /* Square */
}
```

### Image Hover Effect

```css
.image-container {
  position: relative;
  overflow: hidden;
}

.image-container img {
  clip-path: inset(0);
  transition: clip-path 0.4s ease, transform 0.4s ease;
}

.image-container:hover img {
  clip-path: inset(10px);
  transform: scale(1.05);
}
```

---

## CSS Masks

### Gradient Mask

```css
.fade-edges {
  mask-image: linear-gradient(
    to right,
    transparent,
    black 10%,
    black 90%,
    transparent
  );
}
```

### Image Mask

```css
.masked-image {
  mask-image: url('mask.svg');
  mask-size: cover;
  mask-position: center;
}
```

### Animated Mask

```css
.reveal-mask {
  mask-image: linear-gradient(
    to right,
    black 0%,
    transparent 0%
  );
  mask-size: 200% 100%;
  mask-position: 100% 0;
  transition: mask-position 0.8s ease;
}

.reveal-mask.visible {
  mask-position: 0 0;
}
```

### Text Mask (Knockout Effect)

```css
.text-knockout {
  background: url('texture.jpg') center/cover;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
```

### SVG Mask

```html
<svg width="0" height="0">
  <defs>
    <mask id="blob-mask">
      <path fill="white" d="...blob path..." />
    </mask>
  </defs>
</svg>
```

```css
.blob-masked {
  mask: url(#blob-mask);
}
```

---

## Backdrop Filter

### Frosted Glass

```css
.glass-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
}
```

### Dark Glass

```css
.dark-glass {
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}
```

### Glass Navigation

```css
.glass-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

@supports not (backdrop-filter: blur(10px)) {
  .glass-nav {
    background: rgba(255, 255, 255, 0.95);
  }
}
```

### Modal Overlay

```css
.modal-backdrop {
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
}
```

### Combined Filters

```css
.complex-glass {
  backdrop-filter:
    blur(10px)
    saturate(150%)
    brightness(1.1)
    contrast(1.1);
}
```

---

## Mix Blend Mode

### Text Over Image

```css
.hero {
  position: relative;
}

.hero-text {
  mix-blend-mode: difference;
  color: white;
}
```

### Color Overlay

```css
.image-with-overlay {
  position: relative;
}

.image-with-overlay::after {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--color-accent);
  mix-blend-mode: multiply;
  opacity: 0.6;
}
```

### Blend Modes Reference

```css
/* Darkening modes */
.darken { mix-blend-mode: darken; }
.multiply { mix-blend-mode: multiply; }
.color-burn { mix-blend-mode: color-burn; }

/* Lightening modes */
.lighten { mix-blend-mode: lighten; }
.screen { mix-blend-mode: screen; }
.color-dodge { mix-blend-mode: color-dodge; }

/* Contrast modes */
.overlay { mix-blend-mode: overlay; }
.soft-light { mix-blend-mode: soft-light; }
.hard-light { mix-blend-mode: hard-light; }

/* Inversion modes */
.difference { mix-blend-mode: difference; }
.exclusion { mix-blend-mode: exclusion; }

/* Component modes */
.hue { mix-blend-mode: hue; }
.saturation { mix-blend-mode: saturation; }
.color { mix-blend-mode: color; }
.luminosity { mix-blend-mode: luminosity; }
```

### Duotone Effect

```css
.duotone {
  position: relative;
  background: var(--color-primary);
}

.duotone img {
  mix-blend-mode: luminosity;
  filter: grayscale(100%) contrast(1.2);
}
```

---

## Combined Effects

### Premium Card Hover

```css
.premium-card {
  position: relative;
  overflow: hidden;
  border-radius: 16px;
}

.premium-card-bg {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  clip-path: circle(0% at 50% 50%);
  transition: clip-path 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.premium-card:hover .premium-card-bg {
  clip-path: circle(150% at 50% 50%);
}

.premium-card-content {
  position: relative;
  z-index: 1;
  padding: 2rem;
}
```

### Reveal with Glass

```css
.glass-reveal {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  clip-path: inset(100% 0 0 0);
  transition:
    clip-path 0.6s cubic-bezier(0.4, 0, 0.2, 1),
    backdrop-filter 0.3s ease;
}

.glass-reveal.visible {
  clip-path: inset(0 0 0 0);
}
```

### Spotlight Effect

```css
.spotlight {
  position: relative;
}

.spotlight::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(
    circle at var(--mouse-x, 50%) var(--mouse-y, 50%),
    transparent 0%,
    rgba(0, 0, 0, 0.8) 50%
  );
  pointer-events: none;
}
```

```javascript
// Track mouse for spotlight
element.addEventListener('mousemove', (e) => {
  const rect = element.getBoundingClientRect();
  const x = ((e.clientX - rect.left) / rect.width) * 100;
  const y = ((e.clientY - rect.top) / rect.height) * 100;
  element.style.setProperty('--mouse-x', `${x}%`);
  element.style.setProperty('--mouse-y', `${y}%`);
});
```

---

## Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  .clip-animated,
  .mask-animated {
    clip-path: none;
    mask: none;
    transition: none;
  }
}
```

---

## Browser Support Notes

- **clip-path**: Full support, including animations
- **mask-image**: Use `-webkit-mask-image` for Safari
- **backdrop-filter**: Full support; provide fallback background
- **mix-blend-mode**: Full support; may affect stacking contexts

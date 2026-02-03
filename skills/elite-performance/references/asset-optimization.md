# Asset Optimization

Optimize images, fonts, and media for fast loading.

## Table of Contents

1. [Image Optimization](#image-optimization)
2. [Font Optimization](#font-optimization)
3. [Lazy Loading](#lazy-loading)
4. [Critical Path](#critical-path)

---

## Image Optimization

### Format Selection

| Format | Use Case | Browser Support |
|--------|----------|-----------------|
| **AVIF** | Photos, illustrations (best compression) | Chrome 85+, Firefox 93+ |
| **WebP** | Photos, illustrations (good fallback) | All modern browsers |
| **PNG** | Transparency, screenshots | Universal |
| **SVG** | Icons, logos, illustrations | Universal |
| **JPEG** | Photos (legacy fallback) | Universal |

### Picture Element with Fallbacks

```html
<picture>
  <!-- Best quality: AVIF -->
  <source
    srcset="image.avif 1x, image@2x.avif 2x"
    type="image/avif"
  >
  <!-- Good fallback: WebP -->
  <source
    srcset="image.webp 1x, image@2x.webp 2x"
    type="image/webp"
  >
  <!-- Universal fallback: JPEG -->
  <img
    src="image.jpg"
    srcset="image.jpg 1x, image@2x.jpg 2x"
    alt="Description"
    width="800"
    height="600"
    loading="lazy"
    decoding="async"
  >
</picture>
```

### Responsive Images

```html
<img
  src="image-800.jpg"
  srcset="
    image-400.jpg 400w,
    image-800.jpg 800w,
    image-1200.jpg 1200w,
    image-1600.jpg 1600w
  "
  sizes="
    (max-width: 600px) 100vw,
    (max-width: 1200px) 50vw,
    800px
  "
  alt="Description"
  loading="lazy"
  decoding="async"
>
```

### Image Compression Targets

| Image Type | Quality | Max File Size |
|------------|---------|---------------|
| Hero images | 80-85% | < 200KB |
| Product images | 75-80% | < 100KB |
| Thumbnails | 70-75% | < 30KB |
| Icons (PNG) | Lossless | < 10KB |
| Icons (SVG) | Optimized | < 5KB |

### Build-Time Optimization

```javascript
// vite.config.js
import viteImagemin from 'vite-plugin-imagemin';

export default {
  plugins: [
    viteImagemin({
      gifsicle: { optimizationLevel: 7 },
      mozjpeg: { quality: 80 },
      pngquant: { quality: [0.7, 0.9] },
      webp: { quality: 80 },
      avif: { quality: 65 }
    })
  ]
};
```

### SVG Optimization

```javascript
// vite.config.js
import svgo from 'vite-plugin-svgo';

export default {
  plugins: [
    svgo({
      plugins: [
        { name: 'removeViewBox', active: false },
        { name: 'removeDimensions', active: true },
        { name: 'removeUselessStrokeAndFill', active: true }
      ]
    })
  ]
};
```

### Background Images

```css
/* Use modern formats in CSS */
.hero {
  background-image: url('hero.jpg');
}

@supports (background-image: url('test.avif')) {
  .hero {
    background-image: url('hero.avif');
  }
}

/* Or use image-set */
.hero {
  background-image: image-set(
    url('hero.avif') type('image/avif'),
    url('hero.webp') type('image/webp'),
    url('hero.jpg') type('image/jpeg')
  );
}
```

---

## Font Optimization

### Subset Fonts

Only include characters you need:

```bash
# Using glyphhanger
glyphhanger --whitelist="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!?'\"()-" --subset=font.woff2
```

### Font Loading Strategy

```css
/* Use font-display */
@font-face {
  font-family: 'CustomFont';
  src: url('font.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap;  /* Show fallback immediately, swap when loaded */
}
```

### font-display Values

| Value | Behavior |
|-------|----------|
| `swap` | Show fallback immediately, swap when ready |
| `fallback` | Short block (100ms), short swap (3s) |
| `optional` | Short block, no swap (may not show custom font) |
| `block` | Long invisible period (not recommended) |

### Preload Critical Fonts

```html
<head>
  <link
    rel="preload"
    href="/fonts/heading.woff2"
    as="font"
    type="font/woff2"
    crossorigin
  >
  <link
    rel="preload"
    href="/fonts/body.woff2"
    as="font"
    type="font/woff2"
    crossorigin
  >
</head>
```

### Variable Fonts

```css
/* Single file for all weights */
@font-face {
  font-family: 'Inter';
  src: url('Inter-Variable.woff2') format('woff2-variations');
  font-weight: 100 900;  /* Full range */
  font-display: swap;
}

/* Use any weight */
.light { font-weight: 300; }
.regular { font-weight: 400; }
.semibold { font-weight: 600; }
.bold { font-weight: 700; }
```

### System Font Stack (Fastest)

```css
/* Zero font loading */
body {
  font-family:
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    'Helvetica Neue',
    Arial,
    sans-serif;
}
```

---

## Lazy Loading

### Native Lazy Loading

```html
<!-- Images -->
<img src="image.jpg" loading="lazy" alt="">

<!-- Iframes -->
<iframe src="video.html" loading="lazy"></iframe>
```

### Intersection Observer

```javascript
// Lazy load images
const lazyImages = document.querySelectorAll('img[data-src]');

const imageObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      img.removeAttribute('data-src');
      imageObserver.unobserve(img);
    }
  });
}, {
  rootMargin: '50px 0px',  // Load 50px before visible
  threshold: 0.01
});

lazyImages.forEach(img => imageObserver.observe(img));
```

### Lazy Load Components

```javascript
// Lazy load heavy components
const heavySections = document.querySelectorAll('[data-component]');

const componentObserver = new IntersectionObserver((entries) => {
  entries.forEach(async (entry) => {
    if (entry.isIntersecting) {
      const section = entry.target;
      const componentName = section.dataset.component;

      // Dynamic import
      const module = await import(`./components/${componentName}.js`);
      module.init(section);

      componentObserver.unobserve(section);
    }
  });
}, {
  rootMargin: '100px 0px'
});

heavySections.forEach(section => componentObserver.observe(section));
```

### Lazy Load GSAP Animations

```javascript
// Only initialize animations when visible
const animatedSections = document.querySelectorAll('.animate-section');

const animationObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      initSectionAnimation(entry.target);
      animationObserver.unobserve(entry.target);
    }
  });
}, {
  rootMargin: '50px 0px'
});

animatedSections.forEach(section => animationObserver.observe(section));

function initSectionAnimation(section) {
  gsap.from(section.querySelectorAll('.animate-item'), {
    opacity: 0,
    y: 30,
    stagger: 0.1,
    duration: 0.6
  });
}
```

### content-visibility

```css
/* Browser skips rendering until near viewport */
.lazy-section {
  content-visibility: auto;
  contain-intrinsic-size: 0 500px;  /* Estimated height */
}
```

---

## Critical Path

### Inline Critical CSS

```html
<head>
  <!-- Critical CSS inline -->
  <style>
    /* Above-the-fold styles only */
    body { margin: 0; font-family: sans-serif; }
    .hero { min-height: 100vh; display: flex; }
    /* ... minimal critical styles ... */
  </style>

  <!-- Full CSS loads async -->
  <link
    rel="stylesheet"
    href="styles.css"
    media="print"
    onload="this.media='all'"
  >
  <noscript>
    <link rel="stylesheet" href="styles.css">
  </noscript>
</head>
```

### Extract Critical CSS

```javascript
// vite.config.js
import critical from 'rollup-plugin-critical';

export default {
  plugins: [
    critical({
      criticalUrl: 'http://localhost:3000',
      criticalBase: './dist',
      criticalPages: [
        { uri: '/', template: 'index' }
      ],
      criticalConfig: {
        inline: true,
        dimensions: [
          { width: 375, height: 667 },
          { width: 1440, height: 900 }
        ]
      }
    })
  ]
};
```

### Resource Hints

```html
<head>
  <!-- Preconnect to external origins -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://cdn.example.com" crossorigin>

  <!-- DNS prefetch for less critical origins -->
  <link rel="dns-prefetch" href="https://analytics.example.com">

  <!-- Preload critical assets -->
  <link rel="preload" href="hero.webp" as="image">
  <link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>

  <!-- Prefetch next page assets -->
  <link rel="prefetch" href="/about.html">
</head>
```

### Script Loading

```html
<!-- Critical scripts -->
<script src="critical.js"></script>

<!-- Non-critical: defer (maintains order, runs after DOM) -->
<script src="app.js" defer></script>

<!-- Non-critical: async (runs ASAP, no order guarantee) -->
<script src="analytics.js" async></script>

<!-- Module scripts are deferred by default -->
<script type="module" src="app.js"></script>
```

### Module Preload

```html
<!-- Preload modules for faster execution -->
<link rel="modulepreload" href="/js/main.js">
<link rel="modulepreload" href="/js/gsap-core.js">
```

---

## Complete Optimization Checklist

### Images
- [ ] Using AVIF/WebP with JPEG fallback
- [ ] Responsive images with srcset/sizes
- [ ] Proper width/height attributes (prevents CLS)
- [ ] Lazy loading below-fold images
- [ ] Compressed to target file sizes
- [ ] SVGs optimized with SVGO

### Fonts
- [ ] Using WOFF2 format
- [ ] Subsetted to needed characters
- [ ] font-display: swap applied
- [ ] Critical fonts preloaded
- [ ] Variable fonts where appropriate

### Loading
- [ ] Critical CSS inlined
- [ ] Full CSS async loaded
- [ ] Scripts deferred/async
- [ ] Resource hints configured
- [ ] Components lazy loaded
- [ ] content-visibility on sections

### Build
- [ ] Assets minified
- [ ] Gzip/Brotli compression
- [ ] Code splitting by route
- [ ] Tree shaking enabled
- [ ] Source maps for prod debugging

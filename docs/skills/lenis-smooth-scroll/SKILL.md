# Lenis Smooth Scroll Guide & Configuration

Lenis provides ultra-smooth, physics-based momentum scrolling for luxury, high-end agency web applications.

## Production Integration:
```html
<script src="https://unpkg.com/lenis@1.1.20/dist/lenis.min.js"></script>
<script>
  const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    smoothWheel: true,
  });
  function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
  }
  requestAnimationFrame(raf);
</script>
```

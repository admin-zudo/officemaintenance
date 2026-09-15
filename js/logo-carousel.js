/* ============================================================
   Logo Carousel   Infinite Horizontal Scroll
   Duplicates items for seamless loop. Pauses on hover.
   Respects prefers-reduced-motion.
   ============================================================ */

(function () {
  'use strict';

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  document.querySelectorAll('.logo-carousel-track').forEach(function (track) {
    if (reducedMotion) {
      track.style.animation = 'none';
      return;
    }

    // Duplicate children for seamless infinite scroll
    const items = Array.from(track.children);
    items.forEach(function (item) {
      const clone = item.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true');
      track.appendChild(clone);
    });
  });
})();


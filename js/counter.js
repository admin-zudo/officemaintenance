/* ============================================================
   Animated Number Counter   Counts from 0 to target value
   Triggered by Intersection Observer when element scrolls
   into view. Respects prefers-reduced-motion.
   
   Usage: Add data-count="100" to any element.
   The text content will animate from 0 to 100.
   Supports optional data-count-suffix="+" etc.
   ============================================================ */

(function () {
  'use strict';

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const counters = document.querySelectorAll('[data-count]');

  if (!counters.length) return;

  // Easing function: ease-out cubic
  function easeOutCubic(t) {
    return 1 - Math.pow(1 - t, 3);
  }

  function animateCounter(el) {
    const target = parseInt(el.getAttribute('data-count'), 10);
    const suffix = el.getAttribute('data-count-suffix') || '';
    const prefix = el.getAttribute('data-count-prefix') || '';
    const duration = 1800; // ms
    const startTime = performance.now();

    if (reducedMotion || isNaN(target)) {
      el.textContent = prefix + target + suffix;
      return;
    }

    function update(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = easeOutCubic(progress);
      const currentValue = Math.round(eased * target);

      el.textContent = prefix + currentValue + suffix;

      if (progress < 1) {
        requestAnimationFrame(update);
      }
    }

    requestAnimationFrame(update);
  }

  // Use IntersectionObserver to trigger animation on scroll
  const observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.3,
      rootMargin: '0px 0px -20px 0px'
    }
  );

  counters.forEach(function (counter) {
    // Set initial value to 0 (or prefix + 0 + suffix)
    if (!reducedMotion) {
      const suffix = counter.getAttribute('data-count-suffix') || '';
      const prefix = counter.getAttribute('data-count-prefix') || '';
      counter.textContent = prefix + '0' + suffix;
    }
    observer.observe(counter);
  });

})();


/* ============================================================
   Scroll Reveal Animations   Intersection Observer
   Applies .revealed class when elements enter viewport.
   Respects prefers-reduced-motion.
   ============================================================ */

(function () {
  'use strict';

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (reducedMotion) {
    // Make everything visible immediately
    document.querySelectorAll('.reveal, .reveal-left, .reveal-right').forEach(function (el) {
      el.classList.add('revealed');
    });
    return;
  }

  // IntersectionObserver for reveal-on-scroll
  const observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.08,
      rootMargin: '0px 0px -30px 0px'
    }
  );

  document.querySelectorAll('.reveal, .reveal-left, .reveal-right').forEach(function (el) {
    observer.observe(el);
  });

})();


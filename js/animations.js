/* ============================================================
   Scroll Reveal Animations   Intersection Observer
   Applies .revealed class when elements enter viewport.
   Respects prefers-reduced-motion.
   ============================================================ */

(function () {
  'use strict';

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Every page: common blocks fade up as they scroll in, siblings slightly staggered
  var AUTO = '.section .section-header, .service-card, .work-card, .project-card, .loc-card, .sol-card, .post-card, ' +
    '.faq-item, .deliver-card, .problem-item, .process-step, .price-card, .area-group, .team-card, .leader-card, ' +
    '.company-card, .contact-card, .approach-steps, .cta-banner .container, .prose > h2, .table-wrap';
  document.querySelectorAll(AUTO).forEach(function (el) {
    if (el.classList.contains('reveal') || el.closest('.page-hero, .home-hero, .fx, .reveal')) return;
    var i = Array.prototype.indexOf.call(el.parentNode.children, el) % 4;
    el.classList.add('reveal');
    if (i) el.classList.add('reveal-delay-' + i);
  });

  // Count-up for figures marked data-count (the final number is already in the HTML)
  function countUp(el) {
    var target = parseInt(el.getAttribute('data-count'), 10);
    if (!target || target < 2) return;
    var start = null, dur = 1200;
    function step(t) {
      if (start === null) start = t;
      var p = Math.min(1, (t - start) / dur);
      el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(step);
    }
    el.textContent = '0';
    requestAnimationFrame(step);
  }

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
          entry.target.querySelectorAll('[data-count]').forEach(countUp);
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


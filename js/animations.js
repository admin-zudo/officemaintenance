/* ============================================================
   Scroll Reveal Animations   Intersection Observer
   Applies .revealed class when elements enter viewport.
   Includes hero text rotator and enhanced animations.
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

  // -- Hero Text Rotator (SEO Safe) ---------------------------
  function initHeroRotator() {
    const headlineEl = document.querySelector('.hero-content h1');
    const descEl = document.querySelector('.hero-description');
    const heroContent = document.querySelector('.hero-content');

    if (!headlineEl || !descEl || !heroContent) return;

    // List of dynamic marketing variations (SEO remains safe as static HTML loads first)
    const variations = [
      {
        headline: 'AI-Focused Zoho Partner &amp; <span class="text-gradient">IT Solutions Provider</span>',
        description: 'We help growing businesses streamline operations, automate workflows, and scale confidently with custom software development, expert Zoho implementation, and seamless system integrations.'
      },
      {
        headline: 'Making Zoho Actually <span class="text-gradient">Work For Your Team</span>',
        description: 'Powerful business systems only deliver value if your team actually embraces them. We build intuitive, streamlined Zoho workflows that drive adoption and deliver clear insights.'
      },
      {
        headline: 'Focus on Your Core Business. <span class="text-gradient">We\'ll Automate the Rest.</span>',
        description: '<span style="font-size: 0.9em; line-height: 1.4;">Redirect your energy toward growth. For everything else, we engineer the custom software, automated processes, and seamless integrations to run your operations on autopilot.</span>'
      },
      {
        headline: 'World-Class Technology, <span class="text-gradient">Delivered Locally</span>',
        description: 'We believe premium engineering doesn\'t require bloated consulting agencies. By investing in local talent, we deliver high-performing custom systems that support our communities.'
      }
    ];

    let currentIndex = 0;
    const intervalTime = 6000; // Change text every 6 seconds

    function changeText() {
      // Fade out
      heroContent.classList.add('changing');

      setTimeout(function () {
        currentIndex = (currentIndex + 1) % variations.length;
        const current = variations[currentIndex];

        // Update content
        headlineEl.innerHTML = current.headline;
        descEl.innerHTML = current.description;

        // Fade in
        heroContent.classList.remove('changing');
      }, 500); // match transition speed
    }

    // Set transition styles dynamically
    const style = document.createElement('style');
    style.innerHTML = `
      .hero-content h1, .hero-content .hero-description {
        transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out;
        opacity: 1;
        transform: translateY(0);
      }
      .hero-content.changing h1, .hero-content.changing .hero-description {
        opacity: 0;
        transform: translateY(-6px);
      }
    `;
    document.head.appendChild(style);

    // Start interval
    setInterval(changeText, intervalTime);
  }

  // Initialize
  initHeroRotator();



})();


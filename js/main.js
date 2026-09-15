/* ============================================================
   Main JavaScript   Navbar, Mobile Menu, Smooth Scroll,
   Scroll Progress, Active Section Highlighting
   ============================================================ */

(function () {
  'use strict';

  // -- Navbar scroll behavior --------------------------------
  const navbar = document.querySelector('.navbar');

  function handleNavbarScroll() {
    if (!navbar) return;
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', handleNavbarScroll, { passive: true });
  handleNavbarScroll(); // initial check

  // -- Scroll Progress Bar -----------------------------------
  const progressBar = document.getElementById('scrollProgress');

  function updateScrollProgress() {
    if (!progressBar) return;
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (docHeight <= 0) return;
    const scrollPercent = (scrollTop / docHeight) * 100;
    progressBar.style.width = scrollPercent + '%';
  }

  window.addEventListener('scroll', updateScrollProgress, { passive: true });
  updateScrollProgress();

  // -- Mobile menu toggle ------------------------------------
  const toggle = document.querySelector('.navbar-toggle');
  const mobileNav = document.querySelector('.navbar-nav');

  if (toggle && mobileNav) {
    toggle.addEventListener('click', function () {
      const isOpen = toggle.classList.toggle('open');
      mobileNav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', isOpen);
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    // Close mobile menu when a link is clicked
    mobileNav.querySelectorAll('.navbar-link').forEach(function (link) {
      link.addEventListener('click', function () {
        toggle.classList.remove('open');
        mobileNav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });

    // Close on escape key
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.classList.contains('open')) {
        toggle.classList.remove('open');
        mobileNav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
        toggle.focus();
      }
    });
  }

  // -- Active nav link (current page) ------------------------
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';

  document.querySelectorAll('.navbar-link').forEach(function (link) {
    const href = link.getAttribute('href');
    if (href === currentPage ||
      (currentPage === '' && href === 'index.html') ||
      (currentPage === 'index.html' && href === 'index.html')) {
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
    }
  });

  // -- Smooth scroll for anchor links ------------------------
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // -- Brand Showcase Modal Injection & Handling --------------
  function initBrandModal() {
    const modalHTML = `
      <div class="brand-modal" id="brandShowcaseModal" role="dialog" aria-modal="true" aria-labelledby="brand-modal-title">
        <div class="brand-modal-content">
          <button class="brand-modal-close" id="brandModalClose" aria-label="Close credentials display">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
          </button>
          <img src="Asset/icons/Zudo Works Logo SVG.svg" alt="Zudo Works logo" class="brand-modal-logo">
          <h3 class="brand-modal-title" id="brand-modal-title">Zudo Works</h3>
          <p class="brand-modal-subtitle">CORPORATION</p>
          <div class="brand-modal-info">
            <div class="brand-modal-info-row">
              <span class="brand-modal-info-label">Status</span>
              <span class="brand-modal-info-value" style="color: var(--color-secondary);">Active Partner</span>
            </div>
            <div class="brand-modal-info-row">
              <span class="brand-modal-info-label">Zoho Relationship</span>
              <span class="brand-modal-info-value">Authorized Partner</span>
            </div>
            <div class="brand-modal-info-row">
              <span class="brand-modal-info-label">Type</span>
              <span class="brand-modal-info-value">CORPORATION Company</span>
            </div>
            <div class="brand-modal-info-row">
              <span class="brand-modal-info-label">Incorporated In</span>
              <span class="brand-modal-info-value">India</span>
            </div>
          </div>
          <a href="company.html" class="btn btn-primary btn-sm">About the Company</a>
        </div>
      </div>
    `;

    document.body.insertAdjacentHTML('beforeend', modalHTML);

    const modal = document.getElementById('brandShowcaseModal');
    const closeBtn = document.getElementById('brandModalClose');

    if (!modal || !closeBtn) return;

    function openModal() {
      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
      closeBtn.focus();
    }

    function closeModal() {
      modal.classList.remove('open');
      document.body.style.overflow = '';
    }

    document.querySelectorAll('.logo-modal-trigger').forEach(function (trigger) {
      trigger.addEventListener('click', function (e) {
        e.preventDefault();
        openModal();
      });
    });

    closeBtn.addEventListener('click', closeModal);

    modal.addEventListener('click', function (e) {
      if (e.target === modal) {
        closeModal();
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && modal.classList.contains('open')) {
        closeModal();
      }
    });
  }

  initBrandModal();

  // -- FAQ Accordion Toggle -------------------------------
  function initFaqAccordion() {
    const faqItems = document.querySelectorAll('.faq-question');
    if (!faqItems.length) return;

    faqItems.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var item = this.closest('.faq-item');
        var isOpen = item.classList.contains('active');

        // Allow multiple open or single open — here we allow multiple
        item.classList.toggle('active');
        var answer = item.querySelector('.faq-answer');
        if (answer) {
          answer.style.display = isOpen ? 'none' : 'block';
        }
      });

      // Keyboard accessibility
      btn.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          this.click();
        }
      });
    });
  }

  initFaqAccordion();

  // -- Roadmap Scroll Indicators ------------------------------
  function initRoadmapScroll() {
    const roadmapWrapper = document.querySelector('.roadmap-wrapper');
    const scrollLeftBtn = document.querySelector('.roadmap-scroll-indicator.left');
    const scrollRightBtn = document.querySelector('.roadmap-scroll-indicator.right');

    if (roadmapWrapper && (scrollLeftBtn || scrollRightBtn)) {
      if (scrollLeftBtn) {
        scrollLeftBtn.addEventListener('click', function () {
          roadmapWrapper.scrollBy({ left: -250, behavior: 'smooth' });
        });
      }
      if (scrollRightBtn) {
        scrollRightBtn.addEventListener('click', function () {
          roadmapWrapper.scrollBy({ left: 250, behavior: 'smooth' });
        });
      }

      // Hide arrows if reached start or end
      const updateArrows = () => {
        if (scrollLeftBtn) {
          scrollLeftBtn.style.opacity = roadmapWrapper.scrollLeft > 10 ? '1' : '0.2';
          scrollLeftBtn.style.pointerEvents = roadmapWrapper.scrollLeft > 10 ? 'auto' : 'none';
        }
        if (scrollRightBtn) {
          const maxScroll = roadmapWrapper.scrollWidth - roadmapWrapper.clientWidth;
          scrollRightBtn.style.opacity = roadmapWrapper.scrollLeft < maxScroll - 10 ? '1' : '0.2';
          scrollRightBtn.style.pointerEvents = roadmapWrapper.scrollLeft < maxScroll - 10 ? 'auto' : 'none';
        }
      };

      roadmapWrapper.addEventListener('scroll', updateArrows, { passive: true });
      window.addEventListener('resize', updateArrows, { passive: true });
      setTimeout(updateArrows, 150);
    }
  }

  initRoadmapScroll();

})();

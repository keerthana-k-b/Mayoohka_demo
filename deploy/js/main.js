/**
 * MAYOOKHA – The Bridal Studio — Main Client Logic
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileDrawer();
  initSearchModal();
  initWishlist();
  initWhatsAppLinks();
  initDesktopDropdown();
  initHeroSlideshow();
  initProductTabs();
  initProductCarousel();
  initQuickViewModal();
  initCelebrationsRow();
  initCelebrationLightbox();
  initScrollFadeUp();
  initReelsCarousel();
  initReelsHoverPreview();
  initReelsModal();
  initInstaCarousel();
  initCarouselAutoAdvance();
});

/**
 * Desktop Dropdown Toggle Support
 */
function initDesktopDropdown() {
  const dropdownTrigger = document.querySelector('.main-nav .nav-item:nth-child(2) > .nav-link');
  const navItem = dropdownTrigger ? dropdownTrigger.closest('.nav-item') : null;

  if (!dropdownTrigger || !navItem) return;

  dropdownTrigger.addEventListener('click', (e) => {
    if (window.innerWidth >= 768) {
      e.preventDefault();
      navItem.classList.toggle('open');
    }
  });

  document.addEventListener('click', (e) => {
    if (!navItem.contains(e.target)) {
      navItem.classList.remove('open');
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      navItem.classList.remove('open');
    }
  });
}

/**
 * Sticky Header Scroll State
 */
function initStickyHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  const handleScroll = () => {
    if (window.scrollY > 20) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
}

/**
 * Mobile Navigation Drawer & Collapsible Accordion
 */
function initMobileDrawer() {
  const toggleBtn = document.querySelector('.mobile-toggle');
  const drawer = document.querySelector('.mobile-drawer');
  const overlay = document.querySelector('.mobile-drawer-overlay');
  const closeBtn = document.querySelector('.drawer-close-btn');
  const accordionBtn = document.querySelector('.drawer-accordion-btn');
  const accordionContent = document.querySelector('.drawer-accordion-content');

  if (!toggleBtn || !drawer || !overlay) return;

  const getFocusableElements = () => {
    return Array.from(
      drawer.querySelectorAll('button:not([disabled]), a[href], input, select, textarea, [tabindex]:not([tabindex="-1"])')
    ).filter(el => el.offsetParent !== null);
  };

  const handleFocusTrap = (e) => {
    if (e.key !== 'Tab') return;
    const focusables = getFocusableElements();
    if (!focusables.length) return;

    const first = focusables[0];
    const last = focusables[focusables.length - 1];

    if (e.shiftKey) {
      if (document.activeElement === first) {
        e.preventDefault();
        last.focus();
      }
    } else {
      if (document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }
  };

  const openDrawer = () => {
    toggleBtn.classList.add('active');
    toggleBtn.setAttribute('aria-expanded', 'true');
    drawer.classList.add('open');
    drawer.setAttribute('aria-hidden', 'false');
    overlay.classList.add('open');
    overlay.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';

    // Focus close button inside drawer
    setTimeout(() => {
      if (closeBtn) {
        closeBtn.focus();
      } else {
        const focusables = getFocusableElements();
        if (focusables.length) focusables[0].focus();
      }
    }, 50);

    document.addEventListener('keydown', handleFocusTrap);
  };

  const closeDrawer = () => {
    toggleBtn.classList.remove('active');
    toggleBtn.setAttribute('aria-expanded', 'false');
    drawer.classList.remove('open');
    drawer.setAttribute('aria-hidden', 'true');
    overlay.classList.remove('open');
    overlay.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';

    document.removeEventListener('keydown', handleFocusTrap);

    // Return focus to hamburger button
    if (toggleBtn) {
      toggleBtn.focus();
    }
  };

  toggleBtn.addEventListener('click', () => {
    if (drawer.classList.contains('open')) {
      closeDrawer();
    } else {
      openDrawer();
    }
  });

  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  overlay.addEventListener('click', closeDrawer);

  // Esc key listener
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('open')) {
      closeDrawer();
    }
  });

  // Accordion toggle
  if (accordionBtn && accordionContent) {
    accordionBtn.addEventListener('click', () => {
      const isOpen = accordionContent.classList.toggle('open');
      accordionBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      const arrow = accordionBtn.querySelector('.nav-arrow');
      if (arrow) {
        arrow.style.transform = isOpen ? 'rotate(-135deg)' : 'rotate(45deg)';
      }
    });
  }

  // Auto-close if screen resized to desktop width
  window.addEventListener('resize', () => {
    if (window.innerWidth >= 768 && drawer.classList.contains('open')) {
      closeDrawer();
    }
  }, { passive: true });
}

/**
 * Search Overlay Modal
 */
function initSearchModal() {
  const searchTriggers = document.querySelectorAll('.search-trigger');
  const modal = document.querySelector('.search-modal-overlay');
  const closeBtn = document.querySelector('.search-close-btn');
  const searchInput = document.querySelector('.search-input');

  if (!modal) return;

  const openSearch = (e) => {
    if (e) e.preventDefault();
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
    setTimeout(() => {
      if (searchInput) searchInput.focus();
    }, 100);
  };

  const closeSearch = () => {
    modal.classList.remove('open');
    document.body.style.overflow = '';
  };

  searchTriggers.forEach(btn => btn.addEventListener('click', openSearch));
  if (closeBtn) closeBtn.addEventListener('click', closeSearch);

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeSearch();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('open')) {
      closeSearch();
    }
  });
}

/**
 * Wishlist Global Counter & Heart Toggle
 */
function initWishlist() {
  const badgeCounts = document.querySelectorAll('.wishlist-badge');
  let wishlistItems = JSON.parse(localStorage.getItem('store_wishlist') || '[]');

  const updateBadge = () => {
    badgeCounts.forEach(b => {
      b.textContent = wishlistItems.length;
      b.style.display = wishlistItems.length > 0 ? 'flex' : 'none';
    });
  };

  const syncCardButtons = () => {
    document.querySelectorAll('.product-card').forEach(card => {
      const pid = card.dataset.productId;
      const btn = card.querySelector('.product-wishlist-btn');
      if (btn) {
        if (wishlistItems.includes(pid)) {
          btn.classList.add('active');
        } else {
          btn.classList.remove('active');
        }
      }
    });
  };

  updateBadge();
  syncCardButtons();

  // Expose global helper for product cards and modal
  window.toggleWishlist = function(productId, btnElement) {
    const index = wishlistItems.indexOf(productId);
    const isAdding = index === -1;

    if (isAdding) {
      wishlistItems.push(productId);
    } else {
      wishlistItems.splice(index, 1);
    }

    localStorage.setItem('store_wishlist', JSON.stringify(wishlistItems));
    updateBadge();

    // Sync all matching card buttons on the page
    document.querySelectorAll(`.product-card[data-product-id="${productId}"] .product-wishlist-btn`).forEach(btn => {
      if (isAdding) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });

    // Sync Quick View modal button if open
    const qvBtn = document.getElementById('qvWishlistBtn');
    if (qvBtn && qvBtn.dataset.productId === productId) {
      if (isAdding) {
        qvBtn.classList.add('active');
      } else {
        qvBtn.classList.remove('active');
      }
    }
  };
}

/**
 * WhatsApp Helper for Prefilled Enquiries
 */
function initWhatsAppLinks() {
  window.openWhatsAppEnquiry = function(itemName) {
    const text = encodeURIComponent(`Hi Mayookha, I am interested in ${itemName || 'a styling consultation'}. Please share details.`);
    window.open(`https://wa.me/918089101784?text=${text}`, '_blank');
  };
}

/**
 * Hero Section Slideshow Controller
 * - 5 Slanted parallelogram photo panels (Desktop)
 * - Single swipeable image (Mobile)
 * - Autoplay, pause on hover, round arrow controls, indicators, touch swipe
 * - Respects prefers-reduced-motion
 */
function initHeroSlideshow() {
  const heroSection = document.querySelector('.hero-section');
  if (!heroSection) return;

  const desktopSlides = heroSection.querySelectorAll('.hero-slide');
  const mobileSlides = heroSection.querySelectorAll('.hero-mobile-slide');
  const prevBtn = heroSection.querySelector('.hero-arrow-prev');
  const nextBtn = heroSection.querySelector('.hero-arrow-next');
  const dots = heroSection.querySelectorAll('.hero-dot');
  const slider = heroSection.querySelector('.hero-slider');

  if (desktopSlides.length === 0) return;

  let currentIndex = 0;
  let autoplayTimer = null;
  const AUTOPLAY_INTERVAL = 5000;

  const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const showSlide = (index) => {
    // Normalise index
    const totalSlides = desktopSlides.length;
    currentIndex = (index + totalSlides) % totalSlides;

    // Update Desktop Slides
    desktopSlides.forEach((slide, idx) => {
      if (idx === currentIndex) {
        slide.classList.add('active');
      } else {
        slide.classList.remove('active');
      }
    });

    // Update Mobile Slides (if matching count or using index modulo)
    if (mobileSlides.length > 0) {
      const mobIndex = currentIndex % mobileSlides.length;
      mobileSlides.forEach((slide, idx) => {
        if (idx === mobIndex) {
          slide.classList.add('active');
        } else {
          slide.classList.remove('active');
        }
      });
    }

    // Update Indicator Dots
    dots.forEach((dot, idx) => {
      if (idx === currentIndex) {
        dot.classList.add('active');
      } else {
        dot.classList.remove('active');
      }
    });
  };

  const nextSlide = () => {
    showSlide(currentIndex + 1);
  };

  const prevSlide = () => {
    showSlide(currentIndex - 1);
  };

  const startAutoplay = () => {
    if (prefersReducedMotion) return;
    stopAutoplay();
    autoplayTimer = setInterval(nextSlide, AUTOPLAY_INTERVAL);
  };

  const stopAutoplay = () => {
    if (autoplayTimer) {
      clearInterval(autoplayTimer);
      autoplayTimer = null;
    }
  };

  // Button Listeners
  if (nextBtn) {
    nextBtn.addEventListener('click', (e) => {
      e.preventDefault();
      nextSlide();
      startAutoplay(); // Reset timer
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', (e) => {
      e.preventDefault();
      prevSlide();
      startAutoplay(); // Reset timer
    });
  }

  // Dot Listeners
  dots.forEach((dot, idx) => {
    dot.addEventListener('click', (e) => {
      e.preventDefault();
      showSlide(idx);
      startAutoplay();
    });
  });

  // Pause on hover
  heroSection.addEventListener('mouseenter', stopAutoplay);
  heroSection.addEventListener('mouseleave', startAutoplay);

  // Mobile Touch Swipe Handling
  let touchStartX = 0;
  let touchEndX = 0;

  if (slider) {
    slider.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
      stopAutoplay();
    }, { passive: true });

    slider.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      handleSwipe();
      startAutoplay();
    }, { passive: true });
  }

  const handleSwipe = () => {
    const swipeThreshold = 45;
    if (touchEndX < touchStartX - swipeThreshold) {
      // Swiped Left -> Next
      nextSlide();
    } else if (touchEndX > touchStartX + swipeThreshold) {
      // Swiped Right -> Prev
      prevSlide();
    }
  };

  // Listen for reduced motion changes dynamically
  if (window.matchMedia) {
    const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    motionQuery.addEventListener('change', (e) => {
      if (e.matches) {
        stopAutoplay();
      } else {
        startAutoplay();
      }
    });
  }

  // Initialize
  showSlide(0);
  startAutoplay();
}

/**
 * Product Showcase Tabs Controller
 */
function initProductTabs() {
  const tabBtns = document.querySelectorAll('.product-tab-btn');
  const tabPanels = document.querySelectorAll('.product-tab-panel');

  if (tabBtns.length === 0) return;

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetTabId = btn.getAttribute('data-tab');

      // Update button active state
      tabBtns.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');

      // Update panel visibility
      tabPanels.forEach(panel => {
        if (panel.id === targetTabId || panel.id === 'tab-' + targetTabId) {
          panel.classList.add('active');
          panel.hidden = false;
          // Switching product tabs resets that carousel to the first card
          const carousel = panel.querySelector('.product-carousel');
          if (carousel) {
            carousel.scrollTo({ left: 0, behavior: 'smooth' });
          }
        } else {
          panel.classList.remove('active');
          panel.hidden = true;
        }
      });

      // Reset autoplay timer for newly active tab
      if (typeof window.onProductTabSwitch === 'function') {
        window.onProductTabSwitch();
      }

      // Update carousel progress thumb for newly active tab
      if (window.updateCarouselProgress) {
        window.updateCarouselProgress();
      }
    });
  });
}

/**
 * Product Carousel Navigation & Progress Bar
 */
function initProductCarousel() {
  const prevBtn = document.querySelector('.carousel-arrow-prev');
  const nextBtn = document.querySelector('.carousel-arrow-next');
  const carousels = document.querySelectorAll('.product-carousel');

  if (carousels.length === 0) return;

  const getActiveCarousel = () => {
    const activePanel = document.querySelector('.product-tab-panel.active');
    return activePanel ? activePanel.querySelector('.product-carousel') : carousels[0];
  };

  // Scroll active carousel
  const scrollCarousel = (direction) => {
    const carousel = getActiveCarousel();
    if (!carousel) return;

    // Card width + gap
    const card = carousel.querySelector('.product-card');
    const scrollAmount = card ? (card.offsetWidth + 24) * 1.5 : 320;

    carousel.scrollBy({
      left: direction * scrollAmount,
      behavior: 'smooth'
    });
  };

  if (prevBtn) {
    prevBtn.addEventListener('click', (e) => {
      e.preventDefault();
      scrollCarousel(-1);
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', (e) => {
      e.preventDefault();
      scrollCarousel(1);
    });
  }

  // Update progress bar on scroll
  carousels.forEach(carousel => {
    carousel.addEventListener('scroll', () => {
      if (window.updateCarouselProgress) {
        window.updateCarouselProgress();
      }
    }, { passive: true });
  });

  // Enable mouse drag-to-scroll for enhanced UX
  carousels.forEach(carousel => {
    let isDown = false;
    let startX = 0;
    let scrollLeft = 0;

    carousel.addEventListener('mousedown', (e) => {
      // Don't drag if clicking buttons or links
      if (e.target.closest('button') || e.target.closest('a')) return;
      isDown = true;
      carousel.style.cursor = 'grabbing';
      startX = e.pageX - carousel.offsetLeft;
      scrollLeft = carousel.scrollLeft;
    });

    carousel.addEventListener('mouseleave', () => {
      isDown = false;
      carousel.style.cursor = 'grab';
    });

    carousel.addEventListener('mouseup', () => {
      isDown = false;
      carousel.style.cursor = 'grab';
    });

    carousel.addEventListener('mousemove', (e) => {
      if (!isDown) return;
      e.preventDefault();
      const x = e.pageX - carousel.offsetLeft;
      const walk = (x - startX) * 1.5;
      carousel.scrollLeft = scrollLeft - walk;
    });
  });

  // Expose global progress updater
  window.updateCarouselProgress = function() {
    const carousel = getActiveCarousel();
    const thumb = document.querySelector('.carousel-progress-thumb');
    if (!carousel || !thumb) return;

    const maxScroll = carousel.scrollWidth - carousel.clientWidth;
    const progress = maxScroll > 0 ? (carousel.scrollLeft / maxScroll) : 0;
    const visibleRatio = carousel.clientWidth / carousel.scrollWidth;
    const thumbWidthPercent = Math.max(18, Math.min(40, visibleRatio * 100));
    const thumbLeftPercent = progress * (100 - thumbWidthPercent);

    thumb.style.width = `${thumbWidthPercent}%`;
    thumb.style.left = `${thumbLeftPercent}%`;
  };

  // Initial update
  setTimeout(window.updateCarouselProgress, 100);
  window.addEventListener('resize', window.updateCarouselProgress);
}

/**
 * Quick View Modal Logic
 */
function initQuickViewModal() {
  const modal = document.getElementById('quickViewModal');
  const closeBtn = document.getElementById('qvCloseBtn');
  const qvWishlistBtn = document.getElementById('qvWishlistBtn');

  if (!modal) return;

  const allProductCards = Array.from(document.querySelectorAll('.product-card'));
  let currentQvIndex = 0;

  const closeModal = () => {
    modal.classList.remove('open');
    document.body.classList.remove('modal-open');
    document.body.style.overflow = '';
  };

  if (closeBtn) closeBtn.addEventListener('click', closeModal);

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('open')) {
      closeModal();
    }
  });

  const showProductByIndex = (index) => {
    if (!allProductCards.length) return;
    currentQvIndex = (index + allProductCards.length) % allProductCards.length;
    const card = allProductCards[currentQvIndex];
    if (card && card.dataset.productId) {
      window.openQuickView(card.dataset.productId);
    }
  };

  // Mobile Touch Swipe Handling to move between products
  let touchStartX = 0;
  let touchEndX = 0;
  modal.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });

  modal.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    const diff = touchEndX - touchStartX;
    if (diff < -45) {
      showProductByIndex(currentQvIndex + 1);
    } else if (diff > 45) {
      showProductByIndex(currentQvIndex - 1);
    }
  }, { passive: true });

  // Global open function
  window.openQuickView = function(productId) {
    const card = document.querySelector(`.product-card[data-product-id="${productId}"]`);
    if (!card) return;

    currentQvIndex = allProductCards.indexOf(card);
    if (currentQvIndex === -1) currentQvIndex = 0;

    const name = card.dataset.name || 'Signature Ensemble';
    const category = card.dataset.category || 'MAYOOKHA';
    const price = card.dataset.price || 'Price on Request';
    const img = card.dataset.img || '';
    const badge = card.dataset.badge || 'Exclusive';
    const desc = card.dataset.desc || 'Bespoke bridal couture and designer apparel by MAYOOKHA.';

    // Populate modal elements
    const imgEl = document.getElementById('qvImg');
    if (imgEl) {
      imgEl.src = img;
      imgEl.alt = name;
    }

    const metaEl = document.getElementById('qvMeta');
    if (metaEl) metaEl.textContent = category;

    const titleEl = document.getElementById('qvTitle');
    if (titleEl) titleEl.textContent = name;

    const priceEl = document.getElementById('qvPrice');
    if (priceEl) priceEl.textContent = price;

    const badgeEl = document.getElementById('qvBadge');
    if (badgeEl) badgeEl.textContent = badge;

    const descEl = document.getElementById('qvDesc');
    if (descEl) descEl.textContent = desc;

    // Prefilled WhatsApp Enquiry link
    const waBtn = document.getElementById('qvWhatsAppBtn');
    if (waBtn) {
      const waText = encodeURIComponent(`Hello Mayookha, I am enquiring about the ${name} (${price}). Please share details.`);
      waBtn.href = `https://wa.me/918089101784?text=${waText}`;
    }

    // Wishlist button state
    if (qvWishlistBtn) {
      qvWishlistBtn.dataset.productId = productId;
      const wishlistItems = JSON.parse(localStorage.getItem('store_wishlist') || '[]');
      if (wishlistItems.includes(productId)) {
        qvWishlistBtn.classList.add('active');
      } else {
        qvWishlistBtn.classList.remove('active');
      }

      qvWishlistBtn.onclick = (e) => {
        e.preventDefault();
        window.toggleWishlist(productId, qvWishlistBtn);
      };
    }

    // Open Modal, lock body scroll and hide floating whatsapp
    modal.classList.add('open');
    document.body.classList.add('modal-open');
    document.body.style.overflow = 'hidden';
  };
}

/**
 * Celebrations Scroll-Snap Track Arrow Controls
 */
function initCelebrationsRow() {
  const track = document.getElementById('celebrationsTrack');
  const prevBtn = document.querySelector('.celebrations-prev');
  const nextBtn = document.querySelector('.celebrations-next');

  if (!track || !prevBtn || !nextBtn) return;

  const getScrollDistance = () => {
    const card = track.querySelector('.celebration-card');
    return card ? card.offsetWidth + 24 : 304;
  };

  prevBtn.addEventListener('click', () => {
    track.scrollBy({ left: -getScrollDistance() * 2, behavior: 'smooth' });
  });

  nextBtn.addEventListener('click', () => {
    track.scrollBy({ left: getScrollDistance() * 2, behavior: 'smooth' });
  });
}

/**
 * Celebration Lightbox Modal with Keyboard and Arrow Navigation
 */
function initCelebrationLightbox() {
  const lightbox = document.getElementById('celebrationLightbox');
  const backdrop = document.getElementById('lightboxBackdrop');
  const closeBtn = document.getElementById('lightboxCloseBtn');
  const prevBtn = document.getElementById('lightboxPrevBtn');
  const nextBtn = document.getElementById('lightboxNextBtn');
  const imgEl = document.getElementById('lightboxImg');
  const captionEl = document.getElementById('lightboxCaption');
  const counterEl = document.getElementById('lightboxCounter');
  const cards = Array.from(document.querySelectorAll('.celebration-card'));

  if (!lightbox || !cards.length) return;

  let currentIndex = 0;

  const openLightbox = (index) => {
    currentIndex = (index + cards.length) % cards.length;
    const card = cards[currentIndex];
    const fullImg = card.dataset.full || '';
    const caption = card.dataset.caption || '';

    if (imgEl) {
      imgEl.src = fullImg;
      imgEl.alt = caption;
    }
    if (captionEl) {
      captionEl.innerHTML = caption;
    }
    if (counterEl) {
      counterEl.textContent = `${currentIndex + 1} / ${cards.length}`;
    }

    lightbox.style.display = 'flex';
    requestAnimationFrame(() => {
      lightbox.classList.add('open');
    });
    document.body.classList.add('modal-open', 'lightbox-open');
    document.body.style.overflow = 'hidden';
  };

  const closeLightbox = () => {
    lightbox.classList.remove('open');
    document.body.classList.remove('modal-open', 'lightbox-open');
    setTimeout(() => {
      lightbox.style.display = 'none';
      if (imgEl) imgEl.src = '';
    }, 280);
    document.body.style.overflow = '';
  };

  const showPrev = () => openLightbox(currentIndex - 1);
  const showNext = () => openLightbox(currentIndex + 1);

  // Mobile Touch Swipe Handling
  let touchStartX = 0;
  let touchEndX = 0;
  lightbox.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });

  lightbox.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    const diff = touchEndX - touchStartX;
    if (diff < -45) {
      showNext();
    } else if (diff > 45) {
      showPrev();
    }
  }, { passive: true });

  // Card click & enter key triggers
  cards.forEach((card, idx) => {
    card.addEventListener('click', () => openLightbox(idx));
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        openLightbox(idx);
      }
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  if (backdrop) backdrop.addEventListener('click', closeLightbox);
  if (prevBtn) prevBtn.addEventListener('click', showPrev);
  if (nextBtn) nextBtn.addEventListener('click', showNext);

  // Keyboard navigation: Esc, Left, Right
  document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('open')) return;

    if (e.key === 'Escape') {
      closeLightbox();
    } else if (e.key === 'ArrowLeft') {
      showPrev();
    } else if (e.key === 'ArrowRight') {
      showNext();
    }
  });
}

/**
 * Gentle staggered fade-up on scroll (IntersectionObserver, reduced-motion safe)
 */
function initScrollFadeUp() {
  const elements = document.querySelectorAll('.reveal-on-scroll');
  if (!elements.length) return;

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    elements.forEach(el => el.classList.add('is-revealed'));
    return;
  }

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-revealed');
        obs.unobserve(entry.target);
      }
    });
  }, {
    root: null,
    rootMargin: '0px 0px -40px 0px',
    threshold: 0.1
  });

  elements.forEach((el, index) => {
    const delay = (index % 4) * 0.12;
    el.style.transitionDelay = `${delay}s`;
    observer.observe(el);
  });
}

/**
 * Reels Horizontal Carousel Controls
 */
function initReelsCarousel() {
  const carousel = document.querySelector('.reels-carousel');
  const prevBtn = document.querySelector('.reels-nav-prev');
  const nextBtn = document.querySelector('.reels-nav-next');

  if (!carousel || !prevBtn || !nextBtn) return;

  const getScrollDistance = () => {
    const card = carousel.querySelector('.reel-card');
    if (!card) return 260;
    const cardRect = card.getBoundingClientRect();
    return (cardRect.width + 18) * 1.5;
  };

  prevBtn.addEventListener('click', () => {
    carousel.scrollBy({ left: -getScrollDistance(), behavior: 'smooth' });
  });

  nextBtn.addEventListener('click', () => {
    carousel.scrollBy({ left: getScrollDistance(), behavior: 'smooth' });
  });

  const updateCenterCard = () => {
    if (window.innerWidth < 1025) return;
    const cards = carousel.querySelectorAll('.reel-card');
    if (!cards.length) return;
    const carouselRect = carousel.getBoundingClientRect();
    const carouselCenter = carouselRect.left + carouselRect.width / 2;

    let closestCard = null;
    let closestDist = Infinity;

    cards.forEach(card => {
      const cardRect = card.getBoundingClientRect();
      const cardCenter = cardRect.left + cardRect.width / 2;
      const dist = Math.abs(carouselCenter - cardCenter);
      if (dist < closestDist) {
        closestDist = dist;
        closestCard = card;
      }
    });

    cards.forEach(card => {
      if (card === closestCard) {
        card.classList.add('is-center');
      } else {
        card.classList.remove('is-center');
      }
    });
  };

  carousel.addEventListener('scroll', updateCenterCard, { passive: true });
  window.addEventListener('resize', updateCenterCard);
  // Initial check after render
  setTimeout(updateCenterCard, 100);
}

/**
 * Desktop Hover Preview for Reel Cards
 * Muted, loads only on hover, mobile never autoplays.
 */
function initReelsHoverPreview() {
  const isHoverCapable = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  if (!isHoverCapable) return;

  const cards = document.querySelectorAll('.reel-card');

  cards.forEach(card => {
    const video = card.querySelector('.reel-card-video');
    if (!video) return;

    card.addEventListener('mouseenter', () => {
      // Pause any other playing card previews
      document.querySelectorAll('.reel-card-video').forEach(v => {
        if (v !== video) {
          v.pause();
          const parent = v.closest('.reel-card');
          if (parent) parent.classList.remove('is-previewing');
        }
      });

      // Lazy load video src
      if (!video.src && video.dataset.src) {
        video.src = video.dataset.src;
        video.load();
      }

      video.muted = true;
      const playPromise = video.play();
      if (playPromise !== undefined) {
        playPromise.then(() => {
          card.classList.add('is-previewing');
        }).catch(() => {});
      }
    });

    card.addEventListener('mouseleave', () => {
      video.pause();
      card.classList.remove('is-previewing');
    });
  });
}

/**
 * Fullscreen Video Player Modal for Reels
 * Controls, sound on, Esc to close, click outside to close, prev/next arrows,
 * WhatsApp Enquire link, and only one video playing at a time.
 */
function initReelsModal() {
  const modal = document.getElementById('reelModal');
  const modalVideo = document.getElementById('reelModalVideo');
  const modalTitle = document.getElementById('reelModalTitle');
  const modalCategory = document.getElementById('reelModalCategory');
  const modalPrice = document.getElementById('reelModalPrice');
  const modalEnquireBtn = document.getElementById('reelModalEnquireBtn');
  const closeBtn = document.getElementById('reelModalClose');
  const prevBtn = document.getElementById('reelModalPrev');
  const nextBtn = document.getElementById('reelModalNext');

  if (!modal || !modalVideo) return;

  // Collect reel data from cards on page
  const cards = Array.from(document.querySelectorAll('.reel-card'));
  if (!cards.length) return;

  const reelsData = cards.map(c => {
    const posterImg = c.querySelector('.reel-card-poster');
    return {
      video: c.dataset.video || '',
      poster: posterImg ? posterImg.getAttribute('src') || '' : '',
      title: c.dataset.title || 'MAYOOKHA Bridal Studio',
      category: c.dataset.category || 'Contemporary Fashion',
      price: c.dataset.price || '',
    };
  });

  let currentReelIndex = 0;

  const loadReel = (index) => {
    currentReelIndex = index;
    const item = reelsData[currentReelIndex];
    if (!item) return;

    // Pause all preview videos on cards
    document.querySelectorAll('.reel-card-video').forEach(v => {
      v.pause();
      const parent = v.closest('.reel-card');
      if (parent) parent.classList.remove('is-previewing');
    });

    // Set modal video & un-mute for full player experience
    modalVideo.pause();
    if (item.poster) {
      modalVideo.poster = item.poster;
    }
    modalVideo.src = item.video;
    modalVideo.muted = false;
    modalVideo.load();

    if (modalTitle) modalTitle.textContent = item.title;
    if (modalCategory) modalCategory.textContent = item.category;
    if (modalPrice) modalPrice.textContent = item.price;

    if (modalEnquireBtn) {
      const waMsg = encodeURIComponent(`Hello Mayookha, I would like to enquire about the ${item.title} (${item.price}) from your Watch & Shop showcase.`);
      modalEnquireBtn.href = `https://wa.me/918089101784?text=${waMsg}`;
    }

    const playPromise = modalVideo.play();
    if (playPromise !== undefined) {
      playPromise.catch(() => {});
    }
  };

  const openModal = (index) => {
    loadReel(index);
    modal.classList.add('open');
    document.body.classList.add('modal-open', 'reel-modal-open');
    document.body.style.overflow = 'hidden';
  };

  const closeModal = () => {
    modalVideo.pause();
    modalVideo.removeAttribute('src');
    modalVideo.load();
    modal.classList.remove('open');
    document.body.classList.remove('modal-open', 'reel-modal-open');
    document.body.style.overflow = '';
  };

  const showPrevReel = () => {
    const nextIdx = (currentReelIndex - 1 + reelsData.length) % reelsData.length;
    loadReel(nextIdx);
  };

  const showNextReel = () => {
    const nextIdx = (currentReelIndex + 1) % reelsData.length;
    loadReel(nextIdx);
  };

  // Mobile Touch Swipe Handling to move between reels
  let touchStartX = 0;
  let touchEndX = 0;
  modal.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });

  modal.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    const diff = touchEndX - touchStartX;
    if (diff < -45) {
      showNextReel();
    } else if (diff > 45) {
      showPrevReel();
    }
  }, { passive: true });

  // Card click triggers
  cards.forEach((card, idx) => {
    card.addEventListener('click', (e) => {
      // If clicking enquire button directly, let it open WhatsApp and do not open modal
      if (e.target.closest('.reel-enquire-btn')) {
        return;
      }
      openModal(idx);
    });

    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        if (!e.target.closest('.reel-enquire-btn')) {
          e.preventDefault();
          openModal(idx);
        }
      }
    });
  });

  // Modal Controls
  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  if (prevBtn) prevBtn.addEventListener('click', showPrevReel);
  if (nextBtn) nextBtn.addEventListener('click', showNextReel);

  // Click outside dialog to close
  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeModal();
    }
  });

  // Keyboard navigation: Esc, Left, Right
  document.addEventListener('keydown', (e) => {
    if (!modal.classList.contains('open')) return;

    if (e.key === 'Escape') {
      closeModal();
    } else if (e.key === 'ArrowLeft') {
      showPrevReel();
    } else if (e.key === 'ArrowRight') {
      showNextReel();
    }
  });
}


/**
 * Instagram Feed Carousel (Step 6A)
 */
function initInstaCarousel() {
  const track = document.getElementById('instaTrack');
  const prevBtn = document.getElementById('instaArrowPrev');
  const nextBtn = document.getElementById('instaArrowNext');
  if (!track || !prevBtn || !nextBtn) return;

  const cards = Array.from(track.children);
  let currentIndex = 0;

  function getVisible() {
    const w = window.innerWidth;
    if (w < 768) return 1.4;
    if (w < 1024) return 2;
    return 3;
  }

  function getCardWidth() {
    if (!cards.length) return 0;
    const cardRect = cards[0].getBoundingClientRect();
    const style = window.getComputedStyle(track);
    const gap = parseFloat(style.gap) || 16;
    return cardRect.width + gap;
  }

  function slide() {
    const visible = getVisible();
    const maxIndex = Math.max(0, Math.ceil(cards.length - visible));
    currentIndex = Math.min(Math.max(currentIndex, 0), maxIndex);
    const cardW = getCardWidth();
    const maxScroll = Math.max(0, track.scrollWidth - track.clientWidth);
    const targetScroll = maxScroll > 0 ? Math.min(currentIndex * cardW, maxScroll) : currentIndex * cardW;
    track.style.transform = `translateX(-${targetScroll}px)`;
    prevBtn.disabled = currentIndex === 0;
    nextBtn.disabled = currentIndex >= maxIndex || (maxScroll > 0 && targetScroll >= maxScroll - 2);
  }

  prevBtn.addEventListener('click', () => { currentIndex--; slide(); });
  nextBtn.addEventListener('click', () => { currentIndex++; slide(); });
  window.addEventListener('resize', slide);
  slide();

  // Touch/swipe support
  let startX = 0;
  track.addEventListener('touchstart', e => { startX = e.touches[0].clientX; }, { passive: true });
  track.addEventListener('touchend', e => {
    const dx = e.changedTouches[0].clientX - startX;
    if (Math.abs(dx) > 40) {
      if (dx < 0) { currentIndex++; slide(); } else { currentIndex--; slide(); }
    }
  }, { passive: true });
  // Expose advance function for auto-advance
  window.advanceInstaCarousel = function() {
    const visible = getVisible();
    const maxIndex = Math.max(0, Math.ceil(cards.length - visible));
    if (currentIndex >= maxIndex) {
      currentIndex = 0;
    } else {
      currentIndex++;
    }
    slide();
  };
}


/**
 * Gentle Auto-Advance for Home-Page Carousels
 * - Every 4s moves one card to next snap position with smooth scroll (wrap around at end).
 * - Pauses on hover, keyboard focus, touch or drag, modal/lightbox/drawer open, tab hidden, and offscreen.
 * - Resumes 3s after interaction ends.
 * - Respects prefers-reduced-motion.
 * - Staggers start times.
 */
function initCarouselAutoAdvance() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    return; // No autoplay if reduced motion preferred
  }

  function isAnyOverlayOpen() {
    return document.body.classList.contains('modal-open') ||
           document.body.classList.contains('lightbox-open') ||
           document.body.classList.contains('reel-modal-open') ||
           document.body.classList.contains('drawer-open') ||
           Boolean(document.querySelector('.mobile-drawer.open, .quickview-modal-overlay.open, .reel-modal-overlay.open, .celebration-lightbox.open, .search-modal-overlay.open'));
  }

  function setupAutoAdvance({ container, advance, initialDelay, isEnabled }) {
    if (!container) return { pause: () => {} };

    let isHovered = false;
    let isFocused = false;
    let isInteracting = false;
    let isIntersecting = false;
    let resumeTimestamp = Date.now() + initialDelay;
    let lastAdvanceTime = Date.now() + initialDelay - 4000;

    function pauseFor(ms) {
      resumeTimestamp = Math.max(resumeTimestamp, Date.now() + ms);
      lastAdvanceTime = Date.now();
    }

    container.addEventListener('mouseenter', () => { isHovered = true; });
    container.addEventListener('mouseleave', () => {
      isHovered = false;
      pauseFor(3000);
    });

    container.addEventListener('focusin', () => { isFocused = true; });
    container.addEventListener('focusout', () => {
      isFocused = false;
      pauseFor(3000);
    });

    const startInteraction = () => { isInteracting = true; };
    const endInteraction = () => {
      isInteracting = false;
      pauseFor(3000);
    };

    container.addEventListener('touchstart', startInteraction, { passive: true });
    container.addEventListener('touchend', endInteraction, { passive: true });
    container.addEventListener('touchcancel', endInteraction, { passive: true });
    container.addEventListener('pointerdown', startInteraction, { passive: true });
    container.addEventListener('pointerup', endInteraction, { passive: true });
    container.addEventListener('pointercancel', endInteraction, { passive: true });

    container.addEventListener('click', (e) => {
      if (e.target.closest('button, a')) {
        pauseFor(3000);
      }
    });

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        const was = isIntersecting;
        isIntersecting = entry.isIntersecting;
        if (isIntersecting && !was) {
          pauseFor(3000);
        }
      });
    }, { threshold: 0.15 });

    observer.observe(container);

    document.addEventListener('visibilitychange', () => {
      if (!document.hidden) {
        pauseFor(3000);
      }
    });

    setInterval(() => {
      if (document.hidden) return;
      if (!isIntersecting) return;
      if (isHovered || isFocused || isInteracting) return;
      if (Date.now() < resumeTimestamp) return;
      if (isAnyOverlayOpen()) return;
      if (isEnabled && !isEnabled()) return;

      if (Date.now() - lastAdvanceTime >= 4000) {
        lastAdvanceTime = Date.now();
        advance();
      }
    }, 200);

    return {
      pause: pauseFor
    };
  }

  // 1. Product Tabs Track (initialDelay: 800ms)
  const productSection = document.getElementById('products') || document.querySelector('.products-section');
  const productManager = setupAutoAdvance({
    container: productSection,
    initialDelay: 800,
    advance: () => {
      const activePanel = document.querySelector('.product-tab-panel.active');
      const carousel = activePanel ? activePanel.querySelector('.product-carousel') : document.querySelector('.product-carousel');
      if (!carousel) return;
      const card = carousel.querySelector('.product-card');
      const gap = parseFloat(window.getComputedStyle(carousel).gap) || 24;
      const step = card ? card.offsetWidth + gap : 320;
      const maxScroll = carousel.scrollWidth - carousel.clientWidth;
      if (carousel.scrollLeft >= maxScroll - 15) {
        carousel.scrollTo({ left: 0, behavior: 'smooth' });
      } else {
        carousel.scrollBy({ left: step, behavior: 'smooth' });
      }
    }
  });

  window.onProductTabSwitch = function() {
    if (productManager) productManager.pause(3000);
  };

  // 2. Celebrations Row (initialDelay: 1600ms)
  const celebrationsSection = document.getElementById('celebrations') || document.querySelector('.celebrations-section');
  setupAutoAdvance({
    container: celebrationsSection,
    initialDelay: 1600,
    advance: () => {
      const track = document.getElementById('celebrationsTrack');
      if (!track) return;
      const card = track.querySelector('.celebration-card');
      const gap = parseFloat(window.getComputedStyle(track).gap) || 24;
      const step = card ? card.offsetWidth + gap : 304;
      const maxScroll = track.scrollWidth - track.clientWidth;
      if (track.scrollLeft >= maxScroll - 15) {
        track.scrollTo({ left: 0, behavior: 'smooth' });
      } else {
        track.scrollBy({ left: step, behavior: 'smooth' });
      }
    }
  });

  // 3. Reels Carousel (initialDelay: 2400ms)
  const reelsSection = document.getElementById('reels') || document.querySelector('.reels-section');
  setupAutoAdvance({
    container: reelsSection,
    initialDelay: 2400,
    advance: () => {
      const carousel = document.querySelector('.reels-carousel');
      if (!carousel) return;
      const card = carousel.querySelector('.reel-card');
      const track = carousel.querySelector('.reels-track') || carousel;
      const gap = parseFloat(window.getComputedStyle(track).gap) || 18;
      const step = card ? card.offsetWidth + gap : 280;
      const maxScroll = carousel.scrollWidth - carousel.clientWidth;
      if (carousel.scrollLeft >= maxScroll - 15) {
        carousel.scrollTo({ left: 0, behavior: 'smooth' });
      } else {
        carousel.scrollBy({ left: step, behavior: 'smooth' });
      }
    }
  });

  // 4. Instagram Strip (initialDelay: 3200ms)
  const instaSection = document.querySelector('.insta-section');
  setupAutoAdvance({
    container: instaSection,
    initialDelay: 3200,
    advance: () => {
      if (typeof window.advanceInstaCarousel === 'function') {
        window.advanceInstaCarousel();
      }
    }
  });

  // 5. Testimonials Row on Mobile (initialDelay: 4000ms)
  const testimonialsSection = document.querySelector('.testimonials-section');
  setupAutoAdvance({
    container: testimonialsSection,
    initialDelay: 4000,
    isEnabled: () => window.innerWidth < 768,
    advance: () => {
      const grid = document.querySelector('.testimonials-grid');
      if (!grid || window.innerWidth >= 768) return;
      const card = grid.querySelector('.testimonial-card');
      const gap = parseFloat(window.getComputedStyle(grid).gap) || 16;
      const step = card ? card.offsetWidth + gap : 280;
      const maxScroll = grid.scrollWidth - grid.clientWidth;
      if (grid.scrollLeft >= maxScroll - 15) {
        grid.scrollTo({ left: 0, behavior: 'smooth' });
      } else {
        grid.scrollBy({ left: step, behavior: 'smooth' });
      }
    }
  });
}




document.addEventListener('DOMContentLoaded', () => {
  // Mobile Menu Toggle
  const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
  const navLinks = document.querySelector('.nav-links');

  if (mobileMenuBtn && navLinks) {
    mobileMenuBtn.addEventListener('click', () => {
      navLinks.classList.toggle('active');
    });
  }

  // Header Scroll Effect
  const header = document.querySelector('.header');
  
  const handleScroll = () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll);
  handleScroll(); // Init

  // Scroll Reveal Animation (Intersection Observer)
  const revealElements = document.querySelectorAll('.fade-in-up, .reveal-slow');
  
  const revealCallback = (entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  };

  const revealOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px"
  };

  const revealObserver = new IntersectionObserver(revealCallback, revealOptions);

  revealElements.forEach(el => {
    revealObserver.observe(el);
  });

  // Scroll tracker for the About story. Progress is an explicit CSS variable,
  // so every scene has a deliberate resting state before it starts moving.
  const scrollScenes = document.querySelectorAll('.about-scene');
  let ticking = false;

  const updateScroll = () => {
    const windowHeight = window.innerHeight;
    const scrollY = window.scrollY;

    scrollScenes.forEach(scene => {
      // Calculate offset top dynamically
      const rect = scene.getBoundingClientRect();
      const sceneTop = rect.top + scrollY;
      const sceneHeight = rect.height;
      
      // Progress from 0 (top of scene at top of window) to 1 (bottom of scene at bottom of window)
      let p = (scrollY - sceneTop) / (sceneHeight - windowHeight);
      
      // Clamp between 0 and 1
      p = Math.max(0, Math.min(1, p));
      
      scene.style.setProperty('--p', p.toFixed(4));
    });
    ticking = false;
  };

  if (scrollScenes.length > 0) {
    window.addEventListener('scroll', () => {
      if (!ticking) {
        requestAnimationFrame(updateScroll);
        ticking = true;
      }
    });
    window.addEventListener('resize', () => {
      if (!ticking) {
        requestAnimationFrame(updateScroll);
        ticking = true;
      }
    });
    // Init
    updateScroll();
  }

});

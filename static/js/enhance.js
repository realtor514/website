/* ═══════════════════════════════════════════════════════════════
   ENHANCE.JS - Couche de mouvement et d interactions
   ---------------------------------------------------------------
   Charge apres le script principal de baseof.html. Purement additif:
   si ce fichier est retire, le site fonctionne exactement comme avant.
   Tout respecte prefers-reduced-motion.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var lang    = (document.documentElement.getAttribute('lang') || 'fr').slice(0, 2);
  var isRTL   = document.documentElement.getAttribute('dir') === 'rtl';
  var coarse  = window.matchMedia('(hover: none)').matches;

  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  /* ─────────────────────────────────────────────────────────────
     1. Observateur generique: ajoute .is-in une fois visible
     ───────────────────────────────────────────────────────────── */
  var inView = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add('is-in');
      inView.unobserve(e.target);
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -8% 0px' });

  function watch(sel) {
    document.querySelectorAll(sel).forEach(function (el) { inView.observe(el); });
  }

  /* ─────────────────────────────────────────────────────────────
     2. Cascade sur les grilles
     ───────────────────────────────────────────────────────────── */
  function setupStagger() {
    var grids = [
      '.adv-grid', '.articles-grid', '.listings-grid', '.prot-grid',
      '.pillars-grid', '.steps-grid', '.tools-quick-grid',
      '.services__grid', '.calc-shortcuts__grid', '.offices-grid',
      '.adv-facts__grid'
    ].join(',');

    document.querySelectorAll(grids).forEach(function (grid) {
      if (grid.hasAttribute('data-stagger')) return;
      grid.setAttribute('data-stagger', '');
      Array.prototype.forEach.call(grid.children, function (child, i) {
        child.style.setProperty('--i', i);
      });
      // La grille porte souvent .reveal: on evite le double effet
      grid.classList.remove('reveal');
      inView.observe(grid);
    });
  }

  /* ─────────────────────────────────────────────────────────────
     3. Titres de section revelés mot par mot
     ───────────────────────────────────────────────────────────── */
  function setupSplitHeadings() {
    if (reduced) return;
    document.querySelectorAll('.section-header h2').forEach(function (h) {
      if (h.dataset.split || h.querySelector('img, svg, br')) return;
      var text = h.textContent.trim();
      if (!text || text.length > 90) return;
      h.dataset.split = '1';
      h.innerHTML = text.split(/\s+/).map(function (w, i) {
        return '<span class="split-word" style="transition-delay:' + (i * 55) + 'ms">' + w + '</span>';
      }).join(' ');

      // Meme observateur que le reste: seuil bas, declenchement fiable
      splitObs.observe(h);
    });
  }

  var splitObs = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add('split-ready');
      splitObs.unobserve(e.target);
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -5% 0px' });

  /* ─────────────────────────────────────────────────────────────
     4. Trait d accent sous les eyebrows
     ───────────────────────────────────────────────────────────── */
  function setupEyebrows() {
    document.querySelectorAll('.section-header .eyebrow').forEach(function (el) {
      inView.observe(el);
    });
  }

  /* ─────────────────────────────────────────────────────────────
     5. Projecteur qui suit le curseur sur les cartes
     ───────────────────────────────────────────────────────────── */
  function setupSpotlight() {
    if (reduced || coarse) return;
    var sel = '.adv-card, .calc-card, .article-card, .listing-card, .pillar-card, .tools-quick-card';
    document.addEventListener('mousemove', function (e) {
      var card = e.target.closest ? e.target.closest(sel) : null;
      if (!card) return;
      var r = card.getBoundingClientRect();
      card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      card.style.setProperty('--my', (e.clientY - r.top) + 'px');
    }, { passive: true });
  }

  /* ─────────────────────────────────────────────────────────────
     6. Boutons aimantes
     ───────────────────────────────────────────────────────────── */
  function setupMagnetic() {
    if (reduced || coarse) return;
    document.querySelectorAll('.btn-primary, .nav__book-btn, .scroll-top').forEach(function (btn) {
      btn.setAttribute('data-magnetic', '');
      var raf = null;
      btn.addEventListener('mousemove', function (e) {
        if (raf) return;
        raf = requestAnimationFrame(function () {
          var r = btn.getBoundingClientRect();
          var x = (e.clientX - r.left - r.width  / 2) * 0.22;
          var y = (e.clientY - r.top  - r.height / 2) * 0.3;
          btn.style.transform = 'translate(' + x.toFixed(1) + 'px,' + y.toFixed(1) + 'px)';
          raf = null;
        });
      });
      btn.addEventListener('mouseleave', function () { btn.style.transform = ''; });
    });
  }

  /* ─────────────────────────────────────────────────────────────
     7. Parallaxe au defilement
     ───────────────────────────────────────────────────────────── */
  function setupParallax() {
    if (reduced || coarse) return;

    var targets = [];
    document.querySelectorAll('.hero__bg-slideshow').forEach(function (el) {
      targets.push({ el: el, speed: 0.16 });
    });
    document.querySelectorAll('.about__image, .office-gallery__main, .content-hero::before').forEach(function (el) {
      if (el) targets.push({ el: el, speed: 0.07 });
    });
    if (!targets.length) return;

    targets.forEach(function (t) { t.el.setAttribute('data-parallax', ''); });

    var ticking = false;
    function update() {
      var vh = window.innerHeight;
      targets.forEach(function (t) {
        var r = t.el.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) return;
        var progress = (r.top + r.height / 2 - vh / 2) / vh;
        t.el.style.transform = 'translate3d(0,' + (progress * t.speed * 100).toFixed(1) + 'px,0)';
      });
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(update);
    }, { passive: true });
    update();
  }

  /* ─────────────────────────────────────────────────────────────
     8. Devoilement des images par volet
     ───────────────────────────────────────────────────────────── */
  function setupWipe() {
    if (reduced) return;
    document.querySelectorAll('.article-card__image, .listing-card__image, .office-gallery img')
      .forEach(function (el) {
        el.setAttribute('data-wipe', '');
        inView.observe(el);
      });
  }

  /* ─────────────────────────────────────────────────────────────
     9. Bandeau defilant sous le hero
     ───────────────────────────────────────────────────────────── */
  var MARQUEE = {
    fr: ['RE/MAX DU CARTIER INC.', 'Montréal', 'Laval', 'Rive-Nord', 'Rive-Sud', 'Laurentides',
         'Ingénieur (PhD)', '4 langues parlées', 'Tranquilli-T inclus', 'Intégri-T jusqu’à 50 000 $',
         'Évaluation gratuite', 'Réseau mondial RE/MAX'],
    en: ['RE/MAX DU CARTIER INC.', 'Montreal', 'Laval', 'North Shore', 'South Shore', 'Laurentians',
         'Engineer (PhD)', '4 languages spoken', 'Tranquilli-T included', 'Integri-T up to $50,000',
         'Free evaluation', 'RE/MAX global network'],
    es: ['RE/MAX DU CARTIER INC.', 'Montreal', 'Laval', 'Rive-Nord', 'Rive-Sud', 'Laurentides',
         'Ingeniero (PhD)', '4 idiomas', 'Tranquilli-T incluido', 'Integri-T hasta 50 000 $',
         'Evaluación gratuita', 'Red mundial RE/MAX'],
    ar: ['RE/MAX DU CARTIER INC.', 'مونتريال', 'لافال', 'الضفة الشمالية', 'الضفة الجنوبية', 'اللورانتيد',
         'مهندس (دكتوراه)', '4 لغات', 'Tranquilli-T مشمول', 'Integri-T حتى 50,000 $',
         'تقييم مجاني', 'شبكة RE/MAX العالمية']
  };

  function setupMarquee() {
    var hero = document.querySelector('.hero');
    if (!hero || document.querySelector('.marquee')) return;

    var items = MARQUEE[lang] || MARQUEE.fr;
    var group = '<div class="marquee__group">' +
      items.map(function (t) { return '<span class="marquee__item">' + t + '</span>'; }).join('') +
      '</div>';

    var bar = document.createElement('div');
    bar.className = 'marquee';
    bar.setAttribute('aria-hidden', 'true');
    // Deux groupes identiques: la boucle est continue
    bar.innerHTML = '<div class="marquee__track">' + group + group + '</div>';
    hero.insertAdjacentElement('afterend', bar);
  }

  /* ─────────────────────────────────────────────────────────────
     10. Indicateur de defilement dans le hero
     ───────────────────────────────────────────────────────────── */
  var SCROLL_LABEL = { fr: 'Défiler', en: 'Scroll', es: 'Desplazar', ar: 'مرّر' };

  function setupScrollCue() {
    var hero = document.querySelector('.hero');
    if (!hero || reduced || document.querySelector('.hero__scroll-cue')) return;
    var cue = document.createElement('div');
    cue.className = 'hero__scroll-cue';
    cue.setAttribute('aria-hidden', 'true');
    cue.innerHTML =
      '<span>' + (SCROLL_LABEL[lang] || SCROLL_LABEL.fr) + '</span>' +
      '<span class="hero__scroll-cue-track"><span class="hero__scroll-cue-dot"></span></span>';
    hero.appendChild(cue);

    // Disparait des que l on quitte le hero
    window.addEventListener('scroll', function () {
      cue.style.opacity = window.scrollY > 140 ? '0' : '1';
    }, { passive: true });
  }

  /* ─────────────────────────────────────────────────────────────
     11. Compteur sur les chiffres du hero
     ───────────────────────────────────────────────────────────── */
  function setupHeroCounter() {
    if (reduced) return;
    document.querySelectorAll('.hero__trust-num').forEach(function (el) {
      var raw = el.textContent.trim();
      if (!/^\d+$/.test(raw)) return;
      var target = parseInt(raw, 10);
      var obs = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          obs.unobserve(e.target);
          var step = 0, steps = 26;
          var timer = setInterval(function () {
            step++;
            el.textContent = Math.round((1 - Math.pow(1 - step / steps, 3)) * target);
            if (step >= steps) { clearInterval(timer); el.textContent = raw; }
          }, 34);
        });
      }, { threshold: 0.6 });
      obs.observe(el);
    });
  }

  /* ─────────────────────────────────────────────────────────────
     Demarrage
     ───────────────────────────────────────────────────────────── */
  ready(function () {
    setupStagger();
    setupSplitHeadings();
    setupEyebrows();
    setupSpotlight();
    setupMagnetic();
    setupParallax();
    setupWipe();
    setupMarquee();
    setupScrollCue();
    setupHeroCounter();

    /* Filet de securite: rien ne doit jamais rester invisible.
       A chaque defilement, tout ce qui a deja atteint le viewport est
       revele, meme si un observateur a manque son declenchement. */
    function sweep() {
      var limit = window.innerHeight * 0.95;
      document.querySelectorAll('[data-stagger]:not(.is-in), [data-wipe]:not(.is-in), .section-header .eyebrow:not(.is-in)')
        .forEach(function (el) {
          if (el.getBoundingClientRect().top < limit) el.classList.add('is-in');
        });
      document.querySelectorAll('.section-header h2[data-split]:not(.split-ready)')
        .forEach(function (el) {
          if (el.getBoundingClientRect().top < limit) el.classList.add('split-ready');
        });
    }
    var sweeping = false;
    window.addEventListener('scroll', function () {
      if (sweeping) return;
      sweeping = true;
      requestAnimationFrame(function () { sweep(); sweeping = false; });
    }, { passive: true });
    requestAnimationFrame(sweep);
    setTimeout(sweep, 600);
  });
})();

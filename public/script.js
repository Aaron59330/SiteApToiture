document.getElementById('year').textContent = new Date().getFullYear();

const burger = document.querySelector('.burger');
const menu = document.querySelector('.menu');
burger.addEventListener('click', () => {
  const open = menu.classList.toggle('open');
  burger.setAttribute('aria-expanded', open);
});

const form = document.getElementById('form');
if (form) {
  form.addEventListener('submit', e => {
    e.preventDefault();
    const f = new FormData(form);
    const body = `Nom : ${f.get('nom')}\nTéléphone : ${f.get('tel')}\nE-mail : ${f.get('email')}\nTravaux : ${f.get('type')}\n\n${f.get('message')}`;
    form.querySelector('.ok').hidden = false;
    location.href = `mailto:pro.ap.couverture@gmail.com?subject=${encodeURIComponent('Demande de devis')}&body=${encodeURIComponent(body)}`;
  });
}

// Visionneuse des réalisations
(function () {
  if (document.body.hasAttribute('data-admin')) return;
  const items = () => Array.from(document.querySelectorAll('.shot-img'));
  let idx = 0, box;
  const show = i => {
    const list = items(); idx = (i + list.length) % list.length;
    const fig = list[idx].closest('.shot');
    const t = fig.querySelector('.t'), d = fig.querySelector('.d');
    box.querySelector('img').src = list[idx].getAttribute('href');
    box.querySelector('p').innerHTML = '';
    if (t && t.textContent.trim()) { const b = document.createElement('b'); b.textContent = t.textContent; box.querySelector('p').appendChild(b); }
    if (d && d.textContent.trim()) box.querySelector('p').appendChild(document.createTextNode(d.textContent));
  };
  const close = () => { if (box) { box.remove(); box = null; document.removeEventListener('keydown', key); } };
  const key = e => { if (e.key === 'Escape') close(); if (e.key === 'ArrowRight') show(idx + 1); if (e.key === 'ArrowLeft') show(idx - 1); };
  document.addEventListener('click', e => {
    const a = e.target.closest('.shot-img');
    if (!a) return;
    e.preventDefault();
    box = document.createElement('div'); box.className = 'lb';
    box.innerHTML = '<button class="x" aria-label="Fermer">&times;</button><button class="pv" aria-label="Précédente">&#8249;</button><button class="nx" aria-label="Suivante">&#8250;</button><img alt=""><p></p>';
    document.body.appendChild(box);
    box.addEventListener('click', ev => {
      if (ev.target.classList.contains('pv')) show(idx - 1);
      else if (ev.target.classList.contains('nx')) show(idx + 1);
      else if (ev.target.tagName !== 'IMG' && ev.target.tagName !== 'P' && ev.target.tagName !== 'B') close();
    });
    document.addEventListener('keydown', key);
    show(items().indexOf(a));
  });
})();

// Effets d'animation (désactivés en mode administrateur et si l'utilisateur réduit les animations)
(function () {
  const header = document.querySelector('.header');
  const bar = document.createElement('div');
  bar.className = 'progress';
  document.body.appendChild(bar);
  const onScroll = () => {
    const h = document.documentElement;
    const max = h.scrollHeight - h.clientHeight;
    bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(h.scrollTop / max, 1) : 0) + ')';
    if (header) header.classList.toggle('scrolled', h.scrollTop > 10);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  if (document.body.hasAttribute('data-admin')) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) return;

  const groups = '.head, .grid4 > *, .grid3 > *, .grid2 > *, .gallery > *, .srv > *, .two > *, .crow, .cta .container > *, .fgrid > *, .section .container > .lead2';
  const targets = Array.from(document.querySelectorAll(groups)).filter(el => !el.closest('.hero, .banner'));
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  targets.forEach(el => {
    const idx = Array.prototype.indexOf.call(el.parentElement.children, el);
    el.style.setProperty('--d', Math.min(idx, 5) * 0.1 + 's');
    el.classList.add('reveal');
    if (el.getBoundingClientRect().top < window.innerHeight * 0.9) { el.classList.add('in'); el.style.transition = 'none'; requestAnimationFrame(() => { el.style.transition = ''; }); }
    else io.observe(el);
  });
})();

// Reflet brillant sur le logo : copie de l'image actuelle, balayée par un dégradé lumineux
(function () {
  if (document.body.hasAttribute('data-admin')) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const w = document.querySelector('.logo-shine');
  const img = w && w.querySelector('img');
  if (!img) return;
  const copy = img.cloneNode(false);
  copy.className = 'shine-img';
  copy.alt = '';
  copy.setAttribute('aria-hidden', 'true');
  copy.removeAttribute('data-edi');
  copy.removeAttribute('data-edi-orig');
  w.appendChild(copy);
})();

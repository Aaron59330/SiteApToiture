document.getElementById('year').textContent = new Date().getFullYear();

const burger = document.querySelector('.burger');
const menu = document.querySelector('.menu');
burger.addEventListener('click', () => {
  const open = menu.classList.toggle('open');
  burger.setAttribute('aria-expanded', open);
});
menu.addEventListener('click', e => { if (e.target.tagName === 'A') menu.classList.remove('open'); });

// Compteurs animés
const io = new IntersectionObserver(entries => {
  entries.forEach(en => {
    if (!en.isIntersecting) return;
    const el = en.target, end = +el.dataset.count, t0 = performance.now();
    const step = t => {
      const p = Math.min((t - t0) / 1200, 1);
      el.textContent = Math.round(end * p);
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
    io.unobserve(el);
  });
}, { threshold: .5 });
document.querySelectorAll('[data-count]').forEach(el => io.observe(el));

// Formulaire : ouvre le client mail (à remplacer par un vrai service si besoin)
document.getElementById('form').addEventListener('submit', e => {
  e.preventDefault();
  const f = new FormData(e.target);
  const body = `Nom : ${f.get('nom')}\nTél : ${f.get('tel')}\nE-mail : ${f.get('email')}\nTravaux : ${f.get('type')}\n\n${f.get('message')}`;
  e.target.querySelector('.ok').hidden = false;
  location.href = `mailto:apcouvreur@gmail.com?subject=${encodeURIComponent('Demande de devis')}&body=${encodeURIComponent(body)}`;
});

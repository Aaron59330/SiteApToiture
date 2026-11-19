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
    location.href = `mailto:apcouvreur@gmail.com?subject=${encodeURIComponent('Demande de devis')}&body=${encodeURIComponent(body)}`;
  });
}

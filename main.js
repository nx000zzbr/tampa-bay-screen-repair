// Tampa Bay Screen Repair — the small amount of script the page needs.
// Everything here is progressive: without it the page is a readable price list with call and text links.

// Reveal once when an element enters the viewport.
(() => {
  const targets = document.querySelectorAll('[data-reveal]');
  if (!targets.length) return;
  if (!('IntersectionObserver' in window)) { targets.forEach((el) => el.classList.add('is-in')); return; }
  const io = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add('is-in');
      io.unobserve(entry.target);
    }
  }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });
  targets.forEach((el) => io.observe(el));
  window.addEventListener('load', () => setTimeout(() => {
    targets.forEach((el) => { const r = el.getBoundingClientRect(); if (r.top < innerHeight && r.bottom > 0) el.classList.add('is-in'); });
  }, 2500));
})();

// The hero photograph quietly changes, like light shifting in a room. Pauses when the tab is hidden.
(() => {
  const room = document.querySelector('.hero .room');
  if (!room) return;
  const set = () => room.classList.toggle('playing', document.visibilityState === 'visible');
  document.addEventListener('visibilitychange', set);
  set();
})();

// Phone menu.
(() => {
  const btn = document.querySelector('.menu-btn');
  const sheet = document.getElementById('sheet-menu');
  if (!btn || !sheet) return;
  btn.addEventListener('click', () => {
    const open = sheet.hasAttribute('open');
    if (open) sheet.removeAttribute('open'); else sheet.setAttribute('open', '');
    btn.setAttribute('aria-expanded', String(!open));
    btn.textContent = open ? 'Menu' : 'Close';
  });
  sheet.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => { sheet.removeAttribute('open'); btn.textContent = 'Menu'; btn.setAttribute('aria-expanded', 'false'); }));
})();

// The ticket: count your panels. Typical figures, confirmed in writing by Jerry.
(() => {
  const ticket = document.querySelector('.ticket');
  if (!ticket) return;
  const PRICES = { wall: 45, roof: 75, door: 95, noseeum: 6, pet: 15, fullCage: 1200 };
  const counts = { wall: 0, roof: 0, door: 0 };
  const outs = { wall: ticket.querySelector('[data-out="wall"]'), roof: ticket.querySelector('[data-out="roof"]'), door: ticket.querySelector('[data-out="door"]') };
  const total = ticket.querySelector('[data-out="total"]');
  const count = ticket.querySelector('[data-out="count"]');
  const summary = document.getElementById('quote-summary');
  const smsLinks = document.querySelectorAll('[data-sms]');
  const mailLink = document.getElementById('quote-mail');
  const money = (n) => '$' + n.toLocaleString('en-US');

  function mesh() { const c = ticket.querySelector('input[name="mesh"]:checked'); return c ? c.value : 'standard'; }

  function lines() {
    const m = mesh();
    const parts = [];
    if (counts.wall) parts.push(`${counts.wall} wall panel${counts.wall > 1 ? 's' : ''}`);
    if (counts.roof) parts.push(`${counts.roof} roof panel${counts.roof > 1 ? 's' : ''}`);
    if (counts.door) parts.push(`${counts.door} screen door${counts.door > 1 ? 's' : ''}`);
    parts.push(m === 'standard' ? 'standard 18x14 mesh' : m === 'noseeum' ? 'no-see-um 20x20 mesh' : 'pet screen');
    return parts;
  }

  function render() {
    for (const k in outs) if (outs[k]) outs[k].value = counts[k];
    const panels = counts.wall + counts.roof;
    const m = mesh();
    const extra = m === 'noseeum' ? PRICES.noseeum : m === 'pet' ? PRICES.pet : 0;
    let sum = counts.wall * PRICES.wall + counts.roof * PRICES.roof + counts.door * PRICES.door + panels * extra;
    let fromText = 'Typical, for';
    if (panels >= 30) { sum = Math.max(sum, PRICES.fullCage); fromText = 'Full rescreen, typical for'; }
    if (total) total.value = sum ? money(sum) : '$0';
    if (count) count.textContent = panels || counts.door ? `${fromText} ${panels} panel${panels === 1 ? '' : 's'}${counts.door ? ` and ${counts.door} door${counts.door > 1 ? 's' : ''}` : ''}` : 'Add panels to see a typical figure';
    const text = `Hi Jerry, I need a screen quote. ${lines().join(', ')}. Typical figure from your site: ${sum ? money(sum) : 'n/a'}. Photos attached.`;
    if (summary) summary.textContent = text;
    smsLinks.forEach((a) => { a.href = 'sms:+18135165619?&body=' + encodeURIComponent(text); });
    if (mailLink) mailLink.href = 'mailto:TampaBayScreenRepair@gmail.com?subject=' + encodeURIComponent('Screen quote request') + '&body=' + encodeURIComponent(text + '\n\nName:\nPhone:\nCity:\n');
  }

  ticket.querySelectorAll('.stepper').forEach((s) => {
    const key = s.dataset.key;
    s.querySelector('[data-dec]').addEventListener('click', () => { counts[key] = Math.max(0, counts[key] - 1); render(); });
    s.querySelector('[data-inc]').addEventListener('click', () => { counts[key] = Math.min(99, counts[key] + 1); render(); });
  });
  ticket.querySelectorAll('input[name="mesh"]').forEach((r) => r.addEventListener('change', render));
  render();

  // The dialog form: no backend yet. Submitting opens an email with the lines filled in.
  const dialog = document.getElementById('quote-dialog');
  const opener = ticket.querySelector('[data-open-quote]');
  if (dialog && opener && typeof dialog.showModal === 'function') {
    opener.addEventListener('click', (e) => { e.preventDefault(); dialog.showModal(); });
    dialog.querySelector('.close').addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', (e) => { if (e.target === dialog) dialog.close(); });
    const form = dialog.querySelector('form');
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const f = new FormData(form);
      const body = `${summary ? summary.textContent : ''}\n\nName: ${f.get('name') || ''}\nPhone: ${f.get('phone') || ''}\nCity: ${f.get('city') || ''}\nNotes: ${f.get('notes') || ''}\n\n(Please attach your photos to this email.)`;
      location.href = 'mailto:TampaBayScreenRepair@gmail.com?subject=' + encodeURIComponent('Screen quote request') + '&body=' + encodeURIComponent(body);
      dialog.close();
    });
  }
})();

// The drag row: arrows and the progress bar.
(() => {
  const row = document.querySelector('.row');
  const bar = document.querySelector('.row-progress i');
  if (!row) return;
  const update = () => {
    if (!bar) return;
    const max = row.scrollWidth - row.clientWidth;
    const visible = row.clientWidth / row.scrollWidth;
    const pos = max > 0 ? row.scrollLeft / max : 0;
    bar.style.width = (visible * 100) + '%';
    bar.style.transform = `translateX(${pos * (100 / visible - 100)}%)`;
  };
  row.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update);
  update();
  const step = () => Math.min(row.clientWidth * 0.8, 312);
  document.querySelector('[data-row-prev]')?.addEventListener('click', () => row.scrollBy({ left: -step(), behavior: 'smooth' }));
  document.querySelector('[data-row-next]')?.addEventListener('click', () => row.scrollBy({ left: step(), behavior: 'smooth' }));
})();

// "Open now" next to the hours, in Plant City's own time.
(() => {
  const el = document.querySelector('[data-open-now]');
  if (!el) return;
  try {
    const now = new Date();
    const parts = new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', hour: 'numeric', hour12: false, weekday: 'short' }).formatToParts(now);
    const hour = Number(parts.find((p) => p.type === 'hour').value);
    const day = parts.find((p) => p.type === 'weekday').value;
    const open = day !== 'Sun' && hour >= 8 && hour < 19;
    el.textContent = open ? 'Open now' : 'Closed now, text anytime';
  } catch (e) { /* leave the static text */ }
})();

// The phone bar steps out of the way once the footer, which carries the same two links, is on screen.
(() => {
  const bar = document.querySelector('.thumb-bar');
  const foot = document.querySelector('footer.back');
  if (!bar || !foot || !('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) bar.classList.toggle('away', e.isIntersecting);
  }, { threshold: 0.05 });
  io.observe(foot);
})();

// Lightweight enhancements: copy-to-clipboard for prompt blocks
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.prompt').forEach((block) => {
    const btn = document.createElement('button');
    btn.className = 'copy';
    btn.type = 'button';
    btn.textContent = 'Copy';
    btn.addEventListener('click', async () => {
      const text = block.dataset.copy || block.innerText.replace(/^Copy\s*/, '');
      try {
        await navigator.clipboard.writeText(text.trim());
        btn.textContent = 'Copied';
        setTimeout(() => (btn.textContent = 'Copy'), 1500);
      } catch {
        btn.textContent = 'Press Ctrl+C';
      }
    });
    block.appendChild(btn);
  });

  // Mark active nav link based on current page
  const path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach((a) => {
    const href = a.getAttribute('href');
    if (href === path) a.classList.add('active');
  });

  // Lightbox: click any step-figure image to view it full size.
  const figureImgs = document.querySelectorAll('.step-figure img');
  if (figureImgs.length) {
    const lightbox = document.createElement('div');
    lightbox.className = 'lightbox';
    lightbox.setAttribute('role', 'dialog');
    lightbox.setAttribute('aria-modal', 'true');
    lightbox.setAttribute('aria-hidden', 'true');
    lightbox.innerHTML =
      '<button type="button" class="lightbox-close" aria-label="Close">&times;</button>' +
      '<img alt="" />';
    document.body.appendChild(lightbox);

    const lightboxImg = lightbox.querySelector('img');
    const closeBtn = lightbox.querySelector('.lightbox-close');

    const open = (src, alt) => {
      lightboxImg.src = src;
      lightboxImg.alt = alt || '';
      lightbox.classList.add('is-open');
      lightbox.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    };
    const close = () => {
      lightbox.classList.remove('is-open');
      lightbox.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
      // Clear src after the transition so we don't hold the image in memory.
      setTimeout(() => { lightboxImg.src = ''; }, 200);
    };

    figureImgs.forEach((img) => {
      img.addEventListener('click', () => open(img.currentSrc || img.src, img.alt));
    });
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox || e.target === closeBtn) close();
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && lightbox.classList.contains('is-open')) close();
    });
  }

  // "Try it in Outlook" — open Outlook on the Web compose with subject + body
  // pre-populated from the email card the button sits inside.
  document.querySelectorAll('.try-it').forEach((btn) => {
    btn.addEventListener('click', () => {
      const card = btn.closest('.email-card');
      if (!card) return;
      const subject =
        (card.querySelector('.email-subject')?.textContent || '').trim();
      // Use innerText to preserve visual line breaks from the rendered card.
      const body =
        (card.querySelector('.email-body')?.innerText || '').trim();
      const url =
        'https://outlook.office.com/mail/deeplink/compose' +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(body);
      window.open(url, '_blank', 'noopener');
    });
  });

  // Savings calculator
  const calcForm = document.getElementById('savings-form');
  if (calcForm) {
    const $ = (id) => document.getElementById(id);
    const num = (id) => {
      const v = parseFloat($(id).value);
      return Number.isFinite(v) ? v : 0;
    };
    const fmtHours = (h) => {
      if (!Number.isFinite(h)) return '—';
      return Math.round(h).toLocaleString('en-GB') + ' hrs';
    };
    const recalc = () => {
      const volume = Math.max(0, num('calc-volume'));
      const exemptPct = Math.min(100, Math.max(0, num('calc-exempt'))) / 100;
      const s1Mins = Math.max(0, num('calc-s1'));
      const s2Hours = Math.max(0, num('calc-s2'));
      const s3Hours = Math.max(0, num('calc-s3'));
      const eff = Math.min(100, Math.max(0, num('calc-eff'))) / 100;

      // Stages 1 & 3 are semi-automated by the agent across every request.
      const s1SavedHours = (volume * s1Mins / 60) * eff;
      const s3SavedHours = volume * s3Hours * eff;
      // Exempted requests skip stage 2 entirely — pure organisational saving.
      const s2AvoidedHours = volume * exemptPct * s2Hours;

      const total = s1SavedHours + s3SavedHours + s2AvoidedHours;

      $('calc-s1-hours').textContent = fmtHours(s1SavedHours);
      $('calc-s3-hours').textContent = fmtHours(s3SavedHours);
      $('calc-s2-hours').textContent = fmtHours(s2AvoidedHours);
      $('calc-total-hours').textContent =
        Math.round(total).toLocaleString('en-GB');
    };
    calcForm.querySelectorAll('input').forEach((el) => {
      el.addEventListener('input', recalc);
    });
    recalc();
  }
});

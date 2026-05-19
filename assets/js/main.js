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
});

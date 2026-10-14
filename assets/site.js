(function () {
  'use strict';
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#mainnav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      toggle.setAttribute('aria-expanded', String(nav.classList.toggle('open')));
    });
    nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }));
  }
  document.querySelectorAll('a[data-affiliate]').forEach(link => {
    link.addEventListener('click', () => {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({ event: 'affiliate_click', partner: 'trip_com', category: link.dataset.affiliate, page: location.pathname });
    });
  });
  document.querySelectorAll('.blog-browser').forEach(browser => {
    const buttons = browser.querySelectorAll('[data-blog-filter]');
    const cards = browser.querySelectorAll('[data-blog-category]');
    buttons.forEach(button => button.addEventListener('click', () => {
      const category = button.dataset.blogFilter;
      buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
      cards.forEach(card => {
        card.hidden = category !== 'all' && card.dataset.blogCategory !== category;
      });
    }));
  });
  document.querySelectorAll('.ad-frame').forEach(frame => {
    // Preserve the partner widget's readable controls; contain horizontal
    // scrolling within the frame instead of shrinking the search interface.
    if (frame.dataset.adMode === 'scroll') return;
    const iframe = frame.querySelector('iframe');
    const resize = () => {
      const scale = Math.min(1, frame.clientWidth / Number(frame.dataset.adWidth));
      iframe.style.transformOrigin = 'top left';
      iframe.style.transform = `scale(${scale})`;
      frame.style.height = `${Number(frame.dataset.adHeight) * scale}px`;
      frame.style.overflow = 'hidden';
    };
    resize();
    if ('ResizeObserver' in window) new ResizeObserver(resize).observe(frame);
    else window.addEventListener('resize', resize);
  });
}());

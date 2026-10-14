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
  document.querySelectorAll('.news-browser').forEach(browser => {
    const select = browser.querySelector('.news-country');
    const cards = browser.querySelectorAll('.news-card');
    select.addEventListener('change', () => {
      let visible = 0;
      cards.forEach(card => {
        card.hidden = select.value !== 'all' && !card.dataset.newsCountries.split(' ').includes(select.value);
        if (!card.hidden) visible += 1;
      });
      browser.querySelector('.news-empty-filter').hidden = visible > 0;
    });
  });
  document.querySelectorAll('.home-weather').forEach(weather => {
    const select = weather.querySelector('.destination-select');
    const panels = Array.from(weather.querySelectorAll('[data-weather-city]'));
    const update = () => {
      panels.forEach(panel => { panel.hidden = panel.dataset.weatherCity !== select.value; });
      try { localStorage.setItem('stayindanang-destination:v1', select.value); } catch (_) {}
    };
    try {
      const saved = localStorage.getItem('stayindanang-destination:v1');
      if (panels.some(panel => panel.dataset.weatherCity === saved)) select.value = saved;
    } catch (_) {}
    select.addEventListener('change', update);
    update();
  });
  document.querySelectorAll('.trip-planner').forEach(planner => {
    const buttons = planner.querySelectorAll('[data-plan-duration]');
    buttons.forEach(button => button.addEventListener('click', () => {
      buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
      planner.querySelectorAll('[data-plan-panel]').forEach(panel => {
        panel.hidden = panel.dataset.planPanel !== button.dataset.planDuration;
      });
    }));
    const rainToggle = planner.querySelector('.rainy-day-toggle');
    rainToggle.addEventListener('change', () => {
      planner.querySelector('.rainy-day-plan').hidden = !rainToggle.checked;
    });
  });
  document.querySelectorAll('.trip-checklist').forEach(checklist => {
    const key = 'stayindanang-trip-checklist:v1';
    const checks = Array.from(checklist.querySelectorAll('[data-trip-check]'));
    try {
      const saved = JSON.parse(localStorage.getItem(key) || '{}');
      checks.forEach(check => { check.checked = saved?.[check.dataset.tripCheck] === true; });
    } catch (_) { /* The checklist still works if storage is unavailable. */ }
    const update = () => {
      checklist.querySelector('.checklist-progress').value = `${checks.filter(check => check.checked).length} / ${checks.length}`;
      try {
        localStorage.setItem(key, JSON.stringify(Object.fromEntries(checks.map(check => [check.dataset.tripCheck, check.checked]))));
      } catch (_) { /* Do not block trip planning in private/restricted modes. */ }
    };
    checks.forEach(check => check.addEventListener('change', update));
    checklist.querySelector('.checklist-reset').addEventListener('click', () => {
      checks.forEach(check => { check.checked = false; });
      update();
    });
    update();
  });
}());

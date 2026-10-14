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
  const favoritesKey = 'stayindanang-favorites:v1';
  let favorites = new Set();
  try {
    const stored = JSON.parse(localStorage.getItem(favoritesKey) || '[]');
    if (Array.isArray(stored)) favorites = new Set(stored.filter(item => typeof item === 'string').slice(0,200));
  } catch (_) {}
  const updateHotelFilters = () => {
    document.querySelectorAll('#hotels').forEach(section => {
      const selected = section.querySelector('[data-hotel-tab][aria-pressed="true"]')?.dataset.hotelTab || 'all';
      let visible = 0;
      section.querySelectorAll('[data-hotel-group]').forEach(card => {
        card.hidden = selected === 'saved' ? !favorites.has(card.dataset.savedId) : selected !== 'all' && selected !== card.dataset.hotelGroup;
        if (!card.hidden) visible += 1;
      });
      const empty = section.querySelector('.saved-empty');
      if (empty) empty.hidden = visible > 0;
    });
  };
  const refreshFavorites = () => {
    document.querySelectorAll('[data-save-id]').forEach(button => {
      const saved = favorites.has(button.dataset.saveId);
      button.setAttribute('aria-pressed', String(saved));
      button.setAttribute('aria-label', `${saved ? button.dataset.savedLabel : button.dataset.saveLabel}: ${button.dataset.itemTitle}`);
      button.querySelector('span').textContent = saved ? '♥' : '♡';
    });
    updateHotelFilters();
  };
  document.querySelectorAll('[data-save-id]').forEach(button => button.addEventListener('click', () => {
    const key = button.dataset.saveId;
    if (favorites.has(key)) favorites.delete(key); else favorites.add(key);
    try { localStorage.setItem(favoritesKey, JSON.stringify([...favorites])); } catch (_) {}
    refreshFavorites();
  }));
  document.querySelectorAll('[data-hotel-tab]').forEach(button => button.addEventListener('click', () => {
    const section = button.closest('#hotels');
    section.querySelectorAll('[data-hotel-tab]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    updateHotelFilters();
    section.querySelector('.discovery-rail').scrollLeft = 0;
  }));
  refreshFavorites();
  document.querySelectorAll('[data-rail-direction]').forEach(button => button.addEventListener('click', () => {
    const rail = button.closest('.discovery-section').querySelector('.discovery-rail');
    rail.scrollBy({ left: Number(button.dataset.railDirection) * rail.clientWidth * .85, behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
  }));
  const routeElement = document.querySelector('#affiliate-routes');
  const booking = document.querySelector('.booking-hub');
  if (routeElement && booking) {
    try {
      const routes = JSON.parse(routeElement.textContent);
      const destination = booking.querySelector('.booking-destination');
      const service = booking.querySelector('.booking-service');
      const hotel = booking.querySelector('.booking-property');
      const action = booking.querySelector('.booking-action');
      const updateBooking = () => {
        const specific = destination.value === 'da-nang' && service.value === 'hotels';
        hotel.disabled = !specific;
        booking.querySelector('.booking-property-field').hidden = !specific;
        const hotelKey = specific ? hotel.value : '';
        const target = hotelKey ? routes.hotels[hotelKey] : routes.routes[destination.value]?.[service.value] || routes.services[service.value] || routes.default_url;
        const parsed = new URL(target);
        if (parsed.protocol !== 'https:' || parsed.hostname !== 'www.trip.com' || !/^\/(t|w)\/[a-zA-Z0-9]+$/.test(parsed.pathname) || parsed.search || parsed.hash || parsed.username || parsed.password || parsed.port) return;
        action.href = target;
        action.dataset.affiliate = hotelKey ? `hotel-${hotelKey}` : `planner-${destination.value}-${service.value}`;
        const summary = [destination.selectedOptions[0].textContent,service.selectedOptions[0].textContent];
        if (hotelKey) summary.push(hotel.selectedOptions[0].textContent);
        booking.querySelector('.booking-summary').textContent = summary.join(' · ');
      };
      destination.addEventListener('change', () => {
        updateBooking();
        const weather = document.querySelector('#weather-city');
        if (weather) { weather.value = destination.value; weather.dispatchEvent(new Event('change')); }
      });
      service.addEventListener('change',updateBooking);
      hotel.addEventListener('change',updateBooking);
      const weather = document.querySelector('#weather-city');
      if (weather) {
        destination.value = weather.value;
        weather.addEventListener('change', () => { destination.value = weather.value; updateBooking(); });
      }
      updateBooking();
    } catch (_) { /* Keep the validated static affiliate link usable. */ }
  }
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

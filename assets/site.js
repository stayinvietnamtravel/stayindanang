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
    try {
      const names = new Intl.DisplayNames([document.documentElement.lang], {type: 'region'});
      select.querySelectorAll('[data-country-code]').forEach(group => { group.label = names.of(group.dataset.countryCode); });
    } catch (_) {}
    const update = () => {
      panels.forEach(panel => { panel.hidden = panel.dataset.weatherCity !== select.value; });
      try { localStorage.setItem('stayindanang-destination:v1', select.value); } catch (_) {}
    };
    try {
      const saved = localStorage.getItem('stayindanang-destination:v1');
      if (panels.some(panel => panel.dataset.weatherCity === saved)) select.value = saved;
    } catch (_) {}
    const requested = new URLSearchParams(location.search).get('weather');
    if (panels.some(panel => panel.dataset.weatherCity === requested)) select.value = requested;
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
      const continent = booking.querySelector('.booking-continent');
      const country = booking.querySelector('.booking-country');
      const service = booking.querySelector('.booking-service');
      const hotel = booking.querySelector('.booking-property');
      const action = booking.querySelector('.booking-action');
      const weather = document.querySelector('#weather-city');
      let countryNames;
      try { countryNames = new Intl.DisplayNames([document.documentElement.lang], {type:'region'}); } catch (_) {}
      if (countryNames) {
        country.querySelectorAll('[data-country-code]').forEach(option => { option.textContent = countryNames.of(option.dataset.countryCode); });
        destination.querySelectorAll('optgroup').forEach(group => { group.label = countryNames.of(group.dataset.countryCode); });
      }
      const allCountries = Array.from(country.options).map(option => option.cloneNode(true));
      const allGroups = Array.from(destination.children).map(group => group.cloneNode(true));
      const allCities = Array.from(destination.options);
      const preferenceKey = 'stayindanang-booking-destination:v1';
      const filterCountries = () => {
        const previous = country.value;
        country.replaceChildren(...allCountries.filter(option => option.value === 'all' || continent.value === 'all' || option.dataset.continent === continent.value).map(option => option.cloneNode(true)));
        country.value = Array.from(country.options).some(option => option.value === previous) ? previous : 'all';
      };
      const filterCities = (preferred = destination.value) => {
        const groups = allGroups.map(original => {
          const group = original.cloneNode(true);
          Array.from(group.children).forEach(option => {
            if ((continent.value !== 'all' && option.dataset.continent !== continent.value) || (country.value !== 'all' && option.dataset.country !== country.value)) option.remove();
          });
          return group;
        }).filter(group => group.children.length);
        destination.replaceChildren(...groups);
        destination.value = Array.from(destination.options).some(option => option.value === preferred) ? preferred : destination.options[0].value;
      };
      booking.querySelectorAll('[data-booking-service]').forEach(button => button.addEventListener('click', () => { service.value=button.dataset.bookingService;service.dispatchEvent(new Event('change',{bubbles:true})); }));
      const allHotelOptions = Array.from(hotel.options).map(option => option.cloneNode(true));
      const updateBooking = () => {
        booking.querySelectorAll('[data-booking-service]').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.bookingService === service.value)));
        const previousHotel = hotel.value;
        hotel.replaceChildren(...allHotelOptions.filter(option => !option.value || option.dataset.city === destination.value).map(option => option.cloneNode(true)));
        if (Array.from(hotel.options).some(option => option.value === previousHotel)) hotel.value = previousHotel;
        const specific = ['da-nang', 'hanoi'].includes(destination.value) && service.value === 'hotels';
        hotel.disabled = !specific;
        booking.querySelector('.booking-property-field').hidden = !specific;
        const hotelKey = specific ? hotel.value : '';
        const target = hotelKey ? routes.hotels[hotelKey] : routes.routes[destination.value]?.[service.value] || routes.services[service.value] || routes.default_url;
        const parsed = new URL(target);
        if (parsed.protocol !== 'https:' || parsed.hostname !== 'www.trip.com' || !/^\/(t|w)\/[a-zA-Z0-9]+$/.test(parsed.pathname) || parsed.search || parsed.hash || parsed.username || parsed.password || parsed.port) return;
        action.href = target;
        action.dataset.affiliate = hotelKey ? `hotel-${hotelKey}` : `planner-${destination.value}-${service.value}`;
        const city = destination.selectedOptions[0];
        const countryLabel = allCountries.find(option => option.value === city.dataset.country)?.textContent;
        const summary = [city.textContent];
        if (countryLabel && countryLabel !== city.textContent) summary.push(countryLabel);
        summary.push(service.selectedOptions[0].textContent);
        if (hotelKey) summary.push(hotel.selectedOptions[0].textContent);
        booking.querySelector('.booking-summary').textContent = summary.join(' · ');
        try { localStorage.setItem(preferenceKey, destination.value); } catch (_) {}
      };
      const syncWeather = () => {
        if (weather && Array.from(weather.options).some(option => option.value === destination.value)) {
          weather.value = destination.value;
          weather.dispatchEvent(new Event('change'));
        }
      };
      continent.addEventListener('change', () => {
        country.value = 'all';filterCountries();filterCities();updateBooking();syncWeather();
      });
      country.addEventListener('change', () => { filterCities();updateBooking();syncWeather(); });
      destination.addEventListener('change', () => { updateBooking();syncWeather(); });
      service.addEventListener('change', updateBooking);
      hotel.addEventListener('change', updateBooking);
      let initial = weather?.value || 'da-nang';
      try {
        const saved = localStorage.getItem(preferenceKey);
        if (!new URLSearchParams(location.search).get('weather') && allCities.some(option => option.value === saved)) initial = saved;
      } catch (_) {}
      destination.value = initial;
      if (weather) weather.addEventListener('change', () => {
        // Synchronize world forecast choices with the matching country and city.
        if (weather.value === destination.value) return;
        const city = allCities.find(option => option.value === weather.value);
        if (!city) return;
        continent.value = city.dataset.continent;filterCountries();country.value = city.dataset.country;filterCities(weather.value);updateBooking();
      });
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

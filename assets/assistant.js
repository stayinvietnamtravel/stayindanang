(function () {
  'use strict';
  const widget = document.querySelector('.travel-chat');
  if (!widget) return;
  const dialog = widget.querySelector('dialog');
  const messages = widget.querySelector('.chat-messages');
  const form = widget.querySelector('.chat-form');
  const input = form.querySelector('input');
  const locale = document.documentElement.lang || 'en';
  let data, labels, loaded, aiReady = false, busy = false;
  const history = [];
  const clean = text => String(text).normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/đ/g,'d').toLowerCase();
  const api = async (path, options = {}) => {
    if (!data?.backendUrl) throw new Error('Unavailable');
    const response = await fetch(data.backendUrl + path, {...options, signal: AbortSignal.timeout(25000), credentials:'omit'});
    if (!response.ok) throw new Error('Unavailable');
    return response.json();
  };
  const allowedLink = value => {
    try { const url = new URL(value); return url.protocol === 'https:' && !url.username && !url.password && (url.origin + url.pathname).startsWith(data.base) || url.protocol === 'https:' && url.hostname === 'www.trip.com' && !url.username && !url.password && !url.port && !url.search && !url.hash && /^\/(t|w)\/[A-Za-z0-9]+$/.test(url.pathname); } catch (_) { return false; }
  };
  const append = (text, role, links = []) => {
    const article = document.createElement('div');article.className = 'chat-message chat-' + role;
    const paragraph = document.createElement('p');paragraph.textContent = text;article.append(paragraph);
    links.slice(0,5).forEach(link => {
      if (!allowedLink(link.url)) return;
      const anchor = document.createElement('a');anchor.textContent = link.label;anchor.href = link.url;anchor.target = '_blank';anchor.rel = link.url.includes('www.trip.com/') ? 'sponsored noopener noreferrer' : 'noopener noreferrer';
      if (link.url.includes('www.trip.com/')) anchor.addEventListener('click', () => { window.dataLayer = window.dataLayer || [];window.dataLayer.push({event:'affiliate_click',category:'chat-'+(link.service || 'travel'),page:location.pathname}); });
      article.append(anchor);
    });messages.append(article);messages.scrollTop = messages.scrollHeight;
  };
  const guideReply = question => {
    const text = clean(question);
    const isDestination = Object.values(data.cities).some(city => [city.name,...(city.aliases || [])].some(name => clean(name) === text));
    const partial = text.length >= 6 && !isDestination ? data.hotels.filter(h => clean(h.name).includes(text)) : [];
    const hotel = data.hotels.find(h => text.includes(clean(h.name))) || (partial.length === 1 ? partial[0] : null);
    const region = location.pathname.match(/\/explore\/[^/]+\/(asia|europe|americas|oceania)\//)?.[1];
    const selectedCity = document.querySelector('.booking-destination')?.value || (region ? Object.entries(data.cities).find(([,city]) => city.region === region)?.[0] : null);
    const city = Object.entries(data.cities).find(([key,value]) => [value.name,...(value.aliases || [])].some(name => text.includes(clean(name))) || text.includes(key.replace(/-/g,' ')))?.[0] || selectedCity || 'da-nang';
    let service = Object.entries(labels.services).find(([,label]) => text.includes(clean(label)))?.[0];
    const intents = {hotels:/hotel|khach san|resort|住宿|酒店|飯店|отел|숙소|ホテル|होटल|โรงแรม/,flights:/flight|fly|chuyen bay|ve may bay|机票|機票|авиа|항공|航空|उड़ान|เที่ยวบิน/,tours:/tour|ticket|tham quan|旅游|旅遊|門票|门票|тур|투어|ツアー|टूर|ทัวร์/,transfers:/transfer|airport pickup|dua don|接送|трансфер|픽업|送迎|स्थानांतरण|รถรับส่ง/,cars:/car rental|thue xe|租车|租車|аренд|렌터카|レンタカー|किराया|รถเช่า/};
    if (!service) service = Object.keys(intents).find(key => intents[key].test(text));
    if (text.includes(clean(labels.weatherTitle)) || /weather|thoi tiet|天气|天氣|погод|날씨|天気|मौसम|อากาศ|meteo|wetter|cuaca/.test(text)) return {answer:labels.weather,links:[{label:(data.cities[city]?.name || labels.weatherTitle)+' · '+labels.ui[0],url:data.base+(locale==='en'?'':locale+'/')+(data.cities[city]?'?weather='+city:'')+'#weather'}]};
    if (hotel) {
      const requestedGroup = /top deals?|hot deals?/.test(text) ? 'Top Deals' : /hot sellers?/.test(text) ? 'Hot Sellers' : null;
      const offer = hotel.offers?.find(item => item.group === requestedGroup);
      return {answer:hotel.name+'\n'+labels.booking,links:[{label:labels.services.hotels+' · Trip.com'+(offer ? ' · '+offer.group : ''),url:offer?.url || hotel.url,service:'hotels'},{label:labels.ui[5],url:data.base+(hotel.city && hotel.city!=='da-nang'?'blog/'+locale+'/destinations/'+hotel.city+'/hotels/'+hotel.slug+'/':'deals/'+locale+'/'+hotel.slug+'/')}]};
    }
    const guideRegion = data.cities[city]?.region || 'asia';
    const links = [{label:labels.ui[5],url:data.base+'explore/'+locale+'/'+guideRegion+'/'}];
    if (service) links.unshift({label:labels.services[service]+' · Trip.com',url:data.services[service],service});
    else ['hotels','tours','flights'].forEach(key => links.push({label:labels.services[key]+' · Trip.com',url:data.services[key],service:key}));
    return {answer:service ? labels.booking : labels.guide,links};
  };
  const load = () => loaded || (loaded = (async () => {
    const response = await fetch(widget.dataset.chatData,{credentials:'omit'});if (!response.ok) throw new Error('Unavailable');data = await response.json();labels = data.locales[locale] || data.locales.en;
    append(labels.ui[7],'assistant');
    Object.entries(labels.services).forEach(([key,text]) => { const button = document.createElement('button');button.type = 'button';button.textContent = text;button.addEventListener('click', () => { input.value = text;form.requestSubmit(); });widget.querySelector('.chat-questions').append(button); });
    [labels.weatherTitle,labels.planningTitle].forEach(text => { const button = document.createElement('button');button.type = 'button';button.textContent = text;button.addEventListener('click', () => { input.value = text;form.requestSubmit(); });widget.querySelector('.chat-questions').append(button); });
    if (data.backendUrl) {
      try { const status = await api('/health');aiReady = status.chatReady === true;widget.querySelector('.chat-mode').textContent = labels.ui[aiReady ? 6 : 5]; } catch (_) {}
      setupStatistics();
    }
  })());
  widget.querySelector('.chat-open').addEventListener('click', async () => { dialog.showModal();input.focus();try { await load(); } catch (_) { loaded = null; } });
  widget.querySelector('.chat-close').addEventListener('click', () => dialog.close());
  form.addEventListener('submit', async event => {
    event.preventDefault();const question = input.value.trim();if (!question || busy) return;
    try { await load(); } catch (_) { return; }
    busy = true;form.querySelector('button').disabled = true;append(question,'user');input.value = '';
    try {
      let reply;
      if (aiReady) {
        widget.querySelector('.chat-mode').textContent = labels.ui[8];
        try { reply = await api('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:question,language:locale,cityKey:document.querySelector('.booking-destination')?.value || null,history:history.slice(-6)})}); }
        catch (_) { append(labels.ui[9],'assistant');reply = guideReply(question); }
      } else reply = guideReply(question);
      append(reply.answer,'assistant',reply.links || []);history.push({role:'user',content:question},{role:'assistant',content:reply.answer.slice(0,800)});
      if (history.length > 8) history.splice(0,history.length-8);
    } finally { busy = false;form.querySelector('button').disabled = false;widget.querySelector('.chat-mode').textContent = labels.ui[aiReady ? 6 : 5];input.focus(); }
  });
  function setupStatistics() {
    const panel = document.querySelector('.visitor-statistics');if (!panel) return;
    const consentKey = 'stayindanang-analytics-consent:v1';
    const storageGet = key => { try { return localStorage.getItem(key); } catch (_) { return null; } };
    const storageSet = (key,value) => { try { localStorage.setItem(key,value); } catch (_) {} };
    const count = panel.querySelector('.visitor-count');
    const refresh = () => api('/public-stats').then(value => { count.textContent = labels.ui[18]+': '+Number(value.visits || 0)+' · 7d'; }).catch(() => { count.textContent = labels.ui[11]; });
    const record = () => {
      const stamp = new Date().toISOString().slice(0,10), key = 'stayindanang-analytics-day:v1';
      if (storageGet(key) === stamp) return;
      api('/visit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({consent:true,path:location.pathname})}).then(() => { storageSet(key,stamp);refresh(); }).catch(() => {});
    };
    const consent = storageGet(consentKey);
    panel.querySelector('.analytics-consent').hidden = consent !== null;
    panel.querySelector('.analytics-revoke').hidden = consent !== 'yes';
    if (consent === 'yes') record();
    panel.querySelectorAll('[data-analytics-consent]').forEach(button => button.addEventListener('click', () => { storageSet(consentKey,button.dataset.analyticsConsent);panel.querySelector('.analytics-consent').hidden = true;panel.querySelector('.analytics-revoke').hidden = button.dataset.analyticsConsent !== 'yes';if (button.dataset.analyticsConsent === 'yes') record(); }));
    panel.querySelector('.analytics-revoke').addEventListener('click', () => { storageSet(consentKey,'no');panel.querySelector('.analytics-revoke').hidden = true; });
    const adminForm = panel.querySelector('.analytics-admin-form');
    panel.querySelector('.analytics-admin').addEventListener('toggle', event => {
      if (!event.target.open) { panel.querySelector('.analytics-results').replaceChildren();panel.querySelector('.analytics-status').textContent = '';adminForm.elements.token.value = ''; }
    });
    adminForm.addEventListener('submit', async event => {
      event.preventDefault();const token = adminForm.elements.token.value;adminForm.elements.token.value = '';const results = panel.querySelector('.analytics-results');results.replaceChildren();
      try {
        const result = await api('/stats',{headers:{Authorization:'Bearer '+token}});
        if (!panel.querySelector('.analytics-admin').open) return;
        panel.querySelector('.analytics-status').textContent = labels.ui[18]+': '+result.visits+' · '+labels.ui[19]+': '+result.uniqueIps;
        const table = document.createElement('table');
        result.ips.forEach(item => { const row = table.insertRow();row.insertCell().textContent = item.ip;row.insertCell().textContent = String(item.visits);row.insertCell().textContent = new Date(item.lastSeen).toLocaleString(locale,{timeZone:'Asia/Bangkok'}); });results.append(table);
      } catch (_) { panel.querySelector('.analytics-status').textContent = labels.ui[11]; }
    });refresh();
  }
  // No IP collection or external AI request occurs unless a backend is configured.
  if (document.querySelector('.visitor-statistics')) load().catch(() => {});
}());

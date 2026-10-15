"""Responsive discovery cards and affiliate routes preserving supplied short links."""
from pathlib import Path
from html import escape as E
from urllib.parse import urlsplit
import json
import re
from deal_posts import HOTELS, image_path, post_path, index_path, COPY as HOTEL_COPY
from home_tools import COPY as HOME_COPY
from destinations import CITIES, DESTINATIONS
from world_destinations import COUNTRIES, CITY_KEYS, REGIONS, REGION_KEYS, country_name, city_name
from content import CONTENT
from responsive_images import image as responsive_image
from hotel_visuals import cover as hotel_cover
from hanoi_hotels import HOTELS as HANOI_HOTELS
from travel_art import COPY as ART_COPY
from travel_art import cover as art_cover, dimensions as art_dimensions
ROOT=Path(__file__).resolve().parents[1]
CONFIG=json.loads((ROOT/'data/affiliate_routes.json').read_text())

def valid_url(value):
    p=urlsplit(value)
    if p.scheme!='https' or p.hostname!='www.trip.com' or p.username or p.password or p.port or p.query or p.fragment or not re.fullmatch(r'/(t|w)/[A-Za-z0-9]+',p.path) or any(c.isspace() for c in value):
        raise ValueError('Affiliate route must be an original Trip.com short link')
    return value

valid_url(CONFIG['default_url'])
for link in CONFIG['services'].values():valid_url(link)
for city,routes in CONFIG['routes'].items():
    if city not in CITY_KEYS:raise ValueError('Unknown affiliate destination')
    for service,link in routes.items():
        if service not in ('hotels','tours','flights','transfers','cars'):raise ValueError('Unknown affiliate service')
        valid_url(link)
for hotel in HOTELS:valid_url(hotel['url'])

# planner title, destination/service/property labels, all hotels, CTA, fallback notice,
# sights/experiences/hotels headings, more/save/saved/previous/next/all/saved-only/empty.
UI={
'vi':['Lên chuyến đi theo cách của bạn','Điểm đến','Dịch vụ','Khách sạn','Tất cả khách sạn','Mở Trip.com →','Mở Trip.com để tiếp tục chọn điểm đến, dịch vụ và ngày đi.','Điểm đến đáng khám phá ở miền Trung','Trải nghiệm cho chuyến đi đáng nhớ','Khách sạn gợi ý tại Đà Nẵng','Xem thêm →','Lưu','Đã lưu','Trước','Tiếp','Tất cả','Đã lưu','Chưa có mục phù hợp. Hãy lưu một khách sạn hoặc chọn bộ lọc khác.'],
'en':['Plan a trip your way','Destination','Service','Hotel','All hotels','Open Trip.com →','Continue on Trip.com to choose your destination, service and travel dates.','Sights to explore in Central Vietnam','Make room for memorable experiences','Selected hotels in Da Nang','View more →','Save','Saved','Previous','Next','All','Saved','No matching items. Save a hotel or choose another filter.'],
'fr':['Composez votre voyage','Destination','Service','Hôtel','Tous les hôtels','Ouvrir Trip.com →','Sur Trip.com, choisissez destination, service et dates.','Sites à découvrir au centre du Vietnam','Des expériences mémorables','Sélection d’hôtels à Da Nang','Voir plus →','Enregistrer','Enregistré','Précédent','Suivant','Tous','Enregistrés','Aucun résultat. Enregistrez un hôtel ou changez de filtre.'],
'de':['Ihre Reise planen','Reiseziel','Service','Hotel','Alle Hotels','Trip.com öffnen →','Reiseziel, Service und Reisedaten auf Trip.com auswählen.','Sehenswürdigkeiten in Zentralvietnam','Erlebnisse für Ihre Reise','Hotelauswahl in Da Nang','Mehr ansehen →','Merken','Gemerkt','Zurück','Weiter','Alle','Gemerkt','Keine passenden Einträge. Hotel merken oder Filter ändern.'],
'es':['Diseña tu viaje','Destino','Servicio','Hotel','Todos los hoteles','Abrir Trip.com →','Elige destino, servicio y fechas en Trip.com.','Lugares de Vietnam central','Experiencias memorables','Hoteles seleccionados en Da Nang','Ver más →','Guardar','Guardado','Anterior','Siguiente','Todos','Guardados','Sin resultados. Guarda un hotel o cambia el filtro.'],
'zh':['规划你的旅程','目的地','服务','酒店','所有酒店','打开 Trip.com →','在 Trip.com 继续选择目的地、服务和旅行日期。','探索越南中部景点','难忘的旅行体验','岘港精选酒店','查看更多 →','收藏','已收藏','上一页','下一页','全部','已收藏','暂无匹配项目，请收藏酒店或更换筛选。'],
'zh-Hant':['規劃你的旅程','目的地','服務','飯店','所有飯店','開啟 Trip.com →','在 Trip.com 繼續選擇目的地、服務和旅行日期。','探索越南中部景點','難忘的旅行體驗','峴港精選飯店','查看更多 →','收藏','已收藏','上一頁','下一頁','全部','已收藏','暫無符合項目，請收藏飯店或更換篩選。'],
'ru':['Спланируйте путешествие','Направление','Услуга','Отель','Все отели','Открыть Trip.com →','На Trip.com выберите направление, услугу и даты.','Достопримечательности Центрального Вьетнама','Впечатления от путешествия','Выбор отелей в Дананге','Подробнее →','Сохранить','Сохранено','Назад','Далее','Все','Сохранённые','Нет подходящих вариантов. Сохраните отель или смените фильтр.'],
'ko':['나만의 여행 계획','여행지','서비스','호텔','모든 호텔','Trip.com 열기 →','Trip.com에서 여행지, 서비스와 날짜를 선택하세요.','베트남 중부의 명소','기억에 남을 여행 경험','다낭 추천 호텔','더 보기 →','저장','저장됨','이전','다음','전체','저장됨','결과가 없습니다. 호텔을 저장하거나 필터를 바꾸세요.'],
'ja':['自分らしい旅を計画','目的地','サービス','ホテル','すべてのホテル','Trip.com を開く →','Trip.comで目的地、サービスと旅行日を選択してください。','ベトナム中部の見どころ','思い出に残る体験','ダナンのホテル選び','もっと見る →','保存','保存済み','前へ','次へ','すべて','保存済み','該当なし。ホテルを保存するかフィルターを変更してください。'],
'hi':['अपनी यात्रा की योजना बनाएँ','गंतव्य','सेवा','होटल','सभी होटल','Trip.com खोलें →','Trip.com पर गंतव्य, सेवा और यात्रा तारीख चुनें।','मध्य वियतनाम के दर्शनीय स्थल','यादगार यात्रा अनुभव','दा नांग के चुने हुए होटल','और देखें →','सहेजें','सहेजा गया','पिछला','अगला','सभी','सहेजे गए','कोई परिणाम नहीं। होटल सहेजें या फ़िल्टर बदलें।'],
'th':['วางแผนทริปในแบบคุณ','จุดหมาย','บริการ','โรงแรม','โรงแรมทั้งหมด','เปิด Trip.com →','เลือกจุดหมาย บริการและวันเดินทางต่อบน Trip.com','สถานที่น่าเที่ยวในเวียดนามกลาง','ประสบการณ์น่าจดจำ','โรงแรมที่คัดเลือกในดานัง','ดูเพิ่มเติม →','บันทึก','บันทึกแล้ว','ก่อนหน้า','ถัดไป','ทั้งหมด','บันทึกแล้ว','ไม่มีรายการที่ตรงกัน บันทึกโรงแรมหรือเปลี่ยนตัวกรอง'],
'id':['Rencanakan perjalanan Anda','Destinasi','Layanan','Hotel','Semua hotel','Buka Trip.com →','Pilih destinasi, layanan dan tanggal perjalanan di Trip.com.','Tempat menarik di Vietnam tengah','Pengalaman yang berkesan','Pilihan hotel di Da Nang','Lihat lainnya →','Simpan','Tersimpan','Sebelumnya','Berikutnya','Semua','Tersimpan','Tidak ada hasil. Simpan hotel atau ubah filter.'],
}

def favorite(key,title,u):
    return f'<button class="save-card" type="button" data-save-id="{E(key)}" data-save-label="{E(u[11])}" data-saved-label="{E(u[12])}" data-item-title="{E(title)}" aria-label="{E(u[11]+": "+title)}" aria-pressed="false"><span aria-hidden="true">♡</span></button>'

def affiliate_config():
    data={**CONFIG,'hotels':{**{h['slug']:h['url'] for h in HOTELS},**{h['slug']:h['urls'][0] for h in HANOI_HOTELS}}}
    return '<script type="application/json" id="affiliate-routes">'+json.dumps(data,ensure_ascii=False).replace('<','\\u003c')+'</script>'

def booking(lang,current,relative):
    u=UI[lang];content=CONTENT[lang]['ui'];names=DESTINATIONS[lang][3]
    world=REGIONS[lang]
    result=f'<section class="booking-hub" id="booking"><div class="container"><div class="booking-panel"><div class="section-heading"><h2>{E(u[0])}</h2><a class="text-link" href="{relative(current,index_path(lang))}">{E(u[10])}</a></div><div class="booking-geography"><label>{E(world[0])}<select class="booking-continent"><option value="all">{E(world[3])}</option>'
    for key,label in zip(REGION_KEYS,world[4:]):result+=f'<option value="{key}">{E(label)}</option>'
    result+=f'</select></label><label>{E(world[1])}<select class="booking-country"><option value="all">{E(world[3])}</option>'
    for country in COUNTRIES:result+=f'<option value="{country[1]}" data-continent="{country[0]}" data-country-code="{country[1]}">{E(country_name(country,lang))}</option>'
    result+=f'</select></label></div><div class="booking-fields"><label>{E(world[2])}<select class="booking-destination">'
    for country in COUNTRIES:
        result+=f'<optgroup label="{E(country_name(country,lang))}" data-country-code="{country[1]}">'
        for city in country[4]:result+=f'<option value="{city[0]}" data-country="{country[1]}" data-continent="{country[0]}">{E(city_name(city,lang))}</option>'
        result+='</optgroup>'
    result+=f'</select></label><label>{E(u[2])}<select class="booking-service">'
    for key,label in service_labels(lang).items():
        result+=f'<option value="{key}">{E(label)}</option>'
    result+=f'</select></label><label class="booking-property-field">{E(u[3])}<select class="booking-property"><option value="">{E(u[4])}</option>'
    for h in HOTELS:result+=f'<option value="{h["slug"]}" data-city="da-nang">{E(h["display_name"])}</option>'
    for h in HANOI_HOTELS:result+=f'<option value="{h["slug"]}" data-city="hanoi">{E(h["name"])}</option>'
    result+=f'</select></label><a class="btn booking-action" href="{E(CONFIG["services"]["hotels"])}" target="_blank" rel="sponsored noopener noreferrer" data-affiliate="planner-da-nang-hotels">{E(u[5])}</a></div><p class="booking-summary" aria-live="polite">{E(names[0])} · {E(content[3])}</p><p class="notice">{E(u[6])}</p><p class="notice">{E(content[9])}</p></div></div></section>'
    result=result.replace('<div class="booking-geography">',f'<details class="booking-advanced"><summary>{E(world[0])} / {E(world[1])}</summary><div class="booking-geography">',1)
    result=result.replace('</div><div class="booking-fields">','</div></details><div class="booking-fields">',1)
    return result+affiliate_config()

FLIGHTS={'vi':'Chuyến bay','en':'Flights','fr':'Vols','de':'Flüge','es':'Vuelos','zh':'机票','zh-Hant':'機票','ru':'Авиабилеты','ko':'항공편','ja':'航空券','hi':'उड़ानें','th':'เที่ยวบิน','id':'Penerbangan'}

SIGHTS=[('Ba Na Hills · Golden Bridge','tours/da-nang-hoi-an-hue','ba-na-hills','01'),('Ngũ Hành Sơn · Marble Mountains','tours/da-nang-hoi-an-hue','marble-mountains','02'),('Hội An · Old Town','destinations/vietnam-heritage-guide','hoi-an','03'),('Huế · Imperial City','tours/da-nang-hoi-an-hue','hue','04')]
EXPERIENCES=[('destinations','ninh-binh-two-day-escape'),('experiences','sapa-valley-walks'),('tips','phu-quoc-three-day-plan'),('food','vietnam-food-guide'),('experiences','coastal-vietnam-experiences'),('tips','da-nang-hotels-tours-flights-2026'),('destinations','hanoi-ho-chi-minh-city-walks')]
FEATURED=['menora-grand-da-nang','ocean-garden-boutique-da-nang-a-salve-by-haviland','haian-beach-hotel-spa','sala-danang-beach-hotel','hilton-da-nang','tui-blue-han-river','furama-resort-danang','tms-hotel-da-nang-beach']

def rail_start(section,title,more,current,relative,u):
    return f'<section class="discovery-section" id="{section}"><div class="container"><div class="section-heading"><h2>{E(title)}</h2><div class="rail-controls"><a class="text-link" href="{relative(current,more)}">{E(u[10])}</a><button type="button" data-rail-direction="-1" aria-label="{E(u[13])}">‹</button><button type="button" data-rail-direction="1" aria-label="{E(u[14])}">›</button></div></div><div class="discovery-rail" tabindex="0" aria-label="{E(title)}">'

def discovery(lang,current,relative):
    u=UI[lang];content=CONTENT[lang];guide=HOME_COPY[lang][21]
    result=rail_start('destinations',u[7],f'blog/{lang}/tours/da-nang-hoi-an-hue/index.html',current,relative,u)
    for title,article,image,num in SIGHTS:
        path="assets/ai-travel/"+image+".png"
        if not (ROOT/path).exists():path="assets/discovery/"+image+".svg"
        img=responsive_image(path,current,relative,title+" · "+ART_COPY[lang][1])
        result+=f'<article class="sight-card">{favorite("sight-"+num,title,u)}<a class="sight-cover" href="{relative(current,f"blog/{lang}/{article}/index.html")}">{img}<span class="image-ai-badge" title="{E(ART_COPY[lang][1])}">AI</span><div class="sight-caption"><span class="pill">{E(content["ui"][5])}</span><h3>{E(title)}</h3><span>{E(guide)}</span></div></a></article>'
    result+='</div>'+service_action('tours',lang)+'</div></section>'
    result+=rail_start('tours',u[8],f'blog/{lang}/experiences/coastal-vietnam-experiences/index.html',current,relative,u)
    from content import SLUGS
    for category,slug in EXPERIENCES:
        title,intro,_=content['articles'][SLUGS.index((category,slug))]
        art=art_cover(slug);width,height=art_dimensions(art)
        img=responsive_image(art,current,relative,title+" · "+ART_COPY[lang][1],sizes="(max-width: 700px) 80vw, 300px")
        result+=f'<article class="experience-card">{favorite("guide-"+slug,title,u)}<span class="image-ai-badge" title="{E(ART_COPY[lang][1])}">AI</span><a href="{relative(current,f"blog/{lang}/{category}/{slug}/index.html")}">{img}<div class="experience-body"><h3>{E(title)}</h3><span class="text-link">{E(guide)}</span></div></a></article>'
    result+='</div></div></section>'
    result+=rail_start('hotels',u[9],index_path(lang),current,relative,u)
    # Filters precede the rail without duplicating nested button/link hit areas.
    result=result.removesuffix('<div class="discovery-rail" tabindex="0" aria-label="'+E(u[9])+'">')
    result+=f'<div class="hotel-tabs" role="group" aria-label="{E(u[9])}">'
    for key,label in [('all',u[15]),('top-deals','Top Deals'),('hot-sellers','Hot Sellers'),('saved',u[16])]:result+=f'<button type="button" data-hotel-tab="{key}" aria-pressed="{str(key=="all").lower()}">{E(label)}</button>'
    result+=f'</div><div class="discovery-rail hotel-rail" tabindex="0" aria-label="{E(u[9])}">'
    for slug in FEATURED:
        h=next(h for h in HOTELS if h['slug']==slug)
        img=hotel_cover(h,'da-nang',lang,current,relative)
        result+=f'<article class="hotel-pick" data-hotel-group="{h["group"].lower().replace(" ","-")}" data-saved-id="hotel-{slug}">{favorite("hotel-"+slug,h["display_name"],u)}<a class="hotel-artwork" href="{relative(current,post_path(lang,h))}">{img}</a><div class="hotel-pick-body"><small>{E(DESTINATIONS[lang][3][0])} · {h["group"]}</small><h3><a href="{relative(current,post_path(lang,h))}">{E(h["display_name"])}</a></h3><p>{E(HOTEL_COPY[lang][7])}</p><a class="hotel-book-link" href="{E(h["url"])}" target="_blank" rel="sponsored noopener noreferrer" data-affiliate="hotel-{slug}">{E(HOTEL_COPY[lang][3].replace('↗','→'))}</a></div></article>'
    result+=f'</div><p class="saved-empty" hidden>{E(u[17])}</p></div></section>'
    result+=f'<section class="service-links" id="flights"><div class="container"><div class="service-link-card"><span aria-hidden="true">✈</span><div><h2>{E(FLIGHTS[lang])}</h2><p>{E(u[6])}</p></div><a class="btn" href="{E(CONFIG["services"]["flights"])}" target="_blank" rel="sponsored noopener noreferrer" data-affiliate="flight-general">{E(u[5])}</a></div></div></section><section class="service-links" id="deals"><div class="container"><a class="deals-shortcut" href="{relative(current,index_path(lang))}">{E(HOTEL_COPY[lang][0])}<span>{E(u[10])}</span></a></div></section>'
    result+=transport_cards(lang)
    return result

def marketplace(lang,current,relative):return booking(lang,current,relative)+discovery(lang,current,relative)


TRANSPORT={
'vi':['Đưa đón sân bay','Thuê xe'], 'en':['Airport transfers','Car rentals'],
'fr':['Transferts aéroport','Location de voiture'], 'de':['Flughafentransfers','Mietwagen'],
'es':['Traslados al aeropuerto','Alquiler de coches'], 'zh':['机场接送','租车'],
'zh-Hant':['機場接送','租車'], 'ru':['Трансфер из аэропорта','Аренда автомобиля'],
'ko':['공항 픽업','렌터카'], 'ja':['空港送迎','レンタカー'],
'hi':['हवाई अड्डा स्थानांतरण','कार किराया'], 'th':['รถรับส่งสนามบิน','รถเช่า'],
'id':['Transfer bandara','Sewa mobil']}

TOURS={'vi':'Tour & vé tham quan','en':'Tours & tickets','fr':'Excursions et billets','de':'Touren und Tickets','es':'Tours y entradas','zh':'旅游与门票','zh-Hant':'旅遊與門票','ru':'Туры и билеты','ko':'투어 및 티켓','ja':'ツアー・チケット','hi':'टूर और टिकट','th':'ทัวร์และบัตรเข้าชม','id':'Tur dan tiket'}

def service_labels(lang):
    content=CONTENT[lang]['ui']
    return {'hotels':content[3],'tours':TOURS[lang],'flights':FLIGHTS[lang],'transfers':TRANSPORT[lang][0],'cars':TRANSPORT[lang][1]}

def service_url(service,city=None):
    return CONFIG['routes'].get(city,{}).get(service,CONFIG['services'].get(service,CONFIG['default_url']))

def service_action(service,lang):
    return f'<p class="discovery-booking"><a class="text-link" href="{E(service_url(service))}" target="_blank" rel="sponsored noopener noreferrer" data-affiliate="discovery-{service}">{E(service_labels(lang)[service])} · Trip.com →</a></p>'

def transport_cards(lang):
    result='<section class="service-links"><div class="container transport-grid">'
    for service,icon in [('transfers','↔'),('cars','⌁')]:
        result+=f'<div class="service-link-card"><span aria-hidden="true">{icon}</span><div><h2>{E(service_labels(lang)[service])}</h2><p>{E(UI[lang][6])}</p></div><a class="btn" href="{E(service_url(service))}" target="_blank" rel="sponsored noopener noreferrer" data-affiliate="transport-{service}">{E(UI[lang][5])}</a></div>'
    return result+'</div></section>'

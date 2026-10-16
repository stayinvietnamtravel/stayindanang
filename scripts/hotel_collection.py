"""Unified hotel collection using the owner's supplied category and affiliate data."""
from pathlib import Path
from html import escape as E
from deal_posts import HOTELS as DANANG,post_path as danang_post,COPY as DEAL_COPY
from hanoi_hotels import HOTELS as HANOI,post_path as hanoi_post
from hotel_visuals import cover
from content import CONTENT
from southern_hotels import HOTELS as SOUTHERN,post_path as southern_post,CITY_LABELS as SOUTHERN_CITIES
CITY_LABELS={"da-nang":"Đà Nẵng","hanoi":"Hà Nội",**SOUTHERN_CITIES}
COPY={
'vi':['Hot Deals & Hot Sellers','Khám phá các khách sạn tại Việt Nam; so sánh vị trí, loại phòng và điều kiện trước khi đặt.','Tìm theo tên khách sạn','Tất cả điểm đến','Xem toàn bộ khách sạn','Giá và phòng trống cần kiểm tra theo ngày đi. Hot Deals / Hot Sellers là nhóm gợi ý, không phải xác nhận giảm giá hay xếp hạng bán chạy theo thời gian thực.','Không tìm thấy khách sạn phù hợp. Thử đổi bộ lọc hoặc tên tìm kiếm.','Xóa bộ lọc','khách sạn'],
'en':['Hot Deals & Hot Sellers','Explore stays across Vietnam. Compare location, room types and conditions before booking.','Search hotel names','All destinations','View all hotels','Check prices and availability for your travel dates. Hot Deals / Hot Sellers are reference categories, not verified discounts or live sales rankings.','No matching hotels. Try another filter or search term.','Clear filters','hotels'],
'zh':['Hot Deals & Hot Sellers','探索越南酒店，预订前比较位置、房型和条件。','搜索酒店名称','全部目的地','查看所有酒店','请按出行日期确认价格与空房。Hot Deals / Hot Sellers 为参考分类，不代表已核实折扣或实时销量排名。','未找到匹配酒店，请调整筛选或搜索词。','清除筛选','家酒店'],
'zh-Hant':['Hot Deals & Hot Sellers','探索越南飯店，預訂前比較位置、房型及條件。','搜尋飯店名稱','全部目的地','查看所有飯店','請依日期確認價格與空房。Hot Deals / Hot Sellers 為參考分類，不代表已核實折扣或即時銷量。','沒有符合的飯店，請調整篩選或搜尋詞。','清除篩選','間飯店'],
'ru':['Hot Deals & Hot Sellers','Сравните отели Вьетнама по расположению, номерам и условиям бронирования.','Поиск по названию отеля','Все направления','Все отели','Цены и наличие проверяйте на свои даты. Hot Deals / Hot Sellers — справочные категории, не подтверждённые скидки или текущий рейтинг продаж.','Нет подходящих отелей. Измените фильтр или запрос.','Сбросить фильтры','отелей'],
'ko':['Hot Deals & Hot Sellers','베트남 호텔의 위치, 객실 및 예약 조건을 비교하세요.','호텔 이름 검색','모든 목적지','모든 호텔 보기','여행 날짜에 맞는 가격과 객실을 확인하세요. Hot Deals / Hot Sellers는 참고 분류이며 검증된 할인이나 실시간 판매 순위가 아닙니다.','일치하는 호텔이 없습니다. 필터나 검색어를 바꿔보세요.','필터 초기화','호텔'],
'ja':['Hot Deals & Hot Sellers','ベトナムのホテルを、立地・客室・予約条件で比較しましょう。','ホテル名で検索','すべての目的地','すべてのホテル','価格と空室は旅行日で確認してください。Hot Deals / Hot Sellersは参考分類であり、確認済み割引や現在の販売順位ではありません。','該当するホテルがありません。条件や検索語を変更してください。','条件をリセット','軒'],
'hi':['Hot Deals & Hot Sellers','वियतनाम में होटल चुनने से पहले स्थान, कमरे और बुकिंग की शर्तें देखें।','होटल के नाम से खोजें','सभी गंतव्य','सभी होटल देखें','अपनी तारीखों के लिए कीमत और उपलब्धता जाँचें। Hot Deals / Hot Sellers संदर्भ श्रेणियाँ हैं, सत्यापित छूट या वर्तमान बिक्री रैंक नहीं।','कोई होटल नहीं मिला। फ़िल्टर या खोज बदलें।','फ़िल्टर हटाएँ','होटल'],
'fr':['Hot Deals & Hot Sellers','Comparez emplacement, chambres et conditions des hôtels au Vietnam avant de réserver.','Rechercher un hôtel','Toutes les destinations','Tous les hôtels','Vérifiez prix et disponibilité pour vos dates. Hot Deals / Hot Sellers sont des catégories indicatives, pas des remises vérifiées ou un classement actuel.','Aucun hôtel trouvé. Modifiez les filtres ou la recherche.','Effacer les filtres','hôtels'],
'de':['Hot Deals & Hot Sellers','Hotels in Vietnam nach Lage, Zimmern und Buchungsbedingungen vergleichen.','Hotelname suchen','Alle Reiseziele','Alle Hotels','Preise und Verfügbarkeit für die eigenen Daten prüfen. Hot Deals / Hot Sellers sind Orientierungskategorien, keine bestätigten Rabatte oder aktuellen Verkaufsränge.','Keine passenden Hotels. Filter oder Suchbegriff ändern.','Filter löschen','Hotels'],
'es':['Hot Deals & Hot Sellers','Compara ubicación, habitaciones y condiciones de hoteles en Vietnam antes de reservar.','Buscar hotel por nombre','Todos los destinos','Todos los hoteles','Comprueba precio y disponibilidad para tus fechas. Hot Deals / Hot Sellers son categorías orientativas, no descuentos ni rankings actuales verificados.','No hay hoteles coincidentes. Cambia filtros o búsqueda.','Borrar filtros','hoteles'],
'th':['Hot Deals & Hot Sellers','เปรียบเทียบที่ตั้ง ห้องพัก และเงื่อนไขโรงแรมในเวียดนามก่อนจอง','ค้นหาชื่อโรงแรม','ทุกจุดหมาย','ดูโรงแรมทั้งหมด','ตรวจสอบราคาและห้องว่างตามวันเดินทาง Hot Deals / Hot Sellers เป็นหมวดอ้างอิง ไม่ใช่ส่วนลดหรืออันดับขายปัจจุบันที่ยืนยันแล้ว','ไม่พบโรงแรม ลองเปลี่ยนตัวกรองหรือคำค้น','ล้างตัวกรอง','โรงแรม'],
'id':['Hot Deals & Hot Sellers','Bandingkan lokasi, kamar dan syarat hotel di Vietnam sebelum memesan.','Cari nama hotel','Semua destinasi','Lihat semua hotel','Periksa harga dan ketersediaan sesuai tanggal. Hot Deals / Hot Sellers adalah kategori referensi, bukan diskon terverifikasi atau peringkat penjualan langsung.','Tidak ada hotel yang cocok. Ubah filter atau pencarian.','Hapus filter','hotel']}
def rows():
    return [(h,'da-nang') for h in DANANG]+[(h,'hanoi') for h in HANOI]+[(h,h['city']) for h in SOUTHERN]
def path(lang):return f'stays/{lang}/index.html'
def page_pairs(languages):return [(path(lang),{c:path(c) for c in languages}) for lang in languages]
def property_path(lang,h,city):return hanoi_post(lang,h) if city=='hanoi' else danang_post(lang,h) if city=='da-nang' else southern_post(lang,h)
def property_url(h):return h['urls'][0] if h.get('urls') else h['url']
def card(lang,current,relative,h,city,save_button=''):
    name=h.get('display_name',h['name']);group=h['group'].lower().replace(' ','-');label='Hot Deals' if group=='top-deals' else 'Hot Sellers';city_name=CITY_LABELS[city];target=property_path(lang,h,city)
    return f'<article class="hotel-pick collection-card" data-hotel-group="{group}" data-hotel-city="{city}" data-hotel-name="{E(name)}" data-saved-id="hotel-{E(h["slug"])}">{save_button}<a class="hotel-artwork" href="{relative(current,target)}">{cover(h,city,lang,current,relative)}</a><div class="hotel-pick-body"><div class="hotel-card-meta"><span>{E(city_name)}</span><span class="hotel-category {group}">{label}</span></div><h3><a href="{relative(current,target)}">{E(name)}</a></h3><p>{E(DEAL_COPY[lang][7])}</p><a class="hotel-book-link" href="{E(property_url(h))}" target="_blank" rel="sponsored noopener noreferrer" data-affiliate="hotel-{E(h["slug"])}">{E(DEAL_COPY[lang][3].replace("↗","→"))}</a></div></article>'
def filters(lang,saved_label=None):
    u=COPY[lang];all_label=CONTENT[lang]['ui'][24]
    cities=''.join(f'<button type="button" data-hotel-city-filter="{key}" aria-pressed="false">{E(label)}</button>' for key,label in CITY_LABELS.items())
    saved=f'<button type="button" data-hotel-tab="saved" aria-pressed="false">{E(saved_label)}</button>' if saved_label else ''
    return f'<div class="collection-controls"><div class="collection-cities" role="group" aria-label="{E(u[3])}"><button type="button" data-hotel-city-filter="all" aria-pressed="true">{E(u[3])}</button>{cities}</div><label class="hotel-search"><span>{E(u[2])}</span><input type="search" data-hotel-search placeholder="{E(u[2])}" autocomplete="off"></label></div><div class="hotel-tabs collection-tabs" role="group" aria-label="{E(u[0])}"><button type="button" data-hotel-tab="all" aria-pressed="true">{E(all_label)}</button><button type="button" data-hotel-tab="top-deals" aria-pressed="false">Hot Deals</button><button type="button" data-hotel-tab="hot-sellers" aria-pressed="false">Hot Sellers</button>{saved}</div>'
def build_pages(document,relative,url,languages):
    root=Path(__file__).resolve().parents[1]
    for lang in languages:
        u=COPY[lang];current=path(lang)
        total=len(rows());hot=sum(h['group']=='Hot Sellers' for h,_ in rows());deals=total-hot
        body=f'<section class="section collection-page"><div class="container"><nav class="breadcrumbs"><a href="{relative(current,"index.html" if lang=="en" else lang+"/index.html")}">{E(CONTENT[lang]["ui"][0])}</a> / {E(u[0])}</nav><h1>{E(u[0])}</h1><p class="lead">{E(u[1])}</p><div class="collection-summary"><span>{total} {E(u[8])}</span><span>Hot Deals · {deals}</span><span>Hot Sellers · {hot}</span></div><div data-hotel-collection>{filters(lang)}<p class="collection-result" aria-live="polite"><strong data-hotel-result>{total}</strong> {E(u[8])}</p><div class="collection-grid">'+''.join(card(lang,current,relative,h,city) for h,city in rows())+f'</div><div class="collection-empty" hidden><p>{E(u[6])}</p><button type="button" class="btn" data-hotel-reset>{E(u[7])}</button></div></div><p class="editorial-note">{E(u[5])}</p></div></section>'
        items=[{'@type':'ListItem','position':i+1,'url':url(property_path(lang,h,city)),'name':h.get('display_name',h['name'])} for i,(h,city) in enumerate(rows())]
        schema={'@context':'https://schema.org','@type':'CollectionPage','name':u[0],'description':u[1],'url':url(current),'inLanguage':lang,'mainEntity':{'@type':'ItemList','numberOfItems':len(items),'itemListElement':items}}
        target=root/current;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(document(lang,current,u[0],u[1],body,{code:path(code) for code in languages},schema))
    return page_pairs(languages)

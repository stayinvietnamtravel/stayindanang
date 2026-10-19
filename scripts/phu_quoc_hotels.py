"""Phu Quoc property guides preserving all owner-supplied category links."""
from pathlib import Path
from html import escape as E
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'data/phu_quoc_hotels.json').read_text())
HOTELS = DATA['rows']
EDITORIAL = json.loads((ROOT / 'data/phu_quoc_editorial.json').read_text())['hotels']
SOURCE = ('Vietnam Tourism — Phu Quoc', 'https://vietnam.travel/places-to-go/southern-vietnam/phu-quoc')
SCENE = 'assets/ai-travel/hotel-phu-quoc-scene.png'

assert len(HOTELS) == 44 and len(DATA['original_rows']) == 45
assert len({h['slug'] for h in HOTELS}) == len(HOTELS)
assert set(EDITORIAL) == {h['slug'] for h in HOTELS}
assert sorted((h['name'], o['group'], o['url']) for h in HOTELS for o in h['offers']) == sorted((r['name'], r['group'], r['url']) for r in DATA['original_rows'])
for hotel in HOTELS:
    assert hotel['groups'] == [offer['group'] for offer in hotel['offers']]
    assert hotel['url'] == hotel['offers'][0]['url']
    for offer in hotel['offers']:
        assert offer['group'] in ('Top Deals', 'Hot Sellers')
        assert re.fullmatch(r'https://www\.trip\.com/w/[A-Za-z0-9]+', offer['url'])


def index_path(lang):
    return f'blog/{lang}/destinations/phu-quoc/index.html'


def post_path(lang, hotel):
    return f'blog/{lang}/destinations/phu-quoc/hotels/{hotel["slug"]}/index.html'


def page_pairs(languages):
    return ([(index_path(lang), {code: index_path(code) for code in languages}) for lang in languages]
            + [(post_path(lang, h), {code: post_path(code, h) for code in languages}) for lang in languages for h in HOTELS])


def heading(lang):
    from content import CONTENT
    return ('Khách sạn Phú Quốc: Hot Sellers & Top Deals' if lang == 'vi' else
            'Phu Quoc hotels: Hot Sellers & Top Deals' if lang == 'en' else
            'Phú Quốc · ' + CONTENT[lang]['ui'][3] + ' · Hot Sellers & Top Deals')


def teaser(lang, current, relative):
    title = heading(lang)
    text = ('44 khách sạn · 21 Hot Sellers · 24 Top Deals. Một khách sạn có hai link theo nhóm.' if lang == 'vi' else
            '44 hotels · 21 Hot Sellers · 24 Top Deals. One property has two category links.')
    text_lang = 'vi' if lang == 'vi' else 'en'
    return (f'<aside class="deals-callout phu-quoc-callout"><h3>{E(title)}</h3>'
            f'<p lang="{text_lang}">{E(text)}</p><a class="btn" href="{relative(current, index_path(lang))}">{E(title)} →</a></aside>')


def index_filters(lang):
    from content import CONTENT
    from hotel_collection import COPY
    labels = COPY[lang]
    return (f'<div class="collection-controls"><label class="hotel-search"><span>{E(labels[2])}</span>'
            f'<input type="search" data-hotel-search placeholder="{E(labels[2])}" autocomplete="off"></label></div>'
            f'<div class="hotel-tabs collection-tabs" role="group" aria-label="{E(heading(lang))}">'
            f'<button type="button" data-hotel-tab="all" aria-pressed="true">{E(CONTENT[lang]["ui"][24])}</button>'
            '<button type="button" data-hotel-tab="hot-sellers" aria-pressed="false">Hot Sellers · 21</button>'
            '<button type="button" data-hotel-tab="top-deals" aria-pressed="false">Top Deals · 24</button></div>')


def planning(lang):
    code = 'vi' if lang == 'vi' else 'en'
    if code == 'vi':
        return ('<section class="phu-quoc-planning" lang="vi"><h2>Chọn lịch trình trước khi chọn vùng lưu trú</h2>'
                '<p>Phú Quốc có những cụm tham quan khác nhau. Đặt địa chỉ khách sạn và các điểm muốn ghé lên cùng bản đồ; '
                'các gợi ý dưới đây giúp chia lịch, không xác nhận khách sạn cụ thể nằm gần một điểm.</p>'
                '<ul><li><strong>Bắc đảo:</strong> cân nhắc một cụm như Gành Dầu hoặc Grand World theo thời lượng và vé thực tế.</li>'
                '<li><strong>Khu Dương Đông:</strong> ghép ăn uống và một tuyến đi ngắn khi đường đi phù hợp.</li>'
                '<li><strong>Nam đảo:</strong> chọn riêng một chuyến tới cụm An Thới hoặc Bãi Khem, chừa thời gian xe về.</li></ul>'
                '<p>Đối chiếu các chặng với giờ bay hoặc giờ tàu, xem dự báo gần ngày đi và không xếp ba cụm vào một ngày chỉ vì cùng nằm trên đảo. '
                'Hot Sellers và Top Deals là nhóm trong danh sách được cung cấp, không phải số liệu bán hàng hoặc mức giảm giá đang được xác minh.</p></section>')
    return ('<section class="phu-quoc-planning" lang="en"><h2>Choose the route before the hotel area</h2>'
            '<p>Map the actual property address and your planned stops. These are island planning clusters, not verified proximity claims about any hotel.</p>'
            '<ul><li><strong>North:</strong> consider one cluster such as Ganh Dau or Grand World around actual travel and ticket requirements.</li>'
            '<li><strong>Duong Dong:</strong> group food stops and a short outing when the actual route suits.</li>'
            '<li><strong>South:</strong> allow a separate outing towards An Thoi or Bai Khem, including the return transfer.</li></ul>'
            '<p>Fit activities around flight or ferry times and near-term conditions. Do not assume all three clusters belong in one day. '
            'Hot Sellers and Top Deals are supplied reference groups, not independently verified sales data or live discounts.</p></section>')


def article_text(lang, hotel):
    code = 'vi' if lang == 'vi' else 'en'
    info = EDITORIAL[hotel['slug']]
    a, b = info['sections'][code]
    name = hotel['name']
    if code == 'vi':
        sections = [(info['angle']['vi'], a), ('Những chi tiết nên hỏi trước khi thanh toán', b),
                    ('So giá bằng cùng ngày và cùng điều kiện',
                     f'Khi mở link của {name}, nhập đúng ngày, số đêm, người lớn và tuổi trẻ. So loại giường, bữa ăn, thuế, tiền đặt cọc và thời hạn hủy. '
                     'Chỉ so hai mức giá sau khi đã đưa chúng về cùng điều kiện; nhãn Top Deals hoặc Hot Sellers không tự xác nhận có giảm giá.'),
                    ('Ghép khách sạn với lịch khám phá Phú Quốc',
                     'Chọn một cụm tham quan cho mỗi buổi hoặc ngày, đối chiếu với địa chỉ cơ sở thực tế. Ngày đến nên có thời gian nhận phòng và nghỉ; '
                     'ngày về cần tính thu xếp hành lý, trả phòng và xe ra điểm khởi hành. Xem dự báo ngắn hạn và điều kiện vận hành của dịch vụ trước khi mua vé không đổi giờ.')]
    else:
        sections = [(info['angle']['en'], a), ('Details to ask about before paying', b),
                    ('Compare identical dates and conditions',
                     f'Open the supplied {name} link and enter the correct dates, nights, adults and children’s ages. '
                     'Compare beds, meals, taxes, deposits and cancellation deadlines. Put rates on the same basis before comparing them; '
                     'a Top Deals or Hot Sellers label does not establish a discount.'),
                    ('Fit the stay into a Phu Quoc route',
                     'Choose one sightseeing cluster per outing or day and map it against the actual property address. '
                     'Allow check-in and rest on arrival, then packing, checkout and transfer time before departure. '
                     'Review short-range forecasts and service conditions before buying inflexible timed tickets.')]
    body = f'<div class="hotel-planning-copy" lang="{code}">'
    body += ''.join(f'<section><h2>{E(title)}</h2><p>{E(text)}</p></section>' for title, text in sections)
    if code == 'vi':
        body += ('<div class="article-itinerary"><table><caption>Gợi ý 3 ngày 2 đêm — điều chỉnh theo chặng đến và về</caption><tbody>'
                 '<tr><th scope="row">Ngày 1</th><td>Đến đúng cơ sở, gửi hành lý hoặc nhận phòng; chọn một hoạt động gần địa chỉ nếu còn thời gian.</td></tr>'
                 '<tr><th scope="row">Ngày 2</th><td>Chọn một cụm trên đảo hoặc một khoảng nghỉ theo nhu cầu đã nêu, xác nhận xe và vé trước.</td></tr>'
                 '<tr><th scope="row">Ngày 3</th><td>Ăn sáng, kiểm tra hành lý và hóa đơn, giữ khoảng đệm cho chặng khởi hành.</td></tr></tbody></table></div>')
    else:
        body += ('<div class="article-itinerary"><table><caption>Three days, two nights — adapt to actual transport times</caption><tbody>'
                 '<tr><th scope="row">Day 1</th><td>Reach the correct property, arrange luggage or check-in and keep any outing near your actual base.</td></tr>'
                 '<tr><th scope="row">Day 2</th><td>Choose one island cluster or downtime around the planning priorities above; confirm tickets and transport.</td></tr>'
                 '<tr><th scope="row">Day 3</th><td>Breakfast, baggage and account checks, with a buffer before onward travel.</td></tr></tbody></table></div>')
    return body + '</div>'


def build_pages(document, relative, url, languages):
    from content import CONTENT
    from hotel_collection import card, COPY as COLLECTION
    from hotel_visuals import cover
    from travel_art import COPY as ART
    from deal_posts import COPY as BUTTONS
    for lang in languages:
        code = 'vi' if lang == 'vi' else 'en'
        ui = CONTENT[lang]['ui']
        current = index_path(lang)
        title = heading(lang)
        description = ('So sánh 44 khách sạn Phú Quốc trong 21 Hot Sellers và 24 Top Deals, với bài riêng, lịch trình và đúng link affiliate từng cơ sở.' if code == 'vi' else
                       'Compare 44 Phu Quoc hotels across 21 Hot Sellers and 24 Top Deals, with individual planning guides and the supplied property booking links.')
        body = (f'<section class="section collection-page"><div class="container"><nav class="breadcrumbs">'
                f'<a href="{relative(current, "blog/index.html" if lang == "en" else "blog/" + lang + "/index.html")}">{E(ui[1])}</a> / Phú Quốc</nav>'
                f'<h1>{E(title)}</h1><p class="lead" lang="{code}">{E(description)}</p>'
                '<div class="collection-summary"><span>44 ' + E(COLLECTION[lang][8]) + '</span><span>Hot Sellers · 21</span><span>Top Deals · 24</span></div>'
                + f'<p class="collection-lead" lang="{code}">' + ('Sheraton có mặt ở cả hai nhóm với hai link riêng; mỗi khách sạn chỉ có một bài để dễ đối chiếu.' if code == 'vi' else
                'Sheraton belongs to both groups with two links. Each property has one guide so it is counted only once.') + '</p>'
                + '<div data-hotel-collection>' + index_filters(lang)
                + f'<p class="collection-result" aria-live="polite"><strong data-hotel-result>44</strong> {E(COLLECTION[lang][8])}</p><div class="collection-grid">'
                + ''.join(card(lang, current, relative, h, 'phu-quoc') for h in HOTELS)
                + f'</div><div class="collection-empty" hidden><p>{E(COLLECTION[lang][6])}</p><button type="button" class="btn" data-hotel-reset>{E(COLLECTION[lang][7])}</button></div></div>'
                + planning(lang)
                + f'<p><a href="{E(SOURCE[1])}" target="_blank" rel="noopener noreferrer">{E(SOURCE[0])}</a></p></div></section>')
        items = [{'@type': 'ListItem', 'position': i + 1, 'name': h['name'], 'url': url(post_path(lang, h))} for i, h in enumerate(HOTELS)]
        schema = {'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': title, 'description': description,
                  'inLanguage': lang if lang in ('vi', 'en') else [lang, 'en'], 'url': url(current),
                  'mainEntity': {'@type': 'ItemList', 'numberOfItems': len(items), 'itemListElement': items},
                  'spatialCoverage': {'@type': 'Place', 'name': 'Phu Quoc, Vietnam'}}
        write(current, document(lang, current, title, description, body, {c: index_path(c) for c in languages}, schema))
        for number, hotel in enumerate(HOTELS):
            current = post_path(lang, hotel)
            info = EDITORIAL[hotel['slug']]
            title = hotel['name'] + (' — gợi ý lưu trú Phú Quốc' if code == 'vi' else ' — Phu Quoc stay planning')
            description = hotel['name'] + ': ' + info['angle'][code] + ('. Kiểm tra phòng, lịch trình và link đặt đúng khách sạn.' if code == 'vi' else '. Room checks, trip planning and the supplied property link.')
            intro = (f'{hotel["name"]} nằm trong danh sách gợi ý lưu trú Phú Quốc với link đặt riêng. Bắt đầu từ nhu cầu của nhóm và lịch di chuyển, rồi so điều kiện của đúng loại phòng vào ngày đi.' if code == 'vi' else
                     f'This {hotel["name"]} planning guide connects your room choice with transport, itinerary and booking conditions for a Phu Quoc trip. Use the property-specific partner links to check your actual dates.')
            body = (f'<div class="container"><article class="article phu-quoc-article"><nav class="breadcrumbs"><a href="{relative(current, "blog/index.html" if lang == "en" else "blog/" + lang + "/index.html")}">{E(ui[1])}</a> / '
                    f'<a href="{relative(current, index_path(lang))}">Phú Quốc</a> / {E(hotel["name"])}</nav>'
                    f'<span class="pill">Phú Quốc · {E(" · ".join(hotel["groups"]))}</span><h1 lang="{code}">{E(title)}</h1>'
                    f'<p class="intro" lang="{code}">{E(intro)}</p><p class="article-updated"><time datetime="2026-10-19">2026-10-19</time> · Stay in Da Nang</p>'
                    f'<figure class="featured-image">{cover(hotel, "phu-quoc", lang, current, relative, eager=True)}<figcaption>{E(ART[lang][1])}</figcaption></figure>'
                    + article_text(lang, hotel))
            body += f'<section class="hotel-booking-options"><h2>{E(ui[3])} · Trip.com</h2>'
            for offer in hotel['offers']:
                body += (f'<p><a class="btn" href="{E(offer["url"])}" target="_blank" rel="sponsored noopener noreferrer" '
                         f'data-affiliate="phu-quoc-{E(hotel["slug"])}" data-offer-group="{E(offer["group"])}">'
                         f'{E(BUTTONS[lang][3].replace("↗", "→"))} · {E(offer["group"])}</a></p>')
            body += f'</section><p class="editorial-note">{E(COLLECTION[lang][5])}</p><p>{E(ui[11])}</p>'
            body += f'<section class="article-faq" lang="{code}"><h2>' + ('Câu hỏi trước khi đặt' if code == 'vi' else 'Before booking') + '</h2>'
            if len(hotel['offers']) > 1:
                question, answer = ('Vì sao Sheraton có hai link?', 'Hai link do chủ website cung cấp tương ứng Hot Sellers và Top Deals. So cùng ngày và điều kiện; bài viết không xác nhận link nào luôn rẻ hơn.') if code == 'vi' else ('Why are there two Sheraton links?', 'The owner supplied a Hot Sellers link and a Top Deals link. Compare identical dates and conditions; neither is asserted to be always cheaper.')
            else:
                question, answer = ('Nhãn ' + hotel['group'] + ' có bảo đảm giá tốt nhất không?', 'Không. Đây là nhóm gợi ý từ danh sách được cung cấp. Kiểm tra giá cuối cùng, số khách, loại phòng và chính sách của đúng lượt đặt.') if code == 'vi' else ('Does the ' + hotel['group'] + ' label guarantee the best price?', 'No. It is a supplied reference category. Check the final price, occupancy, room and conditions of the actual booking.')
            body += f'<details><summary>{E(question)}</summary><p>{E(answer)}</p></details>'
            question, answer = ('Cần thông tin gì khi đặt xe đến khách sạn?', 'Tên cơ sở đầy đủ, địa chỉ trên xác nhận, giờ đến, số khách và hành lý. Một tên khách sạn gần giống không thay cho đúng địa chỉ.') if code == 'vi' else ('What details does a transfer booking need?', 'The full property name, confirmed address, arrival time, passengers and luggage. A similar hotel name is not a substitute for the correct address.')
            body += f'<details><summary>{E(question)}</summary><p>{E(answer)}</p></details></section>'
            body += f'<aside class="article-related"><h2>{E(ui[1])} · Phú Quốc</h2><ul>'
            related = [HOTELS[(number + 1) % len(HOTELS)], HOTELS[(number + 2) % len(HOTELS)]]
            body += ''.join(f'<li><a href="{relative(current, post_path(lang, h))}">{E(h["name"])}</a></li>' for h in related)
            body += f'<li><a href="{relative(current, "blog/" + lang + "/tips/phu-quoc-three-day-plan/index.html")}">Phú Quốc · 3 {'ngày' if code == 'vi' else 'days'}</a></li></ul></aside>'
            body += f'<p><a class="text-link" href="{relative(current, index_path(lang))}">{E(heading(lang))} →</a></p>'
            body += f'<h2>{E(ui[12])}</h2><ul class="source-list"><li><a href="{E(SOURCE[1])}" target="_blank" rel="noopener noreferrer">{E(SOURCE[0])}</a></li></ul></article></div>'
            schema = {'@context': 'https://schema.org', '@type': 'BlogPosting', 'headline': title,
                      'description': description, 'image': url(SCENE), 'inLanguage': lang if lang in ('vi', 'en') else [lang, 'en'],
                      'mainEntityOfPage': url(current), 'datePublished': '2026-10-19', 'dateModified': '2026-10-19',
                      'author': {'@type': 'Organization', 'name': 'Stay in Da Nang', 'url': url('index.html')},
                      'publisher': {'@type': 'Organization', 'name': 'Stay in Da Nang'}, 'articleSection': hotel['groups'],
                      'citation': [SOURCE[1]], 'spatialCoverage': {'@type': 'Place', 'name': 'Phu Quoc, Vietnam'},
                      'about': {'@type': 'Hotel', 'name': hotel['name'], 'address': {'@type': 'PostalAddress', 'addressLocality': 'Phu Quoc', 'addressCountry': 'VN'}}}
            breadcrumbs = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': ui[1], 'item': url('blog/index.html' if lang == 'en' else f'blog/{lang}/index.html')},
                {'@type': 'ListItem', 'position': 2, 'name': 'Phú Quốc', 'item': url(index_path(lang))},
                {'@type': 'ListItem', 'position': 3, 'name': hotel['name'], 'item': url(current)}]}
            body += '<script type="application/ld+json">' + json.dumps(breadcrumbs, ensure_ascii=False).replace('<', '\\u003c') + '</script>'
            write(current, document(lang, current, title, description, body, {c: post_path(c, hotel) for c in languages}, schema))
    return page_pairs(languages)


def write(path, body):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(body)

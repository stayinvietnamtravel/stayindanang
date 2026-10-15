"""Hanoi hotel guides: exact supplied names/links; no invented hotel amenities."""
from pathlib import Path
from html import escape as E
import json
from responsive_images import image as responsive_image
ROOT=Path(__file__).resolve().parents[1]
HOTELS=json.loads((ROOT/'data/hanoi_hotels.json').read_text())['rows']
# Heading, introduction, comparison heading, city ideas, disclosure.
COPY={
'vi':['Khách sạn Hà Nội','Chọn chỗ ở cho chuyến khám phá Hà Nội: đọc gợi ý từng khách sạn và kiểm tra phòng theo ngày đi.','Cách chọn phòng phù hợp','Dành một buổi cho hồ Hoàn Kiếm và phố cổ, một buổi khác cho Văn Miếu hoặc khu vực Hồ Tây. Sắp xếp các điểm theo cụm; đây là ý tưởng tham quan Hà Nội, không phải cam kết khách sạn nằm gần các điểm đó.','Ảnh chữ giới thiệu, không phải ảnh chụp khách sạn. Top Deals / Hot Sellers là nhóm tham khảo, không xác nhận mức giảm hay thứ hạng bán chạy hiện tại. Link đặt phòng là liên kết tiếp thị; chúng tôi có thể nhận hoa hồng.'],
'en':['Hanoi hotels','Plan your Hanoi stay with individual hotel guides and check rooms for your actual dates.','Choosing your room','Group Hoan Kiem Lake and the Old Quarter into one outing, with the Temple of Literature or West Lake on another. These are city itinerary ideas, not claims about the hotel’s proximity.','Typographic artwork, not a property photograph. Top Deals / Hot Sellers are reference groups, not verified discounts or current sales rankings. Booking links are affiliate links; we may earn a commission.'],
'zh':['河内酒店','查看每家酒店的独立指南，按实际出行日期确认房型。','如何选择客房','可安排还剑湖和老城区，另一天游览文庙或西湖。这些是河内游览建议，并不表示酒店邻近这些景点。','文字设计图，并非酒店实拍。Top Deals / Hot Sellers 是参考分组，不代表已核实折扣或实时销量排名。预订链接为推广链接，我们可能获得佣金。'],
'zh-Hant':['河內飯店','閱讀各飯店指南，依實際日期確認房型。','如何選擇客房','可安排還劍湖與老城區，另一天走訪文廟或西湖。這些是城市行程建議，不表示飯店就在景點附近。','文字設計圖，並非飯店實拍。Top Deals / Hot Sellers 為參考分組，不代表已核實優惠或即時銷量。預訂連結為聯盟行銷連結，我們可能獲得佣金。'],
'ru':['Отели Ханоя','Читайте отдельные гиды по отелям и проверяйте номера на даты поездки.','Как выбрать номер','Объедините озеро Хоанкьем и Старый квартал в одну прогулку, а Храм литературы или Западное озеро — в другую. Это идеи маршрута, а не обещание близости отеля.','Типографическая иллюстрация, не фотография отеля. Top Deals / Hot Sellers — справочные группы, не проверенные скидки или текущий рейтинг продаж. Ссылки партнёрские; мы можем получить комиссию.'],
'ko':['하노이 호텔','호텔별 가이드를 읽고 실제 여행 날짜에 맞는 객실을 확인하세요.','객실 선택하기','호안끼엠 호수와 구시가지는 같은 날, 문묘나 서호는 다른 날 방문해 보세요. 도시 여행 제안이며 호텔과의 근접성을 보장하지 않습니다.','문자 디자인이며 실제 호텔 사진이 아닙니다. Top Deals / Hot Sellers는 참고 분류로 검증된 할인이나 실시간 판매 순위가 아닙니다. 제휴 링크로 수수료를 받을 수 있습니다.'],
'ja':['ハノイのホテル','ホテル別ガイドを読み、実際の旅行日に合わせて客室を確認しましょう。','客室の選び方','ホアンキエム湖と旧市街を同じ日に、文廟や西湖を別の日に組み合わせましょう。市内観光の提案で、ホテルからの近さを保証するものではありません。','文字デザインでありホテルの実写ではありません。Top Deals / Hot Sellersは参考分類で、確認済み割引や現在の販売順位ではありません。予約はアフィリエイトリンクで、手数料を受け取る場合があります。'],
'hi':['हनोई के होटल','हर होटल की गाइड पढ़ें और अपनी यात्रा की तारीखों के लिए कमरे जाँचें।','कमरा कैसे चुनें','होआन कीम झील और पुराने शहर को एक दिन, साहित्य मंदिर या वेस्ट लेक को दूसरे दिन रखें। ये शहर घूमने के सुझाव हैं, होटल की निकटता का दावा नहीं।','यह टेक्स्ट डिज़ाइन है, होटल की वास्तविक तस्वीर नहीं। Top Deals / Hot Sellers संदर्भ श्रेणियाँ हैं, सत्यापित छूट या वर्तमान बिक्री रैंक नहीं। बुकिंग लिंक सहयोगी लिंक हैं; हमें कमीशन मिल सकता है।'],
'fr':['Hôtels à Hanoï','Consultez chaque guide et vérifiez les chambres pour vos dates.','Choisir sa chambre','Regroupez le lac Hoan Kiem et le vieux quartier, puis le temple de la Littérature ou le lac de l’Ouest lors d’une autre sortie. Ces idées ne garantissent pas la proximité de l’hôtel.','Illustration typographique, pas une photo de l’hôtel. Top Deals / Hot Sellers sont des catégories indicatives, sans remise ni classement actuel vérifiés. Liens affiliés : nous pouvons recevoir une commission.'],
'de':['Hotels in Hanoi','Einzelne Hotelführer lesen und Zimmer für die eigenen Reisedaten prüfen.','Das passende Zimmer wählen','Hoan-Kiem-See und Altstadt lassen sich kombinieren, Literaturtempel oder Westsee bei einem weiteren Ausflug. Das sind Stadtideen, keine Zusage zur Nähe des Hotels.','Typografische Illustration, kein Hotelfoto. Top Deals / Hot Sellers sind Orientierungskategorien, keine bestätigten Rabatte oder aktuellen Verkaufsränge. Affiliate-Links können uns eine Provision einbringen.'],
'es':['Hoteles en Hanói','Consulta cada guía y comprueba las habitaciones para tus fechas.','Cómo elegir habitación','Combina el lago Hoan Kiem y el casco antiguo; reserva otra salida para el Templo de la Literatura o el lago del Oeste. Son ideas de ciudad, no garantías de cercanía del hotel.','Diseño tipográfico, no una foto del hotel. Top Deals / Hot Sellers son categorías de referencia, no descuentos ni rankings actuales verificados. Los enlaces son de afiliación y podemos recibir una comisión.'],
'th':['โรงแรมฮานอย','อ่านคู่มือแต่ละโรงแรมและตรวจสอบห้องตามวันเดินทางจริง','เลือกห้องอย่างไร','จัดทะเลสาบฮหว่านเกี๊ยมและย่านเมืองเก่าไว้วันเดียวกัน ส่วนวิหารวรรณกรรมหรือทะเลสาบตะวันตกอีกวัน นี่คือไอเดียเที่ยวเมือง ไม่ได้รับรองว่าโรงแรมอยู่ใกล้','ภาพออกแบบตัวอักษร ไม่ใช่ภาพถ่ายโรงแรม Top Deals / Hot Sellers เป็นหมวดอ้างอิง ไม่ใช่ส่วนลดหรืออันดับยอดขายปัจจุบันที่ตรวจสอบแล้ว ลิงก์จองเป็นลิงก์พันธมิตร เราอาจได้รับค่าคอมมิชชัน'],
'id':['Hotel di Hanoi','Baca panduan setiap hotel dan periksa kamar sesuai tanggal perjalanan.','Memilih kamar','Gabungkan Danau Hoan Kiem dan Kota Tua dalam satu kunjungan, lalu Kuil Sastra atau Danau Barat di hari lain. Ini ide perjalanan kota, bukan jaminan kedekatan hotel.','Desain tipografi, bukan foto hotel. Top Deals / Hot Sellers adalah kategori referensi, bukan diskon atau peringkat penjualan terkini yang terverifikasi. Tautan afiliasi dapat memberi kami komisi.']}
# Distinct editorial angles, describing what to check rather than claiming amenities.
ANGLES=[
('Lịch trình đô thị có khoảng nghỉ','Với Hanoi Daewoo Hotel, hãy đối chiếu địa chỉ nhận phòng với những cuộc hẹn và điểm tham quan trong ngày. Một lịch trình có khoảng nghỉ giữa trưa sẽ thoải mái hơn việc di chuyển liên tục.'),
('Kết hợp chuyến công tác và khám phá','Khi cân nhắc Melia Hanoi, tách thời gian làm việc và thời gian khám phá thành phố. So sánh giờ nhận phòng với giờ đến Hà Nội, rồi xác nhận bữa ăn có nằm trong gói phòng hay không.'),
('So sánh loại phòng trước khi chọn','Với Lotte Hotel Hanoi, đọc kỹ tên loại phòng và số khách được ở. Nếu tầm nhìn là điều bạn quan tâm, kiểm tra mô tả của đúng hạng phòng thay vì suy ra từ ảnh quảng cáo chung.'),
('Một ngày khám phá Hồ Tây','Khi tìm hiểu InterContinental HANOI WESTLAKE by IHG, có thể đưa Hồ Tây vào kế hoạch tham quan riêng. Kiểm tra địa chỉ, tuyến xe và điều kiện từng phòng; tên khách sạn không thay thế việc xác nhận thông tin đặt phòng.'),
('Dạo Hà Nội theo chủ đề văn hóa','Cân nhắc Sofitel Legend Metropole Hanoi cùng một lịch trình tìm hiểu văn hóa, kiến trúc và ẩm thực Hà Nội. Tự xác nhận giờ mở cửa các điểm tham quan và quãng đường thực tế từ địa chỉ khách sạn.'),
('Chủ động cho ngày đến muộn','Với JW Marriott Hotel Hanoi, nếu chuyến bay đến tối, hãy xác nhận quy trình nhận phòng trễ và cách di chuyển từ sân bay. So sánh cả tổng chi phí xe và phòng, không chỉ giá hiển thị ban đầu.'),
('Kiểm tra gói phòng trước thanh toán','Đưa Fairmont Hanoi vào bảng so sánh bằng cùng ngày và số khách. Đọc lại hạng phòng, thuế, đặt cọc và chính sách hủy trước khi thanh toán; không mặc định các gói có cùng điều kiện.'),
('Một chuyến đi dành thời gian cho bản thân','Khi cân nhắc Capella Hanoi, để lịch trình đủ thưa để có thời gian nghỉ. Chọn loại giường và số đêm theo nhu cầu thực tế, rồi kiểm tra các yêu cầu đặc biệt trực tiếp với nơi lưu trú.'),
('Sắp xếp lịch hẹn theo khu vực','Với Grand Plaza Hanoi Hotel, đặt địa chỉ lưu trú và các điểm cần đến trên cùng bản đồ. Ước tính thời gian di chuyển vào giờ cao điểm trước khi quyết định nơi ở.'),
('Lựa chọn phòng cho hành trình ngắn','Aurora Premium - A Lifestyle Hotel có hai liên kết được cung cấp trong danh sách. Bạn có thể mở từng liên kết để kiểm tra; không mặc định hai đường dẫn có giá hay điều kiện giống nhau.'),
('Đọc rõ thông tin thương hiệu và cơ sở','Với Signature Tho Nhuom, a brand of Modern Village Lifestyle, kiểm tra đúng tên cơ sở và địa chỉ trên xác nhận đặt phòng. Lưu lại thông tin liên hệ để tránh nhầm giữa những tên thương hiệu tương tự.'),
('Ở nhiều đêm, xem kỹ điều kiện','Khi cân nhắc Hanoi 20 Hotel & Apartment, xác nhận dịch vụ dọn phòng và các khoản phụ thu cho số đêm thực tế. Từ “Apartment” trong tên không đủ để khẳng định phòng có bếp hay thiết bị cụ thể.'),
('Lên kế hoạch cho khu vực Hồ Tây','Với A89 West Lake Hotel, đối chiếu vị trí trên bản đồ trước khi ghép các điểm quanh Hồ Tây vào cùng một buổi. Kiểm tra tuyến về buổi tối và phương tiện phù hợp với nhóm đi.'),
('So sánh những gì được bao gồm','Khi xem Victory Legend Hotel & Spa, xác nhận riêng các dịch vụ bạn muốn dùng. Từ “Spa” trong tên không có nghĩa dịch vụ đó được bao gồm trong giá phòng hoặc luôn sẵn có.'),
('Lưu thông tin để xem ngoại tuyến','Với Lestar Hotel Hanoi, lưu tên, địa chỉ, giờ nhận phòng và mã xác nhận trước ngày đi. Chuẩn bị bản đồ ngoại tuyến và phương án liên lạc nếu điện thoại chưa có mạng khi đến Hà Nội.'),
('Chọn phòng và dịch vụ riêng biệt','Khi xem Luxe Paradise Suites Hotel & Spa, so sánh đúng loại phòng và quy định sử dụng dịch vụ. Không suy ra diện tích, hạng giường hay dịch vụ miễn phí chỉ từ tên gọi.'),
('Sắp xếp hành trình qua sông','Với M Village Hotel Long Bien, a brand of Modern Village Lifestyle, hãy kiểm tra địa chỉ và tuyến di chuyển phù hợp với lịch trình. Dành thêm thời gian dự phòng nếu ngày đi có nhiều chặng qua các khu vực khác nhau.'),
('Khám phá thành phố theo nhịp chậm','Khi cân nhắc Conifer Boutique Hotel, chọn một cụm điểm tham quan cho mỗi buổi và để thời gian ăn uống, nghỉ chân. Xác nhận giờ giữ hành lý nếu bạn đến trước giờ nhận phòng.'),
('Đi bộ và nghỉ ngơi cân bằng','Với Su Casa Hanoi Old Quarter, hãy xem tuyến đường thực tế từ khách sạn đến nơi định đi bộ. Đọc nhận xét gần đây về tiếng ồn và chọn điều kiện phòng phù hợp nếu bạn cần nghỉ sớm.'),
('Một bảng so sánh dễ đọc','Đưa Gilson Hanoi Hotel vào bảng so sánh với ngày ở, số khách, tổng tiền và điều kiện hủy. Dùng cùng một bộ tiêu chí cho các khách sạn để quyết định dễ hơn.'),
('Tính đủ chi phí hành trình','Với Gloud Hotel, cộng cả xe sân bay, di chuyển nội đô và bữa ăn vào ngân sách. Một phòng có giá ban đầu phù hợp vẫn cần được so sánh trên tổng chi phí chuyến đi.'),
('Xác nhận đúng cơ sở trên địa chỉ','Khi đặt 22land Residence – 50 Truong Cong Giai, đối chiếu đầy đủ tên cơ sở và địa chỉ hiển thị trên Trip.com. Không dùng tên thương hiệu chung để thay thế địa chỉ nhận phòng.'),
('Khởi đầu ngày tham quan chủ động','Với Hanoi Morning Hotel, xác nhận giờ ăn sáng nếu gói phòng có bữa ăn, rồi sắp lịch khởi hành. Nếu cần đi rất sớm, hỏi trước về thủ tục trả phòng.'),
('Đọc chính sách dịch vụ trước khi đi','Khi cân nhắc Grandiose Hotel & Spa, phân biệt dịch vụ trong gói phòng và dịch vụ trả phí. Kiểm tra lịch hoạt động và cách đặt trước đối với những dịch vụ bạn thực sự cần.'),
('Cân đối nhu cầu gia đình','Với Bao Son International Hotel, kiểm tra sức chứa phòng, loại giường và quy định trẻ em theo đúng thành viên đi cùng. Yêu cầu giường phụ hoặc phòng liền nhau cần được xác nhận, không mặc định có sẵn.'),
('Lưu trú dài ngày cần tiêu chí riêng','Khi xem Calidas Landmark72 Royal Residence Hanoi, xác nhận loại phòng và điều kiện ở nhiều đêm. Nếu cần giặt đồ hoặc chuẩn bị bữa ăn, kiểm tra mô tả phòng và hỏi rõ trước khi đặt.'),
('Phân biệt những cơ sở tên gần giống','Với Luxe Paradise Suites Doi Can, lưu đúng tên cơ sở trên xác nhận. Đối chiếu địa chỉ với đường đi dự kiến để tránh nhầm với khách sạn có tên tương tự.'),
('Lịch nhận phòng phù hợp giờ bay','Khi cân nhắc Eli Rina Hotel, so sánh giờ đến Hà Nội với giờ nhận phòng và trả phòng. Hỏi rõ điều kiện giữ hành lý hoặc nhận sớm nếu đây là nhu cầu quan trọng.'),
('Chọn không gian theo số khách','Với The Five Suites Lilas, kiểm tra số người được ở, loại giường và quy định phụ thu. Tên “Suites” không thay thế mô tả của hạng phòng được đặt.'),
('Một hành trình lưu trú linh hoạt','Khi xem Parosand Hanoi Hotel & Apartment, chọn số đêm trước rồi so sánh chính sách thay đổi lịch. Nếu cần tiện nghi cụ thể cho chuyến ở dài, xác nhận trực tiếp trong thông tin gói phòng.')]
# Index by name so reordering the spreadsheet never assigns another hotel's prose.
NAMES=['Hanoi Daewoo Hotel','Melia Hanoi','Lotte Hotel Hanoi','InterContinental HANOI WESTLAKE by IHG','Sofitel Legend Metropole Hanoi','JW Marriott Hotel Hanoi','Fairmont Hanoi','Capella Hanoi','Grand Plaza Hanoi Hotel','Aurora Premium - A Lifestyle Hotel','Signature Tho Nhuom, a brand of Modern Village Lifestyle','Hanoi 20 Hotel & Apartment','A89 West Lake Hotel','Victory Legend Hotel & Spa','Lestar Hotel Hanoi','Luxe Paradise Suites Hotel & Spa','M Village Hotel Long Bien, a brand of Modern Village Lifestyle','Conifer Boutique Hotel','Su Casa Hanoi Old Quarter','Gilson Hanoi Hotel','Gloud Hotel','22land Residence – 50 Truong Cong Giai','Hanoi Morning Hotel','Grandiose Hotel & Spa','Bao Son International Hotel','Calidas Landmark72 Royal Residence Hanoi','Luxe Paradise Suites Doi Can','Eli Rina Hotel','The Five Suites Lilas','Parosand Hanoi Hotel & Apartment']
EDITORIAL=dict(zip(NAMES,ANGLES,strict=True))
def index_path(lang):return f'blog/{lang}/destinations/hanoi/index.html'
def post_path(lang,h):return f'blog/{lang}/destinations/hanoi/hotels/{h["slug"]}/index.html'
def image_path(h):return f'assets/hanoi-hotels/{h["slug"]}.png'
def page_pairs(languages):return [(index_path(lang),{c:index_path(c) for c in languages}) for lang in languages]+[(post_path(lang,h),{c:post_path(c,h) for c in languages}) for lang in languages for h in HOTELS]
def teaser(lang,current,relative):
    return f'<aside class="deals-callout"><h3>{E(COPY[lang][0])} · Top Deals & Hot Sellers</h3><p>{E(COPY[lang][1])}</p><a class="btn" href="{relative(current,index_path(lang))}">{E(COPY[lang][0])} →</a></aside>'
def render_artwork():
    from playwright.sync_api import sync_playwright
    (ROOT/'assets/hanoi-hotels').mkdir(exist_ok=True)
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1600,'height':900},device_scale_factor=1)
        for h in HOTELS:
            name=h['name'];size=72 if len(name)>55 else 86 if len(name)>35 else 106
            title,body=EDITORIAL[name];links=' · '.join(u.replace('https://www.','') for u in h['urls'])
            page.set_content(f'''<html lang="vi"><meta charset="utf-8"><style>*{{box-sizing:border-box}}body{{margin:0;width:1600px;height:900px;background:#092f49;color:#fff;font-family:Arial,sans-serif}}main{{padding:65px 80px;height:900px;background:radial-gradient(ellipse at 100% 0,#177984,transparent 65%)}}.brand{{font-size:25px;letter-spacing:4px}}.badge{{display:inline-block;margin:55px 0 20px;padding:14px 26px;border-radius:30px;background:#f5d39b;color:#173d52;font-size:28px;font-weight:bold}}h1{{font-size:{size}px;line-height:1.14;margin:16px 0 24px;max-width:1350px}}p{{font-size:32px;color:#d4ebed}}footer{{position:absolute;bottom:60px;left:80px;right:80px;border-top:1px solid #7da1af;padding-top:22px;font-size:25px;line-height:1.6}}small{{font-size:22px;color:#d4ebed}}</style><main><div class="brand">STAY IN DA NANG · VIETNAM HOTEL GUIDES</div><div class="badge">HÀ NỘI · {E(h['group'].upper())}</div><h1>{E(name)}</h1><p>{E(title)}</p><footer>{E(links)}<br><small>Kiểm tra phòng theo ngày đi · Liên kết tiếp thị liên kết</small></footer></main>''')
            page.evaluate('document.fonts.ready');assert page.locator('h1').bounding_box()['y']+page.locator('h1').bounding_box()['height']<650,name
            page.screenshot(path=str(ROOT/image_path(h)))
        b.close()
    print(f'Rendered {len(HOTELS)} Hanoi text cards, 1600×900.')
def build_pages(document,relative,url,languages):
    from deal_posts import COPY as CHECKS
    from content import CONTENT
    def write(path,html):
        p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(html)
    for lang in languages:
        u=COPY[lang];c=CHECKS[lang];current=index_path(lang)
        groups={group:sum(h['group']==group for h in HOTELS) for group in ('Top Deals','Hot Sellers')}
        body=f'<section class="section soft hotel-directory hanoi-directory"><div class="container"><nav class="breadcrumbs"><a href="{relative(current,"blog/index.html" if lang=="en" else "blog/"+lang+"/index.html")}">{E(CONTENT[lang]["ui"][1])}</a> / Hà Nội</nav><h1>{E(u[0])}</h1><p class="lead">{E(u[1])}</p><div class="blog-browser"><div class="blog-filters" role="group" aria-label="{E(u[0])}">'
        body+=f'<button data-blog-filter="all" aria-pressed="true">{E(CONTENT[lang]["ui"][24])}</button>'+''.join(f'<button data-blog-filter="{g.lower().replace(" ","-")}" aria-pressed="false">{g} ({count})</button>' for g,count in groups.items())+'</div><div class="blog-grid">'
        for h in HOTELS:
            img=responsive_image(image_path(h),current,relative,h['name'],'blog-cover',sizes='(max-width:700px) 92vw, 300px')
            body+=f'<article class="blog-card" data-blog-category="{h["group"].lower().replace(" ","-")}"><a href="{relative(current,post_path(lang,h))}">{img}</a><div class="blog-card-body"><span class="pill">Hà Nội · {h["group"]}</span><h2><a href="{relative(current,post_path(lang,h))}">{E(h["name"])}</a></h2><p>{E(EDITORIAL[h["name"]][0] if lang=="vi" else u[1])}</p><a class="hotel-book-link" href="{E(h["urls"][0])}" target="_blank" rel="sponsored noopener noreferrer">{E(c[3].replace("↗","→"))}</a></div></article>'
        body+=f'</div></div><p class="editorial-note">{E(u[4])}</p></div></section>'
        write(current,document(lang,current,u[0],u[1],body,{code:index_path(code) for code in languages}))
        for h in HOTELS:
            path=post_path(lang,h);title=h['name']+' | '+u[0];angle,text=EDITORIAL[h['name']]
            intro=(h['name']+': '+angle.lower()+'. Tìm hiểu cách chọn phòng, sắp xếp hành trình và kiểm tra điều kiện đặt phòng cho chuyến đi Hà Nội.') if lang=='vi' else h['name']+' · '+u[1]
            img=responsive_image(image_path(h),path,relative,h['name'],sizes='(max-width:800px) 92vw, 780px',eager=True)
            body=f'<div class="container"><article class="article"><nav class="breadcrumbs"><a href="{relative(path,index_path(lang))}">{E(u[0])}</a> / {E(h["name"])}</nav><span class="pill">Hà Nội · {h["group"]}</span><h1>{E(title)}</h1><p class="intro">{E(intro)}</p><figure class="featured-image">{img}<figcaption>{E(u[4])}</figcaption></figure><h2>{E(angle if lang=="vi" else u[2])}</h2><p>{E(text if lang=="vi" else c[5]+" "+c[6])}</p><h2>{E(u[2])}</h2><p>{E(c[5]+" "+c[6]+" "+c[7])}</p><h2>Hà Nội</h2><p>{E(u[3])}</p>'
            for i,link in enumerate(h['urls'],1):body+=f'<p><a class="btn" href="{E(link)}" target="_blank" rel="sponsored noopener noreferrer" data-affiliate="hanoi-{h["slug"]}-{i}">{E(c[3].replace("↗","→"))}{" · "+str(i) if len(h["urls"])>1 else ""}</a></p>'
            body+=f'<p class="editorial-note">{E(u[4])}</p><p><a href="{relative(path,index_path(lang))}">{E(u[0])} →</a></p></article></div>'
            schema={'@context':'https://schema.org','@type':'BlogPosting','headline':title,'description':intro,'image':url(image_path(h)),'inLanguage':lang,'mainEntityOfPage':url(path),'publisher':{'@type':'Organization','name':'Stay in Da Nang'},'spatialCoverage':{'@type':'Place','name':'Hanoi, Vietnam'}}
            write(path,document(lang,path,title,intro,body,{code:post_path(code,h) for code in languages},schema))
    return page_pairs(languages)
if __name__=='__main__':render_artwork()

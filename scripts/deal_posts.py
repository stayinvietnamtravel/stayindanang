"""Bookdeal-based posts. Names and links are source data, not live deal validation."""
from pathlib import Path
from html import escape as E
from urllib.parse import urlsplit
import json,csv,zipfile,struct
from hotel_editorial import editorial
from responsive_images import image as responsive_image

ROOT=Path(__file__).resolve().parents[1]
EXPORT_ROOT=ROOT.parent/'stayindanang-admin-exports'
DATA=json.loads((ROOT/'data/bookdeal.json').read_text(encoding='utf-8'))
HOTELS=[r for r in DATA['rows'] if r['included']]
SOURCE_NAME=DATA['source']

# heading, lead, source qualification, booking CTA, checklist heading,
# three checks, source label, download label, coastal-corridor note.
COPY={
'en':['Da Nang hotel picks: Top Deals & Hot Sellers','Browse hotels and the individual Trip.com links supplied in Bookdeal.xlsx.','Top Deals and Hot Sellers are the workbook’s labels, not verified discounts or live sales rankings. The file contains no prices or validity dates.','Check rooms and prices on Trip.com ↗','Before you book','Confirm the exact address and transport for your itinerary.','Compare room category, guest count, meals, taxes and cancellation terms.','Check availability and the final price for your actual travel dates.','Source: Bookdeal.xlsx','Download posts and HD artwork','This property is on the coastal Da Nang–Hoi An corridor; check its exact address before booking.'],
'vi':['Khách sạn Đà Nẵng: Top Deals & Hot Sellers','Chọn khách sạn và mở đúng liên kết Trip.com riêng được cung cấp trong Bookdeal.xlsx.','Top Deals và Hot Sellers là nhãn trong file, không phải mức giảm hay thứ hạng bán chạy được xác minh theo thời gian thực. File không có giá hoặc ngày áp dụng.','Xem phòng và giá trên Trip.com ↗','Trước khi đặt phòng','Kiểm tra địa chỉ chính xác và phương án di chuyển theo lịch trình của bạn.','So sánh hạng phòng, số khách, bữa ăn, thuế và điều kiện hủy.','Xem tình trạng phòng và giá cuối cùng theo ngày lưu trú thực tế.','Nguồn: Bookdeal.xlsx','Tải bài post và ảnh HD','Cơ sở này thuộc hành lang ven biển Đà Nẵng–Hội An; kiểm tra địa chỉ cụ thể trước khi đặt.'],
'zh':['岘港酒店精选：Top Deals 与 Hot Sellers','浏览 Bookdeal.xlsx 中的酒店及其各自的 Trip.com 链接。','Top Deals 和 Hot Sellers 是表格标签，并非已核实折扣或实时销量排名。文件未提供价格或有效日期。','在 Trip.com 查看房型与价格 ↗','预订前','确认准确地址与行程交通。','比较房型、人数、餐食、税费和取消条件。','按实际入住日期查看空房与最终价格。','来源：Bookdeal.xlsx','下载帖子与高清图片','此酒店位于岘港–会安海岸走廊，预订前请核实具体地址。'],
'zh-Hant':['峴港飯店精選：Top Deals 與 Hot Sellers','查看 Bookdeal.xlsx 的飯店及各自 Trip.com 連結。','Top Deals 和 Hot Sellers 是表格標籤，並非已查證折扣或即時銷量排名。檔案沒有價格或有效日期。','在 Trip.com 查看房型與價格 ↗','預訂前','確認準確地址與行程交通。','比較房型、人數、餐食、稅金和取消條件。','依實際入住日期確認空房及最終價格。','來源：Bookdeal.xlsx','下載貼文與高清圖片','此飯店位於峴港–會安海岸走廊，預訂前請確認具體地址。'],
'ru':['Отели Дананга: Top Deals и Hot Sellers','Отели и отдельные ссылки Trip.com из Bookdeal.xlsx.','Top Deals и Hot Sellers — категории файла, а не подтверждённые скидки или текущий рейтинг продаж. Цены и сроки в файле отсутствуют.','Проверить номера и цены на Trip.com ↗','Перед бронированием','Уточните адрес и транспорт по маршруту.','Сравните номер, число гостей, питание, налоги и отмену.','Проверьте доступность и итоговую цену на свои даты.','Источник: Bookdeal.xlsx','Скачать тексты и HD-изображения','Отель находится в прибрежном коридоре Дананг–Хойан; уточните адрес перед бронированием.'],
'ko':['다낭 호텔: Top Deals & Hot Sellers','Bookdeal.xlsx에 제공된 호텔별 Trip.com 링크를 확인하세요.','Top Deals와 Hot Sellers는 파일의 분류이며 검증된 할인이나 실시간 판매 순위가 아닙니다. 가격과 적용 날짜는 없습니다.','Trip.com에서 객실과 가격 확인 ↗','예약 전','정확한 주소와 이동 방법을 확인하세요.','객실 유형, 인원, 식사, 세금과 취소 조건을 비교하세요.','실제 숙박 날짜의 객실과 최종 가격을 확인하세요.','출처: Bookdeal.xlsx','게시글과 HD 이미지 다운로드','다낭–호이안 해안 구간의 숙소로 예약 전 정확한 주소를 확인하세요.'],
'ja':['ダナンのホテル：Top Deals & Hot Sellers','Bookdeal.xlsxのホテルと各施設のTrip.comリンクを確認できます。','Top DealsとHot Sellersはファイルの分類であり、確認済み割引や現在の販売順位ではありません。料金や有効日は記載されていません。','Trip.comで客室と料金を確認 ↗','予約前に','正確な住所と移動手段を確認しましょう。','客室、人数、食事、税金、取消条件を比較しましょう。','実際の宿泊日の空き状況と最終料金を確認しましょう。','出典：Bookdeal.xlsx','投稿文とHD画像をダウンロード','ダナン–ホイアンの海岸沿いにある施設です。予約前に正確な住所を確認してください。'],
'hi':['दा नांग होटल: Top Deals और Hot Sellers','Bookdeal.xlsx के होटल और प्रत्येक का अलग Trip.com लिंक देखें।','Top Deals और Hot Sellers फाइल की श्रेणियाँ हैं, सत्यापित छूट या तत्काल बिक्री रैंकिंग नहीं। फाइल में कीमत या लागू तारीख नहीं है।','Trip.com पर कमरे और कीमत देखें ↗','बुकिंग से पहले','सही पता और यात्रा परिवहन जाँचें।','कमरा, अतिथि संख्या, भोजन, कर और रद्द करने की शर्तें तुलना करें।','अपनी वास्तविक तारीख की उपलब्धता और अंतिम कीमत देखें।','स्रोत: Bookdeal.xlsx','पोस्ट और HD चित्र डाउनलोड करें','यह होटल दा नांग–होई आन तटीय क्षेत्र में है; बुकिंग से पहले सही पता जाँचें।'],
'fr':['Hôtels à Da Nang : Top Deals & Hot Sellers','Hôtels et liens Trip.com individuels fournis dans Bookdeal.xlsx.','Top Deals et Hot Sellers sont les catégories du fichier, pas des remises vérifiées ou un classement actuel. Le fichier ne donne ni prix ni dates.','Vérifier chambres et prix sur Trip.com ↗','Avant de réserver','Confirmez l’adresse et les trajets prévus.','Comparez chambre, voyageurs, repas, taxes et annulation.','Vérifiez disponibilité et prix final pour vos dates.','Source : Bookdeal.xlsx','Télécharger les publications et images HD','Cet hôtel se situe sur le corridor côtier Da Nang–Hoi An ; vérifiez son adresse exacte.'],
'de':['Hotels in Da Nang: Top Deals & Hot Sellers','Hotels und einzelne Trip.com-Links aus Bookdeal.xlsx.','Top Deals und Hot Sellers sind Dateikategorien, keine bestätigten Rabatte oder aktuellen Verkaufsränge. Preise und Gültigkeitsdaten fehlen.','Zimmer und Preise auf Trip.com prüfen ↗','Vor der Buchung','Adresse und geplante Fahrten bestätigen.','Zimmer, Gästezahl, Mahlzeiten, Steuern und Stornierung vergleichen.','Verfügbarkeit und Endpreis für die eigenen Daten prüfen.','Quelle: Bookdeal.xlsx','Beiträge und HD-Bilder herunterladen','Das Hotel liegt im Küstenkorridor Da Nang–Hoi An; die genaue Adresse vor Buchung prüfen.'],
'es':['Hoteles de Da Nang: Top Deals & Hot Sellers','Hoteles y enlaces individuales Trip.com de Bookdeal.xlsx.','Top Deals y Hot Sellers son categorías del archivo, no descuentos verificados ni un ranking actual. No hay precios ni fechas de vigencia.','Consultar habitaciones y precios en Trip.com ↗','Antes de reservar','Confirma dirección y transporte para tu ruta.','Compara habitación, viajeros, comidas, impuestos y cancelación.','Comprueba disponibilidad y precio final para tus fechas.','Fuente: Bookdeal.xlsx','Descargar publicaciones e imágenes HD','Este hotel está en el corredor costero Da Nang–Hoi An; confirma la dirección exacta.'],
 'th':['โรงแรมดานัง: Top Deals และ Hot Sellers','ดูโรงแรมและลิงก์ Trip.com เฉพาะแห่งจาก Bookdeal.xlsx','Top Deals และ Hot Sellers เป็นหมวดในไฟล์ ไม่ใช่ส่วนลดที่ยืนยันหรืออันดับขายปัจจุบัน ไฟล์ไม่มีราคาและวันที่ใช้','ดูห้องและราคาบน Trip.com ↗','ก่อนจอง','ตรวจสอบที่อยู่จริงและการเดินทาง','เปรียบเทียบห้อง จำนวนคน อาหาร ภาษี และการยกเลิก','ตรวจสอบห้องว่างและราคาสุดท้ายตามวันเข้าพัก','แหล่งข้อมูล: Bookdeal.xlsx','ดาวน์โหลดโพสต์และภาพ HD','ที่พักนี้อยู่แนวชายฝั่งดานัง–ฮอยอัน โปรดตรวจสอบที่อยู่จริงก่อนจอง'],
'id':['Hotel Da Nang: Top Deals & Hot Sellers','Hotel dan tautan Trip.com masing-masing dari Bookdeal.xlsx.','Top Deals dan Hot Sellers adalah kategori file, bukan diskon terverifikasi atau peringkat penjualan terkini. File tidak memuat harga atau tanggal berlaku.','Periksa kamar dan harga di Trip.com ↗','Sebelum memesan','Pastikan alamat dan transportasi perjalanan.','Bandingkan kamar, tamu, makanan, pajak dan pembatalan.','Periksa ketersediaan serta harga akhir pada tanggal Anda.','Sumber: Bookdeal.xlsx','Unduh tulisan dan gambar HD','Hotel berada di koridor pesisir Da Nang–Hoi An; periksa alamat tepat sebelum memesan.'],
}

ANGLES=[
('Một kỳ nghỉ dễ lên kế hoạch','Chốt số đêm trước, rồi so sánh điều kiện nhận phòng và hủy để lịch đi chủ động hơn.'),
('Chọn phòng theo nhu cầu thật','Hãy xác nhận hạng phòng và số người được ở trước khi quyết định từ ảnh giới thiệu.'),
('Một điểm lưu trú để cân nhắc','Kiểm tra vị trí trên bản đồ và thời gian đến những điểm bạn muốn tham quan.'),
('Đừng chỉ so sánh giá đầu tiên','Xem tổng tiền sau thuế cùng bữa ăn và điều kiện hủy của từng lựa chọn.'),
('Lên lịch linh hoạt cho Đà Nẵng','Để một khoảng nghỉ giữa các chuyến tham quan và hỏi rõ giờ nhận phòng.'),
('Một lựa chọn trong danh sách Top Deals','So sánh cả địa chỉ lẫn phương tiện di chuyển, thay vì chọn chỉ từ tên khách sạn.'),
('Dành ngân sách cho cả hành trình','Tính thêm hành lý, xe sân bay và bữa ăn vào tổng chi phí chuyến đi.'),
('Chủ động với chuyến bay đến muộn','Nếu hạ cánh buổi tối, xác nhận cách nhận phòng trễ với khách sạn trước.'),
('Giữ kỳ nghỉ gọn và rõ ràng','Lưu xác nhận đặt phòng, địa chỉ và thông tin liên hệ để xem ngoại tuyến.'),
('Đi cùng gia đình hoặc bạn bè','Kiểm tra sức chứa phòng, giường phụ và quy định trẻ em theo đúng số khách.'),
('Chọn chỗ ở theo tuyến tham quan','Đặt các điểm bạn muốn đi lên bản đồ, rồi tính thời gian và chi phí di chuyển.'),
('Tìm phòng theo ngày bạn đi','Dùng cùng ngày lưu trú và số khách khi so sánh các phương án.'),
('Kỳ nghỉ ngắn vẫn cần kế hoạch','Cân nhắc giờ đến và giờ về để không mất quá nhiều thời gian cho nhận, trả phòng.'),
('Ưu tiên một hạng phòng phù hợp','Đọc tên loại phòng và điều kiện view; không mặc định mọi phòng có cùng tầm nhìn.'),
('Một gợi ý để mở danh sách so sánh','Đọc nhận xét mới, đặc biệt về vệ sinh và tiếng ồn, rồi đối chiếu với nhu cầu của bạn.'),
('Kiểm tra những gì thực sự được bao gồm','Nếu tên hoặc quảng cáo nhắc tới tiện ích, hãy xác nhận lại trong gói phòng bạn chọn.'),
('Chọn ngày trước khi xem ưu đãi','Giá và tình trạng chỗ có thể khác giữa ngày thường, cuối tuần và ngày lễ.'),
('Đi dài ngày, đọc kỹ điều kiện lưu trú','Hỏi về dịch vụ dọn phòng, các khoản phụ thu và nhu cầu sử dụng phòng của bạn.'),
('Lịch trình thư thả bắt đầu từ chỗ ở','Dự trù thời gian nghỉ và phương tiện về sau một ngày tham quan.'),
('So sánh đúng loại phòng','Hai mức giá chỉ có ý nghĩa khi cùng số khách, loại giường và chính sách hủy.'),
('Đà Nẵng theo nhịp riêng của bạn','Chọn phương án hợp lịch bay và thời gian dành cho biển, thành phố hay chuyến đi trong ngày.'),
('Đặt phòng minh bạch hơn','Xem lại toàn bộ thông tin khách và ngày lưu trú trước bước thanh toán.'),
('Một khách sạn để tìm hiểu thêm','Kiểm tra trang chi tiết thay vì suy ra vị trí hoặc tiện ích chỉ từ tên gọi.'),
('Bắt đầu danh sách Hot Sellers','Dùng nhóm trong file như một danh sách tham khảo, rồi tự so sánh giá theo ngày đi.'),
('Lên kế hoạch cho một chuyến nghỉ khác nhịp','Kiểm tra địa chỉ, điều kiện tiếp cận và phương án di chuyển trước khi chốt phòng.'),
('Một lựa chọn cho bảng so sánh của bạn','Xác nhận hạng phòng và điều kiện view nếu đây là yếu tố quan trọng trong chuyến đi.'),
('Kết hợp lưu trú với khám phá thành phố','Đối chiếu vị trí khách sạn với những điểm tham quan và nhà hàng bạn đã chọn.'),
('Đi cùng người thân, hỏi rõ trước','Nếu quan tâm tới tiện ích gia đình, hãy xem quy định tuổi và phí của gói đã chọn.'),
('Đưa đón cần được xác nhận cụ thể','Khi thông tin tên nhắc tới xe sân bay, hỏi lại lịch chạy, điều kiện và cách đặt chỗ.'),
('Nghỉ dưỡng không cần lịch quá dày','Chừa thời gian nghỉ nhưng vẫn kiểm tra bữa ăn và dịch vụ bao gồm trong giá.'),
('Chủ động với nhu cầu về phòng','Ghi rõ số khách, loại giường và yêu cầu quan trọng trước khi đặt.'),
('Lưu trú và thời gian di chuyển','So sánh tuyến từ sân bay và những điểm sẽ ghé, không chỉ khoảng cách trên ảnh quảng cáo.'),
('Một hành trình dễ theo dõi','Lưu mã đặt dịch vụ và đọc lại thời hạn hủy để tránh bỏ lỡ các mốc quan trọng.'),
('Đặt theo nhu cầu, không theo nhãn','Hot Sellers trong file không thay thế việc kiểm tra điều kiện phù hợp với bạn.'),
('Xem giá cuối cùng trước khi quyết định','Đối chiếu thuế, phụ thu và lựa chọn thanh toán trước khi xác nhận.'),
('Kiểm tra khu vực lưu trú cụ thể','Xem đúng địa chỉ trên bản đồ, đặc biệt khi kết hợp Đà Nẵng và Hội An trong cùng chuyến.'),
('Một kỳ nghỉ với lịch trình linh hoạt','Ưu tiên điều kiện thay đổi hoặc hủy phù hợp nếu ngày đi chưa hoàn toàn chắc chắn.'),
('Dịch vụ đưa đón cần đúng kỳ vọng','Khi tên có nhắc xe ra biển, xác nhận thời gian, điểm đón và điều kiện sử dụng hiện tại.'),
('Lên kế hoạch theo số người','Kiểm tra quy định trẻ em, giường phụ và bữa ăn theo toàn bộ nhóm đi.'),
('Giữ thời gian nghỉ trong lịch','Dành một buổi thư thả và kiểm tra các dịch vụ trả thêm trước khi sử dụng.'),
('Một lựa chọn để nghiên cứu trước chuyến đi','Đọc thông tin phòng và điều kiện đặt trên cùng một nền tảng để dễ đối chiếu.'),
('Đến nơi thuận tiện, về đúng giờ','Hãy tính phương án di chuyển và thời gian dự phòng trước chuyến bay trở về.'),
]
for copy in COPY.values():
    for index,value in enumerate(copy):
        copy[index]=value.replace('Bookdeal.xlsx',SOURCE_NAME)

assert len(ANGLES)==len(HOTELS)==42
for hotel,angle in zip(HOTELS,ANGLES):hotel['angle']=angle

def index_path(lang):return f'deals/{lang}/index.html'
def post_path(lang,h):return f'deals/{lang}/{h["slug"]}/index.html'
def image_path(h):return f'assets/hotel-deals/{h["slug"]}.png'
def page_pairs(languages):
    result=[]
    for lang in languages:
        result.append((index_path(lang),{code:index_path(code) for code in languages}))
        result.extend((post_path(lang,h),{code:post_path(code,h) for code in languages}) for h in HOTELS)
    return result

def social_post(h):
    hook,advice=h['angle'];c=COPY['vi']
    region='\n'+c[10] if h['location_note'] else ''
    return f'''{h['display_name']} | {h['group']}

{hook}. {advice}

Khách sạn có trong nhóm “{h['group']}” của {SOURCE_NAME}. Đây là gợi ý để đưa vào danh sách so sánh cho chuyến đi Đà Nẵng, không phải xác nhận mức giảm giá hay thứ hạng bán chạy hiện tại.{region}

Đối chiếu vị trí với lịch trình, xem đánh giá gần đây, ảnh phòng, lựa chọn bữa sáng và kết nối giao thông. Dành thời gian cho ẩm thực địa phương, Mỹ Khê, sông Hàn hoặc một chuyến riêng đến Hội An nếu phù hợp; các gợi ý này không khẳng định khách sạn nằm ngay cạnh những điểm đó.

Trước khi đặt: kiểm tra địa chỉ, hạng phòng, số khách, bữa ăn, tổng giá sau thuế và điều kiện hủy theo ngày bạn đi.

Xem phòng và giá: {h['url']}

Nguồn: {SOURCE_NAME}; file không có giá hay ngày áp dụng.
Link tiếp thị liên kết: chúng tôi có thể nhận hoa hồng từ đơn đặt hợp lệ, không thu thêm phí từ bạn.

{h.get('hashtags') or '#DaNangHotels #VietnamTravel'} #{h['group'].replace(' ','')}
'''

def short_post(h):
    text=f"{h['display_name']} | {h['group']} (bảng Bookdeal)\nKiểm tra giá và phòng theo ngày đi: {h['url']}\nLink tiếp thị liên kết.\n#DaNangHotels"
    assert len(text)<=280,(h['name'],len(text))
    return text

def render_artwork():
    from playwright.sync_api import sync_playwright
    directory=ROOT/'assets/hotel-deals';directory.mkdir(parents=True,exist_ok=True)
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':1600,'height':900},device_scale_factor=1)
        for h in HOTELS:
            hot=h['group']=='Hot Sellers';accent='#ffd291' if hot else '#92f3de'
            fontsize=66 if len(h['display_name'])>55 else 80 if len(h['display_name'])>35 else 96
            html=f'''<!doctype html><html lang="vi"><meta charset="utf-8"><style>*{{box-sizing:border-box}}body{{margin:0;width:1600px;height:900px;font-family:"Noto Sans",Arial,sans-serif;background:#082f49;color:white;overflow:hidden}}.card{{position:relative;width:100%;height:100%;padding:62px 80px;background:radial-gradient(ellipse at 100% 0,#166e86,transparent 58%),linear-gradient(120deg,#082f49,#094965)}}.brand{{font-size:29px;letter-spacing:3px;font-weight:700}}.badge{{display:inline-block;margin-top:60px;padding:15px 26px;border-radius:40px;background:{accent};color:#123b50;font-size:28px;font-weight:850;letter-spacing:2px}}h1{{position:relative;max-width:1260px;font-size:{fontsize}px;line-height:1.16;letter-spacing:-1px;margin:34px 0 25px;overflow-wrap:anywhere}}.sub{{font-size:32px;color:#d4eff3;margin:0;max-width:1220px}}.footer{{position:absolute;bottom:56px;left:80px;right:80px;border-top:1px solid #6593a2;padding-top:22px}}.link{{font-size:30px;font-weight:700;color:{accent};margin-bottom:12px}}.note{{font-size:24px;color:#cce4eb}}.decor{{position:absolute;right:-35px;bottom:235px;width:200px;height:300px;border:2px solid #8bd5da;border-radius:12px;opacity:.15}}.decor:before{{content:'';position:absolute;inset:30px;background:repeating-linear-gradient(90deg,transparent 0 25px,#8bd5da 25px 38px,transparent 38px 60px)}}.dot{{position:absolute;right:110px;top:65px;border:25px solid {accent};width:140px;height:140px;border-radius:100%;opacity:.14}}</style><div class="card"><div class="dot"></div><div class="decor"></div><div class="brand">STAY IN DA NANG · HOTEL PICKS</div><div class="badge">{h['group'].upper()} · ĐÀ NẴNG</div><h1>{E(h['display_name'])}</h1><p class="sub">{E(h['angle'][0])}</p><div class="footer"><div class="link">{E(h['url'].replace('https://www.',''))}</div><div class="note">Kiểm tra giá theo ngày lưu trú · Link tiếp thị liên kết</div></div></div></html>'''
            page.set_content(html,wait_until='load')
            page.evaluate('document.fonts.ready')
            assert page.locator('h1').bounding_box()['y']+page.locator('h1').bounding_box()['height']<690,h['name']
            assert page.locator('.sub').bounding_box()['y']+page.locator('.sub').bounding_box()['height']<720,h['name']
            page.screenshot(path=str(ROOT/image_path(h)))
        browser.close()
    print('Rendered 42 original typographic PNG cards at 1600 x 900.')

def exports():
    directory=EXPORT_ROOT/'bookdeal-posts';directory.mkdir(parents=True,exist_ok=True)
    for h in HOTELS:
        (directory/f'{h["slug"]}.md').write_text(social_post(h),encoding='utf-8')
        (directory/f'{h["slug"]}.en.md').write_text(h['social_post_en']+'\n',encoding='utf-8')
        (directory/f'{h["slug"]}.blog.en.md').write_text('# '+h['seo_title_en']+'\n\n'+h['blog_content_en']+'\n',encoding='utf-8')
    with (directory/'posts.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.writer(f,lineterminator='\n');writer.writerow(['hotel','group','trip_affiliate_link','post_vi','short_post_vi','post_en','seo_title_en','blog_content_en','booking_cta_en','seo_keywords','hashtags','hd_image','hotel_image_url','image_status'])
        for h in HOTELS:writer.writerow([h['name'],h['group'],h['url'],social_post(h),short_post(h),h['social_post_en'],h['seo_title_en'],h['blog_content_en'],h['booking_cta_en'],h['seo_keywords'],h['hashtags'],image_path(h),h['hotel_image_url'],h['image_status']])
    (directory/'README.txt').write_text(f'42 Vietnamese hotel posts + 42 English source social posts + 42 English source blog drafts + 42 original HD text cards (1600x900). Current content source: {SOURCE_NAME}. Original artwork/name-link source: Bookdeal.xlsx. Top Deals / Hot Sellers are source categories, not live verified rankings or discounts. Prices and dates were not supplied. Seven Hoi An / An Bang entries were excluded. Each post preserves its individual supplied Trip.com URL. No social posts have been sent. Images are text designs, not property photographs. The current workbook has no verified image URLs.\n',encoding='utf-8')
    archive=EXPORT_ROOT/'bookdeal-posts-hd.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        def add(file,name):
            info=zipfile.ZipInfo(name,date_time=(1980,1,1,0,0,0))
            z.writestr(info,file.read_bytes(),compress_type=zipfile.ZIP_DEFLATED)
        for file in sorted(directory.iterdir()):add(file,'posts/'+file.name)
        for h in HOTELS:add(ROOT/image_path(h),'images/'+h['slug']+'.png')
    print('Exported 42 Vietnamese posts, 42 short posts, 42 English social posts, 42 English blog drafts, CSV and ZIP bundle.')

def build_pages(document,relative,url,languages):
    for lang in languages:
        c=COPY[lang];current=index_path(lang)
        body=f'<section class="section soft hotel-directory"><div class="container"><h1>{E(c[0])}</h1><p class="lead">{E(c[7])}</p><div class="blog-browser"><div class="blog-filters" role="group" aria-label="{E(c[0])}"><button type="button" data-blog-filter="all" aria-pressed="true">Top Deals + Hot Sellers</button><button type="button" data-blog-filter="top-deals" aria-pressed="false">Top Deals (23)</button><button type="button" data-blog-filter="hot-sellers" aria-pressed="false">Hot Sellers (19)</button></div><div class="blog-grid">'
        for h in HOTELS:
            img=responsive_image(image_path(h),current,relative,h["display_name"],"blog-cover",sizes="(max-width: 700px) 44vw, 300px")
            body+=f'<article class="blog-card" data-blog-category="{h["group"].lower().replace(" ","-")}"><a href="{relative(current,post_path(lang,h))}">{img}</a><div class="blog-card-body"><span class="pill">{h["group"]}</span><h3><a href="{relative(current,post_path(lang,h))}">{E(h["display_name"])}</a></h3><p>{E(c[7])}</p><a class="hotel-book-link" href="{E(h["url"])}" target="_blank" rel="sponsored noopener noreferrer" data-affiliate="hotel-{h["slug"]}">{E(c[3].replace("↗","→"))}</a></div></article>'

        body+='</div></div></div></section>'
        targets={code:index_path(code) for code in languages}
        write(current,document(lang,current,c[0],c[7],body,targets))
        for h in HOTELS:
            path=post_path(lang,h)
            title,intro,sections=editorial(h,lang)
            img=responsive_image(image_path(h),path,relative,title,sizes="(max-width: 800px) 92vw, 780px",eager=True)
            body=f'<div class="container"><article class="article"><nav class="breadcrumbs"><a href="{relative(path,index_path(lang))}">{E(c[0])}</a></nav><span class="pill">{h["group"]}</span><h1>{E(title)}</h1><p class="intro">{E(intro)}</p><figure class="featured-image">{img}<figcaption>{E(h["display_name"])}</figcaption></figure>'
            if h['location_note']:body+=f'<p class="editorial-note">{E(c[10])}</p>'
            body+=''.join(f'<section class="hotel-editorial"><h2>{E(heading)}</h2><p>{E(text)}</p></section>' for heading,text in sections)
            body+=f'<section><h2>{E(c[4])}</h2><ul>'+''.join(f'<li>{E(check)}</li>' for check in c[5:8])+'</ul></section>'
            body+=f'<p><a class="btn" href="{E(h["url"])}" target="_blank" rel="sponsored noopener noreferrer" data-affiliate="hotel-{h["slug"]}">{E(c[3])}</a></p></article></div>'
            schema={'@context':'https://schema.org','@type':'BlogPosting','headline':title,'description':intro,'image':url(image_path(h)),'inLanguage':lang,'mainEntityOfPage':url(path),'publisher':{'@type':'Organization','name':'Stay in Da Nang'},'keywords':h.get('seo_keywords','')}
            write(path,document(lang,path,title,intro,body,{code:post_path(code,h) for code in languages},schema))
    return page_pairs(languages)

def write(path,text):
    target=ROOT/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(text,encoding='utf-8')

if __name__=='__main__':
    import sys
    if '--render-images' in sys.argv:render_artwork()
    exports()

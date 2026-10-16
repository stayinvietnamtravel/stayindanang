"""Editorial translations used to generate the static site (no runtime dependencies)."""

LANGUAGES = {'en': 'English', 'vi': 'Tiếng Việt', 'zh': '中文', 'ru': 'Русский', 'ko': '한국어', 'ja': '日本語', 'hi': 'हिन्दी'}
SLUGS = [('tips', 'vietnam-travel-planning'), ('hotels', 'where-to-stay-in-da-nang'), ('tours', 'da-nang-hoi-an-hue'), ('destinations', 'vietnam-heritage-guide')]
SOURCES = [
    [('Vietnam Tourism — Travel tips', 'https://vietnam.travel/plan-your-trip'), ('Vietnam Immigration — E-visa', 'https://evisa.gov.vn/')],
    [('Vietnam Tourism — Da Nang', 'https://vietnam.travel/places-to-go/central-vietnam/da-nang')],
    [('UNESCO — Hoi An Ancient Town', 'https://whc.unesco.org/en/list/948/'), ('UNESCO — Complex of Hué Monuments', 'https://whc.unesco.org/en/list/678/')],
    [('UNESCO — Ha Long Bay – Cat Ba Archipelago', 'https://whc.unesco.org/en/list/672/'), ('UNESCO — Trang An Landscape Complex', 'https://whc.unesco.org/en/list/1438/'), ('UNESCO — Phong Nha-Ke Bang National Park and Hin Nam No National Park', 'https://whc.unesco.org/en/list/951/'), ('UNESCO — Hoi An Ancient Town', 'https://whc.unesco.org/en/list/948/'), ('UNESCO — Complex of Hué Monuments', 'https://whc.unesco.org/en/list/678/')],
]

# ui: home, blog, tips, hotels, tours, destinations, hero, lead, booking,
# ad label, fallback, disclosure, source heading, editorial note, back, read,
# intro heading, language label, description, nav label, logo label, footer.
CONTENT = {
 'en': {
  'ui': ['Home', 'Travel blog', 'Travel tips', 'Hotels', 'Tours', 'Destinations', 'Explore Vietnam, one thoughtful trip at a time', 'Real places, practical itineraries and advice for choosing your stay in Da Nang and beyond.', 'Explore on Trip.com ↗', 'Advertisement · Trip.com affiliate partner', 'Banner unavailable? Open Trip.com', 'Affiliate disclosure: We may receive a commission on qualifying Trip.com bookings, at no additional cost to you. Bookings, payments and customer support are handled by Trip.com.', 'Official sources & further reading', 'This guide covers real places and general planning advice, not a first-hand review or a live booking offer. Check current entry rules, weather, opening hours, availability and prices with the official source or provider before travelling.', 'Back to the blog', 'Read guide →', 'Plan your Vietnam trip', 'Language', 'Practical Vietnam travel guides: itineraries, hotel areas and real heritage destinations.', 'Main navigation', 'Stay in Da Nang home', 'Independent Vietnam travel guide.'],
  'articles': [
   ['Planning a Vietnam trip: transport, weather and booking tips', 'Build your itinerary around a region instead of trying to cross the whole country in a few days.', [
    ['Choose a manageable route', 'For a short Central Vietnam visit, use Da Nang as a base and allow separate days for Hoi An and Hue. For a northern trip, combine Hanoi with Ninh Binh or Ha Long rather than adding long transfers to every day. Leave a buffer before international flights.'],
    ['Check entry rules and local conditions', 'Visa eligibility depends on nationality and travel dates. Use Vietnam Immigration’s official e-visa portal and check passport requirements before purchasing non-refundable tickets. Weather varies by region; check local forecasts and warnings, especially before boat trips or mountain excursions.'],
    ['Compare the complete booking conditions', 'Read baggage allowances, cancellation deadlines, transfer arrangements and the final price including taxes. Save your accommodation address and booking reference offline. Use licensed transport and follow local guidance for swimming and outdoor activities.']]],
   ['Where to stay in Da Nang: My Khe, the Han River or Non Nuoc?', 'Pick a neighbourhood for your plans first, then compare specific hotels and recent guest reviews.', [
    ['My Khe and An Thuong: beach access', 'The My Khe beachfront and nearby An Thuong area suit visitors who want beach time and places to eat within walking distance. Check the actual walking route to the beach, road crossings and recent reports about noise. A sea-view room and a beachfront property are different booking choices.'],
    ['Han River: a city base', 'A stay near the Han River can suit riverside walks, restaurants and city sightseeing. Look at the hotel’s exact side of the river and its distance from your planned stops. Allow transfer time for the beach or trips outside the city.'],
    ['Non Nuoc: a quieter resort-style stay', 'The Non Nuoc coastal area near the Marble Mountains is an option for resort stays. Check whether meals, airport transfers and pool access are included, and budget for transport to central Da Nang. Compare room occupancy, children’s policies and cancellation terms rather than relying on promotional photos.']]],
   ['Da Nang, Hoi An and Hue: a flexible four-day itinerary', 'A sample route for Central Vietnam with realistic time for transfers. It is not a packaged tour or guaranteed schedule.', [
    ['Days 1–2: Da Nang and Hoi An', 'Day 1: settle into Da Nang, take a Han River walk and visit My Khe if conditions permit. Day 2: travel to Hoi An for its historic streets and waterfront. Entry to certain heritage buildings uses local ticket arrangements; check the current rules before your visit. Arrange the return journey in advance.'],
    ['Day 3: choose one excursion', 'Choose the Marble Mountains for caves and temples with steps and uneven ground, or Ba Na Hills for its mountain attraction complex and Golden Bridge. These are different experiences: check accessibility, transport, weather and exactly what your ticket includes. Do not assume both fit comfortably into one day.'],
    ['Day 4: Hue or a slower day', 'Hue’s monuments deserve time, and the journey from Da Nang adds a substantial transfer. Consider an overnight stay if you want to see the Imperial City and royal tombs without rushing. Otherwise keep the day for Da Nang. For a guided tour, confirm pickup area, guide language, inclusions and cancellation policy.']]],
   ['Five real heritage destinations to consider in Vietnam', 'These destinations have official UNESCO listings. They are spread across different regions, so choose a few that fit your route.', [
    ['Northern Vietnam: Ha Long–Cat Ba and Trang An', 'Ha Long Bay–Cat Ba Archipelago is known for limestone islands and marine scenery. Check the vessel operator, itinerary and weather cancellation rules before a cruise. Trang An in Ninh Binh combines limestone landscapes with cultural heritage; follow the designated routes and local boat-trip instructions.'],
    ['Central Vietnam: Phong Nha, Hoi An and Hue', 'Phong Nha-Ke Bang is known for karst landscapes and caves; visit only authorised routes and book specialised expeditions through approved operators. Hoi An Ancient Town preserves a historic trading-port setting. The Complex of Hue Monuments includes the former imperial capital and associated sites, which are not all in one walkable area.'],
    ['Travel with context', 'Use the official listings below to understand each site’s heritage value. Follow conservation rules, dress respectfully at places of worship and avoid removing natural or historic objects. Do not treat generic travel photos as evidence of a specific destination or hotel.']]],
  ]
 },
 'vi': {
  'ui': ['Trang chủ', 'Blog du lịch', 'Mẹo du lịch', 'Khách sạn', 'Tour', 'Điểm đến', 'Khám phá Việt Nam qua từng hành trình', 'Địa điểm có thật, lịch trình thiết thực và gợi ý chọn nơi lưu trú tại Đà Nẵng cùng nhiều vùng miền Việt Nam.', 'Khám phá trên Trip.com ↗', 'Quảng cáo · Đối tác tiếp thị liên kết Trip.com', 'Banner không tải? Mở Trip.com', 'Thông tin liên kết: Chúng tôi có thể nhận hoa hồng từ đặt dịch vụ hợp lệ trên Trip.com, không thu thêm phí từ bạn. Trip.com xử lý đặt dịch vụ, thanh toán và hỗ trợ khách hàng.', 'Nguồn chính thức và đọc thêm', 'Bài viết giới thiệu địa điểm có thật và kinh nghiệm lập kế hoạch chung, không phải đánh giá trải nghiệm trực tiếp hay ưu đãi đặt dịch vụ theo thời gian thực. Hãy kiểm tra quy định nhập cảnh, thời tiết, giờ mở cửa, tình trạng chỗ và giá với nguồn chính thức hoặc nhà cung cấp trước khi đi.', 'Về trang blog', 'Đọc bài →', 'Lên kế hoạch khám phá Việt Nam', 'Ngôn ngữ', 'Cẩm nang du lịch Việt Nam: lịch trình, khu vực lưu trú và các di sản có thật.', 'Điều hướng chính', 'Trang chủ Stay in Da Nang', 'Cẩm nang du lịch Việt Nam độc lập.'],
  'articles': [
   ['Mẹo lên kế hoạch du lịch Việt Nam: di chuyển, thời tiết và đặt dịch vụ', 'Chọn một vùng làm trọng tâm thay vì cố đi xuyên Việt chỉ trong vài ngày.', [
    ['Chọn tuyến đi vừa sức', 'Nếu có ít ngày ở miền Trung, bạn có thể lấy Đà Nẵng làm điểm lưu trú và dành ngày riêng cho Hội An, Huế. Với miền Bắc, kết hợp Hà Nội với Ninh Bình hoặc Hạ Long sẽ giúp giảm việc di chuyển liên tục. Luôn chừa thời gian dự phòng trước chuyến bay quốc tế.'],
    ['Kiểm tra nhập cảnh và điều kiện địa phương', 'Điều kiện thị thực phụ thuộc quốc tịch và ngày đi. Khách quốc tế nên dùng cổng thị thực điện tử chính thức của cơ quan xuất nhập cảnh Việt Nam và kiểm tra yêu cầu hộ chiếu trước khi mua vé không hoàn tiền. Thời tiết khác nhau giữa các vùng; xem dự báo và cảnh báo địa phương trước chuyến tàu, thuyền hoặc đi núi.'],
    ['So sánh đầy đủ điều kiện đặt dịch vụ', 'Đọc hạn mức hành lý, thời hạn hủy, phương án đưa đón và giá cuối cùng đã gồm thuế. Lưu địa chỉ khách sạn và mã đặt dịch vụ để xem ngoại tuyến. Chọn đơn vị vận chuyển hợp pháp và tuân thủ hướng dẫn địa phương khi tắm biển hoặc hoạt động ngoài trời.']]],
   ['Ở đâu tại Đà Nẵng: Mỹ Khê, sông Hàn hay Non Nước?', 'Chọn khu vực phù hợp lịch trình trước, rồi so sánh từng khách sạn và đánh giá gần đây của khách.', [
    ['Mỹ Khê và An Thượng: thuận tiện đi biển', 'Dải ven biển Mỹ Khê và khu An Thượng gần đó phù hợp với người muốn dành thời gian cho bãi biển và đi bộ tìm quán ăn. Kiểm tra đường đi thực tế, điểm sang đường và nhận xét gần đây về tiếng ồn. Phòng nhìn ra biển không đồng nghĩa khách sạn nằm sát bãi biển.'],
    ['Sông Hàn: lưu trú gần nhịp sống đô thị', 'Khu vực gần sông Hàn thuận tiện cho đi dạo ven sông, ăn uống và tham quan trong thành phố. Xem khách sạn nằm ở bờ nào và khoảng cách tới các điểm trong lịch trình. Dự trù thời gian đi biển hoặc di chuyển ra ngoài trung tâm.'],
    ['Non Nước: lựa chọn nghỉ dưỡng', 'Khu ven biển Non Nước gần Ngũ Hành Sơn là một lựa chọn cho kỳ nghỉ ở resort. Kiểm tra bữa ăn, đưa đón sân bay và quyền sử dụng hồ bơi có được bao gồm không; tính thêm chi phí vào trung tâm Đà Nẵng. So sánh số người mỗi phòng, chính sách trẻ em và điều kiện hủy, đừng chỉ dựa vào ảnh quảng cáo.']]],
   ['Lịch trình linh hoạt 4 ngày: Đà Nẵng – Hội An – Huế', 'Gợi ý khám phá miền Trung có chừa thời gian di chuyển. Đây không phải tour bán sẵn hay lịch trình được bảo đảm.', [
    ['Ngày 1–2: Đà Nẵng và Hội An', 'Ngày 1 nhận phòng tại Đà Nẵng, đi dạo sông Hàn và ghé Mỹ Khê nếu điều kiện cho phép. Ngày 2 tới Hội An khám phá phố cổ và ven sông. Một số công trình di sản áp dụng quy định vé tham quan địa phương; kiểm tra trước khi đến. Sắp xếp phương tiện về từ trước.'],
    ['Ngày 3: chọn một chuyến tham quan', 'Chọn Ngũ Hành Sơn để thăm hang động và chùa với nhiều bậc thang, nền không bằng phẳng; hoặc Bà Nà Hills với khu du lịch trên núi và Cầu Vàng. Hai trải nghiệm khác nhau: kiểm tra khả năng tiếp cận, phương tiện, thời tiết và những mục có trong vé. Không nên mặc định có thể đi cả hai thoải mái trong một ngày.'],
    ['Ngày 4: Huế hoặc nghỉ chậm lại', 'Quần thể di tích Huế cần thời gian tham quan, còn hành trình từ Đà Nẵng cũng chiếm một khoảng đáng kể. Cân nhắc ngủ lại nếu muốn thăm Đại Nội và lăng tẩm mà không vội. Nếu không, dành ngày cuối ở Đà Nẵng. Khi đặt tour, hỏi rõ khu vực đón, ngôn ngữ hướng dẫn, dịch vụ bao gồm và chính sách hủy.']]],
   ['5 điểm đến di sản có thật nên cân nhắc khi du lịch Việt Nam', 'Các điểm đến này có hồ sơ UNESCO chính thức và nằm ở nhiều vùng khác nhau; hãy chọn nơi phù hợp tuyến đi.', [
    ['Miền Bắc: Hạ Long – Cát Bà và Tràng An', 'Vịnh Hạ Long – Quần đảo Cát Bà nổi bật với đảo đá vôi và cảnh quan biển. Trước khi đặt du thuyền, kiểm tra đơn vị vận hành, tuyến đi và chính sách hủy do thời tiết. Tràng An tại Ninh Bình kết hợp cảnh quan núi đá vôi với giá trị văn hóa; đi đúng tuyến cho phép và làm theo hướng dẫn khi đi thuyền.'],
    ['Miền Trung: Phong Nha, Hội An và Huế', 'Phong Nha – Kẻ Bàng nổi tiếng với địa hình karst và hang động; chỉ đi tuyến được phép và đặt các chuyến thám hiểm chuyên biệt qua đơn vị được cấp phép. Phố cổ Hội An lưu giữ không gian thương cảng lịch sử. Quần thể di tích Cố đô Huế gồm kinh đô cũ cùng các di tích liên quan, không phải tất cả đều nằm trong một khu đi bộ.'],
    ['Du lịch có hiểu biết', 'Dùng hồ sơ chính thức bên dưới để tìm hiểu giá trị từng di sản. Tuân thủ quy định bảo tồn, mặc phù hợp khi tới nơi thờ tự và không lấy vật tự nhiên hoặc hiện vật lịch sử. Ảnh du lịch minh họa không phải bằng chứng về một địa điểm hoặc khách sạn cụ thể.']]],
  ]
 },
 'zh': {
  'ui': ['首页', '旅行博客', '旅行贴士', '酒店', '行程', '目的地', '用心规划，探索越南', '真实目的地、实用行程，以及岘港和越南各地的住宿区域建议。', '在 Trip.com 上探索 ↗', '广告 · Trip.com 联盟合作伙伴', '横幅无法加载？打开 Trip.com', '联盟披露：符合条件的 Trip.com 预订可能为我们带来佣金，您无需向我们支付额外费用。预订、付款和客户服务由 Trip.com 处理。', '官方资料与延伸阅读', '本文介绍真实地点和一般规划建议，并非亲身体验评测或实时优惠。出行前请向官方机构或供应商核实入境规定、天气、开放时间、余位和价格。', '返回博客', '阅读指南 →', '规划越南之旅', '语言', '越南实用旅行指南：行程、住宿区域和真实遗产目的地。', '主导航', 'Stay in Da Nang 首页', '独立越南旅行指南。'],
  'articles': [
   ['越南旅行规划：交通、天气与预订贴士', '以一个地区为重点，不要试图在短短几天内走遍越南。', [
    ['选择合理路线', '短期中部旅行可住在岘港，为会安和顺化分别安排一天。北部旅行可以将河内与宁平或下龙组合，避免每天都花大量时间转车。国际航班前应留出缓冲时间。'],
    ['核实入境要求与当地情况', '签证条件取决于国籍和旅行日期。购买不可退款机票前，请查询越南出入境管理部门的官方电子签证网站和护照要求。各地天气不同，乘船或登山前应查看当地预报和预警。'],
    ['比较完整预订条款', '阅读行李额度、取消期限、接送安排以及含税最终价格。离线保存酒店地址和预订编号。选择合法交通服务，并遵守游泳和户外活动的当地指引。']]],
   ['岘港住哪里：美溪、韩江还是 Non Nuoc？', '先根据行程选择区域，再比较具体酒店和近期住客评价。', [
    ['美溪与 An Thuong：方便去海滩', '美溪海滨及附近的 An Thuong 区适合希望享受海滩并步行寻找餐厅的旅客。核实实际步行路线、过街位置和近期噪音评价。海景房并不等于酒店直接临海。'],
    ['韩江：城市观光据点', '韩江附近适合河畔散步、用餐和市区观光。查看酒店位于哪一岸，以及与计划景点的距离。前往海滩或城外景点时应预留交通时间。'],
    ['Non Nuoc：度假住宿', '五行山附近的 Non Nuoc 海岸可考虑度假村住宿。确认餐食、机场接送和泳池使用是否包含在费用内，并计入前往岘港市中心的交通开支。比较入住人数、儿童政策和取消条款，不要只看宣传照片。']]],
   ['岘港、会安与顺化：灵活的四日行程', '这是一条预留交通时间的越南中部示例路线，并非出售的跟团产品或保证执行的日程。', [
    ['第1–2天：岘港与会安', '第1天在岘港入住，沿韩江散步，条件允许时去美溪海滩。第2天前往会安，游览古街与河畔。部分历史建筑实行当地参观票制度，请提前确认现行规则，并安排好回程交通。'],
    ['第3天：选择一个郊游项目', '五行山有洞穴、寺庙、台阶和不平整地面；巴拿山则是拥有金桥的山地景区。两者体验不同，须确认无障碍条件、交通、天气和门票包含项目。不要默认一天内能轻松游览两处。'],
    ['第4天：顺化或放慢节奏', '顺化古迹值得慢慢游览，从岘港过去也需要较多交通时间。若想从容参观皇城和皇陵，可考虑住一晚；否则将最后一天留给岘港。预订导览时确认接送区域、导游语言、费用包含项目和取消政策。']]],
   ['越南五个真实的遗产目的地', '这些目的地都有联合国教科文组织官方名录，分布在不同地区，请结合路线选择。', [
    ['北部：下龙—吉婆与长安', '下龙湾—吉婆群岛以石灰岩岛屿和海景闻名。预订游船前确认运营方、路线和天气原因取消政策。宁平的长安结合了石灰岩景观与文化遗产；遵循指定路线及当地乘船指引。'],
    ['中部：峰牙、会安与顺化', '峰牙—己榜以喀斯特地形和洞穴著称，应只走获准路线，并通过获准运营商安排专业探险。会安古城保留了历史贸易港口风貌。顺化古迹群涵盖原皇城及相关遗址，并非全部位于同一片可步行区域。'],
    ['了解背景，尊重遗产', '通过下方官方名录了解各地的遗产价值。遵守保护规定，进入宗教场所时穿着得体，不带走自然物或历史物件。通用旅行图片不能证明某个具体地点或酒店的真实样貌。']]],
  ]
 },
 'ru': {
  'ui': ['Главная', 'Блог о путешествиях', 'Советы', 'Отели', 'Маршруты', 'Направления', 'Откройте Вьетнам с продуманным маршрутом', 'Реальные места, практичные маршруты и советы по выбору района для проживания в Дананге и других городах.', 'Посмотреть на Trip.com ↗', 'Реклама · партнёрская программа Trip.com', 'Баннер не загрузился? Открыть Trip.com', 'Партнёрские ссылки: мы можем получать комиссию за подходящие бронирования на Trip.com без дополнительной платы с вашей стороны. Бронирования, оплату и поддержку обрабатывает Trip.com.', 'Официальные источники', 'Здесь описаны реальные места и общие советы, а не личный отзыв или предложение с актуальной ценой. Перед поездкой уточните правила въезда, погоду, часы работы, наличие мест и цены у официальных источников или поставщика.', 'Вернуться в блог', 'Читать →', 'Спланируйте путешествие по Вьетнаму', 'Язык', 'Практичные путеводители по Вьетнаму: маршруты, районы отелей и объекты наследия.', 'Основная навигация', 'Главная Stay in Da Nang', 'Независимый путеводитель по Вьетнаму.'],
  'articles': [
   ['Планирование поездки во Вьетнам: транспорт, погода и бронирования', 'Выберите один регион вместо попытки пересечь всю страну за несколько дней.', [
    ['Составьте посильный маршрут', 'Для короткой поездки по Центральному Вьетнаму можно остановиться в Дананге и выделить отдельные дни для Хойана и Хюэ. На севере сочетайте Ханой с Ниньбинем или Халонгом, чтобы не проводить каждый день в дороге. Перед международным вылетом оставьте запас времени.'],
    ['Уточните правила въезда и местные условия', 'Визовые требования зависят от гражданства и дат поездки. До покупки невозвратных билетов проверьте официальный портал электронной визы миграционной службы Вьетнама и требования к паспорту. Погода различается по регионам; перед прогулкой на лодке или поездкой в горы изучите местный прогноз и предупреждения.'],
    ['Сравните все условия', 'Проверьте багаж, сроки отмены, трансфер и итоговую стоимость с налогами. Сохраните адрес отеля и номер бронирования офлайн. Пользуйтесь легальными перевозчиками и соблюдайте местные указания при купании и активном отдыхе.']]],
   ['Где жить в Дананге: Микхе, река Хан или Нонныок?', 'Сначала выберите район под свой маршрут, затем сравните отели и свежие отзывы гостей.', [
    ['Микхе и Антхыонг: рядом с пляжем', 'Побережье Микхе и соседний район Антхыонг подойдут тем, кто хочет проводить время у моря и ходить в кафе пешком. Проверьте реальный путь до пляжа, переходы через дорогу и свежие отзывы о шуме. Номер с видом на море не означает, что отель находится непосредственно на пляже.'],
    ['Река Хан: городская база', 'Район у реки Хан удобен для прогулок по набережной, ресторанов и осмотра города. Уточните, на каком берегу находится отель и насколько далеко нужные вам места. На поездки к морю и за город оставьте время.'],
    ['Нонныок: курортный отдых', 'Побережье Нонныок рядом с Мраморными горами подходит для курортного размещения. Уточните, включены ли питание, трансфер из аэропорта и бассейн, и учтите стоимость поездок в центр Дананга. Сравнивайте вместимость номера, правила для детей и условия отмены, а не только рекламные фотографии.']]],
   ['Дананг, Хойан и Хюэ: гибкий маршрут на четыре дня', 'Пример поездки по Центральному Вьетнаму с запасом времени на переезды. Это не продаваемый тур и не гарантированное расписание.', [
    ['Дни 1–2: Дананг и Хойан', 'В первый день заселитесь в Дананге, прогуляйтесь у реки Хан и при подходящих условиях посетите Микхе. Во второй день отправляйтесь в Хойан, к историческим улицам и набережной. Для некоторых памятников действуют местные билеты; заранее уточните правила и организуйте обратную поездку.'],
    ['День 3: одна экскурсия на выбор', 'Мраморные горы — это пещеры, храмы, ступени и неровные дорожки. Бана-Хиллс — горный туристический комплекс с Золотым мостом. Проверьте доступность, транспорт, погоду и состав билета. Не рассчитывайте без спешки посетить оба места за один день.'],
    ['День 4: Хюэ или отдых без спешки', 'Памятники Хюэ требуют времени, а дорога из Дананга добавляет продолжительный переезд. Для спокойного осмотра императорского города и гробниц подумайте о ночёвке. Иначе оставьте день для Дананга. При заказе экскурсии уточните место встречи, язык гида, включённые услуги и отмену.']]],
   ['Пять реальных направлений наследия во Вьетнаме', 'У этих мест есть официальные записи ЮНЕСКО. Они расположены в разных регионах, поэтому выбирайте подходящие для вашего маршрута.', [
    ['Север: Халонг — Катба и Чанган', 'Залив Халонг и архипелаг Катба известны известняковыми островами и морскими пейзажами. До бронирования круиза проверьте оператора, маршрут и отмену из-за погоды. Чанган в Ниньбине сочетает известняковые ландшафты и культурное наследие; соблюдайте разрешённые маршруты и указания при поездке на лодке.'],
    ['Центр: Фонгня, Хойан и Хюэ', 'Фонгня-Кебанг известен карстом и пещерами. Посещайте только разрешённые маршруты, а специальные экспедиции заказывайте у уполномоченных операторов. Старый город Хойана сохраняет облик исторического торгового порта. Комплекс памятников Хюэ включает бывшую столицу и связанные объекты, расположенные не в одной пешеходной зоне.'],
    ['Путешествуйте с пониманием', 'Официальные записи ниже помогут узнать ценность каждого объекта. Соблюдайте правила охраны, выбирайте уместную одежду для религиозных мест и не забирайте природные или исторические предметы. Общие туристические фотографии не подтверждают вид конкретного места или отеля.']]],
  ]
 },
 'ko': {
  'ui': ['홈', '여행 블로그', '여행 팁', '호텔', '여행 코스', '여행지', '차근차근 계획하는 베트남 여행', '실제 여행지, 실용적인 일정, 다낭과 베트남의 숙박 지역 선택 가이드입니다.', 'Trip.com에서 둘러보기 ↗', '광고 · Trip.com 제휴 파트너', '배너가 보이지 않나요? Trip.com 열기', '제휴 안내: 조건에 맞는 Trip.com 예약으로 수수료를 받을 수 있으며, 이용자에게 별도 비용을 청구하지 않습니다. 예약, 결제 및 고객 지원은 Trip.com이 처리합니다.', '공식 자료 및 더 읽기', '실제 장소와 일반적인 여행 계획을 소개하는 글이며, 직접 체험한 후기나 실시간 특가가 아닙니다. 출발 전에 공식 기관이나 제공 업체에서 입국 규정, 날씨, 운영 시간, 예약 가능 여부와 가격을 확인하세요.', '블로그로 돌아가기', '가이드 읽기 →', '베트남 여행 계획하기', '언어', '베트남 여행 가이드: 일정, 숙박 지역, 실제 유산 여행지.', '주요 탐색', 'Stay in Da Nang 홈', '독립적인 베트남 여행 가이드.'],
  'articles': [
   ['베트남 여행 계획: 교통, 날씨, 예약 팁', '며칠 만에 전국을 이동하기보다는 한 지역을 중심으로 일정을 짜세요.', [
    ['무리 없는 경로 선택하기', '중부를 짧게 방문한다면 다낭에 머물며 호이안과 후에에 각각 하루를 배정할 수 있습니다. 북부에서는 하노이와 닌빈 또는 하롱을 함께 계획하면 매일 긴 이동을 줄일 수 있습니다. 국제선 출발 전에는 여유 시간을 남기세요.'],
    ['입국 규정과 현지 상황 확인하기', '비자 조건은 국적과 여행 날짜에 따라 다릅니다. 환불 불가 항공권을 구매하기 전에 베트남 출입국 당국의 공식 전자비자 사이트와 여권 요건을 확인하세요. 지역별 날씨가 다르므로 배를 타거나 산으로 가기 전에는 현지 예보와 경보를 살펴보세요.'],
    ['전체 예약 조건 비교하기', '수하물 허용량, 취소 기한, 픽업 조건과 세금 포함 최종 가격을 확인하세요. 숙소 주소와 예약 번호를 오프라인으로 저장하세요. 합법적인 운송 업체를 이용하고 수영이나 야외 활동 시 현지 안내를 따르세요.']]],
   ['다낭 숙박 지역: 미케, 한강, 논느억 비교', '여행 계획에 맞는 지역을 고른 뒤 개별 호텔과 최근 이용 후기를 비교하세요.', [
    ['미케와 안트엉: 해변 가까이', '미케 해변과 인근 안트엉 지역은 해변을 즐기고 걸어서 식당을 찾고 싶은 여행자에게 어울립니다. 실제 도보 경로, 횡단 지점과 최근 소음 후기를 확인하세요. 바다가 보이는 객실과 해변 바로 앞 호텔은 다릅니다.'],
    ['한강 주변: 도심 여행의 거점', '한강 주변은 강변 산책, 식사와 도심 관광에 편리합니다. 호텔이 강 어느 쪽에 있는지, 계획한 장소와 얼마나 떨어져 있는지 확인하세요. 해변이나 외곽으로 이동할 시간도 필요합니다.'],
    ['논느억: 리조트형 휴식', '오행산 근처 논느억 해안은 리조트 숙박을 고려할 수 있는 지역입니다. 식사, 공항 이동과 수영장 이용이 포함되는지 확인하고 다낭 중심부 교통비도 계산하세요. 홍보 사진만 보지 말고 객실 정원, 아동 정책과 취소 조건을 비교하세요.']]],
   ['다낭·호이안·후에: 유연한 4일 일정', '이동 시간을 고려한 중부 베트남 예시 코스입니다. 판매 중인 패키지나 보장된 일정이 아닙니다.', [
    ['1–2일 차: 다낭과 호이안', '첫날은 다낭에 체크인한 뒤 한강을 산책하고 여건이 맞으면 미케 해변에 가세요. 둘째 날은 호이안의 옛 거리와 강변을 둘러보세요. 일부 유산 건물에는 현지 관람권 규정이 있으므로 미리 확인하고 돌아오는 교통편도 준비하세요.'],
    ['3일 차: 한 가지 나들이 선택', '오행산에는 동굴, 사원, 계단과 고르지 않은 길이 있습니다. 바나힐은 골든브리지가 있는 산악 관광 단지입니다. 접근성, 교통, 날씨와 입장권 포함 사항을 확인하세요. 두 곳을 하루에 여유롭게 갈 수 있다고 가정하지 마세요.'],
    ['4일 차: 후에 또는 여유로운 하루', '후에 유적을 둘러보는 데 시간이 필요하고 다낭에서의 이동도 깁니다. 황성과 왕릉을 서두르지 않고 보려면 숙박을 고려하세요. 그렇지 않으면 다낭에서 하루를 보내세요. 투어 예약 시 픽업 지역, 가이드 언어, 포함 사항과 취소 정책을 확인하세요.']]],
   ['베트남의 실제 유산 여행지 다섯 곳', '아래 여행지는 유네스코 공식 목록에 등재되어 있습니다. 여러 지역에 흩어져 있으므로 경로에 맞춰 선택하세요.', [
    ['북부: 하롱–깟바와 짱안', '하롱베이–깟바 군도는 석회암 섬과 바다 경관으로 유명합니다. 크루즈 예약 전 운영 업체, 경로와 날씨로 인한 취소 규정을 확인하세요. 닌빈의 짱안은 석회암 지형과 문화유산을 함께 볼 수 있는 곳입니다. 지정 경로와 현지 보트 안내를 따르세요.'],
    ['중부: 퐁냐, 호이안, 후에', '퐁냐케방은 카르스트 지형과 동굴로 알려져 있습니다. 허용된 경로만 방문하고 전문 탐험은 승인된 업체를 통해 예약하세요. 호이안 고도시는 역사적인 무역항의 모습을 보존합니다. 후에 유적군은 옛 수도와 관련 유적을 포함하며 모두 한 도보 구역에 있지는 않습니다.'],
    ['배경을 이해하며 여행하기', '아래 공식 자료에서 각 유산의 가치를 알아보세요. 보존 규칙을 지키고 종교 시설에서는 적절한 복장을 갖추며 자연물이나 역사적 물건을 가져가지 마세요. 일반적인 여행 사진은 특정 장소나 호텔의 실제 모습에 대한 증거가 아닙니다.']]],
  ]
 },
 'ja': {
  'ui': ['ホーム', '旅のブログ', '旅のヒント', 'ホテル', '旅程', '目的地', '一つずつ計画するベトナムの旅', '実在する目的地、実用的な旅程、ダナンとベトナム各地の宿泊エリア選びをご案内します。', 'Trip.comで探す ↗', '広告 · Trip.comアフィリエイトパートナー', 'バナーが表示されない場合はTrip.comへ', 'アフィリエイトについて：対象となるTrip.comの予約で報酬を受け取る場合があります。お客様に追加料金は請求しません。予約、決済、サポートはTrip.comが行います。', '公式情報と参考資料', '実在する場所と一般的な計画のヒントを紹介しており、実体験のレビューやリアルタイムの販売情報ではありません。渡航前に公式機関や提供会社で入国規則、天候、営業時間、空き状況、料金を確認してください。', 'ブログへ戻る', 'ガイドを読む →', 'ベトナム旅行を計画する', '言語', 'ベトナム旅行ガイド：旅程、宿泊エリア、実在する世界遺産の目的地。', 'メインナビゲーション', 'Stay in Da Nang ホーム', '独立したベトナム旅行ガイド。'],
  'articles': [
   ['ベトナム旅行の計画：交通・天候・予約のヒント', '数日で国全体を巡ろうとせず、一つの地域を中心に旅程を組みましょう。', [
    ['無理のないルートを選ぶ', '中部の短い旅ならダナンを拠点にし、ホイアンとフエに別々の日を設ける方法があります。北部ではハノイとニンビン、またはハロンを組み合わせると毎日の長距離移動を減らせます。国際線の出発前には余裕を残しましょう。'],
    ['入国条件と現地の状況を確認する', 'ビザ条件は国籍と渡航日によって変わります。返金不可の航空券を買う前に、ベトナム入国管理当局の公式電子ビザサイトと旅券要件を確認してください。地域ごとに天候が異なるため、船や山への移動前には現地の予報と警報を確認しましょう。'],
    ['予約条件全体を比較する', '手荷物の制限、キャンセル期限、送迎の条件、税込みの最終料金を確認してください。宿泊先の住所と予約番号はオフラインで保存しましょう。適法な交通サービスを選び、海水浴や屋外活動では現地の案内に従ってください。']]],
   ['ダナンの宿泊エリア：ミーケー、ハン川、ノンヌオック', '旅程に合うエリアを選んでから、各ホテルと最近の宿泊者レビューを比べましょう。', [
    ['ミーケーとアントゥオン：海辺へのアクセス', 'ミーケー海岸と近くのアントゥオン地区は、海で過ごし徒歩で飲食店を探したい人に向いています。実際の徒歩ルート、道路の横断場所、最近の騒音のレビューを確認してください。海が見える客室とビーチに面したホテルは別の条件です。'],
    ['ハン川周辺：街歩きの拠点', 'ハン川周辺は川沿いの散歩、食事、市内観光に便利です。ホテルが川のどちら側にあるか、訪問予定地からどれくらい離れているかを確認しましょう。海岸や郊外へ出かける移動時間も必要です。'],
    ['ノンヌオック：リゾートで過ごす', '五行山に近いノンヌオック海岸はリゾート滞在の選択肢です。食事、空港送迎、プール利用が含まれるかを確認し、ダナン中心部への交通費も計算しましょう。宣伝写真だけでなく定員、子どもの宿泊条件、キャンセル規定を比べてください。']]],
   ['ダナン・ホイアン・フエ：柔軟な4日間の旅程', '移動時間を考慮した中部ベトナムの参考ルートです。販売ツアーや保証された日程ではありません。', [
    ['1〜2日目：ダナンとホイアン', '初日はダナンでチェックインし、ハン川を散歩して、状況がよければミーケーへ。2日目はホイアンの歴史的な街路と川沿いを訪れます。一部の歴史建造物には現地の入場券制度があるため、最新の規則を確認し帰りの交通手段も用意してください。'],
    ['3日目：一つの遠足を選ぶ', '五行山には洞窟、寺院、階段、起伏のある道があります。バーナーヒルズはゴールデンブリッジを含む山の観光施設です。アクセス、移動、天候、チケットの内容を確認しましょう。両方を一日で無理なく回れるとは限りません。'],
    ['4日目：フエまたはゆっくり過ごす', 'フエの史跡には見学時間が必要で、ダナンからの移動も長くなります。王宮と帝陵を落ち着いて訪ねるなら宿泊を検討しましょう。そうでなければダナンで一日過ごせます。ガイドツアーでは送迎場所、案内言語、含まれるサービス、取消条件を確認してください。']]],
   ['ベトナムの実在する五つの遺産旅行先', '以下の目的地にはユネスコの公式登録があります。各地に分散しているので、ルートに合う場所を選びましょう。', [
    ['北部：ハロン–カットバとチャンアン', 'ハロン湾–カットバ群島は石灰岩の島々と海の景観で知られています。クルーズ予約前に運航会社、ルート、悪天候による取消条件を確認してください。ニンビンのチャンアンは石灰岩の景観と文化遺産を組み合わせた地域です。指定ルートと現地の船の案内に従いましょう。'],
    ['中部：フォンニャ、ホイアン、フエ', 'フォンニャ–ケバンはカルスト地形と洞窟で知られます。許可されたルートのみを訪れ、専門的な探検は認可された事業者に依頼してください。ホイアンの古い町並みは歴史的交易港の姿を伝えます。フエの建造物群は旧都と関連遺跡を含み、すべてが一つの徒歩圏内にあるわけではありません。'],
    ['背景を知って旅する', '下記の公式資料で各遺産の価値を調べましょう。保護規則を守り、宗教施設では適切な服装をし、自然物や歴史的な物を持ち帰らないでください。一般的な旅行写真は特定の場所やホテルの実景を示す証拠にはなりません。']]],
  ]
 },
 'hi': {
  'ui': ['मुखपृष्ठ', 'यात्रा ब्लॉग', 'यात्रा सुझाव', 'होटल', 'यात्रा कार्यक्रम', 'गंतव्य', 'सोच-समझकर वियतनाम की यात्रा करें', 'वास्तविक जगहें, व्यावहारिक यात्रा कार्यक्रम और दा नांग तथा वियतनाम में ठहरने के इलाके चुनने की सलाह।', 'Trip.com पर देखें ↗', 'विज्ञापन · Trip.com सहयोगी भागीदार', 'बैनर नहीं दिख रहा? Trip.com खोलें', 'सहयोगी लिंक सूचना: योग्य Trip.com बुकिंग से हमें कमीशन मिल सकता है। आपसे कोई अतिरिक्त शुल्क नहीं लिया जाता। बुकिंग, भुगतान और ग्राहक सहायता Trip.com संभालता है।', 'आधिकारिक स्रोत और आगे पढ़ें', 'यह लेख वास्तविक स्थानों और सामान्य योजना की सलाह पर आधारित है, निजी अनुभव की समीक्षा या तत्काल बुकिंग ऑफर नहीं है। यात्रा से पहले आधिकारिक स्रोत या सेवा प्रदाता से प्रवेश नियम, मौसम, खुलने का समय, उपलब्धता और कीमत जाँचें।', 'ब्लॉग पर वापस जाएँ', 'गाइड पढ़ें →', 'वियतनाम यात्रा की योजना बनाएँ', 'भाषा', 'वियतनाम यात्रा गाइड: यात्रा कार्यक्रम, होटल के इलाके और वास्तविक विरासत स्थल।', 'मुख्य नेविगेशन', 'Stay in Da Nang मुखपृष्ठ', 'स्वतंत्र वियतनाम यात्रा गाइड।'],
  'articles': [
   ['वियतनाम यात्रा की योजना: परिवहन, मौसम और बुकिंग सुझाव', 'कुछ दिनों में पूरे देश को पार करने के बजाय एक क्षेत्र को आधार बनाकर यात्रा करें।', [
    ['व्यावहारिक मार्ग चुनें', 'मध्य वियतनाम की छोटी यात्रा में दा नांग को आधार बनाकर होई आन और हुए के लिए अलग दिन रखें। उत्तर में हनोई के साथ निन्ह बिन्ह या हा लॉन्ग जोड़ सकते हैं, ताकि हर दिन लंबी यात्रा न करनी पड़े। अंतरराष्ट्रीय उड़ान से पहले अतिरिक्त समय रखें।'],
    ['प्रवेश नियम और स्थानीय परिस्थितियाँ जाँचें', 'वीज़ा नियम राष्ट्रीयता और यात्रा की तारीख पर निर्भर करते हैं। बिना रिफंड वाली टिकट खरीदने से पहले वियतनाम के आव्रजन विभाग का आधिकारिक ई-वीज़ा पोर्टल और पासपोर्ट की आवश्यकताएँ जाँचें। अलग क्षेत्रों का मौसम अलग होता है; नाव या पहाड़ की यात्रा से पहले स्थानीय पूर्वानुमान और चेतावनी देखें।'],
    ['बुकिंग की पूरी शर्तें पढ़ें', 'सामान की सीमा, रद्द करने की अंतिम तारीख, आने-जाने की व्यवस्था और कर सहित अंतिम कीमत देखें। होटल का पता और बुकिंग नंबर ऑफलाइन रखें। वैध परिवहन सेवाएँ चुनें और तैराकी या बाहरी गतिविधियों में स्थानीय निर्देशों का पालन करें।']]],
   ['दा नांग में कहाँ ठहरें: माय खे, हान नदी या नॉन नुओक?', 'पहले अपने कार्यक्रम के अनुसार इलाका चुनें, फिर होटल और हाल की अतिथि समीक्षाएँ देखें।', [
    ['माय खे और आन थुओंग: समुद्र तट के पास', 'माय खे समुद्र तट और पास का आन थुओंग इलाका समुद्र किनारे समय बिताने और पैदल भोजनालय खोजने वालों के लिए उपयोगी हैं। समुद्र तट तक असली पैदल मार्ग, सड़क पार करने की जगह और शोर से जुड़ी हाल की समीक्षाएँ देखें। समुद्र दिखने वाला कमरा और सीधे समुद्र तट पर स्थित होटल अलग बातें हैं।'],
    ['हान नदी: शहर घूमने का आधार', 'हान नदी के पास ठहरना नदी किनारे सैर, भोजन और शहर घूमने के लिए सुविधाजनक हो सकता है। होटल नदी के किस किनारे है और आपके चुने स्थानों से कितना दूर है, यह देखें। समुद्र तट और शहर के बाहर जाने के लिए समय रखें।'],
    ['नॉन नुओक: रिसॉर्ट में आराम', 'मार्बल माउंटेन्स के पास नॉन नुओक तट रिसॉर्ट में रहने का विकल्प है। भोजन, हवाई अड्डे से परिवहन और पूल का उपयोग कीमत में शामिल है या नहीं, यह जाँचें। दा नांग केंद्र तक जाने का खर्च भी जोड़ें। प्रचार तस्वीरों के बजाय कमरे की क्षमता, बच्चों की नीति और रद्द करने की शर्तें तुलना करें।']]],
   ['दा नांग, होई आन और हुए: लचीला चार दिन का कार्यक्रम', 'मध्य वियतनाम का नमूना मार्ग, जिसमें आने-जाने का समय रखा गया है। यह बिक्री वाला पैकेज या निश्चित समय-सारणी नहीं है।', [
    ['दिन 1–2: दा नांग और होई आन', 'पहले दिन दा नांग में ठहरें, हान नदी किनारे चलें और परिस्थितियाँ ठीक हों तो माय खे जाएँ। दूसरे दिन होई आन की ऐतिहासिक गलियाँ और नदी किनारा देखें। कुछ विरासत इमारतों के लिए स्थानीय प्रवेश टिकट नियम हैं; पहले जाँचें और वापसी का परिवहन तय करें।'],
    ['दिन 3: एक भ्रमण चुनें', 'मार्बल माउंटेन्स में गुफाएँ, मंदिर, सीढ़ियाँ और असमतल रास्ते हैं। बा ना हिल्स गोल्डन ब्रिज वाला पहाड़ी पर्यटन परिसर है। पहुँच की सुविधा, परिवहन, मौसम और टिकट में शामिल चीज़ें देखें। यह न मानें कि दोनों जगहों को एक दिन में आराम से देखा जा सकता है।'],
    ['दिन 4: हुए या आराम का दिन', 'हुए के स्मारक देखने में समय लगता है और दा नांग से यात्रा भी लंबी है। शाही शहर और समाधियों को बिना जल्दबाजी देखने के लिए रात रुकने पर विचार करें। नहीं तो दिन दा नांग में बिताएँ। निर्देशित टूर लेते समय पिकअप इलाका, गाइड की भाषा, शामिल सेवाएँ और रद्द करने की नीति जाँचें।']]],
   ['वियतनाम के पाँच वास्तविक विरासत गंतव्य', 'इन स्थानों की आधिकारिक यूनेस्को सूची उपलब्ध है। ये अलग-अलग क्षेत्रों में हैं, इसलिए अपने मार्ग के अनुसार चुनें।', [
    ['उत्तर: हा लॉन्ग–कैट बा और ट्रांग आन', 'हा लॉन्ग खाड़ी–कैट बा द्वीपसमूह चूना पत्थर के द्वीपों और समुद्री दृश्यों के लिए प्रसिद्ध है। क्रूज़ बुक करने से पहले संचालक, मार्ग और मौसम के कारण रद्द होने की नीति देखें। निन्ह बिन्ह का ट्रांग आन चूना पत्थर के परिदृश्य और सांस्कृतिक विरासत को जोड़ता है। निर्धारित मार्ग और स्थानीय नाव निर्देशों का पालन करें।'],
    ['मध्य क्षेत्र: फोंग न्हा, होई आन और हुए', 'फोंग न्हा–के बांग कार्स्ट भूभाग और गुफाओं के लिए जाना जाता है। केवल अनुमति वाले मार्ग पर जाएँ और विशेष अभियान स्वीकृत संचालकों से बुक करें। होई आन प्राचीन नगर ऐतिहासिक व्यापारिक बंदरगाह का स्वरूप संजोता है। हुए स्मारक समूह में पुरानी राजधानी और संबंधित स्थल हैं; सभी एक ही पैदल क्षेत्र में नहीं हैं।'],
    ['स्थल का महत्व समझकर यात्रा करें', 'नीचे के आधिकारिक स्रोत हर स्थल की विरासत का महत्व बताते हैं। संरक्षण नियमों का पालन करें, पूजा स्थलों पर उचित कपड़े पहनें और प्राकृतिक या ऐतिहासिक वस्तुएँ न ले जाएँ। सामान्य यात्रा तस्वीरें किसी खास स्थान या होटल का प्रमाण नहीं हैं।']]],
  ]
 },
}

# This source was provided by the owner in chat; X access is unavailable here.
from x_post import ARTICLES as X_ARTICLES, SLUG as X_SLUG, SOURCE as X_SOURCE, BOOKING as X_BOOKING, NOTES as X_NOTES

SLUGS.append(X_SLUG)
SOURCES.append([
    ('@stayindanang — Stay in Da Nang: Best Hotels - Tours - Flights 2026 (X)', X_SOURCE),
    ('Vietnam Tourism — Da Nang', 'https://vietnam.travel/places-to-go/central-vietnam/da-nang'),
    ('UNESCO — Hoi An Ancient Town', 'https://whc.unesco.org/en/list/948/'),
])
ARTICLE_DETAILS = {X_SLUG[1]: {'booking': X_BOOKING, 'source_notes': X_NOTES}}
for code in LANGUAGES:
    CONTENT[code]['articles'].append(X_ARTICLES[code])

from extra_locales import LANGUAGES as EXTRA_LANGUAGES, CONTENT as EXTRA_CONTENT
from extra_topics import SLUGS as EXTRA_SLUGS, SOURCES as EXTRA_SOURCES, ARTICLES as EXTRA_ARTICLES, LABELS as EXTRA_LABELS

LANGUAGES.update(EXTRA_LANGUAGES)
for code, data in EXTRA_CONTENT.items():
    CONTENT[code] = {'ui': data['ui'], 'articles': data['articles']}
    ARTICLE_DETAILS[X_SLUG[1]]['source_notes'][code] = data['note']
SLUGS.extend(EXTRA_SLUGS)
SOURCES.extend(EXTRA_SOURCES)
ALL_LABELS = {'en':'All topics','vi':'Tất cả chủ đề','zh':'全部主题','zh-Hant':'全部主題','ru':'Все темы','ko':'모든 주제','ja':'すべてのテーマ','hi':'सभी विषय','fr':'Tous les thèmes','de':'Alle Themen','es':'Todos los temas','th':'ทุกหัวข้อ','id':'Semua topik'}
FEATURE_CAPTIONS = {}
for code in LANGUAGES:
    CONTENT[code]['ui'].extend(EXTRA_LABELS[code][:2] + [ALL_LABELS[code]])
    CONTENT[code]['articles'].extend(EXTRA_ARTICLES[code])
    FEATURE_CAPTIONS[code] = EXTRA_LABELS[code][2]

from vietnam_ideas import register as register_vietnam_ideas
register_vietnam_ideas(CONTENT,LANGUAGES,SLUGS,SOURCES,ARTICLE_DETAILS)

from world_posters import register as register_world_posters
register_world_posters(CONTENT,LANGUAGES,SLUGS,SOURCES,ARTICLE_DETAILS)

from campaign_guides import register as register_campaign_guides
register_campaign_guides(CONTENT,LANGUAGES,SLUGS,SOURCES,ARTICLE_DETAILS)

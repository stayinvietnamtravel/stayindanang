"""Food, outdoor experiences and city walks in thirteen language editions."""
SLUGS = [('food','vietnam-food-guide'),('experiences','coastal-vietnam-experiences'),('destinations','hanoi-ho-chi-minh-city-walks')]
SOURCES = [
 [('Vietnam Tourism — Food and travel', 'https://vietnam.travel/')],
 [('Vietnam Tourism — Da Nang','https://vietnam.travel/places-to-go/central-vietnam/da-nang'),('UNESCO — Hoi An Ancient Town','https://whc.unesco.org/en/list/948/')],
 [('Vietnam Tourism — Hanoi','https://vietnam.travel/places-to-go/northern-vietnam/ha-noi'),('Vietnam Tourism — Ho Chi Minh City','https://vietnam.travel/places-to-go/southern-vietnam/ho-chi-minh-city')],
]
LABELS = {
 'en':['Food & drink','Experiences','Original editorial illustration, not a photograph of a specific place or property.'],
 'vi':['Ẩm thực','Trải nghiệm','Ảnh minh họa biên tập, không phải ảnh chụp địa điểm hay cơ sở cụ thể.'],
 'zh':['美食','体验','原创编辑插画，并非特定地点或住宿的实景照片。'],
 'zh-Hant':['美食','體驗','原創編輯插畫，並非特定地點或住宿的實景照片。'],
 'ru':['Еда и напитки','Впечатления','Оригинальная иллюстрация, не фотография конкретного места или отеля.'],
 'ko':['음식','체험','직접 제작한 편집 삽화이며 특정 장소나 숙소의 실제 사진이 아닙니다.'],
 'ja':['グルメ','体験','独自の編集イラストであり、特定の場所や宿泊施設の実写ではありません。'],
 'hi':['खान-पान','अनुभव','मूल संपादकीय चित्रण; किसी खास जगह या होटल की वास्तविक तस्वीर नहीं।'],
 'fr':['Gastronomie','Expériences','Illustration éditoriale originale, pas une photographie d’un lieu ou établissement précis.'],
 'de':['Essen & Trinken','Erlebnisse','Eigene redaktionelle Illustration, kein Foto eines bestimmten Ortes oder Hotels.'],
 'es':['Gastronomía','Experiencias','Ilustración editorial original, no una fotografía de un lugar o alojamiento concreto.'],
 'th':['อาหาร','ประสบการณ์','ภาพประกอบต้นฉบับ ไม่ใช่ภาพถ่ายสถานที่หรือที่พักแห่งใดโดยเฉพาะ'],
 'id':['Kuliner','Pengalaman','Ilustrasi editorial asli, bukan foto tempat atau penginapan tertentu.'],
}
ARTICLES = {
'vi':[
 ['Ăn gì ở Việt Nam: gợi ý món ngon từ Bắc vào Nam','Ẩm thực là một cách hiểu thêm về điểm đến. Chọn vài món theo từng vùng thay vì cố tìm một danh sách quán “tốt nhất” chưa được kiểm chứng.',[
 ['Miền Bắc: phở, bún chả và cà phê','Tại Hà Nội, bạn có thể tìm hiểu phở với nước dùng, bánh phở và thịt; bún chả với thịt nướng, bún và nước chấm. Công thức và cách phục vụ khác nhau giữa các quán. Nếu thử cà phê trứng, hỏi rõ nguyên liệu khi có dị ứng; đồ uống này có thể chứa trứng và sữa. Đi bộ quanh phố cổ, xem thực đơn và giá trước khi gọi sẽ giúp chủ động hơn.'],
 ['Miền Trung: mì Quảng, cao lầu và bánh mì','Mì Quảng gắn với vùng Quảng Nam, thường có sợi mì, rau, phần đạm và lượng nước dùng vừa phải; topping tùy nơi. Cao lầu là món tiêu biểu để tìm hiểu khi tới Hội An. Bánh mì có nhiều biến thể về nhân và nước sốt, không chỉ một công thức chung. Hãy hỏi kích thước phần ăn, nguyên liệu và món có sẵn trong ngày thay vì chọn chỉ vì ảnh quảng cáo.'],
 ['Miền Nam và cách chọn bữa ăn phù hợp','Ở TP.HCM, có thể tìm hiểu hủ tiếu hoặc bánh xèo; cách chế biến thay đổi theo vùng và từng quán. Khi ăn theo nhóm, gọi ít món trước rồi gọi thêm để tránh lãng phí. Người ăn chay nên hỏi về nước dùng và nước mắm; người dị ứng cần xác nhận đậu phộng, hải sản, trứng hoặc sữa và nguy cơ dùng chung dụng cụ. Chọn nơi chế biến sạch, xem giá niêm yết và mang nước uống phù hợp cho thời tiết nóng.']]],
 ['Trải nghiệm biển miền Trung: Mỹ Khê, Non Nước và một ngày ở Hội An','Một kỳ nghỉ biển có thể kết hợp đi dạo, khám phá văn hóa và thời gian nghỉ, không cần lấp đầy ngày bằng tour.',[
 ['Buổi sáng ở Mỹ Khê','Dành thời gian đi dạo bãi biển trước khi trời quá nóng, giữ đồ dùng gọn và không để tài sản không trông coi. Muốn tắm biển, chỉ xuống nước trong khu vực được phép và làm theo cờ hiệu, nhân viên cứu hộ cùng điều kiện tại thời điểm đó. Biển đẹp trong ảnh không chứng minh rằng hôm nay có thể bơi an toàn.'],
 ['Non Nước và Ngũ Hành Sơn','Có thể kết hợp thời gian ở khu ven biển Non Nước với một chuyến tới Ngũ Hành Sơn. Hang động, chùa và các bậc thang đòi hỏi thời gian và khả năng di chuyển; xem thông tin tiếp cận trước khi chọn tuyến. Mang giày phù hợp, dành khoảng nghỉ và mặc lịch sự khi vào nơi thờ tự. Đây là gợi ý tự lên kế hoạch, không phải tour có dịch vụ được bảo đảm.'],
 ['Hội An và hoạt động trên nước','Dành một buổi riêng cho phố cổ, quán ăn và ven sông Hội An. Nếu muốn đi thuyền hoặc trải nghiệm thuyền thúng ở khu vực quanh Hội An, hỏi rõ địa điểm, đơn vị vận hành, áo phao, sức chứa và phương án hủy do thời tiết. Không mặc định vé phố cổ bao gồm mọi hoạt động. Thỏa thuận giá và giờ về trước, đồng thời để lịch linh hoạt khi có mưa lớn.']]],
 ['Đi bộ khám phá Hà Nội và TP.HCM: hai hành trình riêng','Hai thành phố nằm ở hai miền khác nhau. Các gợi ý dưới đây là hai chuyến đi bộ độc lập, không phải lịch trình di chuyển giữa hai nơi trong một ngày.',[
 ['Hà Nội: hồ Hoàn Kiếm và phố cổ','Bắt đầu quanh hồ Hoàn Kiếm rồi chọn một vài tuyến phố cổ gần đó để quan sát đời sống, kiến trúc và tìm bữa ăn. Nếu vào đền Ngọc Sơn, kiểm tra điều kiện tham quan hiện tại và trang phục phù hợp. Giữ tuyến đi ngắn, dừng nghỉ khi nóng hoặc mưa; vỉa hè và giao thông có thể khiến thời gian đi bộ khác dự tính.'],
 ['TP.HCM: trung tâm Quận 1','Có thể chọn khu vực Bưu điện Trung tâm và đường sách Nguyễn Văn Bình, rồi dành một buổi khác cho Dinh Độc Lập. Kiểm tra giờ mở cửa, vé và quy định tại từng điểm; các công trình có thể hạn chế tham quan vì bảo trì hoặc sự kiện. Không nên dựa vào ảnh cũ để xác định khả năng vào bên trong.'],
 ['Kết hợp bữa ăn và điểm dừng','Chọn quán theo thực đơn, giá rõ ràng và nhu cầu ăn uống, không theo một lời hứa “ngon nhất” thiếu cơ sở. Xen kẽ các đoạn đi bộ với nghỉ trong bóng râm hoặc không gian trong nhà; dùng phương tiện hợp pháp khi cần đi xa. Lưu bản đồ ngoại tuyến và địa chỉ nơi ở, đồng thời giữ đồ cá nhân gọn khi ở nơi đông người.']]],
],
'en':[
 ['What to eat in Vietnam: a regional food guide','Food can add context to a journey. Explore a few regional dishes instead of relying on an unverified “best restaurant” list.',[
 ['Northern flavours','In Hanoi, learn about pho with broth, rice noodles and meat, or bun cha with grilled pork, noodles and dipping sauce. Recipes vary by vendor. Egg coffee can contain egg and milk: check ingredients if you have allergies. Read the menu and prices before ordering around the Old Quarter.'],
 ['Central Vietnam','Mi Quang is associated with Quang Nam and combines noodles, herbs, protein and a relatively small amount of broth; toppings vary. Cao lau is a dish to explore in Hoi An. Banh mi fillings and sauces differ between vendors, so ask about portions and ingredients rather than choosing only from promotional photos.'],
 ['Southern dishes and dietary needs','In Ho Chi Minh City, explore hu tieu or banh xeo, with regional variations. Order gradually when sharing. Vegetarian travellers should ask about broth and fish sauce; confirm peanuts, seafood, egg, milk and shared preparation equipment for allergies. Choose clean preparation, clear prices and suitable drinking water.']]],
 ['Coastal Central Vietnam: My Khe, Non Nuoc and Hoi An experiences','Combine beach walks, cultural visits and rest without filling every hour with a tour.',[
 ['A morning at My Khe','Walk before the strongest heat and keep belongings attended. Swim only where allowed and follow flags, lifeguards and current conditions. An attractive beach photograph does not establish that swimming is safe today.'],
 ['Non Nuoc and the Marble Mountains','Combine time on the Non Nuoc coast with a visit to the Marble Mountains. Caves, temples and stairs require time and suitable mobility; check access before choosing a route. Wear practical shoes, take breaks and dress respectfully at religious sites. This is a planning suggestion, not a guaranteed tour.'],
 ['Hoi An and time on the water','Allow a separate outing for Hoi An’s historic streets, food and riverfront. For boat or basket-boat activities nearby, confirm the location, operator, life jackets, capacity and weather cancellation rules. Old Town admission does not automatically cover every activity. Agree on price and return time and leave room to change plans in heavy rain.']]],
 ['Walking Hanoi and Ho Chi Minh City: two separate routes','These cities are in different regions. Treat these as two independent walks, not a one-day transfer itinerary.',[
 ['Hanoi: Hoan Kiem and the Old Quarter','Start around Hoan Kiem Lake and choose nearby Old Quarter streets for architecture, daily life and food. Check current access and dress expectations for Ngoc Son Temple. Keep the route short and pause in heat or rain; pavements and traffic affect walking time.'],
 ['Ho Chi Minh City: central District 1','Explore the Central Post Office area and Nguyen Van Binh Book Street, then allow a separate visit for the Independence Palace. Check hours, tickets and rules at each stop; maintenance or events may limit access. Older photos do not establish that an interior is currently open.'],
 ['Meals and breaks','Choose food using menus, clear prices and dietary needs rather than unsupported “best” claims. Alternate walking with shaded or indoor stops and use licensed transport for longer distances. Save an offline map and accommodation address and keep belongings secure in busy areas.']]],
],
'zh':[
 ['越南吃什么：从北到南的美食指南','通过地域菜肴认识目的地，不必依赖未经核实的“最佳餐厅”榜单。',[
 ['北部风味','在河内了解河粉的汤底、米粉与肉类，或尝试烤猪肉、米线和蘸汁组成的 bun cha。不同店铺做法不同。鸡蛋咖啡可能含蛋和奶，过敏者应确认原料。点餐前看清菜单与价格。'],
 ['中部菜肴','广南的 mi Quang 常结合面条、香草、蛋白质食材和少量汤汁，配料各有差异。会安可了解 cao lau。越南法棍的馅料和酱汁也不同，先问分量及原料，不要只看宣传照片。'],
 ['南部与饮食需求','胡志明市可了解 hu tieu 或 banh xeo。分享时逐步加点，避免浪费。素食者询问汤底和鱼露；过敏者确认花生、海鲜、蛋、奶及共用器具。选择制作卫生、价格清晰的店铺和合适饮水。']]],
 ['越南中部海岸体验：美溪、Non Nuoc 与会安','结合海边散步、文化参观和休息，无须每个小时都安排跟团活动。',[
 ['美溪的早晨','在酷热前散步并看好物品。仅在允许区域游泳，遵守旗帜、救生员和当时的海况。漂亮海滩照片不证明今天适合安全游泳。'],
 ['Non Nuoc 与五行山','把海岸休息与五行山参观结合。洞穴、寺庙和台阶需要时间与行动能力，先核实可达条件。穿合适鞋子、安排休息，在宗教场所穿着得体。此为规划建议，并非保证执行的旅游产品。'],
 ['会安与水上活动','另留时间给古街、美食和河畔。附近乘船或竹篮船体验需确认地点、运营方、救生衣、载客量和天气取消规则。古城门票不自动包含所有活动。先谈好价格与返程时间，暴雨时保持计划灵活。']]],
 ['步行河内与胡志明市：两条独立路线','两城位于不同地区，以下是分别进行的步行路线，不是一日两城行程。',[
 ['河内：还剑湖与老城区','从还剑湖周边开始，选附近古街观察建筑、生活与餐饮。玉山祠需确认当时参观规定和穿着。路线不宜过长，炎热或下雨时休息；人行道和交通会影响耗时。'],
 ['胡志明市：第一郡中心','可走中央邮局周边和阮文平书街，另留时间参观统一宫。确认各点开放时间、门票与规则，维修或活动可能限制进入。旧照片无法证明室内目前开放。'],
 ['餐饮与休息','按菜单、明码价格和饮食需求选餐，不依赖无依据的“最好吃”。穿插阴凉或室内休息，远距离使用合法交通。保存离线地图及住宿地址，在拥挤区域保管好物品。']]],
],
'zh-Hant':[
 ['越南吃什麼：由北到南的美食指南','用地域料理認識目的地，不必依賴未查證的「最佳餐廳」榜單。',[
 ['北部風味','在河內認識河粉的湯底、米粉與肉類，或嘗試烤豬肉、米線及沾醬組成的 bun cha。各店做法不同。雞蛋咖啡可能含蛋與奶，過敏者應確認原料。點餐前查看菜單和價格。'],
 ['中部料理','廣南的 mi Quang 常有麵條、香草、蛋白質食材和少量湯汁，配料依店而異。會安可認識 cao lau。越南法國麵包的餡料與醬汁也不同，先問份量及食材，不要只看廣告照片。'],
 ['南部與飲食需求','胡志明市可認識 hu tieu 或 banh xeo。分享時逐步加點以減少浪費。素食者詢問湯底與魚露；過敏者確認花生、海鮮、蛋、奶及共用器具。選擇製作衛生、價格清楚的店家和合適飲水。']]],
 ['越南中部海岸體驗：美溪、Non Nuoc 與會安','結合海邊散步、文化參觀和休息，不必每小時都排導覽。',[
 ['美溪早晨','避開酷熱時間散步並看好物品。只在許可區域游泳，遵守旗幟、救生員及當時海況。漂亮照片不代表今天適合安全游泳。'],
 ['Non Nuoc 與五行山','結合海岸休息和五行山參觀。洞穴、寺廟、階梯需要時間及行動能力，先確認通行條件。穿合適鞋子、安排休息，宗教場所穿著合宜。這是規劃建議，不是保證成行產品。'],
 ['會安與水上活動','另留時間給古街、美食及河畔。附近搭船或竹籃船活動應確認地點、業者、救生衣、載客量和天候取消規則。古城票不自動包含所有活動。先談好價格及返程時間，大雨時保留調整空間。']]],
 ['步行河內與胡志明市：兩條獨立路線','兩城位於不同地區，以下是分開進行的步行路線，非一日兩城行程。',[
 ['河內：還劍湖與老城區','從還劍湖開始，選附近古街觀察建築、生活及餐飲。玉山祠需確認當時規定和服裝要求。路線不宜太長，炎熱或下雨時休息；人行道及交通會影響時間。'],
 ['胡志明市：第一郡中心','可遊中央郵局周邊及阮文平書街，另留時間給統一宮。確認營業時間、門票及規則，維修或活動可能限制參觀。舊照片不代表室內目前開放。'],
 ['用餐與休息','按菜單、清楚價格和飲食需求選餐，不依賴無根據的「最好吃」。穿插陰涼或室內休息，遠距離用合法交通。保存離線地圖與住宿地址，在人多處保管物品。']]],
],
'fr':[
 ['Que manger au Vietnam : un guide par région','Découvrez des plats régionaux plutôt qu’un classement de restaurants non vérifié.',[
 ['Le Nord','À Hanoï, découvrez le pho, son bouillon et ses nouilles, ou le bun cha avec porc grillé et sauce. Les recettes varient. Le café aux œufs peut contenir œuf et lait : vérifiez les ingrédients en cas d’allergie. Consultez menu et prix avant de commander.'],
 ['Le Centre','Le mi Quang est associé à Quang Nam, avec nouilles, herbes, garniture et peu de bouillon. À Hoi An, explorez le cao lau. Les garnitures et sauces du banh mi varient aussi : renseignez-vous sur portions et ingrédients plutôt que sur les seules photos.'],
 ['Le Sud et les besoins alimentaires','À Ho Chi Minh-Ville, découvrez hu tieu ou banh xeo. Commandez progressivement à plusieurs. Les végétariens doivent demander la composition du bouillon et la présence de sauce de poisson ; vérifiez allergènes et ustensiles partagés. Choisissez préparation propre, prix clairs et eau adaptée.']]],
 ['La côte du Centre : My Khe, Non Nuoc et Hoi An','Associez promenades, culture et repos sans remplir toutes les heures.',[
 ['Matin à My Khe','Marchez avant la forte chaleur et surveillez vos affaires. Baignez-vous seulement dans les zones autorisées, selon drapeaux, sauveteurs et conditions du jour. Une belle photo ne garantit pas la sécurité de la baignade.'],
 ['Non Nuoc et montagnes de Marbre','Combinez la côte avec une visite des grottes et temples. Escaliers et sols irréguliers demandent une mobilité adaptée ; vérifiez l’accès. Portez des chaussures pratiques et une tenue respectueuse. Il s’agit d’une idée de parcours, pas d’un circuit garanti.'],
 ['Hoi An et activités sur l’eau','Réservez du temps aux rues historiques et au fleuve. Pour un bateau ou bateau-panier, confirmez lieu, opérateur, gilets, capacité et annulation météo. Le billet de la vieille ville ne couvre pas automatiquement toutes les activités. Convenez du prix et du retour, avec un plan flexible en cas de pluie.']]],
 ['Hanoï et Ho Chi Minh-Ville à pied : deux parcours distincts','Les villes sont dans des régions différentes : ce ne sont pas deux visites à faire dans la même journée.',[
 ['Hanoï','Partez du lac Hoan Kiem et choisissez quelques rues du vieux quartier. Pour le temple Ngoc Son, vérifiez accès et tenue. Gardez un parcours court avec pauses par chaleur ou pluie ; trottoirs et circulation modifient les temps de marche.'],
 ['Ho Chi Minh-Ville','Explorez la Poste centrale et la rue des livres Nguyen Van Binh, puis prévoyez une visite distincte au palais de l’Indépendance. Vérifiez horaires, billets et règles : entretien ou événements peuvent limiter l’accès.'],
 ['Repas et pauses','Choisissez selon menu, prix et besoins alimentaires, sans promesse infondée de « meilleur ». Alternez marche et pauses à l’ombre ou à l’intérieur. Utilisez un transport autorisé pour les longues distances et gardez carte et adresse hors ligne.']]],
],
'de':[
 ['Was in Vietnam essen? Ein regionaler Überblick','Regionale Gerichte entdecken statt ungeprüften Restaurant-Ranglisten folgen.',[
 ['Der Norden','In Hanoi Pho mit Brühe und Reisnudeln oder Bun Cha mit gegrilltem Schweinefleisch probieren. Rezepte unterscheiden sich. Eierkaffee kann Ei und Milch enthalten; bei Allergien nachfragen. Speisekarte und Preise vor Bestellung lesen.'],
 ['Zentralvietnam','Mi Quang gehört zu Quang Nam und verbindet Nudeln, Kräuter, Einlagen und wenig Brühe. In Hoi An Cao Lau kennenlernen. Auch Banh-Mi-Füllungen und Saucen variieren: Portionsgrößen und Zutaten erfragen, nicht nur Fotos ansehen.'],
 ['Der Süden und Ernährungswünsche','In Ho-Chi-Minh-Stadt Hu Tieu oder Banh Xeo entdecken. Zum Teilen schrittweise bestellen. Vegetarier sollten Brühe und Fischsauce klären; Allergene und gemeinsame Geräte erfragen. Saubere Zubereitung, klare Preise und geeignetes Trinkwasser wählen.']]],
 ['Zentralvietnams Küste: My Khe, Non Nuoc und Hoi An','Strandspaziergänge, Kultur und Erholung ohne einen übervollen Plan verbinden.',[
 ['Morgens in My Khe','Vor der stärksten Hitze spazieren und Sachen beaufsichtigen. Nur in erlaubten Bereichen schwimmen und Flaggen, Rettungspersonal und aktuelle Bedingungen beachten. Ein schönes Foto garantiert kein sicheres Baden.'],
 ['Non Nuoc und Marmorberge','Küste mit Höhlen und Tempeln verbinden. Treppen und unebener Boden verlangen geeignete Beweglichkeit; Zugang prüfen. Passende Schuhe und respektvolle Kleidung tragen. Das ist ein Planungsvorschlag, keine garantierte Tour.'],
 ['Hoi An auf dem Wasser','Zeit für Altstadt und Ufer lassen. Bei Boots- oder Korbbootfahrten Ort, Betreiber, Schwimmwesten, Kapazität und Wetterstornierung bestätigen. Altstadttickets umfassen nicht automatisch jede Aktivität. Preis und Rückkehr vereinbaren und bei Starkregen flexibel bleiben.']]],
 ['Hanoi und Ho-Chi-Minh-Stadt zu Fuß: zwei eigene Routen','Die Städte liegen in verschiedenen Regionen, nicht in einer gemeinsamen Tagesroute.',[
 ['Hanoi','Am Hoan-Kiem-See beginnen und nahe Altstadtstraßen wählen. Für den Ngoc-Son-Tempel Zugang und Kleidung prüfen. Kurze Route mit Pausen bei Hitze oder Regen wählen; Gehwege und Verkehr beeinflussen die Dauer.'],
 ['Ho-Chi-Minh-Stadt','Hauptpost und Nguyen-Van-Binh-Buchstraße erkunden, den Wiedervereinigungspalast separat einplanen. Öffnungszeiten, Eintritt und Regeln prüfen; Wartung oder Veranstaltungen können Zugang begrenzen.'],
 ['Essen und Pausen','Nach Speisekarte, Preisen und Ernährungsbedarf wählen, nicht nach unbelegten „Besten“-Versprechen. Gehstrecken mit Schatten oder Innenräumen abwechseln. Für weite Wege zugelassene Verkehrsmittel nutzen und Karte sowie Unterkunftsadresse offline speichern.']]],
],
'es':[
 ['Qué comer en Vietnam: guía por regiones','Descubre platos regionales en lugar de clasificaciones de restaurantes sin verificar.',[
 ['El norte','En Hanói descubre pho con caldo y fideos o bun cha con cerdo a la parrilla y salsa. Las recetas varían. El café con huevo puede incluir huevo y leche: pregunta si tienes alergias. Mira menú y precios antes de pedir.'],
 ['El centro','Mi Quang se asocia a Quang Nam y mezcla fideos, hierbas, proteína y poco caldo. En Hoi An descubre cao lau. Los rellenos y salsas del banh mi también cambian: pregunta por raciones e ingredientes, no elijas solo por fotos.'],
 ['El sur y necesidades alimentarias','En Ho Chi Minh descubre hu tieu o banh xeo. Si compartes, pide poco y añade después. Los vegetarianos deben preguntar por caldo y salsa de pescado; confirma alérgenos y utensilios compartidos. Busca preparación limpia, precios claros y agua adecuada.']]],
 ['Costa del centro: My Khe, Non Nuoc y Hoi An','Combina paseos, cultura y descanso sin llenar cada hora.',[
 ['Mañana en My Khe','Camina antes del calor fuerte y vigila tus objetos. Nada solo donde esté permitido y sigue banderas, socorristas y condiciones actuales. Una foto bonita no confirma que hoy sea seguro bañarse.'],
 ['Non Nuoc y Montañas de Mármol','Combina costa con cuevas y templos. Escaleras y terreno irregular requieren movilidad adecuada: consulta accesibilidad. Usa calzado práctico y ropa respetuosa. Es una sugerencia de planificación, no una excursión garantizada.'],
 ['Hoi An y el agua','Deja tiempo para calles históricas y el río. Para barcas o barcos-cesta, confirma lugar, operador, chalecos, capacidad y cancelación por clima. La entrada del casco antiguo no incluye automáticamente todas las actividades. Acuerda precio y regreso y mantén flexibilidad si llueve mucho.']]],
 ['Hanói y Ho Chi Minh a pie: dos rutas independientes','Están en regiones diferentes y no forman una visita de un solo día.',[
 ['Hanói','Empieza en el lago Hoan Kiem y elige calles cercanas del casco antiguo. Revisa acceso y vestimenta para Ngoc Son. Mantén el recorrido corto con pausas por calor o lluvia; aceras y tráfico cambian los tiempos.'],
 ['Ho Chi Minh','Explora Correos Central y la calle de libros Nguyen Van Binh, y dedica otra visita al Palacio de la Independencia. Comprueba horarios, entradas y normas; mantenimiento o eventos pueden limitar el acceso.'],
 ['Comidas y pausas','Elige según menú, precios y necesidades, no por promesas infundadas de “mejor”. Alterna caminatas con sombra o interiores. Usa transporte autorizado para distancias largas y guarda mapa y dirección del alojamiento sin conexión.']]],
],
'th':[
 ['กินอะไรในเวียดนาม: อาหารแต่ละภูมิภาค','รู้จักเมืองผ่านอาหารท้องถิ่น แทนการใช้อันดับร้านที่ยังไม่ตรวจสอบ',[
 ['ภาคเหนือ','ฮานอยมีเฝอที่ประกอบด้วยน้ำซุป เส้น และเนื้อ หรือบุนจ๋าที่มีหมูย่างกับน้ำจิ้ม สูตรต่างกันตามร้าน กาแฟไข่อาจมีไข่และนม ผู้แพ้ควรถามส่วนผสม ดูเมนูและราคาก่อนสั่ง'],
 ['ภาคกลาง','หมี่กว๋างเกี่ยวข้องกับกว๋างนาม มีเส้น ผัก เนื้อหรือโปรตีนและน้ำซุปไม่มาก ฮอยอันมีเกาเหลา ส่วนไส้และซอสบั๋นหมี่ต่างกัน ควรถามปริมาณและส่วนผสม ไม่เลือกจากภาพอย่างเดียว'],
 ['ภาคใต้และความต้องการอาหาร','โฮจิมินห์มีหูเตี๋ยวหรือบั๋นแส่ว เมื่อกินร่วมกันให้สั่งทีละน้อย ผู้กินมังสวิรัติต้องถามน้ำซุปและน้ำปลา ผู้แพ้ควรตรวจสอบส่วนผสมและอุปกรณ์ใช้ร่วม เลือกร้านสะอาด ราคาชัด และน้ำดื่มเหมาะสม']]],
 ['ประสบการณ์ชายฝั่งภาคกลาง: หมีเค นอนเนือก และฮอยอัน','รวมการเดินเล่น วัฒนธรรม และพักผ่อน โดยไม่ต้องจัดทัวร์ทุกชั่วโมง',[
 ['เช้าที่หมีเค','เดินก่อนอากาศร้อนจัดและดูแลสิ่งของ ลงน้ำเฉพาะพื้นที่อนุญาตและทำตามธง เจ้าหน้าที่ และสภาพทะเลขณะนั้น ภาพชายหาดสวยไม่ได้รับรองว่าวันนี้ว่ายน้ำปลอดภัย'],
 ['นอนเนือกและภูเขาหินอ่อน','ผสมเวลาชายฝั่งกับชมถ้ำและวัด บันไดและพื้นไม่เรียบต้องอาศัยความคล่องตัว ควรตรวจสอบทางเข้าถึง ใส่รองเท้าเหมาะสมและแต่งกายสุภาพ นี่เป็นข้อเสนอวางแผน ไม่ใช่ทัวร์ที่รับประกัน'],
 ['ฮอยอันและกิจกรรมทางน้ำ','เผื่อเวลาถนนเก่าและริมแม่น้ำ หากนั่งเรือหรือเรือตะกร้าให้ถามสถานที่ ผู้ให้บริการ เสื้อชูชีพ จำนวนคนและการยกเลิกเพราะอากาศ ตั๋วเมืองเก่าไม่ได้รวมทุกกิจกรรม ตกลงราคาและเวลาเดินทางกลับก่อน และยืดหยุ่นเมื่อฝนหนัก']]],
 ['เดินเที่ยวฮานอยและโฮจิมินห์: สองเส้นทางแยกกัน','เมืองอยู่คนละภูมิภาค ไม่ใช่เส้นทางสองเมืองในวันเดียว',[
 ['ฮานอย','เริ่มที่ทะเลสาบฮว่านเกี๊ยมแล้วเลือกถนนใกล้ย่านเมืองเก่า วัดหง็อกเซินควรตรวจสอบการเข้าชมและการแต่งกาย เลือกเส้นทางสั้นและพักเมื่อร้อนหรือฝน ทางเท้าและการจราจรมีผลต่อเวลา'],
 ['โฮจิมินห์','เที่ยวแถวไปรษณีย์กลางและถนนหนังสือเหงียนวันบิญ แล้วจัดเวลาอีกส่วนให้ทำเนียบอิสรภาพ ตรวจสอบเวลา ตั๋วและกฎ การซ่อมหรือกิจกรรมอาจจำกัดการเข้าชม'],
 ['อาหารและจุดพัก','เลือกจากเมนู ราคาและความต้องการ ไม่ใช่คำกล่าวว่าอร่อยที่สุดโดยไม่มีหลักฐาน สลับเดินกับพักในร่ม ใช้ขนส่งถูกกฎหมายเมื่อไกล และบันทึกแผนที่กับที่อยู่ที่พักออฟไลน์']]],
],
'id':[
 ['Makan apa di Vietnam: panduan regional','Kenali wilayah lewat makanan, bukan daftar restoran terbaik yang belum diverifikasi.',[
 ['Utara','Di Hanoi, kenali pho dengan kaldu dan mi beras atau bun cha dengan babi panggang serta saus. Resep berbeda antarkedai. Kopi telur dapat mengandung telur dan susu: tanyakan bahan jika alergi. Baca menu serta harga sebelum memesan.'],
 ['Tengah','Mi Quang terkait Quang Nam, dengan mi, herba, lauk dan sedikit kuah. Di Hoi An, kenali cao lau. Isian serta saus banh mi juga beragam: tanyakan porsi dan bahan, jangan hanya memilih dari foto.'],
 ['Selatan dan kebutuhan makanan','Di Ho Chi Minh City, kenali hu tieu atau banh xeo. Pesan bertahap saat berbagi. Vegetarian perlu menanyakan kaldu dan saus ikan; pastikan alergen serta alat bersama. Pilih tempat bersih, harga jelas dan air minum sesuai.']]],
 ['Pengalaman pesisir tengah: My Khe, Non Nuoc dan Hoi An','Gabungkan jalan pantai, budaya dan istirahat tanpa mengisi setiap jam.',[
 ['Pagi di My Khe','Berjalan sebelum panas terik dan awasi barang. Berenang hanya di area yang diizinkan sesuai bendera, penjaga dan kondisi saat itu. Foto indah tidak menjamin laut aman untuk berenang hari ini.'],
 ['Non Nuoc dan Marble Mountains','Gabungkan pesisir dengan gua dan kuil. Tangga serta tanah tidak rata memerlukan mobilitas sesuai; periksa akses. Gunakan sepatu praktis dan pakaian sopan. Ini saran rencana, bukan tur terjamin.'],
 ['Hoi An dan kegiatan air','Sisakan waktu untuk jalan bersejarah dan sungai. Untuk perahu atau perahu keranjang, pastikan lokasi, operator, pelampung, kapasitas dan pembatalan cuaca. Tiket kota tua tidak otomatis mencakup semua kegiatan. Sepakati harga serta waktu kembali dan fleksibel saat hujan lebat.']]],
 ['Berjalan di Hanoi dan Ho Chi Minh City: dua rute terpisah','Kota berada di wilayah berbeda, bukan kunjungan dua kota dalam sehari.',[
 ['Hanoi','Mulai di Danau Hoan Kiem dan pilih jalan sekitar kota tua. Periksa akses serta pakaian untuk Kuil Ngoc Son. Buat rute singkat dengan jeda saat panas atau hujan; trotoar dan lalu lintas memengaruhi waktu.'],
 ['Ho Chi Minh City','Jelajahi Kantor Pos Pusat dan Jalan Buku Nguyen Van Binh, lalu sisihkan kunjungan lain untuk Istana Kemerdekaan. Periksa jam, tiket dan aturan; perawatan atau acara bisa membatasi akses.'],
 ['Makan dan beristirahat','Pilih berdasarkan menu, harga dan kebutuhan, bukan klaim terbaik tanpa dasar. Selang-selingkan berjalan dan tempat teduh atau dalam ruangan. Gunakan transportasi berizin untuk jarak jauh dan simpan peta serta alamat secara luring.']]],
],
'ru':[
 ['Что попробовать во Вьетнаме: кухня по регионам','Знакомьтесь с местами через блюда, а не через непроверенные рейтинги ресторанов.',[
 ['Север','В Ханое познакомьтесь с фо — бульоном и рисовой лапшой — или бунча со свининой на гриле и соусом. Рецепты различаются. Яичный кофе может содержать яйцо и молоко: уточняйте состав при аллергии. До заказа посмотрите меню и цены.'],
 ['Центр','Микуанг связан с Куангнамом: лапша, зелень, начинка и немного бульона. В Хойане попробуйте узнать о каолау. Начинки и соусы баньми различаются; спросите состав и размер порции, не выбирайте только по фото.'],
 ['Юг и питание','В Хошимине познакомьтесь с хутиеу или баньсео. Заказывайте постепенно при совместной трапезе. Вегетарианцам нужно уточнять бульон и рыбный соус; при аллергии — ингредиенты и общие приборы. Выбирайте чистое приготовление, понятные цены и подходящую питьевую воду.']]],
 ['Побережье Центрального Вьетнама: Микхе, Нонныок и Хойан','Сочетайте прогулки, культуру и отдых, не заполняя экскурсиями каждый час.',[
 ['Утро на Микхе','Гуляйте до сильной жары и следите за вещами. Купайтесь только в разрешённых местах по флагам, указаниям спасателей и текущим условиям. Красивый снимок не гарантирует безопасное купание сегодня.'],
 ['Нонныок и Мраморные горы','Совместите побережье с пещерами и храмами. Ступени и неровные дорожки требуют подходящей подвижности; проверьте доступность. Наденьте удобную обувь и уместную одежду. Это предложение для планирования, не гарантированный тур.'],
 ['Хойан и вода','Оставьте время для исторических улиц и реки. Для лодок или круглых лодок уточните место, оператора, жилеты, вместимость и отмену из-за погоды. Билет старого города не включает автоматически все развлечения. Согласуйте цену и возвращение, сохраняйте гибкость при сильном дожде.']]],
 ['Ханой и Хошимин пешком: два отдельных маршрута','Города в разных регионах: это не поездка по двум городам за один день.',[
 ['Ханой','Начните у озера Хоанкием и выберите близкие улицы старого квартала. Для храма Нгокшон проверьте доступ и одежду. Делайте короткие маршруты с паузами при жаре или дожде; тротуары и движение влияют на время.'],
 ['Хошимин','Посетите район Центральной почты и книжную улицу Нгуенванбинь, затем отдельно запланируйте Дворец независимости. Уточняйте часы, билеты и правила: ремонт или мероприятия могут ограничить посещение.'],
 ['Еда и остановки','Выбирайте по меню, ценам и потребностям, а не по необоснованным обещаниям «лучшего». Чередуйте прогулки с тенью или помещениями. Для дальних расстояний пользуйтесь законным транспортом и сохраняйте карту с адресом офлайн.']]],
],
'ko':[
 ['베트남에서 무엇을 먹을까: 지역별 음식 안내','검증되지 않은 맛집 순위보다 지역 음식으로 여행지를 알아보세요.',[
 ['북부','하노이에서 국물과 쌀국수로 만드는 포, 구운 돼지고기와 소스가 있는 분짜를 알아보세요. 조리법은 가게마다 다릅니다. 에그커피는 달걀과 우유를 포함할 수 있어 알레르기가 있으면 확인하세요. 주문 전 메뉴와 가격을 보세요.'],
 ['중부','미꽝은 꽝남과 관련된 면, 허브, 고명과 적은 국물의 음식입니다. 호이안에서는 까오러우를 알아보세요. 반미의 속과 소스도 다르므로 사진만 보지 말고 양과 재료를 물어보세요.'],
 ['남부와 식단','호찌민에서는 후띠에우나 반쎄오를 알아보세요. 나눠 먹을 때 조금씩 주문하세요. 채식인은 육수와 생선 소스를, 알레르기가 있으면 재료와 공용 기구를 확인해야 합니다. 청결한 조리, 명확한 가격과 적절한 음료를 선택하세요.']]],
 ['중부 해안 체험: 미케, 논느억, 호이안','모든 시간을 투어로 채우지 않고 산책, 문화와 휴식을 조합하세요.',[
 ['미케의 아침','강한 더위 전 산책하고 소지품을 지키세요. 허용된 곳에서만 수영하며 깃발, 구조요원과 당일 상황을 따르세요. 아름다운 사진이 오늘의 안전한 수영을 보장하지 않습니다.'],
 ['논느억과 오행산','해안과 동굴, 사원을 함께 계획하세요. 계단과 고르지 않은 길은 이동 능력이 필요하므로 접근성을 확인하세요. 편한 신발과 적절한 복장을 준비하세요. 이 글은 계획 제안이며 보장된 투어가 아닙니다.'],
 ['호이안과 수상 활동','옛 거리와 강변에 시간을 남기세요. 배나 바구니배 체험은 장소, 업체, 구명조끼, 정원과 날씨 취소를 확인하세요. 고도시 입장권에 모든 활동이 자동 포함되지는 않습니다. 가격과 돌아올 시간을 합의하고 폭우 때는 유연하게 조정하세요.']]],
 ['하노이와 호찌민 도보 여행: 두 개의 독립 코스','두 도시는 다른 지역에 있어 하루에 연결하는 코스가 아닙니다.',[
 ['하노이','호안끼엠 호수에서 시작해 가까운 구시가지 거리를 고르세요. 응옥썬 사당은 입장과 복장을 확인하세요. 더위나 비에 쉬며 짧게 계획하세요. 보도와 교통이 소요 시간에 영향을 줍니다.'],
 ['호찌민','중앙우체국 주변과 응우옌반빈 책거리를 둘러보고 통일궁은 별도 시간을 배정하세요. 운영 시간, 티켓과 규칙을 확인하세요. 보수나 행사가 입장을 제한할 수 있습니다.'],
 ['식사와 휴식','근거 없는 최고라는 주장보다 메뉴, 가격과 식단으로 고르세요. 걷기와 그늘 또는 실내 휴식을 번갈아 하세요. 먼 곳은 합법 교통을 이용하고 오프라인 지도와 숙소 주소를 저장하세요.']]],
],
'ja':[
 ['ベトナムで何を食べる？地域別のグルメ案内','未確認の店の順位ではなく、地域の料理から旅先を知りましょう。',[
 ['北部','ハノイではスープと米麺のフォー、焼き豚とたれのブンチャーを知ることができます。作り方は店ごとに違います。エッグコーヒーには卵や乳が含まれる場合があるので、アレルギーがあれば確認しましょう。注文前にメニューと料金を見てください。'],
 ['中部','ミークアンはクアンナムと関わる麺、香草、具材と少量の汁の料理です。ホイアンではカオラウを調べてみましょう。バインミーの具やソースも異なるため、写真だけでなく量と材料を聞いてください。'],
 ['南部と食事の希望','ホーチミン市ではフーティウやバインセオを知ることができます。シェアするときは少しずつ注文しましょう。菜食ならスープと魚醤、アレルギーなら材料と共用器具を確認してください。清潔な調理、明確な価格、適切な飲料水を選びましょう。']]],
 ['中部の海岸体験：ミーケー、ノンヌオック、ホイアン','毎時間ツアーを入れず、散歩、文化、休息を組み合わせましょう。',[
 ['ミーケーの朝','強い暑さの前に歩き、持ち物を見守ってください。許可区域だけで泳ぎ、旗、救助員、当日の状況に従いましょう。美しい写真は今日の遊泳の安全を保証しません。'],
 ['ノンヌオックと五行山','海岸と洞窟、寺院を組み合わせます。階段と不整地には歩行能力が必要なのでアクセスを確認してください。適切な靴と服装を選びましょう。計画の提案であり、保証されたツアーではありません。'],
 ['ホイアンと水上活動','古い街路と川沿いに時間を残しましょう。船やかご舟は場所、事業者、救命胴衣、定員、悪天候の取消条件を確認してください。古い町の入場券が全活動を含むとは限りません。料金と帰着時刻を決め、豪雨では柔軟に変更しましょう。']]],
 ['ハノイとホーチミン市を歩く：別々の二つのルート','両市は別地域にあり、一日で回る連続ルートではありません。',[
 ['ハノイ','ホアンキエム湖から近隣の旧市街を選びましょう。玉山祠の入場と服装を確認し、暑さや雨では休憩を入れて短いルートにします。歩道と交通で時間が変わります。'],
 ['ホーチミン市','中央郵便局周辺とグエンバンビンの本の通りを訪れ、統一会堂は別に時間を取りましょう。営業時間、券、規則を確認してください。修理や行事で入場が限られる場合があります。'],
 ['食事と休憩','根拠のない最高という宣伝よりメニュー、価格、食事の希望で選びましょう。歩行と日陰や屋内の休憩を交互にし、遠距離は適法な交通を利用してください。地図と宿の住所はオフラインで保存しましょう。']]],
],
'hi':[
 ['वियतनाम में क्या खाएँ: क्षेत्रीय भोजन गाइड','बिना जाँची सर्वश्रेष्ठ रेस्तरां सूची के बजाय क्षेत्रीय भोजन से जगह को जानें।',[
 ['उत्तर','हनोई में शोरबा और चावल नूडल्स वाला फो या ग्रिल्ड पोर्क और सॉस वाला बुन चा जानें। हर दुकान की विधि अलग है। एग कॉफी में अंडा और दूध हो सकता है; एलर्जी हो तो पूछें। ऑर्डर से पहले मेनू और कीमत देखें।'],
 ['मध्य क्षेत्र','मी क्वांग क्वांग नाम से जुड़ा नूडल्स, जड़ी-बूटी, टॉपिंग और थोड़े शोरबे वाला भोजन है। होई आन में काओ लाउ जानें। बान्ह मी की भराई और सॉस भी बदलती है; फोटो के अलावा मात्रा और सामग्री पूछें।'],
 ['दक्षिण और भोजन जरूरतें','हो ची मिन्ह सिटी में हू तिएउ या बान्ह सेओ जानें। साझा भोजन में थोड़ा-थोड़ा ऑर्डर करें। शाकाहारी लोग शोरबा और फिश सॉस, एलर्जी वाले सामग्री और साझा उपकरण पूछें। साफ तैयारी, स्पष्ट कीमत और उचित पीने का पानी चुनें।']]],
 ['मध्य तट के अनुभव: माय खे, नॉन नुओक और होई आन','हर घंटे टूर भरने के बजाय सैर, संस्कृति और आराम मिलाएँ।',[
 ['माय खे की सुबह','तेज गर्मी से पहले चलें और सामान पर नजर रखें। केवल अनुमति क्षेत्र में तैरें तथा झंडे, लाइफगार्ड और मौजूदा हालात मानें। अच्छी तस्वीर आज सुरक्षित तैराकी की गारंटी नहीं है।'],
 ['नॉन नुओक और मार्बल माउंटेन्स','तट को गुफाओं और मंदिरों के साथ जोड़ें। सीढ़ियाँ और असमतल रास्ते उपयुक्त चलने की क्षमता माँगते हैं; पहुँच जाँचें। ठीक जूते और सम्मानजनक कपड़े पहनें। यह योजना सुझाव है, निश्चित टूर नहीं।'],
 ['होई आन और पानी पर गतिविधियाँ','पुरानी गलियों और नदी के लिए समय रखें। नाव या बास्केट बोट में जगह, संचालक, लाइफ जैकेट, क्षमता और मौसम रद्द नीति पूछें। पुराने शहर का टिकट सभी गतिविधियाँ नहीं समेटता। कीमत और वापसी समय तय करें तथा भारी बारिश में बदलाव रखें।']]],
 ['हनोई और हो ची मिन्ह सिटी पैदल: दो अलग मार्ग','दोनों अलग क्षेत्रों में हैं; यह एक दिन में दोनों शहर घूमने का कार्यक्रम नहीं है।',[
 ['हनोई','होआन किएम झील से पास की पुरानी गलियाँ चुनें। न्गोक सोन मंदिर का प्रवेश और पहनावा जाँचें। गर्मी या बारिश में विराम के साथ छोटी राह रखें; फुटपाथ और यातायात समय बदलते हैं।'],
 ['हो ची मिन्ह सिटी','केंद्रीय डाकघर और न्गुएन वान बिन्ह बुक स्ट्रीट देखें, स्वतंत्रता महल को अलग समय दें। समय, टिकट और नियम जाँचें; मरम्मत या कार्यक्रम से प्रवेश सीमित हो सकता है।'],
 ['खाना और विराम','बिना आधार के सर्वश्रेष्ठ दावे के बजाय मेनू, कीमत और जरूरत से चुनें। चलने के बीच छाँव या अंदर आराम करें। लंबी दूरी पर वैध परिवहन लें और ऑफलाइन नक्शा तथा ठहरने का पता रखें।']]],
],
}

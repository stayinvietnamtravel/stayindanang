"""Attributed weather and practical, interactive ideas for the landing pages."""
from pathlib import Path
from datetime import datetime, timedelta, timezone
from html import escape as E
import json
from urllib.parse import quote
from destinations import CITIES, DESTINATIONS
from world_weather import CITIES as WORLD_CITIES, TIMEZONES
from world_destinations import COUNTRIES, city_name, REGIONS
from zoneinfo import ZoneInfo
from world_guides import COPY as WORLD_GUIDE_COPY
from travel_portal import display_time

ROOT=Path(__file__).resolve().parents[1]
# weather title, lead, missing data, source update label, rainfall, wind,
# ideas title, lead, 1/3/5-day labels, three plans, rainy toggle/body,
# checklist title, three checklist items, reset, read-guide label.
COPY={
'vi':['Dự báo thời tiết Đà Nẵng','Các mốc dự báo trong 24 giờ tới, không phải số đo quan trắc trực tiếp.','Chưa có dữ liệu dự báo mới. Bạn có thể xem Đà Nẵng trên Yr.','Mô hình cập nhật','Mưa','Gió','Ý tưởng cho chuyến đi của bạn','Chọn thời gian bạn có, rồi điều chỉnh theo thời tiết và nhịp đi của mình.','1 ngày','3 ngày','5 ngày','Một ngày ở Đà Nẵng: dành buổi sáng cho Mỹ Khê nếu điều kiện phù hợp, nghỉ ăn trưa và đi dạo khu vực sông Hàn.','Ba ngày: khám phá Đà Nẵng, dành ngày riêng cho Hội An, rồi chọn Ngũ Hành Sơn hoặc một ngày nghỉ. Chừa thời gian cho di chuyển.','Năm ngày: mở rộng hành trình với Huế hoặc Bà Nà Hills, thay vì cố ghé mọi nơi. Cân nhắc ngủ lại Huế để giảm việc đi về trong ngày.','Ý tưởng cho ngày mưa','Ưu tiên bữa ăn địa phương, quán cà phê hoặc Bảo tàng Điêu khắc Chăm. Kiểm tra giờ mở cửa và đường đi; điều chỉnh các hoạt động biển, thuyền và núi theo hướng dẫn địa phương.','Checklist trước chuyến đi','Kiểm tra giấy tờ và ngày bay','Xác nhận phòng, số khách và điều kiện hủy','Sắp xếp xe sân bay và bản đồ ngoại tuyến','Đặt lại checklist','Đọc hướng dẫn →'],
'en':['Da Nang weather forecast','Forecast points for the next 24 hours, not live measured observations.','No recent forecast is available yet. You can check Da Nang on Yr.','Model updated','Rain','Wind','Ideas for your trip','Choose how much time you have, then adjust for the weather and your own pace.','1 day','3 days','5 days','One day in Da Nang: allow a morning at My Khe if conditions permit, a lunch break and a walk by the Han River.','Three days: explore Da Nang, give Hoi An its own day, then choose the Marble Mountains or a rest day. Allow transfer time.','Five days: extend with Hue or Ba Na Hills rather than trying every stop. Consider staying overnight in Hue to reduce same-day travel.','Rainy-day ideas','Consider local food, a café or the Museum of Cham Sculpture. Check hours and access; adjust sea, boat and mountain activities to local guidance.','Before-you-go checklist','Check travel documents and flight dates','Confirm room, guests and cancellation terms','Arrange airport transport and an offline map','Reset checklist','Read guide →'],
'fr':['Météo prévue à Da Nang','Prévisions des prochaines 24 heures, pas des mesures en direct.','Aucune prévision récente disponible. Consultez Da Nang sur Yr.','Modèle mis à jour','Pluie','Vent','Idées pour votre voyage','Choisissez votre durée puis adaptez à la météo et à votre rythme.','1 jour','3 jours','5 jours','Une journée à Da Nang : My Khe le matin si les conditions le permettent, pause déjeuner et promenade près de la rivière Han.','Trois jours : Da Nang, une journée à Hoi An, puis montagnes de Marbre ou repos. Prévoyez les transferts.','Cinq jours : ajoutez Hué ou Ba Na Hills sans vouloir tout visiter. Une nuit à Hué réduit les allers-retours.','Idées par temps de pluie','Cuisine locale, café ou musée de la sculpture cham. Vérifiez horaires et accès ; adaptez mer, bateaux et montagne aux consignes locales.','Liste avant le départ','Vérifier documents et dates de vol','Confirmer chambre, voyageurs et annulation','Préparer transport aéroport et carte hors ligne','Réinitialiser','Lire le guide →'],
'de':['Wettervorhersage für Da Nang','Vorhersagepunkte für 24 Stunden, keine aktuellen Messungen.','Noch keine aktuelle Vorhersage. Da Nang auf Yr ansehen.','Modell aktualisiert','Regen','Wind','Ideen für Ihre Reise','Dauer auswählen und an Wetter sowie eigenes Tempo anpassen.','1 Tag','3 Tage','5 Tage','Ein Tag: morgens My Khe bei passenden Bedingungen, Mittagspause und Spaziergang am Han-Fluss.','Drei Tage: Da Nang, ein eigener Tag in Hoi An, dann Marmorberge oder Ruhe. Fahrzeit einplanen.','Fünf Tage: Hue oder Ba Na Hills ergänzen statt alles zu besuchen. Eine Nacht in Hue spart Hin- und Rückfahrten.','Ideen bei Regen','Lokales Essen, Café oder Museum für Cham-Skulpturen. Zeiten und Zugang prüfen; Meer, Boot und Berge nach örtlichen Hinweisen planen.','Checkliste vor der Reise','Dokumente und Flugdaten prüfen','Zimmer, Gästezahl und Stornierung bestätigen','Flughafentransfer und Offline-Karte vorbereiten','Zurücksetzen','Ratgeber lesen →'],
'es':['Previsión del tiempo en Da Nang','Previsiones de las próximas 24 horas, no mediciones en directo.','Todavía no hay previsión reciente. Consulta Da Nang en Yr.','Modelo actualizado','Lluvia','Viento','Ideas para tu viaje','Elige tu duración y adapta el plan al clima y a tu ritmo.','1 día','3 días','5 días','Un día: My Khe por la mañana si las condiciones lo permiten, almuerzo y paseo por el río Han.','Tres días: Da Nang, un día para Hoi An y luego Montañas de Mármol o descanso. Deja tiempo para traslados.','Cinco días: añade Hue o Ba Na Hills sin intentar verlo todo. Dormir en Hue reduce viajes de ida y vuelta.','Ideas para días lluviosos','Comida local, café o Museo de Escultura Cham. Confirma horarios y acceso; adapta playa, barcas y montaña a indicaciones locales.','Lista antes del viaje','Comprobar documentos y fechas de vuelos','Confirmar habitación, viajeros y cancelación','Preparar transporte al aeropuerto y mapa sin conexión','Reiniciar lista','Leer guía →'],
'th':['พยากรณ์อากาศดานัง','ข้อมูลพยากรณ์ 24 ชั่วโมงข้างหน้า ไม่ใช่ค่าที่วัดสด','ยังไม่มีพยากรณ์ล่าสุด สามารถดูดานังบน Yr','อัปเดตแบบจำลอง','ฝน','ลม','ไอเดียสำหรับทริป','เลือกเวลาที่มีแล้วปรับตามอากาศและจังหวะของคุณ','1 วัน','3 วัน','5 วัน','หนึ่งวัน: หมีเคช่วงเช้าหากเหมาะสม พักกินกลางวัน แล้วเดินริมแม่น้ำฮาน','สามวัน: เที่ยวดานัง ให้ฮอยอันหนึ่งวัน แล้วเลือกภูเขาหินอ่อนหรือพัก เผื่อเวลาเดินทาง','ห้าวัน: เพิ่มเว้หรือบานาฮิลล์แทนการไปทุกแห่ง การค้างคืนเว้ช่วยลดการไปกลับ','ไอเดียวันฝนตก','เลือกอาหารท้องถิ่น คาเฟ่ หรือพิพิธภัณฑ์ประติมากรรมจาม ตรวจสอบเวลาและทางเข้า ปรับกิจกรรมทะเล เรือและภูเขาตามคำแนะนำท้องถิ่น','รายการก่อนเดินทาง','ตรวจสอบเอกสารและวันบิน','ยืนยันห้อง จำนวนคนและการยกเลิก','จัดรถสนามบินและแผนที่ออฟไลน์','เริ่มรายการใหม่','อ่านคู่มือ →'],
'id':['Prakiraan cuaca Da Nang','Prakiraan 24 jam mendatang, bukan pengukuran langsung.','Belum ada prakiraan terbaru. Lihat Da Nang di Yr.','Model diperbarui','Hujan','Angin','Ide untuk perjalanan','Pilih waktu yang tersedia, lalu sesuaikan cuaca dan ritme Anda.','1 hari','3 hari','5 hari','Satu hari: My Khe pagi bila kondisi memungkinkan, makan siang dan berjalan di Sungai Han.','Tiga hari: Da Nang, satu hari Hoi An, lalu Marble Mountains atau istirahat. Sisakan waktu transfer.','Lima hari: tambahkan Hue atau Ba Na Hills tanpa mencoba semua tempat. Bermalam di Hue mengurangi perjalanan pulang-pergi.','Ide saat hujan','Makanan lokal, kafe atau Museum Patung Cham. Periksa jam dan akses; sesuaikan laut, perahu dan gunung dengan petunjuk setempat.','Daftar sebelum berangkat','Periksa dokumen dan tanggal penerbangan','Konfirmasi kamar, tamu dan pembatalan','Atur transportasi bandara dan peta luring','Atur ulang daftar','Baca panduan →'],
'zh':['岘港天气预报','未来24小时的预报时间点，并非实时观测。','暂无近期预报，可在 Yr 查看岘港。','模型更新','降雨','风速','旅行灵感','选择停留时间，再按天气和自己的节奏调整。','1天','3天','5天','一天：条件允许时早上去美溪，午餐休息后沿韩江散步。','三天：探索岘港，会安单独一天，再選五行山或休息，预留交通时间。','五天：加入顺化或巴拿山，不必走遍全部。顺化过夜可减少往返。','雨天灵感','考虑当地美食、咖啡馆或占婆雕刻博物馆。确认开放时间与通行条件，海滩、乘船和山地活动遵循当地指引。','出发前清单','确认旅行证件及航班日期','确认客房、人数与取消条件','安排机场交通和离线地图','重置清单','阅读指南 →'],
'zh-Hant':['峴港天氣預報','未來24小時的預報時間點，並非即時觀測。','暫無近期預報，可在 Yr 查看峴港。','模型更新','降雨','風速','旅行靈感','選擇停留時間，再依天氣和自己的步調調整。','1天','3天','5天','一天：條件允許時早上去美溪，午餐休息後沿韓江散步。','三天：探索峴港，會安單獨一天，再選五行山或休息，預留交通時間。','五天：加入順化或巴拿山，不必走遍全部。順化過夜可減少往返。','雨天靈感','考慮在地美食、咖啡館或占婆雕刻博物館。確認開放時間及通行條件，海灘、搭船和山地活動遵循當地指引。','出發前清單','確認旅行文件及航班日期','確認客房、人數與取消條件','安排機場交通和離線地圖','重設清單','閱讀指南 →'],
'ru':['Прогноз погоды в Дананге','Прогноз на 24 часа, а не измерения в реальном времени.','Свежего прогноза пока нет. Посмотрите Дананг на Yr.','Модель обновлена','Дождь','Ветер','Идеи для вашей поездки','Выберите длительность и учитывайте погоду и свой темп.','1 день','3 дня','5 дней','Один день: Микхе утром при подходящих условиях, обед и прогулка у реки Хан.','Три дня: Дананг, отдельный день Хойану, затем Мраморные горы или отдых. Учтите переезды.','Пять дней: добавьте Хюэ или Бана-Хиллс, не пытаясь увидеть всё. Ночёвка в Хюэ уменьшает дорогу туда и обратно.','Идеи на дождливый день','Местная еда, кафе или музей Чамской скульптуры. Проверьте часы и доступ; море, лодки и горы планируйте по местным указаниям.','Список перед поездкой','Проверить документы и даты рейсов','Подтвердить номер, гостей и отмену','Организовать трансфер и офлайн-карту','Сбросить список','Читать →'],
'ko':['다낭 날씨 예보','향후 24시간 예보이며 실시간 관측값이 아닙니다.','아직 최근 예보가 없습니다. Yr에서 다낭을 확인하세요.','모델 업데이트','강수','바람','여행 아이디어','머무는 기간을 고르고 날씨와 자신의 속도에 맞춰 조정하세요.','1일','3일','5일','하루: 여건이 맞으면 아침 미케, 점심 휴식과 한강 산책을 계획하세요.','3일: 다낭, 호이안 하루, 오행산 또는 휴식으로 구성하고 이동 시간을 남기세요.','5일: 후에나 바나힐을 추가하되 모두 가려 하지 마세요. 후에 숙박은 왕복 이동을 줄입니다.','비 오는 날 아이디어','현지 음식, 카페 또는 참 조각 박물관을 고려하세요. 운영 시간과 접근을 확인하고 바다, 배와 산 활동은 현지 안내에 따르세요.','출발 전 체크리스트','서류와 항공 날짜 확인','객실, 인원과 취소 조건 확인','공항 교통과 오프라인 지도 준비','체크리스트 초기화','가이드 읽기 →'],
'ja':['ダナンの天気予報','今後24時間の予報であり、リアルタイム観測ではありません。','最新の予報はまだありません。Yrでダナンを確認できます。','モデル更新','降水','風','旅行のアイデア','滞在日数を選び、天候と自分のペースに合わせましょう。','1日','3日','5日','1日：条件がよければ朝のミーケー、昼食と休憩、ハン川沿いの散歩。','3日：ダナン、ホイアンに一日、五行山または休息。移動時間を残しましょう。','5日：フエかバーナーヒルズを追加し、全部を回ろうとしない計画に。フエ泊は往復移動を減らします。','雨の日のアイデア','地元料理、カフェ、チャム彫刻博物館を検討しましょう。時間とアクセスを確認し、海、船、山の活動は現地案内に従ってください。','出発前チェックリスト','書類とフライト日程を確認','客室、人数、取消条件を確認','空港交通とオフライン地図を準備','リセット','ガイドを読む →'],
'hi':['दा नांग मौसम पूर्वानुमान','अगले 24 घंटे का पूर्वानुमान, प्रत्यक्ष लाइव माप नहीं।','अभी नया पूर्वानुमान उपलब्ध नहीं है। Yr पर दा नांग देखें।','मॉडल अपडेट','बारिश','हवा','यात्रा के नए विचार','अपने दिनों को चुनें और मौसम तथा अपनी गति के अनुसार बदलें।','1 दिन','3 दिन','5 दिन','एक दिन: परिस्थितियाँ ठीक हों तो सुबह माय खे, दोपहर भोजन और हान नदी की सैर।','तीन दिन: दा नांग, होई आन का अलग दिन, फिर मार्बल माउंटेन्स या आराम। परिवहन का समय रखें।','पाँच दिन: हुए या बा ना हिल्स जोड़ें, हर जगह जाने की कोशिश न करें। हुए में रात रुकना आने-जाने को कम करता है।','बारिश के दिन विचार','स्थानीय भोजन, कैफे या चाम मूर्तिकला संग्रहालय चुनें। समय और पहुँच जाँचें; समुद्र, नाव और पहाड़ के लिए स्थानीय निर्देश मानें।','यात्रा से पहले सूची','दस्तावेज़ और उड़ान तारीख जाँचें','कमरा, अतिथि और रद्द नीति की पुष्टि','हवाई अड्डे का परिवहन और ऑफलाइन नक्शा तैयार','सूची रीसेट','गाइड पढ़ें →'],
}
CONDITIONS={
'vi':['Trời quang','Ít mây','Nhiều mây','Mưa','Mưa rào','Dông','Tuyết','Sương mù','Chưa rõ'],
'en':['Clear','Partly cloudy','Cloudy','Rain','Showers','Thunder','Snow','Fog','Unknown'],
'fr':['Ciel clair','Peu nuageux','Nuageux','Pluie','Averses','Orage','Neige','Brouillard','Inconnu'],
'de':['Klar','Teilweise bewölkt','Bewölkt','Regen','Schauer','Gewitter','Schnee','Nebel','Unbekannt'],
'es':['Despejado','Parcialmente nublado','Nublado','Lluvia','Chubascos','Tormenta','Nieve','Niebla','Sin datos'],
'th':['ฟ้าโปร่ง','เมฆบางส่วน','เมฆมาก','ฝน','ฝนซู่','พายุฝนฟ้าคะนอง','หิมะ','หมอก','ไม่ทราบ'],
'id':['Cerah','Berawan sebagian','Berawan','Hujan','Hujan singkat','Guntur','Salju','Kabut','Tidak diketahui'],
'zh':['晴朗','局部多云','多云','雨','阵雨','雷雨','雪','雾','未知'],
'zh-Hant':['晴朗','局部多雲','多雲','雨','陣雨','雷雨','雪','霧','未知'],
'ru':['Ясно','Переменная облачность','Облачно','Дождь','Ливни','Гроза','Снег','Туман','Неизвестно'],
'ko':['맑음','부분적으로 흐림','흐림','비','소나기','천둥','눈','안개','미상'],
'ja':['晴れ','一部曇り','曇り','雨','にわか雨','雷','雪','霧','不明'],
'hi':['साफ','आंशिक बादल','बादल','बारिश','बौछार','गरज','बर्फ','कोहरा','अज्ञात'],
}


def forecast_points(data,now):
    updated=data.get('source_updated_at')
    if not updated:return []
    model=datetime.fromisoformat(updated)
    if model.tzinfo is None or model<now-timedelta(hours=48) or model>now+timedelta(hours=1):return []
    future=[point for point in data.get('points',[]) if datetime.fromisoformat(point['time'])>=now]
    selected=[]
    for hours in (0,6,12,18,24):
        target=now+timedelta(hours=hours)
        candidates=[point for point in future if point['time'] not in {item['time'] for item in selected}]
        if not candidates:break
        nearest=min(candidates,key=lambda point:abs((datetime.fromisoformat(point['time'])-target).total_seconds()))
        if abs((datetime.fromisoformat(nearest['time'])-target).total_seconds())<=7200:selected.append(nearest)
    return selected


def condition(code,lang):
    if 'thunder' in code:index=5
    elif 'snow' in code or 'sleet' in code:index=6
    elif 'showers' in code:index=4
    elif 'rain' in code:index=3
    elif 'fog' in code:index=7
    elif 'partlycloudy' in code or 'fair' in code:index=1
    elif 'cloudy' in code:index=2
    elif 'clearsky' in code:index=0
    else:index=8
    icon=['☀','⛅','☁','🌧','🌦','⛈','❄','🌫','◌'][index]
    if index==0 and code.endswith('_night'):icon='☾'
    return icon,CONDITIONS[lang][index]


def weather(lang,now=None):
    u=COPY[lang];heading,select_label,missing,names,suggestions=DESTINATIONS[lang]
    heading=WORLD_HEADINGS[lang]
    cache=json.loads((ROOT/'data/weather.json').read_text());cities=cache.get('cities',{'da-nang':cache})
    result=f'<section class="home-weather" id="weather" aria-labelledby="weather-title"><div class="container"><div class="weather-panel"><h2 id="weather-title">{E(heading)}</h2><p>{E(u[1])}</p><p class="notice">{E(WORLD_GUIDE_COPY[lang][5])}</p><label class="destination-label" for="weather-city">{E(select_label)}</label><select id="weather-city" class="destination-select">'
    labels={city[0]:city_name(city,lang) for *_,entries in COUNTRIES for city in entries}
    regions={city[0]:region for region,_,_,_,entries in COUNTRIES for city in entries}
    for country in COUNTRIES:
        result+=f'<optgroup data-country-code="{country[1]}" label="{E(country[3] if lang=="vi" else country[2])}">'
        for city in country[4]:result+=f'<option value="{city[0]}">{E(labels[city[0]])}</option>'
        result+='</optgroup>'
    result+='</select><div class="destination-results" aria-live="polite">'
    for index,(key,(city,_,_)) in enumerate(WORLD_CITIES.items()):
        data=cities.get(key,{});points=forecast_points(data,now or datetime.now(timezone.utc))
        hidden=' hidden' if index else ''
        result+=f'<div data-weather-city="{key}"{hidden}><h3>{E(labels[key])}</h3><p class="notice">{E(TIMEZONES[key])}</p>'
        if points:
            result+='<div class="weather-grid">'
            for point in points:
                icon,label=condition(point['symbol_code'],lang)
                rain='—' if point['precipitation_mm'] is None else f'{point["precipitation_mm"]:g} mm / {point["precipitation_hours"]} h'
                local_time=datetime.fromisoformat(point["time"]).astimezone(ZoneInfo(TIMEZONES[key])).strftime("%Y-%m-%d %H:%M %Z")
                result+=f'<article class="weather-card"><time datetime="{E(point["time"])}">{local_time}</time><span class="weather-icon" aria-hidden="true">{icon}</span><strong class="weather-temperature">{point["temperature_c"]:.0f} °C</strong><p>{E(label)}</p><small>{E(u[4])}: {rain}<br>{E(u[5])}: {point["wind_mps"]:g} m/s</small></article>'
            result+=f'</div><p class="weather-updated">{E(u[3])}: <time datetime="{E(data["source_updated_at"])}">{display_time(data["source_updated_at"])}</time></p>'
        else:result+=f'<p class="weather-unavailable">{E(missing)}</p>'
        result+=f'<aside class="destination-inspiration"><h4>{E(u[6])} · {E(labels[key])}</h4><p>{E(suggestions[list(CITIES).index(key)] if key in CITIES else u[7])}</p></aside><p class="notice"><a href="https://www.yr.no/en/search?q={quote(city)}" target="_blank" rel="noopener noreferrer">Yr · {E(labels[key])} ↗</a></p></div>'
    result+='</div><p class="notice"><a href="https://www.met.no/en" target="_blank" rel="noopener noreferrer">MET Norway</a> · <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener noreferrer">CC BY 4.0</a></p></div></div></section>'
    return result


def ideas(lang,current,relative):
    u=COPY[lang]
    links=[f'blog/{lang}/food/vietnam-food-guide/index.html',f'blog/{lang}/tours/da-nang-hoi-an-hue/index.html',f'blog/{lang}/destinations/vietnam-heritage-guide/index.html']
    result=f'<section class="section soft" id="trip-ideas" aria-labelledby="trip-ideas-title"><div class="container"><h2 id="trip-ideas-title">{E(u[6])}</h2><p class="lead">{E(u[7])}</p><div class="home-ideas-grid"><div class="trip-planner"><div class="plan-controls" role="group" aria-label="{E(u[6])}">'
    for index,days in enumerate(('1','3','5')):
        result+=f'<button type="button" data-plan-duration="{days}" aria-controls="idea-plan-{days}" aria-pressed="{str(index==0).lower()}">{E(u[8+index])}</button>'
    result+='</div><div class="plan-results">'
    for index,days in enumerate(('1','3','5')):
        hidden=' hidden' if index else ''
        result+=f'<article class="idea-plan" id="idea-plan-{days}" data-plan-panel="{days}"{hidden}><h3>{E(u[8+index])}</h3><p>{E(u[11+index])}</p><a class="blog-link" href="{relative(current,links[index])}">{E(u[21])}</a></article>'
    result+=f'</div><label class="rain-toggle"><input type="checkbox" class="rainy-day-toggle" aria-controls="rainy-day-plan"> {E(u[14])}</label><p class="rainy-day-plan" id="rainy-day-plan" hidden>{E(u[15])}</p></div><div class="trip-checklist"><h3>{E(u[16])}</h3><div class="checklist-items">'
    for index,key in enumerate(('documents','booking','transport')):
        result+=f'<label><input type="checkbox" data-trip-check="{key}"> {E(u[17+index])}</label>'
    result+=f'</div><div class="checklist-footer"><output class="checklist-progress" aria-live="polite">0 / 3</output><button type="button" class="checklist-reset">{E(u[20])}</button></div></div></div></div></section>'
    return result


def home_tools(lang,current,relative):return weather(lang)+ideas(lang,current,relative)

WORLD_HEADINGS={'vi':'Dự báo thời tiết các điểm đến trên thế giới','en':'World destination weather forecasts','fr':'Météo des destinations du monde','de':'Wettervorhersagen für Reiseziele weltweit','es':'Pronóstico de destinos del mundo','zh':'全球目的地天气预报','zh-Hant':'全球目的地天氣預報','ru':'Погода в туристических городах мира','ko':'세계 여행지 날씨 예보','ja':'世界の旅行先の天気予報','hi':'दुनिया के गंतव्यों का मौसम पूर्वानुमान','th':'พยากรณ์อากาศจุดหมายทั่วโลก','id':'Prakiraan cuaca destinasi dunia'}

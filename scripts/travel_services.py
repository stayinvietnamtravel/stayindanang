"""Service topic guides with transparent, category-specific affiliate destinations."""
from html import escape as E
from pathlib import Path
from content import CONTENT
from responsive_images import image as responsive_image
KEYS=('hotels','flights','tours','transfers','cars')
ART={'hotels':'hotel-inspiration','flights':'flight-planning','tours':'ha-long-bay','transfers':'travel-planning','cars':'tour-road-trip'}
ADVICE={
'vi':{
'hotels':('Chọn khách sạn theo lịch trình','Bắt đầu từ khu vực bạn muốn khám phá, rồi so sánh phòng theo cùng ngày và số khách. Đọc địa chỉ, hạng giường, bữa ăn, tổng thuế phí và hạn hủy. Danh sách Đà Nẵng và Hà Nội có link riêng cho từng khách sạn; giá và phòng trống cần kiểm tra trên Trip.com.'),
'flights':('So sánh chuyến bay và tổng chi phí','Kiểm tra sân bay đi và đến, giờ địa phương, hành lý xách tay và ký gửi, thời gian nối chuyến và quy định đổi vé. Tính cả chi phí đến sân bay và một khoảng dự phòng trước chuyến bay. Link bên dưới mở mục chuyến bay trên Trip.com để bạn tự chọn chặng, ngày và hành khách.'),
'tours':('Chọn tour và vé tham quan phù hợp','Đối chiếu điểm đón, thời lượng, ngôn ngữ hướng dẫn, điều kiện hủy và những gì được bao gồm. Với tour biển hoặc núi, xem dự báo thời tiết và thông báo của đơn vị tổ chức. Không mặc định vé có xe đưa đón, bữa ăn hoặc mọi điểm tham quan trong khu vực.'),
'transfers':('Đặt xe sân bay theo chuyến đến','Xác nhận đúng sân bay, nhà ga, số chuyến bay, giờ đón, số khách và hành lý. Đọc thời gian chờ, phụ phí đi đêm, ghế trẻ em và cách liên hệ tài xế. Kiểm tra điều kiện thay đổi khi chuyến bay trễ trước khi thanh toán.'),
'cars':('Thuê xe cho hành trình chủ động','Phân biệt xe tự lái và xe có tài xế trong gói được chọn. Kiểm tra giấy phép cần có, đặt cọc, bảo hiểm, nhiên liệu, giới hạn quãng đường và nơi trả xe. Lập lịch với thời gian nghỉ, tránh tự lái khi mệt và kiểm tra quy định địa phương.')},
'en':{
'hotels':('Choose a stay around your route','Compare the same dates and guest count, then check the exact address, bed type, meals, taxes and cancellation deadline. The Da Nang and Hanoi directories preserve individual hotel booking links. Confirm current availability and the final price on Trip.com.'),
'flights':('Compare flights and the full journey cost','Check departure and arrival airports, local times, cabin and checked baggage, connection time and change rules. Allow a buffer before departure and include airport transport in your budget. Choose your own route, dates and passengers on Trip.com.'),
'tours':('Check what your tour or ticket includes','Confirm the meeting point, duration, guide language, cancellation policy and included services. Check local forecasts and operator notices for sea and mountain trips. Do not assume transport, meals or every nearby attraction are included.'),
'transfers':('Match your pickup to your arrival','Confirm the airport, terminal, flight number, pickup time, passengers and luggage. Read waiting-time rules, night surcharges, child-seat arrangements and driver contact instructions. Check the policy for delayed flights.'),
'cars':('Plan a rental around the actual conditions','Distinguish self-drive rentals from cars with drivers. Check required driving documents, deposits, insurance, fuel policy, mileage and return location. Leave time for breaks and follow local driving rules.')}
}
def topic_path(lang,key):return f'travel/{lang}/{key}/index.html'
def page_pairs(languages):return [(topic_path(lang,key),{c:topic_path(c,key) for c in languages}) for lang in languages for key in KEYS]
def build_pages(document,relative,url,languages):
    from marketplace import service_labels,service_url,UI
    from deal_posts import COPY as HOTEL_COPY
    from travel_art import COPY as ART_COPY
    from world_destinations import COUNTRIES,country_name
    root=Path(__file__).resolve().parents[1]
    for lang in languages:
        u=CONTENT[lang]['ui'];labels=service_labels(lang)
        for key in KEYS:
            path=topic_path(lang,key);label=labels[key];title=label+' · '+country_name(COUNTRIES[0],lang)
            if lang=='en':title=label+' in Vietnam & worldwide'
            if lang=='vi':title=label+' tại Việt Nam và thế giới'
            heading,text=ADVICE.get(lang,{}).get(key,(u[2],CONTENT[lang]['articles'][0][2][2][1]))
            intro=UI[lang][6]
            img=responsive_image('assets/ai-travel/'+ART[key]+'.png',path,relative,label,sizes='(max-width:800px) 92vw, 780px',eager=True)
            body=f'<div class="container"><article class="article"><nav class="breadcrumbs"><a href="{relative(path,"index.html" if lang=="en" else lang+"/index.html")}">{E(u[0])}</a> / {E(label)}</nav><h1>{E(title)}</h1><p class="intro">{E(intro)}</p><figure class="featured-image">{img}<figcaption>{E(ART_COPY[lang][1])}</figcaption></figure><h2>{E(heading)}</h2><p>{E(text)}</p><a class="btn" href="{E(service_url(key))}" target="_blank" rel="sponsored noopener noreferrer" data-affiliate="topic-{key}">{E(label)} · Trip.com →</a><p class="editorial-note">{E(UI[lang][6])}</p><p>{E(u[11])}</p>'
            if key=='hotels':body+=f'<div class="city-stay-links"><a href="{relative(path,"deals/"+lang+"/index.html")}">Đà Nẵng →</a><a href="{relative(path,"blog/"+lang+"/destinations/hanoi/index.html")}">Hà Nội →</a></div>'
            guide='tips/vietnam-travel-planning' if key in ('flights','transfers','cars') else 'tours/da-nang-hoi-an-hue' if key=='tours' else 'hotels/where-to-stay-in-da-nang'
            body+=f'<p><a class="text-link" href="{relative(path,"blog/"+lang+"/"+guide+"/index.html")}">{E(u[15])}</a></p><p><a class="text-link" href="{relative(path,"index.html" if lang=="en" else lang+"/index.html")}#weather">☀ {E(u[5])} →</a></p><h2>{E(u[12])}</h2><a class="text-link" href="https://vietnam.travel/plan-your-trip" target="_blank" rel="noopener noreferrer">Vietnam Tourism →</a><div class="topic-shortcuts">'+''.join(f'<a href="{relative(path,topic_path(lang,other))}">{E(otherlabel)} →</a>' for other,otherlabel in labels.items() if other!=key)+'</div></article></div>'
            schema={'@context':'https://schema.org','@type':'Article','headline':title,'description':text,'inLanguage':lang,'mainEntityOfPage':url(path),'image':url('assets/ai-travel/'+ART[key]+'.png'),'about':{'@type':'Thing','name':label},'publisher':{'@type':'Organization','name':'Stay in Da Nang'},'citation':['https://vietnam.travel/plan-your-trip']}
            target=root/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(document(lang,path,title,text,body,{code:topic_path(code,key) for code in languages},schema))
    return page_pairs(languages)

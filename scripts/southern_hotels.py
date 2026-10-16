"""Owner-supplied southern hotel names and exact affiliate links."""
from pathlib import Path
from html import escape as E
import json
ROOT=Path(__file__).resolve().parents[1]
HOTELS=json.loads((ROOT/'data/southern_hotels.json').read_text())['rows']
CITY_LABELS={'ho-chi-minh-city':'TP. Hồ Chí Minh','vung-tau':'Vũng Tàu','ho-tram':'Hồ Tràm','long-hai':'Long Hải'}
def post_path(lang,h):return f'blog/{lang}/destinations/{h["city"]}/hotels/{h["slug"]}/index.html'
def page_pairs(languages):return [(post_path(lang,h),{c:post_path(c,h) for c in languages}) for lang in languages for h in HOTELS]
def build_pages(document,relative,url,languages):
    from hotel_visuals import cover
    from hotel_collection import path as collection_path,COPY as COLLECTION_COPY
    from deal_posts import COPY as CHECKS
    from content import CONTENT
    from travel_art import COPY as ART_COPY
    for lang in languages:
        c=CHECKS[lang];u=CONTENT[lang]['ui']
        for h in HOTELS:
            current=post_path(lang,h);city=CITY_LABELS[h['city']];title=h['name']+' | '+city;intro=h['name']+' · '+COLLECTION_COPY[lang][1]
            if lang=='vi':intro=f'Cân nhắc {h["name"]} cho chuyến đi {city}: đối chiếu địa chỉ với lịch trình, so sánh hạng phòng và kiểm tra điều kiện đặt theo ngày bạn đi.'
            elif lang=='en':intro=f'Considering {h["name"]} for {city}? Match the address to your itinerary, compare room categories and check the conditions for your travel dates.'
            img=cover(h,h['city'],lang,current,relative,eager=True)
            body=f'<div class="container"><article class="article"><nav class="breadcrumbs"><a href="{relative(current,collection_path(lang))}">{E(COLLECTION_COPY[lang][0])}</a> / {E(city)}</nav><span class="pill">{E(city)} · {h["group"]}</span><h1>{E(title)}</h1><p class="intro">{E(intro)}</p><figure class="featured-image">{img}<figcaption>{E(ART_COPY[lang][1])}</figcaption></figure><h2>{E(c[4])}</h2><ul>'+''.join(f'<li>{E(t)}</li>' for t in c[5:8])+'</ul>'
            if lang=='vi':
                body+=f'<h2>Chọn {E(h["name"])} theo nhu cầu chuyến đi</h2><p>Đặt địa chỉ cơ sở và các điểm cần đến trên cùng bản đồ. Kiểm tra đúng loại giường, số khách, bữa ăn, thuế và thời hạn hủy. Tên khách sạn hoặc hình minh họa không xác nhận tiện nghi hay dịch vụ trong gói phòng.</p>'
                if h['city']=='ho-chi-minh-city':body+='<h2>Gợi ý khám phá TP.HCM</h2><p>Chọn một cụm điểm cho mỗi buổi, như khu Bưu điện Trung tâm, khu phố đi bộ Nguyễn Huệ hoặc một bảo tàng phù hợp sở thích. Đây là gợi ý tham quan thành phố, không phải cam kết khách sạn gần các điểm đó. Dự phòng thời gian di chuyển giờ cao điểm và xác nhận đúng sân bay, nhà ga trước khi đặt xe.</p>'
                else:body+=f'<h2>Lên lịch tại {E(city)}</h2><p>Kiểm tra địa chỉ và phương tiện di chuyển từ nơi xuất phát trước khi đặt phòng. Giữ một khoảng nghỉ giữa các hoạt động, xem dự báo ngắn hạn và tuân thủ biển cảnh báo khi ra biển. Không mặc định mọi phòng đều có tầm nhìn biển hoặc quyền sử dụng tiện ích giống nhau.</p>'
            elif lang=='en':body+='<h2>Match the stay to your itinerary</h2><p>Map the exact property address and your planned stops. Compare the actual room, guest count, meals, taxes and cancellation deadline. A hotel name or illustration does not verify facilities or services included in a room package. Allow transfer buffers and check local conditions before travelling.</p>'
            body+=f'<p><a class="btn" href="{E(h["url"])}" target="_blank" rel="sponsored noopener noreferrer" data-affiliate="hotel-{h["slug"]}">{E(c[3].replace("↗","→"))}</a></p><p class="editorial-note">{E(COLLECTION_COPY[lang][5])}</p><p>{E(u[11])}</p><p><a class="text-link" href="{relative(current,collection_path(lang))}?city={h["city"]}">{E(COLLECTION_COPY[lang][4])} →</a></p></article></div>'
            schema={'@context':'https://schema.org','@type':'BlogPosting','headline':title,'description':intro,'image':url('assets/ai-travel/'+('hotel-saigon-scene' if h['city']=='ho-chi-minh-city' else 'hotel-southern-coast-scene')+'.png'),'inLanguage':lang,'mainEntityOfPage':url(current),'publisher':{'@type':'Organization','name':'Stay in Da Nang'},'spatialCoverage':{'@type':'Place','name':city+', Vietnam'}}
            target=ROOT/current;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(document(lang,current,title,intro,body,{code:post_path(code,h) for code in languages},schema))
    return page_pairs(languages)

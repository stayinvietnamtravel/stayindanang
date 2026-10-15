"""Original AI artwork, reusable blog covers and download links."""
from pathlib import Path
from html import escape as E
from responsive_images import image as responsive_image, registry as image_registry
import json
ROOT=Path(__file__).resolve().parents[1]
COPY={
'vi':['Bộ ảnh cảm hứng du lịch','Hình minh họa do AI tạo, không phải ảnh chụp thực tế của địa điểm hoặc khách sạn.','Mở / tải ảnh HD'],
'en':['Travel inspiration artwork','AI-generated illustrations, not actual photographs of destinations or hotels.','Open / download HD image'],
'fr':['Images pour inspirer le voyage','Illustrations générées par IA, pas des photos réelles de lieux ou d’hôtels.','Ouvrir / télécharger en HD'],
'de':['Reiseinspiration in Bildern','KI-Illustrationen, keine echten Fotos von Reisezielen oder Hotels.','HD-Bild öffnen / herunterladen'],
'es':['Imágenes para inspirar viajes','Ilustraciones de IA, no fotografías reales de destinos u hoteles.','Abrir / descargar imagen HD'],
'zh':['旅行灵感图片','AI 生成的插画，并非目的地或酒店的真实照片。','打开 / 下载高清图片'],
'zh-Hant':['旅行靈感圖片','AI 生成的插畫，並非目的地或飯店的真實照片。','開啟 / 下載高清圖片'],
'ru':['Иллюстрации для путешествий','Изображения созданы ИИ и не являются реальными фотографиями мест или отелей.','Открыть / скачать HD'],
'ko':['여행 영감 이미지','AI가 만든 일러스트이며 실제 여행지나 호텔 사진이 아닙니다.','HD 이미지 열기 / 다운로드'],
'ja':['旅のインスピレーション画像','AI生成のイラストで、実際の旅行先やホテルの写真ではありません。','HD画像を開く / 保存'],
'hi':['यात्रा प्रेरणा चित्र','AI से बने चित्र, स्थानों या होटलों की वास्तविक तस्वीरें नहीं।','HD चित्र खोलें / डाउनलोड करें'],
'th':['ภาพสร้างแรงบันดาลใจเที่ยว','ภาพประกอบสร้างด้วย AI ไม่ใช่ภาพถ่ายจริงของสถานที่หรือโรงแรม','เปิด / ดาวน์โหลดภาพ HD'],
'id':['Gambar inspirasi perjalanan','Ilustrasi AI, bukan foto asli destinasi atau hotel.','Buka / unduh gambar HD']}
ART={'da-nang-hotels-tours-flights-2026':'discover-vietnam.png','vietnam-food-guide':'taste-vietnam.png','vietnam-travel-planning':'travel-planning.png','where-to-stay-in-da-nang':'hotel-inspiration.png','da-nang-hoi-an-hue':'ba-na-hills.png','vietnam-heritage-guide':'hoi-an.png','coastal-vietnam-experiences':'coastal-vietnam.png','hanoi-ho-chi-minh-city-walks':'city-walks.png'}
def cover(slug):
    target='assets/ai-travel/'+ART[slug] if slug in ART else ''
    return target if target and (ROOT/target).exists() else f'assets/blog/{slug}.svg'
def dimensions(path):
    if path.endswith('.png'):
        import struct
        with (ROOT/path).open('rb') as image:header=image.read(24)
        return struct.unpack('>II',header[16:24])
    return 1020,540
def gallery(lang,current,relative):
    u=COPY[lang];result=f'<section class="section travel-art" id="travel-art"><div class="container"><h2>{E(u[0])}</h2><p class="notice">{E(u[1])}</p><div class="travel-art-grid">'
    for filename,title in [('discover-vietnam.png','Discover Vietnam'),('taste-vietnam.png','Taste Vietnam')]:
        path='assets/ai-travel/'+filename
        if not (ROOT/path).exists():continue
        width,height=dimensions(path)
        variants=image_registry().get(path,{}).get("variants",[])
        webp=variants[-1]["file"] if variants else path
        img=responsive_image(path,current,relative,title+" · "+u[1],sizes="(max-width: 800px) 92vw, 700px")
        result+=f'<figure><a href="{relative(current,path)}">{img}</a><figcaption><strong>{title}</strong><a class="text-link" href="{relative(current,path)}" download>PNG · {E(u[2])} →</a><a class="text-link" href="{relative(current,webp)}" download>WebP →</a></figcaption></figure>'
    result+='</div>'
    entries=json.loads((ROOT/'assets/ai-travel/manifest.json').read_text())
    more=[item for item in entries if item['file'] not in ('discover-vietnam.png','taste-vietnam.png')]
    if more:
        result+=f'<details class="art-library-more"><summary>{E(u[0])} · {len(more)}</summary><div class="art-library-grid">'
        for item in more:
            path='assets/ai-travel/'+item['file'];variants=image_registry().get(path,{}).get('variants',[]);webp=variants[-1]['file'] if variants else path;img=responsive_image(path,current,relative,item['topic']+' · '+u[1],sizes='(max-width: 700px) 44vw, 270px')
            result+=f'<figure><a href="{relative(current,path)}">{img}</a><figcaption><strong>{E(item["topic"])}</strong><a class="text-link" href="{relative(current,path)}" download>PNG · {E(u[2])} →</a><a class="text-link" href="{relative(current,webp)}" download>WebP →</a></figcaption></figure>'
        result+='</div></details>'
    return result+'</div></section>'

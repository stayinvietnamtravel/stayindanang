"""International reference directory and attributed cached-news pages."""
from pathlib import Path
from html import escape as E
from datetime import datetime
from zoneinfo import ZoneInfo
from urllib.parse import urlsplit
import json

ROOT=Path(__file__).resolve().parents[1]
SOURCES=json.loads((ROOT/'data/travel_sources.json').read_text())
UI={
'vi':['Nguồn du lịch quốc tế','Tham khảo trang du lịch chính thức và tạp chí để tìm hiểu điểm đến, văn hóa và thông tin lên kế hoạch.','Trang du lịch chính thức','Tạp chí và cổng thông tin du lịch','Tin du lịch quốc tế','Tiêu đề được tổng hợp từ RSS của nhà xuất bản, kèm nguồn và ngày đăng khi được cung cấp.','Đọc tại nguồn ↗','Chưa có bản tin tải thành công. Bạn có thể đọc trực tiếp tại các nguồn bên dưới.','Tất cả điểm đến','Lần tải thành công gần nhất','Nguồn chưa cung cấp ngày đăng','Tiêu đề giữ ngôn ngữ của nguồn. Các nhãn điểm đến dựa trên tên được nhắc trong tiêu đề và phạm vi của nguồn.','Nguồn & tin tức','Mở trang nguồn ↗','Các liên kết là nguồn tham khảo, không thể hiện quan hệ hợp tác hay bảo chứng.','Xem tin du lịch','Xem danh bạ nguồn','Quốc tế','Lọc theo điểm đến'],
'en':['International travel resources','Explore official tourism sites and magazines for destination, culture and planning information.','Official tourism sites','Travel magazines & publications','International travel news','Headlines from publisher RSS feeds, with source links and publication dates when provided.','Read at source ↗','No headlines have been fetched successfully yet. Read directly at the sources below.','All destinations','Last successful fetch','Publication date not supplied','Headlines retain their source language. Destination tags use names mentioned in the headline and the source’s scope.','Resources & news','Open source site ↗','These are reference links and do not imply partnership or endorsement.','View travel news','View resource directory','International','Filter by destination'],
'fr':['Ressources touristiques internationales','Consultez sites touristiques officiels et magazines pour découvrir destinations, culture et conseils.','Sites touristiques officiels','Magazines et publications','Actualités touristiques internationales','Titres issus des flux RSS des éditeurs, avec source et date lorsque disponible.','Lire à la source ↗','Aucun titre chargé avec succès pour le moment. Consultez les sources ci-dessous.','Toutes les destinations','Dernier chargement réussi','Date non fournie','Les titres gardent la langue de leur source. Les tags suivent les lieux cités et le périmètre de la source.','Ressources et actualités','Ouvrir la source ↗','Liens de référence, sans relation de partenariat ni garantie.','Voir les actualités','Voir les ressources','International','Filtrer par destination'],
'de':['Internationale Reisequellen','Offizielle Tourismusseiten und Magazine für Reiseziele, Kultur und Planung entdecken.','Offizielle Tourismusseiten','Reisemagazine und Publikationen','Internationale Reisenachrichten','RSS-Schlagzeilen von Herausgebern mit Quellenlinks und Datum, sofern vorhanden.','Bei der Quelle lesen ↗','Noch keine Schlagzeilen erfolgreich geladen. Die Quellen unten direkt öffnen.','Alle Reiseziele','Letzter erfolgreicher Abruf','Datum nicht angegeben','Schlagzeilen bleiben in der Quellsprache. Ziel-Tags folgen genannten Orten und dem Umfang der Quelle.','Quellen und Nachrichten','Quelle öffnen ↗','Referenzlinks bedeuten keine Partnerschaft oder Empfehlungsgarantie.','Nachrichten ansehen','Quellenverzeichnis ansehen','International','Nach Reiseziel filtern'],
'es':['Recursos de viaje internacionales','Consulta turismo oficial y revistas para conocer destinos, cultura y planificación.','Sitios oficiales de turismo','Revistas y publicaciones','Noticias de turismo internacional','Titulares RSS de los editores con fuente y fecha cuando están disponibles.','Leer en la fuente ↗','Aún no se han cargado titulares. Consulta las fuentes directamente abajo.','Todos los destinos','Última descarga correcta','Fecha no proporcionada','Los titulares conservan el idioma original. Las etiquetas siguen lugares mencionados y el ámbito de la fuente.','Fuentes y noticias','Abrir fuente ↗','Son enlaces de referencia, sin implicar colaboración ni garantía.','Ver noticias','Ver directorio','Internacional','Filtrar por destino'],
'th':['แหล่งท่องเที่ยวต่างประเทศ','ค้นหาเว็บไซต์ท่องเที่ยวทางการและนิตยสารเพื่อศึกษาจุดหมาย วัฒนธรรม และการวางแผน','เว็บไซต์ท่องเที่ยวทางการ','นิตยสารและสื่อท่องเที่ยว','ข่าวท่องเที่ยวต่างประเทศ','หัวข้อจาก RSS ของผู้เผยแพร่ พร้อมลิงก์และวันที่เมื่อมีข้อมูล','อ่านจากต้นทาง ↗','ยังโหลดข่าวไม่สำเร็จ สามารถอ่านโดยตรงจากแหล่งด้านล่าง','ทุกจุดหมาย','โหลดสำเร็จล่าสุด','ต้นทางไม่ระบุวันที่','หัวข้อใช้ภาษาต้นทาง ป้ายจุดหมายมาจากสถานที่ที่กล่าวถึงและขอบเขตของแหล่งข่าว','แหล่งข้อมูลและข่าว','เปิดแหล่งข่าว ↗','ลิงก์อ้างอิงไม่ได้หมายถึงพันธมิตรหรือการรับรอง','ดูข่าวท่องเที่ยว','ดูรายชื่อแหล่งข้อมูล','นานาชาติ','กรองจุดหมาย'],
'id':['Sumber perjalanan internasional','Jelajahi situs wisata resmi dan majalah untuk destinasi, budaya dan rencana perjalanan.','Situs wisata resmi','Majalah dan publikasi','Berita wisata internasional','Judul dari RSS penerbit dengan sumber dan tanggal jika tersedia.','Baca di sumber ↗','Belum ada judul yang berhasil dimuat. Baca langsung di sumber berikut.','Semua destinasi','Pengambilan berhasil terakhir','Tanggal tidak disediakan','Judul mempertahankan bahasa sumber. Tag mengikuti lokasi yang disebut dan cakupan sumber.','Sumber dan berita','Buka sumber ↗','Tautan referensi tidak menyatakan kemitraan atau jaminan.','Lihat berita','Lihat direktori','Internasional','Filter destinasi'],
'zh':['国际旅游资源','浏览官方旅游网站和杂志，了解目的地、文化与行程规划。','官方旅游网站','旅游杂志与媒体','国际旅游新闻','来自出版商 RSS 的标题，附来源链接及已提供的发布日期。','在来源阅读 ↗','目前尚未成功获取标题，可直接访问下方来源。','全部目的地','最近成功获取','来源未提供日期','标题保留来源语言。目的地标签依据标题提及的名称及来源范围。','资源与新闻','打开来源网站 ↗','这些参考链接不代表合作关系或背书。','查看旅游新闻','查看资源目录','国际','按目的地筛选'],
'zh-Hant':['國際旅遊資源','瀏覽官方旅遊網站與雜誌，了解目的地、文化及行程規劃。','官方旅遊網站','旅遊雜誌與媒體','國際旅遊新聞','來自出版商 RSS 的標題，附來源連結及已提供的發布日期。','在來源閱讀 ↗','目前尚未成功取得標題，可直接造訪下方來源。','全部目的地','最近成功取得','來源未提供日期','標題保留來源語言。目的地標籤依標題提及名稱與來源範圍。','資源與新聞','開啟來源網站 ↗','參考連結不代表合作關係或背書。','查看旅遊新聞','查看資源目錄','國際','依目的地篩選'],
'ru':['Международные туристические ресурсы','Официальные туристические сайты и журналы для знакомства с местами, культурой и планированием.','Официальные туристические сайты','Журналы и публикации','Международные туристические новости','Заголовки RSS издателей со ссылками и датами, если они предоставлены.','Читать у источника ↗','Заголовки пока не загружены. Откройте источники ниже напрямую.','Все направления','Последняя успешная загрузка','Дата не предоставлена','Заголовки сохраняют язык источника. Метки основаны на упомянутых местах и тематике источника.','Источники и новости','Открыть источник ↗','Справочные ссылки не означают партнёрство или гарантию.','Посмотреть новости','Открыть каталог','Международное','Фильтр по направлению'],
'ko':['국제 여행 자료','공식 관광 사이트와 잡지에서 여행지, 문화와 계획 정보를 알아보세요.','공식 관광 사이트','여행 잡지와 매체','국제 여행 뉴스','발행사 RSS 제목에 출처 링크와 제공된 날짜를 표시합니다.','출처에서 읽기 ↗','아직 제목을 가져오지 못했습니다. 아래 출처를 직접 방문하세요.','모든 여행지','마지막 성공한 가져오기','날짜 미제공','제목은 출처 언어를 유지합니다. 여행지 표시는 제목의 장소명과 출처 범위에 따릅니다.','자료와 뉴스','출처 열기 ↗','참고 링크이며 제휴나 보증을 뜻하지 않습니다.','뉴스 보기','자료 목록 보기','국제','여행지 필터'],
'ja':['世界の旅行情報源','公式観光サイトや雑誌で目的地、文化、旅行計画を調べましょう。','公式観光サイト','旅行雑誌とメディア','世界の旅行ニュース','発行元RSSの見出しに出典リンクと提供された日付を表示します。','出典で読む ↗','まだ見出しを取得できていません。下記の出典へ直接アクセスできます。','すべての目的地','最終取得成功','日付の提供なし','見出しは元の言語です。目的地タグは見出しの地名と出典の範囲に基づきます。','情報源とニュース','出典を開く ↗','参考リンクであり、提携や保証を示しません。','ニュースを見る','情報源一覧を見る','国際','目的地で絞る'],
'hi':['अंतरराष्ट्रीय यात्रा स्रोत','आधिकारिक पर्यटन साइट और पत्रिकाओं से जगह, संस्कृति और यात्रा योजना जानें।','आधिकारिक पर्यटन साइट','यात्रा पत्रिकाएँ और प्रकाशन','अंतरराष्ट्रीय यात्रा समाचार','प्रकाशक RSS के शीर्षक, स्रोत लिंक और उपलब्ध प्रकाशन तारीख के साथ।','स्रोत पर पढ़ें ↗','अभी शीर्षक सफलतापूर्वक नहीं मिले हैं। नीचे के स्रोत सीधे खोलें।','सभी गंतव्य','अंतिम सफल डाउनलोड','तारीख नहीं दी गई','शीर्षक स्रोत की भाषा में रहते हैं। गंतव्य टैग शीर्षक के स्थान और स्रोत के क्षेत्र से बनते हैं।','स्रोत और समाचार','स्रोत खोलें ↗','संदर्भ लिंक साझेदारी या समर्थन का दावा नहीं हैं।','समाचार देखें','स्रोत सूची देखें','अंतरराष्ट्रीय','गंतव्य फ़िल्टर'],
}
EMPTY_FILTER={
 'vi':'Chưa có tin cho điểm đến này trong bộ tin hiện tại.',
 'en':'No headlines for this destination in the current cache.',
 'fr':'Aucun titre pour cette destination dans les données actuelles.',
 'de':'Keine Schlagzeilen für dieses Reiseziel im aktuellen Bestand.',
 'es':'No hay titulares para este destino en los datos actuales.',
 'th':'ยังไม่มีข่าวของจุดหมายนี้ในข้อมูลปัจจุบัน',
 'id':'Tidak ada judul untuk destinasi ini pada data saat ini.',
 'zh':'当前缓存中没有此目的地的标题。',
 'zh-Hant':'目前快取中沒有此目的地的標題。',
 'ru':'В текущем наборе нет заголовков для этого направления.',
 'ko':'현재 저장된 뉴스에 이 여행지의 제목이 없습니다.',
 'ja':'現在の保存データにはこの目的地の見出しがありません。',
 'hi':'मौजूदा डेटा में इस गंतव्य के शीर्षक नहीं हैं।',
}


def resources_path(lang):return f'resources/{lang}/index.html'
def news_path(lang):return f'news/{lang}/index.html'
def page_pairs(languages):
    return [(func(lang),{code:func(code) for code in languages}) for func in (resources_path,news_path) for lang in languages]


def display_time(value):
    if not value:return None
    try:
        date=datetime.fromisoformat(value.replace('Z','+00:00'))
        if date.tzinfo is None:return None
        return date.astimezone(ZoneInfo('Asia/Bangkok')).strftime('%Y-%m-%d %H:%M +07:00')
    except (ValueError,TypeError):return None


def teaser(lang,current,relative):
    u=UI[lang]
    return f'<aside class="travel-portal-callout"><h3>{E(u[4])}</h3><p>{E(u[5])}</p><div class="hero-actions"><a class="btn" href="{relative(current,news_path(lang))}">{E(u[15])} →</a><a class="blog-link" href="{relative(current,resources_path(lang))}">{E(u[16])} →</a></div></aside>'


def safe_articles(cache):
    feeds={f['id']:f for f in SOURCES['feeds']}
    articles=[]
    for item in cache.get('articles',[]):
        source=feeds.get(item.get('source_id'))
        if not source:continue
        parsed=urlsplit(item.get('url',''))
        if parsed.scheme!='https' or parsed.hostname not in source['article_hosts'] or parsed.username or parsed.password:continue
        if not isinstance(item.get('title'),str) or not item['title'].strip():continue
        articles.append({**item,'publisher':source['name']})
    return articles


def build_pages(document,relative,url,languages):
    cache=json.loads((ROOT/'data/travel_news.json').read_text())
    articles=safe_articles(cache)
    country_names={site['id']:site['country'] for site in SOURCES['official_sites']}
    for lang in languages:
        u=UI[lang];path=resources_path(lang)
        body=f'<section class="section soft"><div class="container"><h1>{E(u[0])}</h1><p class="lead">{E(u[1])}</p><p class="notice">{E(u[14])}</p><h2>{E(u[2])}</h2><div class="resource-grid">'
        for site in SOURCES['official_sites']:
            body+=f'<article class="resource-card"><span class="pill">{E(site["country"])}</span><h3>{E(site["name"])}</h3><a class="blog-link" href="{E(site["url"])}" target="_blank" rel="noopener noreferrer">{E(u[13])}</a></article>'
        body+=f'</div><h2>{E(u[3])}</h2><div class="resource-grid">'
        for publication in SOURCES['magazines']:
            body+=f'<article class="resource-card"><span class="pill">{E(publication["market"])}</span><h3>{E(publication["name"])}</h3><a class="blog-link" href="{E(publication["url"])}" target="_blank" rel="noopener noreferrer">{E(u[13])}</a></article>'
        body+='</div>'+teaser(lang,path,relative)+'</div></section>'
        write(path,document(lang,path,u[0],u[1],body,{code:resources_path(code) for code in languages}))
        path=news_path(lang)
        body=f'<section class="section soft"><div class="container"><h1>{E(u[4])}</h1><p class="lead">{E(u[5])}</p><p class="notice">{E(u[11])}</p>'
        checked=display_time(cache.get('last_updated'))
        if checked:body+=f'<p>{E(u[9])}: <time datetime="{E(cache["last_updated"])}">{checked}</time></p>'
        if articles:
            body+=f'<div class="news-browser"><label for="news-country">{E(u[18])}</label><select id="news-country" class="news-country"><option value="all">{E(u[8])}</option><option value="international">{E(u[17])}</option>'
            body+=''.join(f'<option value="{country}">{E(name)}</option>' for country,name in country_names.items())+'</select><div class="news-grid">'
            for item in articles:
                tags=[tag for tag in item.get('countries',[]) if tag in country_names or tag=='international'] or ['international']
                body+=f'<article class="news-card" data-news-countries="{E(" ".join(tags))}"><span class="pill">{E(item["publisher"])}</span><h2><a href="{E(item["url"])}" target="_blank" rel="noopener noreferrer">{E(item["title"])}</a></h2>'
                published=display_time(item.get('published_at'))
                body+=f'<p class="news-date"><time datetime="{E(item["published_at"])}">{published}</time></p>' if published else f'<p class="news-date">{E(u[10])}</p>'
                body+='<p class="news-tags">'+E(' · '.join(country_names.get(tag,u[17]) for tag in tags))+'</p>'
                body+=f'<a class="blog-link" href="{E(item["url"])}" target="_blank" rel="noopener noreferrer">{E(u[6])}</a></article>'
            body+=f'</div><p class="news-empty-filter" hidden>{E(EMPTY_FILTER[lang])}</p></div>'
        else:
            body+=f'<aside class="editorial-note news-cache-empty">{E(u[7])}</aside>'
        body+=f'<h2>{E(u[12])}</h2><div class="resource-grid">'
        for source in SOURCES['feeds']:
            body+=f'<article class="resource-card"><h3>{E(source["name"])}</h3><a class="blog-link" href="{E(source["homepage"])}" target="_blank" rel="noopener noreferrer">{E(u[6])}</a></article>'
        body+=f'</div><p><a class="btn" href="{relative(path,resources_path(lang))}">{E(u[16])} →</a></p></div></section>'
        write(path,document(lang,path,u[4],u[5],body,{code:news_path(code) for code in languages}))
    return page_pairs(languages)


def write(path,text):
    target=ROOT/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(text,encoding='utf-8')

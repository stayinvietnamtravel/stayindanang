"""Public reading index for campaign blog articles; scheduling stays outside the UI."""
from pathlib import Path
from html import escape as E
from campaign_guides import DAYS,VI
from responsive_images import image
from content import CONTENT
TITLE={'vi':'30 ý tưởng khám phá Việt Nam','en':'30 ideas for exploring Vietnam','zh':'探索越南的30个灵感','zh-Hant':'探索越南的30個靈感','ru':'30 идей для поездки во Вьетнам','ko':'베트남 여행 아이디어 30가지','ja':'ベトナムを旅する30のアイデア','hi':['वियतनाम घूमने के 30 विचार'][0],'fr':'30 idées pour explorer le Vietnam','de':'30 Ideen für Vietnam','es':'30 ideas para explorar Vietnam','th':'30 ไอเดียเที่ยวเวียดนาม','id':'30 ide menjelajahi Vietnam'}
def path(lang):return f'ideas/{lang}/index.html'
def page_pairs(languages):return [(path(lang),{code:path(code) for code in languages}) for lang in languages]
def callout(lang,current,relative):return f'<aside class="deals-callout"><h3>{E(TITLE[lang])}</h3><p>{E(CONTENT[lang]["ui"][18])}</p><a class="btn" href="{relative(current,path(lang))}">{E(TITLE[lang])} →</a></aside>'
def build_pages(document,relative,url,languages):
    root=Path(__file__).resolve().parents[1]
    for lang in languages:
        current=path(lang);u=CONTENT[lang]['ui'];body=f'<section class="section soft campaign-library"><div class="container"><h1>{E(TITLE[lang])}</h1><p class="lead">{E(u[18])}</p><div class="blog-grid">';items=[]
        for i,item in enumerate(DAYS):
            title=VI[i][0] if lang=='vi' else item['title_en'];target=f'blog/{lang}/{item["category"]}/{item["slug"]}/index.html';img=image(item['image'],current,relative,title,'blog-cover poster-cover',sizes='(max-width:700px) 92vw, 380px')
            body+=f'<a class="blog-card" href="{relative(current,target)}">{img}<div class="blog-card-body"><h2>{E(title)}</h2><span class="text-link">{E(u[15])}</span></div></a>';items.append({'@type':'ListItem','position':i+1,'name':title,'url':url(target)})
        body+='</div></div></section>';schema={'@context':'https://schema.org','@type':'CollectionPage','name':TITLE[lang],'inLanguage':lang,'mainEntity':{'@type':'ItemList','numberOfItems':30,'itemListElement':items}}
        p=root/current;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(document(lang,current,TITLE[lang],u[18],body,{code:path(code) for code in languages},schema))
    return page_pairs(languages)

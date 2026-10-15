"""Shared booking-first homepage for every language edition."""
from html import escape as E
import re
from content import CONTENT
from marketplace import booking,discovery,service_labels
from responsive_images import image as responsive_image
from travel_art import COPY as ART_COPY
from world_guides import teaser as world_teaser
from home_tools import home_tools
from deal_posts import index_path as deals_index
from travel_services import topic_path
ICONS={'hotels':'▣','flights':'✈','tours':'⌖','transfers':'↔','cars':'◇'}
def header(lang,current,relative,language_picker):
    u=CONTENT[lang]['ui']
    links=[('#booking',u[3]),('#destinations',u[5]),('#tours',u[4]),('#blog',u[1]),('#weather', 'Weather' if lang=='en' else 'Thời tiết' if lang=='vi' else '☀')]
    return f'<header class="header home-header"><div class="container header-inner"><a class="logo" href="{relative(current,"index.html" if lang=="en" else lang+"/index.html")}"><span class="brand-mark" aria-hidden="true">∿</span>Stay in Da Nang</a><nav class="home-nav" aria-label="{E(u[19])}">'+''.join(f'<a href="{target}">{E(label)}</a>' for target,label in links)+f'</nav>{language_picker}</div></header>'
def body(lang,current,relative,cards):
    u=CONTENT[lang]['ui'];labels=service_labels(lang)
    img=responsive_image('assets/ai-travel/coastal-vietnam.png',current,relative,ART_COPY[lang][1],'home-hero-image',sizes='(max-width:700px) 100vw, 1180px',eager=True)
    result=f'<section class="home-hero" id="home"><div class="container home-hero-inner"><div class="home-hero-copy"><span class="eyebrow">VIETNAM & BEYOND</span><h1>{E(u[6])}</h1><p>{E(u[7])}</p></div>{img}</div></section>'
    panel=booking(lang,current,relative)
    tabs='<div class="booking-tabs" role="group" aria-label="'+E(u[3]+' · '+u[4])+'">'+''.join(f'<button type="button" data-booking-service="{key}" aria-pressed="{str(key=="hotels").lower()}"><span aria-hidden="true">{ICONS[key]}</span>{E(labels[key])}</button>' for key in ('hotels','flights','tours','transfers','cars'))+'</div>'
    panel=panel.replace('<div class="booking-panel">','<div class="booking-panel">'+tabs,1)
    result+=panel
    result+='<section class="home-topics"><div class="container topic-shortcuts">'+''.join(f'<a href="{relative(current,topic_path(lang,key))}"><span aria-hidden="true">{ICONS[key]}</span><strong>{E(label)}</strong><span aria-hidden="true">→</span></a>' for key,label in labels.items())+'</div></section>'
    result+=f'<section class="container city-stays"><div><span class="eyebrow">VIETNAM</span><h2>{E(u[3])} · Đà Nẵng & Hà Nội</h2></div><div class="city-stay-links"><a href="{relative(current,deals_index(lang))}">Đà Nẵng · 42 {E(u[3])} →</a><a href="{relative(current,"blog/"+lang+"/destinations/hanoi/index.html")}">Hà Nội · 30 {E(u[3])} →</a></div></section>'
    discovery_html=discovery(lang,current,relative)
    hotel=re.search(r'<section[^>]+id="hotels".*?</section>',discovery_html,re.S)
    result+=(hotel.group(0)+discovery_html.replace(hotel.group(0),'',1)) if hotel else discovery_html
    result+=world_teaser(lang,current,relative)
    result+=f'<section class="section soft" id="blog"><div class="container"><h2>{E(u[16])}</h2><p class="lead main-blog-heading">{E(u[18])}</p>{cards(lang,current)}</div></section>'
    result+=home_tools(lang,current,relative)
    return result

def schema(lang,current,url):
    from world_destinations import COUNTRIES,city_name
    from world_weather import CITIES
    items=[]
    for country in COUNTRIES:
        if country[1]!='VN':continue
        for city in country[4][:5]:
            key=city[0];forecast=CITIES[key]
            target='blog/'+lang+'/destinations/hanoi/index.html' if key=='hanoi' else 'deals/'+lang+'/index.html' if key=='da-nang' else current+'?weather='+key+'#weather'
            items.append({'@type':'ListItem','position':len(items)+1,'item':{'@type':'Place','name':city_name(city,lang),'url':url(target),'geo':{'@type':'GeoCoordinates','latitude':forecast[1],'longitude':forecast[2]}}})
    return {'@context':'https://schema.org','@type':'CollectionPage','name':CONTENT[lang]['ui'][6],'inLanguage':lang,'url':url(current),'mainEntity':{'@type':'ItemList','name':CONTENT[lang]['ui'][5],'itemListElement':items},'about':[{'@type':'Thing','name':label,'url':url(topic_path(lang,key))} for key,label in service_labels(lang).items()]}

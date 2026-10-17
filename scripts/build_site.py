#!/usr/bin/env python3
"""Build multilingual HTML and sitemap using only the Python standard library."""
from pathlib import Path
from html import escape
import json
import os
import re
import xml.etree.ElementTree as ET
from content import CONTENT, LANGUAGES, SLUGS, SOURCES, ARTICLE_DETAILS, FEATURE_CAPTIONS
from feature_images import build_images
from deal_posts import build_pages as build_deal_pages, exports as export_deal_posts, COPY as DEAL_COPY, index_path as deals_index
from travel_portal import build_pages as build_travel_pages, teaser as travel_teaser, UI as TRAVEL_UI, resources_path, news_path
from home_tools import home_tools

from marketplace import marketplace, service_url, service_labels
from world_guides import build_pages as build_world_pages, teaser as world_teaser
from seo import extras as seo_extras, discovery_files
from responsive_images import image as responsive_image, registry as image_registry
from travel_art import cover as art_cover, dimensions as art_dimensions, contextual_images, COPY as ART_COPY
from assistant import build_data as build_assistant_data, widget as assistant_widget, stats as assistant_stats
from hanoi_hotels import build_pages as build_hanoi_pages, teaser as hanoi_teaser
from home_layout import body as homepage_body, header as homepage_header, schema as homepage_schema
from travel_services import build_pages as build_service_pages
from hotel_collection import build_pages as build_collection_pages,path as collection_path
from southern_hotels import build_pages as build_southern_pages
from campaign_pages import build_pages as build_campaign_pages,callout as campaign_callout
from site_links import footer as footer_network
from practical_guides import before_sections as guide_before, after_sections as guide_after

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://stayinvietnamtravel.github.io/stayindanang/'
E = escape
CATEGORY_LABELS = {'tips': 2, 'hotels': 3, 'tours': 4, 'destinations': 5, 'food':22, 'experiences':23}


def home(lang):
    return 'index.html' if lang == 'en' else f'{lang}/index.html'


def blog(lang):
    return 'blog/index.html' if lang == 'en' else f'blog/{lang}/index.html'


def article(lang, index):
    category, slug = SLUGS[index]
    return f'blog/{lang}/{category}/{slug}/index.html'


def url(path):
    return BASE + path.removesuffix('index.html')


def relative(current, target):
    return os.path.relpath(target, Path(current).parent).replace(os.sep, '/')


def language_links(lang, current, counterparts):
    links = []
    for code, label in LANGUAGES.items():
        active = ' aria-current="page"' if code == lang else ''
        links.append(f'<a href="{relative(current, counterparts[code])}" lang="{code}" hreflang="{code}"{active}>{label}</a>')
    label = E(CONTENT[lang]['ui'][17])
    return f'<details class="language-picker"><summary>{label} · {E(LANGUAGES[lang])}</summary><nav class="language-bar" aria-label="{label}">' + ''.join(links) + '</nav></details>'



def document(lang, path, title, description, body, counterparts, structured=None):
    u = CONTENT[lang]['ui']
    alternates = ''.join(f'<link rel="alternate" hreflang="{code}" href="{url(target)}">' for code, target in counterparts.items())
    alternates += f'<link rel="alternate" hreflang="x-default" href="{url(counterparts["en"])}">'
    schema = '' if structured is None else '<script type="application/ld+json">' + json.dumps(structured, ensure_ascii=False).replace('<', '\\u003c') + '</script>'
    image_metadata = f'<meta property="og:image" content="{BASE}assets/social/travel-guide.png"><meta property="og:image:alt" content="Stay in Da Nang travel guides">' if not structured or 'image' not in structured else f'<meta property="og:image" content="{E(structured["image"])}"><meta property="og:image:alt" content="{E(title)}">'
    is_home=path==home(lang)
    header=homepage_header(lang,path,relative,language_links(lang,path,counterparts)) if is_home else ''
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0b3152"><title>{E(title)} | Stay in Da Nang</title>
<meta name="description" content="{E(description)}"><link rel="canonical" href="{url(path)}">{alternates}
<meta property="og:type" content="{'article' if structured and structured.get('@type') == 'BlogPosting' else 'website'}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(description)}"><meta property="og:url" content="{url(path)}">
<link rel="stylesheet" href="{relative(path, 'assets/site.css')}"><script src="{relative(path, 'assets/site.js')}" defer></script>{image_metadata}{schema}{seo_extras(lang,path,title,description,structured.get("image") if structured else None)}<script src="{relative(path, "assets/assistant.js")}" defer></script></head><body class="{'home-page' if is_home else 'content-page'}"><a class="skip" href="#main">{E(u[0])} →</a>{header}
{'' if is_home else f'''<header class="header simple-header"{' hidden' if is_home else ''}><div class="container header-inner"><a class="logo" href="{relative(path, home(lang))}" aria-label="{E(u[20])}"><span class="brand-mark" aria-hidden="true">∿</span>Stay in Da Nang</a>{language_links(lang, path, counterparts)}</div></header>
<nav class="container site-links" aria-label="{E(u[19])}"><a href="{relative(path, home(lang))}">{E(u[0])}</a><a href="{relative(path, blog(lang))}">{E(u[1])}</a><a href="{relative(path, collection_path(lang))}">Hot Deals & Hot Sellers</a><a href="{relative(path,news_path(lang))}">{E(TRAVEL_UI[lang][15])}</a><a href="{relative(path,resources_path(lang))}">{E(TRAVEL_UI[lang][16])}</a></nav>
'''}
<main id="main">{body}</main><footer class="footer"><div class="container"><div class="footer-directory"><strong>Stay in Da Nang</strong><nav aria-label="{E(u[19])}"><a href="{relative(path,home(lang))}">{E(u[0])}</a><a href="{relative(path,collection_path(lang))}">Hot Deals & Hot Sellers</a><a href="{relative(path,blog(lang))}">{E(u[1])}</a><a href="{relative(path,news_path(lang))}">{E(TRAVEL_UI[lang][15])}</a></nav></div><p>{E(u[21])}</p><p>{E(u[11])}</p><p>© 2026 Stay in Da Nang</p>{assistant_stats(lang)}{footer_network(lang)}</div></footer>{assistant_widget(lang,path,relative)}</body></html>
'''


def cards(lang, current):
    u = CONTENT[lang]['ui']
    result = []
    articles=list(enumerate(CONTENT[lang]['articles']))
    if current==home(lang):articles=articles[-6:]
    for i, (title, intro, _) in articles:
        category = u[CATEGORY_LABELS[SLUGS[i][0]]]
        image = art_cover(SLUGS[i][1])
        width,height=art_dimensions(image)
        img=responsive_image(image,current,relative,title,"blog-cover"+(" poster-cover" if ARTICLE_DETAILS.get(SLUGS[i][1],{}).get("poster_download") else ""),sizes="(max-width: 780px) 92vw, 390px")
        result.append(f'<a class="blog-card" data-blog-category="{SLUGS[i][0]}" href="{relative(current, article(lang, i))}">{img}<div class="blog-card-body"><span class="pill">{E(category)}</span><h3>{E(title)}</h3><p>{E(intro)}</p><span class="blog-link">{E(u[15])}</span></div></a>')
    if current==home(lang):
        return campaign_callout(lang,current,relative)+'<div class="blog-grid home-journal-grid">'+''.join(result)+f'</div><p class="journal-more"><a class="btn" href="{relative(current,blog(lang))}">{E(u[1])} →</a></p>'+travel_teaser(lang,current,relative)
    filters = f'<div class="blog-filters" role="group" aria-label="{E(u[1])}"><button type="button" data-blog-filter="all" aria-pressed="true">{E(u[24])}</button>'
    filters += ''.join(f'<button type="button" data-blog-filter="{category}" aria-pressed="false">{E(u[label])}</button>' for category,label in CATEGORY_LABELS.items()) + '</div>'
    deal_link = f'<aside class="deals-callout"><h3>{E(DEAL_COPY[lang][0])}</h3><p>{E(DEAL_COPY[lang][7])}</p><a class="btn" href="{relative(current,deals_index(lang))}">{E(DEAL_COPY[lang][0])} →</a></aside>'
    return '<div class="blog-browser">' + filters + '<div class="blog-grid">' + ''.join(result) + '</div></div>' + campaign_callout(lang,current,relative) + deal_link + hanoi_teaser(lang,current,relative) + travel_teaser(lang,current,relative)


def write(path, html):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding='utf-8')


def build():
    build_images(ROOT)
    all_pages = []
    for lang in LANGUAGES:
        u = CONTENT[lang]['ui']
        counterparts = {code: home(code) for code in LANGUAGES}
        all_pages.append((home(lang), counterparts))
        path=home(lang)
        body=homepage_body(lang,path,relative,cards)
        write(path,document(lang,path,u[6],u[18],body,counterparts,homepage_schema(lang,path,url)))
        path = blog(lang)
        counterparts = {code: blog(code) for code in LANGUAGES}
        all_pages.append((path,counterparts))
        body = f'<section class="section soft"><div class="container"><h1>{E(u[1])}</h1><p class="lead main-blog-heading">{E(u[18])}</p>{cards(lang,path)}<p class="editorial-note">{E(u[13])}</p></div></section>'
        write(path, document(lang,path,u[1],u[18],body,counterparts,{'@context':'https://schema.org','@type':'Blog','name':u[1],'url':url(path),'inLanguage':lang}))
        for i, (title, intro, sections) in enumerate(CONTENT[lang]['articles']):
            path = article(lang,i)
            category = u[CATEGORY_LABELS[SLUGS[i][0]]]
            details = ARTICLE_DETAILS.get(SLUGS[i][1], {})
            description = details.get('description', {}).get(lang, details.get('description', {}).get('en', intro))
            booking = details.get('booking', service_url({'hotels':'hotels','tours':'tours','experiences':'tours','destinations':'tours'}.get(SLUGS[i][0], 'home')))
            counterparts = {code: article(code,i) for code in LANGUAGES}
            all_pages.append((path,counterparts))
            heading_language=' lang="en"' if details.get('practical_guide') and lang not in ('en','vi') else ''
            body = f'<div class="container"><article class="article"><nav class="breadcrumbs" aria-label="{E(u[19])}"><a href="{relative(path, blog(lang))}">{E(u[14])}</a> / {E(category)}</nav><span class="pill">{E(category)}</span><h1{heading_language}>{E(title)}</h1><p class="intro"{heading_language}>{E(intro)}</p>'
            image = art_cover(SLUGS[i][1])
            poster_class=' poster-feature' if details.get('poster_download') else ''
            width,height=art_dimensions(image)
            img=responsive_image(image,path,relative,title,sizes="(max-width: 800px) 92vw, 780px",eager=True)
            body += f'<figure class="featured-image{poster_class}">{img}<figcaption>{E(ART_COPY[lang][1] if image.startswith(("assets/ai-travel/","assets/campaign/")) else FEATURE_CAPTIONS[lang])}</figcaption></figure>'
            if details.get('poster_download'):
                variants=image_registry().get(image,{}).get('variants',[])
                webp=variants[-1]['file'] if variants else image
                body+=f'<p class="poster-downloads"><a class="text-link" href="{relative(path,image)}" download>{E(ART_COPY[lang][2])} · PNG →</a><a class="text-link" href="{relative(path,webp)}" download>WebP →</a></p>'
            if 'source_notes' in details:
                body += f'<aside class="editorial-note source-note">{E(details["source_notes"][lang])}</aside>'
            if details.get('source_summary_en') and lang not in ('en','vi'):
                body+=f'<section lang="en"><h2>Planning idea · English</h2><p>{E(details["source_summary_en"])}</p></section>'
            body += guide_before(lang,SLUGS[i][1])
            body += ''.join(f'<section><h2>{E(heading)}</h2><p>{E(text)}</p></section>' for heading,text in sections)
            body += guide_after(lang,path,relative,SLUGS[i][1])
            body += contextual_images(lang,path,relative,SLUGS[i][1])
            if details.get('booking_services'):
                body+='<div class="topic-shortcuts">'+''.join(f'<a href="{E(service_url(key))}" target="_blank" rel="sponsored noopener noreferrer" data-affiliate="idea-{key}">{E(service_labels(lang)[key])} · Trip.com →</a>' for key in details['booking_services'])+'</div>'
            body += f'<aside class="editorial-note">{E(u[13])}</aside><h2>{E(u[12])}</h2><ul class="source-list">'
            body += ''.join(f'<li><a href="{E(source)}" target="_blank" rel="noopener noreferrer">{E(label)}</a></li>' for label,source in SOURCES[i])
            body += f'</ul><p><a class="btn" href="{E(booking)}" target="_blank" rel="sponsored noopener noreferrer" data-affiliate="blog-{SLUGS[i][0]}">{E(u[8])}</a></p><p><a href="{relative(path, blog(lang))}">{E(u[14])} →</a></p></article></div>'
            structured = {'@context':'https://schema.org','@type':'BlogPosting','headline':title,'description':description,'image':BASE+image,'inLanguage':lang,'mainEntityOfPage':url(path),'publisher':{'@type':'Organization','name':'Stay in Da Nang'},'citation':[source for _,source in SOURCES[i]]}
            if details.get('published'):
                structured.update(datePublished=details['published'], dateModified=details['published'], author={'@type':'Organization','name':'Stay in Da Nang','url':BASE})
                structured['articleSection']=category
                if lang not in ('en','vi'):
                    structured['inLanguage']=[lang,'en']
            if details.get('place'):
                place=details['place']
                structured['spatialCoverage']={'@type':'Place','name':place['name'],'geo':{'@type':'GeoCoordinates','latitude':place['latitude'],'longitude':place['longitude']}}
            if details.get('places'):
                structured['spatialCoverage']=[{'@type':'Place','name':place['name'],'geo':{'@type':'GeoCoordinates','latitude':place['latitude'],'longitude':place['longitude']}} for place in details['places']]
            write(path,document(lang,path,title,description,body,counterparts,structured))
    all_pages.extend(build_campaign_pages(document,relative,url,LANGUAGES))
    all_pages.extend(build_collection_pages(document,relative,url,LANGUAGES))
    all_pages.extend(build_southern_pages(document,relative,url,LANGUAGES))
    all_pages.extend(build_service_pages(document,relative,url,LANGUAGES))
    export_deal_posts()
    all_pages.extend(build_deal_pages(document, relative, url, LANGUAGES))
    all_pages.extend(build_hanoi_pages(document, relative, url, LANGUAGES))
    all_pages.extend(build_travel_pages(document, relative, url, LANGUAGES))
    all_pages.extend(build_world_pages(document,relative,url,LANGUAGES))
    discovery_files(ROOT)
    build_assistant_data()
    ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    ET.register_namespace('xhtml','http://www.w3.org/1999/xhtml')
    sitemap = ET.Element('{http://www.sitemaps.org/schemas/sitemap/0.9}urlset')
    for path, counterparts in all_pages:
        entry = ET.SubElement(sitemap,'{http://www.sitemaps.org/schemas/sitemap/0.9}url')
        ET.SubElement(entry,'{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text = url(path)
        for code,target in counterparts.items():
            ET.SubElement(entry,'{http://www.w3.org/1999/xhtml}link',{'rel':'alternate','hreflang':code,'href':url(target)})
        ET.SubElement(entry,'{http://www.w3.org/1999/xhtml}link',{'rel':'alternate','hreflang':'x-default','href':url(counterparts['en'])})
    ET.ElementTree(sitemap).write(ROOT/'sitemap.xml',encoding='utf-8',xml_declaration=True)
    print(f'Generated {len(all_pages)-1} pages and sitemap with {len(all_pages)} URLs.')


if __name__ == '__main__':
    build()

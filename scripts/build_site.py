#!/usr/bin/env python3
"""Build multilingual HTML and sitemap using only the Python standard library."""
from pathlib import Path
from html import escape
import json
import os
import re
import xml.etree.ElementTree as ET
from content import CONTENT, LANGUAGES, SLUGS, SOURCES, SEARCH_COPY, ARTICLE_DETAILS

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://stayinvietnamtravel.github.io/stayindanang/'
BANNERS = [('S14984461', 'hotel', 900, 200), ('SB20219796', 'web_tripbanner', 300, 250), ('DB13678212', 'web_danang', 250, 250)]
E = escape
CATEGORY_LABELS = {'tips': 2, 'hotels': 3, 'tours': 4, 'destinations': 5}


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
    return f'<nav class="language-bar" aria-label="{E(CONTENT[lang]["ui"][17])}">' + ''.join(links) + '</nav>'


def ads(lang, ids=None):
    u = CONTENT[lang]['ui']
    frames = []
    search = ''
    for ident, sub, width, height in BANNERS:
        if ids is not None and ident not in ids:
            continue
        src = f'https://www.trip.com/partners/ad/{ident}?Allianceid=7874910&SID=295648032&trip_sub1={sub}'
        if ident == 'S14984461':
            title, description, hint = SEARCH_COPY[lang]
            search = f'<section class="hotel-search" id="hotel-search" aria-labelledby="hotel-search-title"><div class="container"><div class="search-panel"><p class="ad-label">{E(u[9])}</p><h2 id="hotel-search-title">{E(title)}</h2><p>{E(description)}</p><div class="ad-frame search-frame" data-ad-width="900" data-ad-height="200" data-ad-mode="scroll" style="width:900px" tabindex="0" role="region" aria-label="{E(title)}"><iframe src="{E(src)}" width="900" height="200" title="{E(title)}" id="{ident}" loading="eager" referrerpolicy="strict-origin-when-cross-origin" scrolling="no" style="border:0;width:900px;height:200px"></iframe></div><p class="search-hint">{E(hint)}</p><p class="ad-fallback"><a href="https://www.trip.com/t/Ygo40EEhzV2" target="_blank" rel="sponsored noopener noreferrer" data-affiliate="hotel-search-fallback">{E(u[10])} ↗</a></p></div></div></section>'
            continue
        frames.append(f'<div class="ad-frame" data-ad-width="{width}" data-ad-height="{height}" style="width:{width}px"><iframe src="{E(src)}" width="{width}" height="{height}" title="{E(u[9])} — {ident}" id="{ident}" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" scrolling="no" style="border:0;width:{width}px;height:{height}px"></iframe></div>')
    if not frames:
        return search
    return search + f'<section class="ad-section" aria-label="{E(u[9])}"><div class="container"><p class="ad-label">{E(u[9])}</p><div class="banner-grid">' + ''.join(frames) + f'</div><p class="ad-fallback"><a href="https://www.trip.com/t/Ygo40EEhzV2" target="_blank" rel="sponsored noopener noreferrer" data-affiliate="banner-fallback">{E(u[10])} ↗</a></p></div></section>'


def document(lang, path, title, description, body, counterparts, structured=None):
    u = CONTENT[lang]['ui']
    alternates = ''.join(f'<link rel="alternate" hreflang="{code}" href="{url(target)}">' for code, target in counterparts.items())
    alternates += f'<link rel="alternate" hreflang="x-default" href="{url(counterparts["en"])}">'
    schema = '' if structured is None else '<script type="application/ld+json">' + json.dumps(structured, ensure_ascii=False).replace('<', '\\u003c') + '</script>'
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0b3152"><title>{E(title)} | Stay in Da Nang</title>
<meta name="description" content="{E(description)}"><link rel="canonical" href="{url(path)}">{alternates}
<meta property="og:type" content="{'article' if structured and structured.get('@type') == 'BlogPosting' else 'website'}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(description)}"><meta property="og:url" content="{url(path)}">
<link rel="stylesheet" href="{relative(path, 'assets/site.css')}"><script src="{relative(path, 'assets/site.js')}" defer></script>{schema}</head><body>
<header class="header simple-header"><div class="container header-inner"><a class="logo" href="{relative(path, home(lang))}" aria-label="{E(u[20])}">☀ Stay in Da Nang</a>{language_links(lang, path, counterparts)}</div></header>
<nav class="container site-links" aria-label="{E(u[19])}"><a href="{relative(path, home(lang))}">{E(u[0])}</a><a href="{relative(path, blog(lang))}">{E(u[1])}</a></nav>
<main id="main">{body}</main><footer class="footer"><div class="container"><p>{E(u[21])}</p><p>{E(u[11])}</p><p>© 2026 Stay in Da Nang</p></div></footer></body></html>
'''


def cards(lang, current):
    u = CONTENT[lang]['ui']
    result = []
    for i, (title, intro, _) in enumerate(CONTENT[lang]['articles']):
        category = u[CATEGORY_LABELS[SLUGS[i][0]]]
        result.append(f'<a class="blog-card" href="{relative(current, article(lang, i))}"><span class="pill">{E(category)}</span><h3>{E(title)}</h3><p>{E(intro)}</p><span class="blog-link">{E(u[15])}</span></a>')
    return '<div class="blog-grid">' + ''.join(result) + '</div>'


def write(path, html):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding='utf-8')


def build():
    all_pages = []
    for lang in LANGUAGES:
        u = CONTENT[lang]['ui']
        counterparts = {code: home(code) for code in LANGUAGES}
        all_pages.append((home(lang), counterparts))
        if lang != 'en':
            path = home(lang)
            body = f'<section class="localized-hero"><div class="container"><div class="eyebrow">{E(u[21])}</div><h1>{E(u[6])}</h1><p>{E(u[7])}</p><div class="hero-actions"><a class="btn btn-light" href="#hotel-search">{E(SEARCH_COPY[lang][0])} ↓</a><a class="btn btn-outline" href="{relative(path, blog(lang))}">{E(u[1])} →</a></div></div></section>'
            body += ads(lang, ['S14984461'])
            body += f'<section class="section soft"><div class="container"><h2>{E(u[16])}</h2><p class="lead main-blog-heading">{E(u[18])}</p>{cards(lang,path)}</div></section>'
            body += ads(lang, ['SB20219796', 'DB13678212'])
            body += f'<section class="section"><div class="container"><h2>{E(u[3])} · {E(u[4])}</h2><p>{E(u[14])}</p><a class="btn" href="https://www.trip.com/t/Ygo40EEhzV2" target="_blank" rel="sponsored noopener noreferrer" data-affiliate="localized-booking">{E(u[8])}</a><p class="notice">{E(u[13])}</p></div></section>'
            write(path, document(lang,path,u[6],u[18],body,counterparts))
        path = blog(lang)
        counterparts = {code: blog(code) for code in LANGUAGES}
        all_pages.append((path,counterparts))
        body = f'<section class="section soft"><div class="container"><h1>{E(u[1])}</h1><p class="lead main-blog-heading">{E(u[18])}</p>{cards(lang,path)}<p class="editorial-note">{E(u[13])}</p></div></section>' + ads(lang)
        write(path, document(lang,path,u[1],u[18],body,counterparts,{'@context':'https://schema.org','@type':'Blog','name':u[1],'url':url(path),'inLanguage':lang}))
        for i, (title, intro, sections) in enumerate(CONTENT[lang]['articles']):
            path = article(lang,i)
            category = u[CATEGORY_LABELS[SLUGS[i][0]]]
            details = ARTICLE_DETAILS.get(SLUGS[i][1], {})
            booking = details.get('booking', 'https://www.trip.com/t/Ygo40EEhzV2')
            counterparts = {code: article(code,i) for code in LANGUAGES}
            all_pages.append((path,counterparts))
            body = f'<div class="container"><article class="article"><nav class="breadcrumbs" aria-label="{E(u[19])}"><a href="{relative(path, blog(lang))}">{E(u[14])}</a> / {E(category)}</nav><span class="pill">{E(category)}</span><h1>{E(title)}</h1><p class="intro">{E(intro)}</p>'
            if 'source_notes' in details:
                body += f'<aside class="editorial-note source-note">{E(details["source_notes"][lang])}</aside>'
            body += ''.join(f'<section><h2>{E(heading)}</h2><p>{E(text)}</p></section>' for heading,text in sections)
            body += f'<aside class="editorial-note">{E(u[13])}</aside><h2>{E(u[12])}</h2><ul class="source-list">'
            body += ''.join(f'<li><a href="{E(source)}" target="_blank" rel="noopener noreferrer">{E(label)}</a></li>' for label,source in SOURCES[i])
            body += f'</ul><p><a class="btn" href="{E(booking)}" target="_blank" rel="sponsored noopener noreferrer" data-affiliate="blog-{SLUGS[i][0]}">{E(u[8])}</a></p><p><a href="{relative(path, blog(lang))}">{E(u[14])} →</a></p></article></div>' + ads(lang,['SB20219796','DB13678212'])
            structured = {'@context':'https://schema.org','@type':'BlogPosting','headline':title,'description':intro,'inLanguage':lang,'mainEntityOfPage':url(path),'publisher':{'@type':'Organization','name':'Stay in Da Nang'},'citation':[source for _,source in SOURCES[i]]}
            write(path,document(lang,path,title,intro,body,counterparts,structured))
    # Keep the hand-maintained English landing page's blog cards in sync.
    english = ROOT / 'index.html'
    section = '<section class="section" id="blog"><div class="container"><div class="eyebrow">Practical travel guides</div><h2>Vietnam Travel Blog</h2><p class="lead main-blog-heading">Real places, hotel areas and flexible itineraries with official sources for further reading.</p>' + cards('en', 'index.html') + '</div></section>'
    updated, matches = re.subn(r'<section class="section" id="blog">.*?</section>', lambda _: section, english.read_text(encoding='utf-8'), flags=re.S)
    if matches != 1:
        raise ValueError('Expected exactly one English homepage blog section')
    english.write_text(updated, encoding='utf-8')
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

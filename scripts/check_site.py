#!/usr/bin/env python3
"""Check the generated site without a server or third-party packages."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, parse_qs, unquote
import json
import xml.etree.ElementTree as ET
from build_site import BASE, BANNERS, home, blog, article, url
from content import LANGUAGES

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.alternates = {}
        self.frames = []
        self.lang = None
        self.canonical = None
        self.script = None
        self.schemas = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'html':
            self.lang = a.get('lang')
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical = a['href']
        if tag == 'link' and a.get('rel') == 'alternate':
            self.alternates[a['hreflang']] = a['href']
        if tag == 'a' and 'hreflang' in a:
            self.links.append(('language', a['href']))
        if tag in ('a', 'link', 'script', 'img'):
            target = a.get('href') or a.get('src')
            if target:
                self.links.append((tag, target))
        if tag == 'iframe':
            self.frames.append(a)
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.script = ''

    def handle_data(self, data):
        if self.script is not None:
            self.script += data

    def handle_endtag(self, tag):
        if tag == 'script' and self.script is not None:
            self.schemas.append(json.loads(self.script))
            self.script = None


def check():
    paths = [p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*.html')]
    pages = {}
    for path in paths:
        page = Page()
        page.feed((ROOT/path).read_text(encoding='utf-8'))
        pages[path] = page
        assert page.lang in LANGUAGES, path
        assert page.canonical == url(path), (path, 'canonical')
        assert len(page.ids) == len(set(page.ids)), (path, 'duplicate id')
        assert set(page.alternates) == set(LANGUAGES) | {'x-default'}, (path, 'alternates')
        assert sum(kind == 'language' for kind, _ in page.links) == 7, (path, 'language selector')
        for kind, link in page.links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc:
                continue
            target = (ROOT/path).parent/unquote(parts.path) if parts.path else ROOT/path
            if target.is_dir():
                target /= 'index.html'
            assert target.is_file(), (path, 'missing local target', link)
            assert target.resolve().is_relative_to(ROOT), (path, 'outside site', link)
            if parts.fragment and target.suffix == '.html':
                dest = Page()
                dest.feed(target.read_text(encoding='utf-8'))
                assert unquote(parts.fragment) in dest.ids, (path, 'missing anchor', link)
        expected_ids = {b[0] for b in BANNERS}
        actual_ids = {f['id'] for f in page.frames}
        assert actual_ids <= expected_ids and len(page.frames) == len(actual_ids), (path, 'banners')
        if path == home(page.lang) or path == blog(page.lang):
            assert actual_ids == expected_ids, (path, 'all three banners required')
        for frame in page.frames:
            ident, sub, width, height = next(b for b in BANNERS if b[0] == frame['id'])
            src = urlsplit(frame['src'])
            assert src.scheme == 'https' and src.netloc == 'www.trip.com'
            assert src.path == '/partners/ad/'+ident
            assert parse_qs(src.query) == {'Allianceid':['7874910'],'SID':['295648032'],'trip_sub1':[sub]}
            assert frame['width'] == str(width) and frame['height'] == str(height)
            assert frame.get('title') and frame.get('loading') == 'lazy'
    assert len(paths) == 42, len(paths)
    for path, page in pages.items():
        for lang in LANGUAGES:
            target = page.alternates[lang].removeprefix(BASE)+'index.html'
            assert pages[target].lang == lang, (path, lang)
            assert pages[target].alternates[page.lang] == url(path), (path, 'reciprocal alternate', lang)
    sitemap = ET.parse(ROOT/'sitemap.xml')
    locations = [e.text for e in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    assert Counter(locations) == Counter(url(path) for path in paths), 'sitemap mismatch'
    print(f'PASS: {len(paths)} HTML pages, local links and anchors, 7-language navigation, reciprocal hreflang, banner parameters, structured data and sitemap.')


if __name__ == '__main__':
    check()

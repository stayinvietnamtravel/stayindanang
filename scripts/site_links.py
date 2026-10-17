"""Owner-supplied public links, rendered locally without third-party embeds."""
from pathlib import Path
from html import escape as E
from urllib.parse import urlsplit
import json
from functools import lru_cache

ROOT = Path(__file__).resolve().parents[1]
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M7 17 17 7M7 7h10v10"/></svg>'
LABELS = {
    'vi': ('Kết nối với Stay in Da Nang', 'Website khác', 'Mở trong tab mới'),
    'en': ('Connect with Stay in Da Nang', 'More websites', 'Opens in a new tab'),
    'zh': ('关注 Stay in Da Nang', '更多网站', '在新标签页中打开'),
    'zh-Hant': ('關注 Stay in Da Nang', '更多網站', '在新分頁中開啟'),
    'ru': ('Stay in Da Nang в сети', 'Другие сайты', 'Открывается в новой вкладке'),
    'ko': ('Stay in Da Nang 채널', '다른 웹사이트', '새 탭에서 열림'),
    'ja': ('Stay in Da Nang とつながる', 'その他のウェブサイト', '新しいタブで開きます'),
    'hi': ('Stay in Da Nang से जुड़ें', 'अन्य वेबसाइटें', 'नए टैब में खुलता है'),
    'fr': ('Retrouvez Stay in Da Nang', 'Autres sites', 'Ouvre un nouvel onglet'),
    'de': ('Stay in Da Nang online', 'Weitere Websites', 'Öffnet einen neuen Tab'),
    'es': ('Conecta con Stay in Da Nang', 'Otros sitios', 'Se abre en otra pestaña'),
    'th': ('ติดตาม Stay in Da Nang', 'เว็บไซต์อื่น', 'เปิดในแท็บใหม่'),
    'id': ('Terhubung dengan Stay in Da Nang', 'Situs lainnya', 'Terbuka di tab baru'),
}


@lru_cache(maxsize=1)
def links():
    items = json.loads((ROOT / 'data/site_links.json').read_text())['links']
    seen = set()
    for item in items:
        url = item['url']
        parts = urlsplit(url)
        if (parts.scheme != 'https' or not parts.hostname or parts.username or parts.password
                or any(ord(c) < 33 for c in url) or item['kind'] not in ('social', 'website')
                or not item['label'].strip() or url in seen):
            raise ValueError('Invalid or duplicate public footer link')
        seen.add(url)
    return items


def identity_urls():
    return [item['url'] for item in links() if item.get('same_as') is True]


def footer(lang):
    labels = LABELS[lang]
    groups = []
    for kind, heading in (('social', labels[0]), ('website', labels[1])):
        items = [item for item in links() if item['kind'] == kind]
        if not items:
            continue
        anchors = ''.join(
            f'<a href="{E(item["url"], quote=True)}" target="_blank" '
            f'rel="me noopener noreferrer" aria-label="{E(item["label"] + " · " + labels[2], quote=True)}">'
            f'{E(item["label"])} {ARROW}</a>'
            if item.get('same_as') else
            f'<a href="{E(item["url"], quote=True)}" target="_blank" rel="noopener noreferrer" '
            f'aria-label="{E(item["label"] + " · " + labels[2], quote=True)}">'
            f'{E(item["label"])} {ARROW}</a>'
            for item in items)
        groups.append(f'<section class="footer-link-group"><h2>{E(heading)}</h2>'
                      f'<nav aria-label="{E(heading)}">{anchors}</nav></section>')
    return '<div class="footer-network">' + ''.join(groups) + '</div>' if groups else ''

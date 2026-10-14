#!/usr/bin/env python3
"""Import spreadsheet content as data; never execute formulas or image briefs."""
from pathlib import Path
from urllib.parse import urlsplit
import argparse
import hashlib
import json
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {
    'SEO Blog Title': 'seo_title_en',
    'Travel Blog Content (EN)': 'blog_content_en',
    'Facebook / X Post (EN)': 'social_post_en',
    'Booking CTA': 'booking_cta_en',
    'SEO Keywords': 'seo_keywords',
    'Hashtags': 'hashtags',
    'Hotel Image URL (verified)': 'hotel_image_url',
    'Image Search / Creative Brief': 'image_brief',
    'Image Status': 'image_status',
    'Google Place ID': 'google_place_id',
    'Image Source': 'image_source',
    'Photo Attribution': 'photo_attribution',
}


def main():
    from openpyxl import load_workbook
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workbook', type=Path)
    args = parser.parse_args()
    path = args.workbook
    previous = json.loads((ROOT/'data/bookdeal.json').read_text(encoding='utf-8'))
    old_by_name = {row['name']: row for row in previous['rows']}
    old_by_url = {row['url']: row for row in previous['rows']}
    workbook = load_workbook(path, data_only=True)
    records = []
    for sheet in workbook:
        if sheet.title not in ('Top Deals', 'Hot Sellers'):
            raise ValueError(f'Unsupported sheet: {sheet.title}')
        header = None
        for cells in sheet:
            names = {cell.value: cell.column-1 for cell in cells if isinstance(cell.value, str)}
            if 'ten' in names and 'link' in names:
                header = names
                continue
            if not header:
                continue
            name = cells[header['ten']].value
            link_cell = cells[header['link']]
            link = link_cell.value
            if not name and not link:
                continue
            if not isinstance(name, str) or not isinstance(link, str):
                raise ValueError(f'Invalid name/link in {sheet.title}:{cells[0].row}')
            parsed = urlsplit(link)
            if parsed.scheme != 'https' or parsed.netloc != 'www.trip.com' or not re.fullmatch(r'/w/[A-Za-z0-9]+', parsed.path) or parsed.query or parsed.fragment:
                raise ValueError(f'Unexpected hotel booking URL for {name}')
            if link_cell.hyperlink and link_cell.hyperlink.target != link:
                raise ValueError(f'Hyperlink/value conflict for {name}')
            old = old_by_name.get(name) or old_by_url.get(link)
            normalized = unicodedata.normalize('NFKD', name).encode('ascii','ignore').decode().lower()
            row = dict(old or {})
            row.update(name=name, display_name=name.split(' - ')[0], url=link, group=sheet.title, sheet_row=cells[0].row)
            row.setdefault('slug', re.sub('[^a-z0-9]+','-',normalized).strip('-'))
            row.setdefault('included', not ('hoi an' in name.lower() or 'an bang' in name.lower()))
            row.setdefault('location_note', 'coastal-corridor' if name == 'Shilla Monogram Danang' else None)
            for label,key in FIELDS.items():
                row[key] = cells[header[label]].value if label in header else None
            for field in ('blog_content_en','social_post_en','booking_cta_en'):
                value = row[field]
                if not isinstance(value, str):
                    raise ValueError(f'Missing {field}: {name}')
                if re.findall(r'https?://\S+', value) != [link]:
                    raise ValueError(f'Booking URL mismatch in {field}: {name}')
            if not row['seo_title_en']:
                raise ValueError(f'Missing SEO title: {name}')
            records.append(row)
    if len({r['name'] for r in records}) != len(records) or len({r['url'] for r in records}) != len(records):
        raise ValueError('Duplicate hotel names or booking URLs')
    old_names = set(old_by_name)
    new_names = {r['name'] for r in records}
    if old_names-new_names:
        raise ValueError('Source omits existing hotels; review required before replacing the dataset')
    data = {
        'source': path.name,
        'previous_source': previous.get('previous_source',previous['source']),
        'source_date': None,
        'contains_prices': False,
        'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'google_sheet_url': 'https://docs.google.com/spreadsheets/d/1S9652irrTDY6i_tOy_VCDLtFwtSys9nyuw0uB_S4HyE/edit?gid=1507230027',
        'rows': records,
    }
    (ROOT/'data/bookdeal.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Imported {len(records)} rows; {sum(r["included"] for r in records)} included. Verified all blog/social/CTA URLs against each hotel link. Image URLs supplied: {sum(bool(r["hotel_image_url"]) for r in records)}.')


if __name__ == '__main__':
    main()

"""Practical sourced articles and accessible itinerary/related-reading blocks."""
from pathlib import Path
from html import escape as E
import json

ROOT = Path(__file__).resolve().parents[1]
GUIDES = json.loads((ROOT / 'data/practical_guides.json').read_text())['guides']
ROUTES = json.loads((ROOT / 'data/affiliate_routes.json').read_text())


def register(content, languages, slugs, sources, details):
    for guide in GUIDES:
        slugs.append((guide['category'], guide['slug']))
        sources.append(guide['sources'])
        details[guide['slug']] = {
            'booking_services': guide['services'],
            'practical_guide': guide['slug'],
            'published': guide['published'],
            'booking': ROUTES['default_url'] if guide['service'] == 'home' else ROUTES['services'][guide['service']],
            'poster_download': True,
            'description': {code: guide[code]['description'] for code in ('en', 'vi')},
        }
        if guide.get('places'):
            details[guide['slug']]['places'] = guide['places']
        elif guide.get('place'):
            details[guide['slug']]['place'] = guide['place']
        for lang in languages:
            draft = guide['vi' if lang == 'vi' else 'en']
            # English content is explicitly marked in other language editions.
            intro = draft['intro']
            sections = draft['sections'] if lang in ('en', 'vi') else []
            content[lang]['articles'].append([draft['title'], intro, sections])


def find(slug):
    return next((guide for guide in GUIDES if guide['slug'] == slug), None)


def before_sections(lang, slug):
    guide = find(slug)
    if not guide:
        return ''
    code = 'vi' if lang == 'vi' else 'en'
    draft = guide[code]
    updated = 'Xuất bản' if code == 'vi' else 'Published'
    label = 'Lịch trình và các bước tham khảo' if code == 'vi' else 'Suggested route and planning steps'
    rows = ''.join(f'<tr><th scope="row">{E(day)}</th><td>{E(plan)}</td></tr>'
                   for day, plan in draft['itinerary'])
    body = (f'<p class="article-updated" lang="{code}">{updated}: '
            f'<time datetime="{guide["published"]}">{guide["published"]}</time> · Stay in Da Nang</p>'
            f'<div class="article-itinerary" lang="{code}"><table><caption>{label}</caption>'
            f'<tbody>{rows}</tbody></table></div>')
    if lang not in ('en', 'vi'):
        body += '<section class="english-guide" lang="en"><h2>Full planning guide · English</h2>'
        body += f'<p>{E(draft["intro"])}</p>'
        body += ''.join(f'<section><h3>{E(heading)}</h3><p>{E(text)}</p></section>'
                        for heading, text in draft['sections'])
        body += '</section>'
    return body


def after_sections(lang, current, relative, slug):
    guide = find(slug)
    if not guide:
        return ''
    code = 'vi' if lang == 'vi' else 'en'
    draft = guide[code]
    heading = 'Câu hỏi thường gặp' if code == 'vi' else 'Common planning questions'
    body = f'<section class="article-faq" lang="{code}"><h2>{heading}</h2>'
    body += ''.join(f'<details><summary>{E(question)}</summary><p>{E(answer)}</p></details>'
                    for question, answer in draft['faq'])
    body += '</section>'
    heading = 'Đọc tiếp để hoàn thiện hành trình' if code == 'vi' else 'Continue planning your trip'
    body += f'<aside class="article-related" lang="{code}"><h2>{heading}</h2><ul>'
    for related_slug in guide['related']:
        related = find(related_slug)
        target = f'blog/{lang}/{related["category"]}/{related_slug}/index.html'
        body += f'<li><a href="{relative(current, target)}">{E(related[code]["title"])}</a></li>'
    body += '</ul></aside>'
    return body

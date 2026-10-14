#!/usr/bin/env python3
"""Cache attributed RSS headlines, never execute or republish article bodies."""
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
SOURCES=json.loads((ROOT/'data/travel_sources.json').read_text())
MAX_BYTES=2_000_000
MAX_PER_SOURCE=12
ALIASES={
 'vietnam':['vietnam','viet nam','hanoi','da nang','ho chi minh','hoi an'],
 'thailand':['thailand','thai','bangkok','phuket','chiang mai'],
 'japan':['japan','japanese','tokyo','kyoto','osaka'],
 'south-korea':['south korea','seoul','busan','jeju'],
 'singapore':['singapore'], 'indonesia':['indonesia','bali','jakarta'],
 'malaysia':['malaysia','kuala lumpur','penang'], 'philippines':['philippines','manila','cebu'],
 'india':['india','delhi','mumbai'], 'france':['france','paris'],
 'germany':['germany','berlin'], 'spain':['spain','madrid','barcelona'],
 'italy':['italy','rome','milan'], 'united-kingdom':['united kingdom','britain','london'],
 'united-states':['united states','new york','los angeles'],
 'canada':['canada','toronto','vancouver'], 'australia':['australia','sydney','melbourne'],
 'new-zealand':['new zealand','auckland'],
}


class PlainText(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.ignored=0
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'):self.ignored+=1
    def handle_endtag(self,tag):
        if tag in ('script','style'):self.ignored=max(0,self.ignored-1)
    def handle_data(self,text):
        if not self.ignored:self.parts.append(text)


def plain(value):
    parser=PlainText();parser.feed(unescape(value or ''))
    return ' '.join(' '.join(parser.parts).split())[:300]


def date_value(value):
    if not value:return None
    try:
        date=parsedate_to_datetime(value)
    except (ValueError,TypeError,OverflowError):
        try:date=datetime.fromisoformat(value.replace('Z','+00:00'))
        except (ValueError,TypeError):return None
    if date.tzinfo is None:return None
    return date.astimezone(timezone.utc)


def countries(title,default):
    matched=[country for country,aliases in ALIASES.items() if any(re.search(r'(?<!\w)'+re.escape(alias)+r'(?!\w)',title,re.I) for alias in aliases)]
    if default!='international' and default not in matched:matched.append(default)
    return matched or ['international']


def parse_feed(raw,source,now):
    if len(raw)>MAX_BYTES or b'<!DOCTYPE' in raw.upper():raise ValueError('Unsafe or oversized feed')
    root=ET.fromstring(raw)
    tag=root.tag.rsplit('}',1)[-1]
    if tag not in ('rss','feed','RDF'):raise ValueError('Response is not an RSS/Atom feed')
    entries=[el for el in root.iter() if el.tag.rsplit('}',1)[-1] in ('item','entry')]
    records=[];seen=set()
    for item in entries:
        values={};href=None
        for child in item:
            local=child.tag.rsplit('}',1)[-1]
            if local=='link' and child.get('href') and child.get('rel','alternate')=='alternate':href=child.get('href')
            if child.text:values[local]=child.text.strip()
        link=(href or values.get('link','')).strip()
        try:
            parsed=urlsplit(link)
            if parsed.scheme!='https' or parsed.hostname not in source['article_hosts'] or parsed.username or parsed.password or parsed.port not in (None,443):continue
        except ValueError:
            continue
        title=plain(values.get('title'))
        if not title or link in seen:continue
        date=date_value(values.get('pubDate') or values.get('published') or values.get('date'))
        if date and (date>now+timedelta(hours=1) or date<now-timedelta(days=60)):continue
        seen.add(link)
        records.append({'title':title,'url':link,'source_id':source['id'],'publisher':source['name'],'published_at':date.isoformat() if date else None,'countries':countries(title,source['default_country'])})
    records.sort(key=lambda item:item['published_at'] or '',reverse=True)
    return records[:MAX_PER_SOURCE]


def refresh():
    target=ROOT/'data/travel_news.json'
    previous=json.loads(target.read_text()) if target.exists() else {'last_updated':None,'articles':[],'sources':{}}
    now=datetime.now(timezone.utc)
    results=[];states=dict(previous.get('sources',{}));success=0
    for source in SOURCES['feeds']:
        old_state=states.get(source['id'],{})
        try:
            request=Request(source['url'],headers={'User-Agent':'StayInDaNang-News/1.0 (+https://github.com/stayinvietnamtravel/stayindanang)','Accept':'application/rss+xml, application/atom+xml, application/xml, text/xml'})
            with urlopen(request,timeout=25) as response:
                raw=response.read(MAX_BYTES+1)
            records=parse_feed(raw,source,now)
            results.extend(records);success+=1
            states[source['id']]={'last_attempt_at':now.isoformat(),'last_success_at':now.isoformat(),'status':'ok','count':len(records)}
            print(f'{source["name"]}: fetched {len(records)} recent attributed headlines.')
        except Exception as error:
            # Keep valid old headlines for a temporarily unavailable publisher.
            results.extend(item for item in previous.get('articles',[]) if item['source_id']==source['id'])
            states[source['id']]={'last_attempt_at':now.isoformat(),'last_success_at':old_state.get('last_success_at'),'status':'unavailable','count':old_state.get('count',0)}
            print(f'{source["name"]}: unavailable ({type(error).__name__}); existing cache retained.',file=sys.stderr)
    unique={}
    for item in results:
        published=date_value(item.get('published_at'))
        if published and published<now-timedelta(days=60):continue
        unique.setdefault(item['url'],item)
    articles=sorted(unique.values(),key=lambda item:item['published_at'] or '',reverse=True)[:36]
    data={'last_updated':now.isoformat() if success else previous.get('last_updated'),'articles':articles,'sources':states}
    target.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    if success==0:
        print('No feeds fetched successfully; no current-news readiness claim.',file=sys.stderr)
        return 1
    return 0


if __name__=='__main__':
    sys.exit(refresh())

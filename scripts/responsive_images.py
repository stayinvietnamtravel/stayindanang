"""Standard-library rendering of already exported lightweight artwork."""
from pathlib import Path
from html import escape as E
import json
from functools import lru_cache
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'assets/image-variants.json'
@lru_cache(maxsize=1)
def registry():return json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
def image(path,current,relative,alt='',css='',sizes='(max-width: 700px) 80vw, 300px',eager=False):
    data=registry()
    entry=data.get(path);variants=entry['variants'] if entry else []
    source=variants[min(1,len(variants)-1)]['file'] if eager and variants else variants[0]['file'] if variants else path
    width,height=(entry['width'],entry['height']) if entry else (1020,540)
    attrs=f' src="{relative(current,source)}" width="{width}" height="{height}" alt="{E(alt)}" decoding="async"'
    if variants:attrs+=' srcset="'+', '.join(relative(current,v['file'])+' '+str(v['width'])+'w' for v in variants)+'" sizes="'+E(sizes)+'"'
    attrs+=f' class="{E(css)}"' if css else ''
    attrs+=' loading="eager" fetchpriority="high"' if eager else ' loading="lazy"'
    return '<img'+attrs+'>'

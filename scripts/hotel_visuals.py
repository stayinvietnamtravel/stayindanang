"""Lightweight city artwork with accessible, property-specific HTML typography."""
from html import escape as E
from pathlib import Path
from responsive_images import image as responsive_image
from travel_art import COPY
ROOT=Path(__file__).resolve().parents[1]
def cover(h,city,lang,current,relative,eager=False):
    from southern_hotels import CITY_LABELS
    name=h.get('display_name',h['name'])
    scenes={'hanoi':'hotel-hanoi-scene','da-nang':'hotel-danang-scene','ho-chi-minh-city':'hotel-saigon-scene','phu-quoc':'hotel-phu-quoc-scene'}
    scene='assets/ai-travel/'+scenes.get(city,'hotel-southern-coast-scene')+'.png'
    label={'hanoi':'Hà Nội','da-nang':'Đà Nẵng','phu-quoc':'Phú Quốc',**CITY_LABELS}[city]
    img=responsive_image(scene,current,relative,name+' · '+label+' · '+COPY[lang][1],sizes='(max-width:700px) 90vw, 300px' if not eager else '(max-width:800px) 92vw, 780px',eager=eager)
    return f'<div class="hotel-visual" data-hotel-art="{E(h["slug"])}">{img}<span class="image-ai-badge" title="{E(COPY[lang][1])}">AI</span><span class="hotel-visual-context">{E(label)} · {E(" · ".join(h.get("groups",[h["group"]])))}</span><div class="hotel-visual-title"><small>STAY IN DA NANG · VIETNAM</small><strong>{E(name)}</strong></div></div>'

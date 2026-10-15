"""Lightweight city artwork with accessible, property-specific HTML typography."""
from html import escape as E
from pathlib import Path
from responsive_images import image as responsive_image
from travel_art import COPY
ROOT=Path(__file__).resolve().parents[1]
def cover(h,city,lang,current,relative,eager=False):
    name=h.get('display_name',h['name']);scene='assets/ai-travel/hotel-'+('hanoi' if city=='hanoi' else 'danang')+'-scene.png'
    if not (ROOT/scene).exists():
        scene='assets/ai-travel/hotel-inspiration.png' if city!='hanoi' else 'assets/ai-travel/city-walks.png'
    label='Hà Nội' if city=='hanoi' else 'Đà Nẵng'
    img=responsive_image(scene,current,relative,name+' · '+label+' · '+COPY[lang][1],sizes='(max-width:700px) 90vw, 300px' if not eager else '(max-width:800px) 92vw, 780px',eager=eager)
    return f'<div class="hotel-visual" data-hotel-art="{E(h["slug"])}">{img}<span class="image-ai-badge" title="{E(COPY[lang][1])}">AI</span><span class="hotel-visual-context">{E(label)} · {E(h["group"])}</span><div class="hotel-visual-title"><small>STAY IN DA NANG · VIETNAM</small><strong>{E(name)}</strong></div></div>'

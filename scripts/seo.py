"""Truthful publisher identity, discoverability metadata and AI-readable guide index."""
from html import escape as E
from pathlib import Path
import json
BASE='https://stayinvietnamtravel.github.io/stayindanang/'
def extras(lang,path,title,description,image=None):
    image=image or BASE+'assets/social/travel-guide.png'
    website={'@context':'https://schema.org','@type':'WebSite','@id':BASE+'#website','url':BASE,'name':'Stay in Da Nang','publisher':{'@id':BASE+'#organization'},'inLanguage':lang}
    organization={'@context':'https://schema.org','@type':'Organization','@id':BASE+'#organization','name':'Stay in Da Nang','url':BASE,'sameAs':['https://x.com/stayindanang']}
    return f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(title)}"><meta name="twitter:description" content="{E(description)}"><meta name="twitter:image" content="{E(image)}">'+''.join('<script type="application/ld+json">'+json.dumps(obj,ensure_ascii=False).replace('<','\\u003c')+'</script>' for obj in (website,organization))
def discovery_files(root):
    from world_guides import REGION_KEYS
    text='# Stay in Da Nang\n\n> Independent travel planning guides, hotel affiliate links and attributed destination forecasts.\n\n'
    text+='## International guides\n\n'
    for region in REGION_KEYS:
        text+=f'- [{region.title()} travel planning]({BASE}explore/en/{region}/): Sample routes, food ideas, destination lists and official tourism references.\n'
    from travel_services import KEYS
    text+='\n## Booking topic guides\n\n'
    for key in KEYS:text+=f'- [{key.title()} planning]({BASE}travel/en/{key}/): Category-specific advice and disclosed Trip.com affiliate links.\n'
    text+=f'\n## Vietnam and services\n\n- [Travel blog]({BASE}blog/)\n- [Hotel collection: Hot Deals and Hot Sellers]({BASE}stays/en/)\n- [Da Nang hotels]({BASE}deals/en/)\n- [Hanoi hotel guides]({BASE}blog/en/destinations/hanoi/)\n- [Official tourism sources]({BASE}resources/en/)\n- [Attributed travel news]({BASE}news/en/)\n- [World weather]({BASE}#weather)\n- [Sitemap]({BASE}sitemap.xml)\n\n## Editorial scope\n\nGuides are planning suggestions, not firsthand reviews. Check entry requirements, opening hours and availability with official sources. Hotel links are affiliate links; prices are checked on Trip.com. Weather uses MET Norway Locationforecast, CC BY 4.0, at fixed city-center coordinates. Forecast times use the destination IANA timezone. Model update timestamps and missing/stale data are visible. Forecasts are not observations or a substitute for official local warnings. This file is an optional reading index, not a guarantee of crawler support or search visibility.\n'
    (Path(root)/'llms.txt').write_text(text,encoding='utf-8')

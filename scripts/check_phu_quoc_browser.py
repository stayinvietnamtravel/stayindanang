"""Optional browser regression checks; start a local static server first."""
import sys,json,os,shutil
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
BASE=os.environ.get('STAYINDANANG_TEST_BASE_URL','http://127.0.0.1:8000').rstrip('/')+'/'
from content import LANGUAGES
from phu_quoc_hotels import HOTELS,index_path,post_path
from marketplace import CONFIG
from hotel_collection import rows
sheraton=next(h for h in HOTELS if len(h['offers'])==2)
seller=sheraton['offers'][0]['url'];deal=sheraton['offers'][1]['url']
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path=os.environ.get('STAYINDANANG_CHROMIUM_PATH') or shutil.which('chromium'),args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':390,'height':844});errors=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.route('**/*',lambda r:r.continue_() if r.request.url.startswith(BASE) else r.abort())
 def visible():return page.locator('[data-hotel-collection] [data-hotel-group]:visible').count()
 def route(expected):
  assert page.locator(f'[data-saved-id="hotel-{sheraton["slug"]}"] .hotel-book-link').get_attribute('href')==expected
 for lang in LANGUAGES:
  page.goto(BASE+index_path(lang))
  assert visible()==44,lang
  assert page.locator('.footer-network a').count()==8
  page.locator('[data-hotel-tab="top-deals"]').click();assert visible()==24,(lang,'deals');route(deal)
  page.locator('[data-hotel-tab="hot-sellers"]').click();assert visible()==21,(lang,'sellers');route(seller)
  page.locator('[data-hotel-tab="all"]').click();assert visible()==44;route(seller)
  page.locator('[data-hotel-search]').fill('sheraton');assert visible()==1
  page.locator('[data-hotel-tab="top-deals"]').click();assert visible()==1;route(deal)
  page.locator('[data-hotel-search]').fill('no-such-property');assert visible()==0 and page.locator('.collection-empty').is_visible()
  page.locator('[data-hotel-reset]').click();assert visible()==44;route(seller)
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),lang
 for lang in ('vi','en'):
  for h in HOTELS:
   page.goto(BASE+post_path(lang,h))
   assert page.locator('.hotel-booking-options a').count()==len(h['offers'])
   assert page.locator('.hotel-booking-options a').evaluate_all('(nodes)=>nodes.map(n=>n.href)')==[o['url'] for o in h['offers']]
   assert page.locator('.hotel-visual-title strong').inner_text()==h['name']
   page.wait_for_function('document.querySelector(".featured-image img").naturalWidth>0')
   assert page.locator('.featured-image img').evaluate('(e)=>e.currentSrc').endswith('.webp')
   assert page.locator('.article-related a').count()==3
   assert page.locator('.article-faq details').count()==2
   assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),(lang,h['name'])
 for lang in ('vi','en','ja'):
  page.goto('http://127.0.0.1:8000/stays/'+lang+'/')
  assert visible()==154
  page.locator('[data-hotel-city-filter="phu-quoc"]').click();assert visible()==44
  page.locator('[data-hotel-tab="top-deals"]').click();assert visible()==24;route(deal)
  page.locator('[data-hotel-tab="hot-sellers"]').click();assert visible()==21;route(seller)
  page.locator('[data-hotel-search]').fill('does-not-exist');page.locator('[data-hotel-reset]').click();assert visible()==154
 page.goto(BASE+'vi/')
 page.locator('.booking-destination').select_option('phu-quoc');page.locator('[data-booking-service="hotels"]').click()
 assert page.locator('.booking-property option').count()==45
 for h in HOTELS:
  page.locator('.booking-property').select_option(h['slug'])
  assert page.locator('.booking-action').get_attribute('href')==h['url'],h['name']
 page.locator('[data-booking-service="flights"]').click();assert page.locator('.booking-action').get_attribute('href')==CONFIG['services']['flights']
 page.locator('[data-booking-service="hotels"]').click();page.locator('.booking-destination').select_option('hanoi')
 assert page.locator('.booking-action').get_attribute('href')==CONFIG['services']['hotels']
 page.locator('[data-hotel-city-filter="phu-quoc"]').click();assert visible()==7
 page.locator('[data-hotel-tab="top-deals"]').click();assert visible()==4;route(deal)
 page.locator('[data-hotel-tab="hot-sellers"]').click();assert visible()==4;route(seller)
 page.locator('[data-save-id="hotel-'+sheraton['slug']+'"]').click();page.locator('[data-hotel-tab="saved"]').click();assert visible()==1
 page.locator('.chat-open').click()
 for group,url in [('Top Deals',deal),('Hot Sellers',seller)]:
  page.locator('#travel-chat-input').fill(sheraton['name']+' '+group);page.locator('.chat-form').evaluate('(e)=>e.requestSubmit()')
  page.wait_for_function('(url)=>{const replies=document.querySelectorAll(".chat-assistant");return replies.length>0&&replies[replies.length-1].querySelector("a")?.href===url}',arg=url)
 page.locator('.chat-close').click()
 page.goto(BASE+index_path('vi'));page.set_viewport_size({'width':1440,'height':1000});page.locator('.collection-card').first.scroll_into_view_if_needed();page.wait_for_function('document.querySelector(".collection-card img").naturalWidth>0');page.screenshot(path='/tmp/phu-quoc-catalog-desktop.png')
 page.set_viewport_size({'width':390,'height':844});page.goto(BASE+post_path('vi',sheraton));page.locator('.hotel-booking-options').scroll_into_view_if_needed();page.screenshot(path='/tmp/phu-quoc-sheraton-mobile.png')
 page.locator('.featured-image').scroll_into_view_if_needed();page.screenshot(path='/tmp/phu-quoc-hotel-hero-mobile.png')
 assert not errors,errors
 browser.close()
print('PASS: 13 indexes, 88 property pages, 154-hotel catalog, category-specific Sheraton routing, 44 planner targets, chat group links, favorites, responsive artwork and no overflow/JS errors.')

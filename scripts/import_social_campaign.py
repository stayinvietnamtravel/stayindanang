"""Import CSV cells as campaign data; never execute embedded instructions."""
from pathlib import Path
from urllib.parse import urlsplit,urlencode
import argparse,csv,json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
BASE='https://stayinvietnamtravel.github.io/stayindanang/'
def main():
 p=argparse.ArgumentParser();p.add_argument('posts',type=Path);p.add_argument('prompts',type=Path);a=p.parse_args()
 posts=list(csv.DictReader(a.posts.open(encoding='utf-8-sig',newline='')));prompts=list(csv.DictReader(a.prompts.open(encoding='utf-8-sig',newline='')))
 assert len(posts)==150 and len(prompts)==30
 platforms={'Facebook','Instagram','X','TikTok','Pinterest'};assert {r['Platform'] for r in posts}==platforms
 config=json.loads((ROOT/'data/affiliate_routes.json').read_text());days=[]
 for image in prompts:
  day=int(image['Day']);matches=[r for r in posts if int(r['Day'])==day];assert len(matches)==5 and {r['Platform'] for r in matches}==platforms
  assert all(r['Post Title']==image['Post Title'] for r in matches)
  for r in matches:
   u=urlsplit(r['Website UTM Link']);assert u.scheme=='https' and u.hostname=='stayinvietnamtravel.github.io' and u.path=='/stayindanang/'
   u=urlsplit(r['Trip.com Affiliate URL']);assert u.scheme=='https' and u.netloc=='www.trip.com' and re.fullmatch('/t/[A-Za-z0-9]+',u.path)
  slug='campaign-'+str(day).zfill(2)+'-'+re.sub('[^a-z0-9]+','-',image['Post Title'].lower()).strip('-')
  service='hotels' if 6<=day<=15 else 'tours' if 16<=day<=23 else {24:'flights',25:'home',26:'cars',27:'transfers',28:'cars'}.get(day,'home')
  category='hotels' if service=='hotels' else 'tours' if service=='tours' else 'tips'
  fb=next(r for r in matches if r['Platform']=='Facebook');paragraphs=fb['English Caption'].split('\n\n');summary=paragraphs[1].strip()
  days.append({'day':day,'slug':slug,'category':category,'title_en':image['Post Title'],'summary_en':summary,'seo_keywords':image['SEO Keywords'],'image_concept':image['Image Concept'],'image_prompt':image['Image Prompt'],'image':'assets/campaign/day-'+str(day).zfill(2)+'.png','service':service,'affiliate_url':config['services'].get(service,config['default_url']),'original_posts':matches})
 assert {d['day'] for d in days}==set(range(1,31));days.sort(key=lambda d:d['day'])
 out={'source_sha256':{'posts':hashlib.sha256(a.posts.read_bytes()).hexdigest(),'prompts':hashlib.sha256(a.prompts.read_bytes()).hexdigest()},'imported_date':'2026-10-16','source_rows':150,'days':days}
 (ROOT/'data/social_campaign.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print('Imported 150 original social drafts into 30 distinct topics; normalized service links and preserved source captions/prompts as data.')
if __name__=='__main__':main()

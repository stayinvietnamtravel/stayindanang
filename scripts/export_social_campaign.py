"""Build platform-ready JPEGs/captions and a private review bundle from campaign data."""
from pathlib import Path
from urllib.parse import urlencode
from PIL import Image,ImageOps
import csv,json,re,hashlib,zipfile
ROOT=Path(__file__).resolve().parents[1]
BASE='https://stayinvietnamtravel.github.io/stayindanang/'
EXPORT=ROOT.parent/'stayindanang-admin-exports'/'social-campaign'
PLATFORMS={'x':'X','facebook':'Facebook','instagram':'Instagram'}
def x_weight(text):
    without_urls=re.sub(r'https?://\S+','',text)
    return sum(1 if ord(c)<128 else 2 for c in without_urls)+23*len(re.findall(r'https?://\S+',text))
def blog_path(item,lang='en'):return f'blog/{lang}/{item["category"]}/{item["slug"]}/'
def caption(item,platform):
    params={'utm_source':platform,'utm_medium':'organic_social','utm_campaign':'vietnam_30days_2026','utm_content':f'd{item["day"]:02d}_{item["slug"]}'}
    url=BASE+blog_path(item)+'?'+urlencode(params)
    summary=item['summary_en']
    if platform=='x':
        short=summary.split('. ')[0].rstrip('.')+'.'
        text=f'{item["title_en"]}\n{short}\n{url}\nAI illustration. Affiliate links. #VietnamTravel'
        while x_weight(text)>280 and len(short)>20:
            short=short.rsplit(' ',1)[0].rstrip('.,')+'…'
            text=f'{item["title_en"]}\n{short}\n{url}\nAI illustration. Affiliate links. #VietnamTravel'
        if x_weight(text)>280:raise ValueError('X caption exceeds conservative weighted length')
    else:
        hashtags=next(r['Hashtags'] for r in item['original_posts'] if r['Platform']==PLATFORMS[platform])
        text=f'{item["title_en"]}\n\n{summary}\n\nRead the guide'+(' (copy the link)' if platform=='instagram' else '')+f': {url}\n\nAI illustration, not a verified property photograph. Affiliate links may earn us a commission.\n\n{hashtags}'
        if platform=='instagram' and len(text)>2200:raise ValueError('Instagram caption is too long')
    return text,url

def main():
    data=json.loads((ROOT/'data/social_campaign.json').read_text());out=[]
    directory=ROOT/'assets/campaign/social';directory.mkdir(parents=True,exist_ok=True);EXPORT.mkdir(parents=True,exist_ok=True)
    for item in data['days']:
        source=ROOT/item['image']
        if not source.is_file():raise ValueError('Poster missing for day '+str(item['day']))
        with Image.open(source) as original:
            original=ImageOps.exif_transpose(original).convert('RGB')
            for platform in PLATFORMS:
                maximum=(1080,1080) if platform=='instagram' else (1200,1200)
                image=ImageOps.contain(original,maximum,Image.Resampling.LANCZOS)
                ratio=image.width/image.height
                if platform=='instagram' and not .8<=ratio<=1.91:
                    canvas=Image.new('RGB',(1080,1350),'#0c2d49');contained=ImageOps.contain(image,(1080,1350));canvas.paste(contained,((1080-contained.width)//2,(1350-contained.height)//2));image=canvas
                target=directory/f'day-{item["day"]:02d}-{platform}.jpg'
                image.save(target,'JPEG',quality=88,optimize=True,progressive=True)
                text,url=caption(item,platform)
                post={'day':item['day'],'platform':platform,'title':item['title_en'],'text':text,'blog_url':url,'affiliate_url':item['affiliate_url'],'image':target.relative_to(ROOT).as_posix(),'width':image.width,'height':image.height,'image_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'status':'ready_for_connection'}
                out.append(post)
                (EXPORT/f'day-{item["day"]:02d}-{platform}.txt').write_text(text+'\n')
    (ROOT/'social/outbox.json').write_text(json.dumps({'version':1,'posts':out},ensure_ascii=False,indent=2)+'\n')
    with (EXPORT/'posts.csv').open('w',encoding='utf-8-sig',newline='') as f:
        fields=['day','platform','title','text','blog_url','affiliate_url','image','width','height','status'];writer=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');writer.writeheader();writer.writerows(out)
    with (EXPORT/'source-150-posts.csv').open('w',encoding='utf-8-sig',newline='') as f:
        originals=[r for item in data['days'] for r in item['original_posts']];writer=csv.DictWriter(f,fieldnames=list(originals[0]));writer.writeheader();writer.writerows(originals)
    review='# 30-day social campaign review\n\n90 prepared posts for X, Facebook and Instagram. No posts have been sent by this export. The 150 original platform drafts are preserved separately.\n\n'
    for item in data['days']:review+=f'- Day {item["day"]:02d}: {item["title_en"]} — {BASE}{blog_path(item)}\n'
    (EXPORT/'REVIEW.md').write_text(review)
    archive=EXPORT.parent/'social-campaign-30days.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for file in sorted(EXPORT.iterdir()):
            if file.is_file():z.write(file,'review/'+file.name)
        for file in sorted(directory.glob('*.jpg')):z.write(file,'images/'+file.name)
    print(f'Prepared {len(out)} caption/JPEG pairs; preserved 150 source drafts; review bundle: {archive}')
if __name__=='__main__':main()

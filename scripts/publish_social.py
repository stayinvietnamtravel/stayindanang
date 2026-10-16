"""Publish approved campaign days; dry-run by default and verify account identities first."""
from pathlib import Path
from urllib.parse import urlencode, urlsplit, urlunsplit, parse_qsl, quote
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from datetime import datetime, date, timezone
from zoneinfo import ZoneInfo
import argparse, base64, hashlib, hmac, json, mimetypes, os, secrets, time

ROOT=Path(__file__).resolve().parents[1]
BASE='https://stayinvietnamtravel.github.io/stayindanang/'
PLATFORMS=('x','facebook','instagram')

class ApiError(RuntimeError):
    def __init__(self,status=None):
        self.status=status
        super().__init__('Social API request failed'+(' (HTTP '+str(status)+')' if status else ' (network error)'))

class Transport:
    def request(self,method,url,headers=None,body=None):
        host=urlsplit(url).hostname
        if host not in ('api.x.com','graph.facebook.com','stayinvietnamtravel.github.io'):
            raise ValueError('Unapproved network destination')
        try:
            with urlopen(Request(url,data=body,headers=headers or {},method=method),timeout=45) as response:
                if method=='HEAD':return {'status':response.status,'content_type':response.headers.get('Content-Type','')}
                raw=response.read()
                return json.loads(raw) if raw else {}
        except HTTPError as error:raise ApiError(error.code) from None
        except (URLError,TimeoutError):raise ApiError() from None

def atomic_json(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    temporary.replace(path)

def campaign_day(start,today=None):
    first=date.fromisoformat(start)
    current=today or datetime.now(ZoneInfo('Asia/Bangkok')).date()
    day=(current-first).days+1
    return day if 1<=day<=30 else None

def validate_post(post):
    if post.get('platform') not in PLATFORMS or not 1<=int(post.get('day',0))<=30:raise ValueError('Invalid campaign post')
    if not isinstance(post.get('text'),str) or not post['text'].strip():raise ValueError('Missing post text')
    asset=(ROOT/post['image']).resolve()
    if not asset.is_relative_to((ROOT/'assets/campaign/social').resolve()) or asset.suffix.lower()!='.jpg':raise ValueError('Invalid social image path')
    if not asset.is_file() or not asset.read_bytes().startswith(b'\xff\xd8'):raise ValueError('Social JPEG is not ready')
    if asset.stat().st_size>5_000_000:raise ValueError('Social JPEG is too large')
    if not post.get('blog_url','').startswith(BASE+'blog/'):raise ValueError('Invalid blog destination')
    return asset

class Publisher:
    def __init__(self,config,ledger_path,transport=None,env=None,sleep=time.sleep):
        self.config=config;self.ledger_path=Path(ledger_path);self.http=transport or Transport()
        self.env=os.environ if env is None else env;self.sleep=sleep
        self.ledger=json.loads(self.ledger_path.read_text()) if self.ledger_path.exists() else {'version':1,'entries':{}}
        self.ig_id=None;self.verified=set()

    def required_secrets(self,platforms):
        required=[]
        if 'x' in platforms:required+=['X_API_KEY','X_API_SECRET','X_ACCESS_TOKEN','X_ACCESS_TOKEN_SECRET']
        if any(p in platforms for p in ('facebook','instagram')):required+=['META_PAGE_ACCESS_TOKEN']
        return [key for key in required if not self.env.get(key)]

    def x_request(self,method,path,payload=None,body=None,content_type=None):
        url='https://api.x.com'+path
        oauth={'oauth_consumer_key':self.env['X_API_KEY'],'oauth_token':self.env['X_ACCESS_TOKEN'],'oauth_signature_method':'HMAC-SHA1','oauth_timestamp':str(int(time.time())),'oauth_nonce':secrets.token_hex(16),'oauth_version':'1.0'}
        parts=urlsplit(url);params=list(parse_qsl(parts.query))+list(oauth.items())
        enc=lambda s:quote(str(s),safe='~')
        normalized='&'.join(enc(k)+'='+enc(v) for k,v in sorted(params,key=lambda pair:(enc(pair[0]),enc(pair[1]))))
        uri=urlunsplit((parts.scheme,parts.netloc,parts.path,'',''))
        signature_base='&'.join(enc(s) for s in (method,uri,normalized))
        key=enc(self.env['X_API_SECRET'])+'&'+enc(self.env['X_ACCESS_TOKEN_SECRET'])
        oauth['oauth_signature']=base64.b64encode(hmac.new(key.encode(),signature_base.encode(),hashlib.sha1).digest()).decode()
        headers={'Authorization':'OAuth '+', '.join(enc(k)+'="'+enc(v)+'"' for k,v in sorted(oauth.items()))}
        if payload is not None:body=json.dumps(payload).encode();content_type='application/json'
        if content_type:headers['Content-Type']=content_type
        return self.http.request(method,url,headers,body)

    def graph(self,method,path,values=None):
        token=self.env['META_PAGE_ACCESS_TOKEN']
        url='https://graph.facebook.com/'+self.config['graph_api_version']+path
        body=None;headers={'Authorization':'Bearer '+token}
        if method=='GET' and values:url+='?'+urlencode(values)
        elif values:body=urlencode(values).encode();headers['Content-Type']='application/x-www-form-urlencoded'
        return self.http.request(method,url,headers,body)

    def verify_accounts(self,platforms):
        missing=self.required_secrets(platforms)
        if missing:raise ValueError('Missing GitHub Actions secrets: '+', '.join(missing))
        if 'x' in platforms:
            account=self.x_request('GET','/2/users/me').get('data',{})
            if str(account.get('username','')).casefold()!=self.config['expected_x_username'].casefold():raise ValueError('X account does not match the configured username')
        if any(p in platforms for p in ('facebook','instagram')):
            page=self.graph('GET','/me',{'fields':'id,name,category'})
            if str(page.get('id'))!=self.config['expected_facebook_page_id'] or not page.get('category'):raise ValueError('Meta token is not for the configured Facebook Page; personal profiles are not supported')
        if 'instagram' in platforms:
            connection=self.graph('GET','/'+self.config['expected_facebook_page_id'],{'fields':'instagram_business_account'})
            self.ig_id=str(connection.get('instagram_business_account',{}).get('id',''))
            if not self.ig_id:raise ValueError('No professional Instagram account is connected to the configured Facebook Page')
            account=self.graph('GET','/'+self.ig_id,{'fields':'id,username'})
            if str(account.get('username','')).casefold()!=self.config['expected_instagram_username'].casefold():raise ValueError('Instagram account does not match the configured username')
        self.verified.update(platforms)

    def save(self):atomic_json(self.ledger_path,self.ledger)

    def transition(self,key,state,**fields):
        entry=self.ledger['entries'].setdefault(key,{})
        entry.update(state=state,updated_at=datetime.now(timezone.utc).isoformat(),**fields);self.save()

    def upload_x_image(self,asset):
        boundary='campaign-'+secrets.token_hex(16)
        body=(f'--{boundary}\r\nContent-Disposition: form-data; name="media_category"\r\n\r\ntweet_image\r\n--{boundary}\r\nContent-Disposition: form-data; name="media"; filename="poster.jpg"\r\nContent-Type: image/jpeg\r\n\r\n').encode()+asset.read_bytes()+f'\r\n--{boundary}--\r\n'.encode()
        result=self.x_request('POST','/2/media/upload',body=body,content_type='multipart/form-data; boundary='+boundary)
        media=str(result.get('data',{}).get('id',''))
        if not media:raise ValueError('X upload did not return a media identifier')
        return media

    def publish(self,post):
        if post.get('platform') not in self.verified:raise ValueError('Verify the destination account before publishing')
        asset=validate_post(post);key=f'day-{int(post["day"]):02d}:{post["platform"]}'
        prior=self.ledger['entries'].get(key,{})
        if prior.get('state')=='published':return {'key':key,'state':'already-published'}
        if prior.get('state') in ('publishing','uncertain'):raise ValueError('Publication outcome requires manual review before retry: '+key)
        digest=hashlib.sha256((post['text']+post['image']).encode()+asset.read_bytes()).hexdigest()
        self.transition(key,'preparing',content_sha256=digest)
        image_url=BASE+post['image']
        head=self.http.request('HEAD',image_url)
        if head.get('status')!=200 or 'image/jpeg' not in head.get('content_type',''):raise ValueError('Published JPEG is unavailable; wait for GitHub Pages deployment')
        platform=post['platform']
        try:
            if platform=='x':
                media=self.upload_x_image(asset)
                self.transition(key,'publishing',media_id=media)
                result=self.x_request('POST','/2/tweets',{'text':post['text'],'media':{'media_ids':[media]}})
                identifier=str(result.get('data',{}).get('id',''))
                public_url='https://x.com/'+self.config['expected_x_username']+'/status/'+identifier
            elif platform=='facebook':
                self.transition(key,'publishing')
                result=self.graph('POST','/'+self.config['expected_facebook_page_id']+'/photos',{'url':image_url,'caption':post['text'],'published':'true'})
                identifier=str(result.get('post_id') or result.get('id') or '')
                public_url='https://www.facebook.com/'+identifier
            else:
                container=self.graph('POST','/'+self.ig_id+'/media',{'image_url':image_url,'caption':post['text']})
                container_id=str(container.get('id',''))
                if not container_id:raise ValueError('Instagram did not return a media container')
                self.transition(key,'preparing',container_id=container_id)
                for attempt in range(20):
                    status=self.graph('GET','/'+container_id,{'fields':'status_code'}).get('status_code')
                    if status=='FINISHED':break
                    if status in ('ERROR','EXPIRED'):raise ValueError('Instagram media processing failed')
                    self.sleep(3)
                else:raise ValueError('Instagram media is not ready; no publication was requested')
                self.transition(key,'publishing',container_id=container_id)
                result=self.graph('POST','/'+self.ig_id+'/media_publish',{'creation_id':container_id})
                identifier=str(result.get('id',''));public_url=''
            if not identifier:raise ValueError('Social API did not return a publication identifier')
            self.transition(key,'published',id=identifier,url=public_url)
            return {'key':key,'state':'published','id':identifier,'url':public_url}
        except Exception as error:
            if self.ledger['entries'][key]['state']=='publishing':
                known_rejection=isinstance(error,ApiError) and error.status is not None and 400<=error.status<500 and error.status not in (408,429)
                self.transition(key,'failed' if known_rejection else 'uncertain')
            raise

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--day',type=int);parser.add_argument('--scheduled',action='store_true')
    parser.add_argument('--platform',choices=('all',)+PLATFORMS,default='all')
    parser.add_argument('--publish',action='store_true',help='Actually send posts; omitted means offline preview')
    parser.add_argument('--verify-accounts',action='store_true',help='Read-only account checks without publishing')
    args=parser.parse_args();config=json.loads((ROOT/'social/publishing.json').read_text())
    if args.scheduled:
        if os.environ.get('SOCIAL_AUTO_PUBLISH')!='true':print('Automatic publishing is disabled.');return
        start=os.environ.get('SOCIAL_START_DATE','')
        if not start:raise ValueError('Configure SOCIAL_START_DATE before enabling the daily schedule')
        args.day=campaign_day(start)
        if args.day is None:print('Outside the 30-day campaign window.');return
    platforms=list(PLATFORMS) if args.platform=='all' else [args.platform]
    publisher=Publisher(config,ROOT/'data/social_publications.json')
    if args.verify_accounts:publisher.verify_accounts(platforms);print('Configured account identities verified.');return
    if args.day is None or not 1<=args.day<=30:raise ValueError('Select a campaign day from 1 through 30')
    outbox=json.loads((ROOT/'social/outbox.json').read_text())
    posts=[p for p in outbox['posts'] if p['day']==args.day and p['platform'] in platforms]
    if len(posts)!=len(platforms):raise ValueError('Campaign day is incomplete')
    for post in posts:validate_post(post)
    if not args.publish:
        print(json.dumps({'mode':'preview','day':args.day,'platforms':platforms,'posts':posts,'missing_secrets':publisher.required_secrets(platforms)},ensure_ascii=False,indent=2));return
    publisher.verify_accounts(platforms)
    for post in posts:print(json.dumps(publisher.publish(post),ensure_ascii=False))

if __name__=='__main__':
    try:main()
    except (ValueError,ApiError) as error:raise SystemExit(str(error)) from None

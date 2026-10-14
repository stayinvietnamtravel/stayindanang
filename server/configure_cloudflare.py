"""Configure account-scoped deployment without placing credentials in files."""
import json,os,re,sys
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError
ROOT=Path(__file__).resolve().parents[1]
def main():
    account=os.environ.get('CLOUDFLARE_ACCOUNT_ID','');token=os.environ.get('CLOUDFLARE_API_TOKEN','')
    if not re.fullmatch(r'[a-f0-9]{32}',account) or not token:raise ValueError('Set Cloudflare account ID and API token')
    def api(path,method='GET',payload=None,missing_ok=False):
        request=Request('https://api.cloudflare.com/client/v4/accounts/'+account+path,data=None if payload is None else json.dumps(payload).encode(),method=method,headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'})
        try:
            with urlopen(request,timeout=30) as response:result=json.load(response)
        except HTTPError as error:
            if missing_ok and error.code==404:return {}
            raise ValueError('Cloudflare API request failed; check account and token permissions') from None
        except Exception:raise ValueError('Cloudflare API request failed; check account and token permissions') from None
        if not result.get('success'):raise ValueError('Cloudflare configuration request failed')
        return result['result']
    databases=api('/d1/database?per_page=100')
    database=next((item for item in databases if item['name']=='stayindanang-analytics'),None)
    if database is None:database=api('/d1/database','POST',{'name':'stayindanang-analytics'})
    database_id=database['uuid']
    if not re.fullmatch(r'[a-f0-9-]{36}',database_id):raise ValueError('Invalid D1 identifier returned')
    subdomain=api('/workers/subdomain',missing_ok=True).get('subdomain')
    if not subdomain:subdomain=api('/workers/subdomain','POST',{'subdomain':'stayindanang-'+account[:8]}).get('subdomain')
    if not subdomain or not re.fullmatch(r'[a-z0-9-]+',subdomain):raise ValueError('Register a Workers.dev subdomain in Cloudflare')
    config=ROOT/'server/wrangler.jsonc';settings=json.loads(config.read_text());settings['d1_databases'][0]['database_id']=database_id;config.write_text(json.dumps(settings,indent=2)+'\n')
    public=ROOT/'data/assistant_config.json';settings=json.loads(public.read_text());settings['backend_url']='https://stayindanang-travel-assistant.'+subdomain+'.workers.dev';public.write_text(json.dumps(settings,indent=2)+'\n')
    print('Cloudflare database and public endpoint configured. No credentials were written to repository files.')
if __name__=='__main__':
    try:main()
    except ValueError as error:print(str(error),file=sys.stderr);sys.exit(1)

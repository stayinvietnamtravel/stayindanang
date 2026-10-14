#!/usr/bin/env python3
"""Cache independent MET Norway forecasts for 101 world destinations."""
from pathlib import Path
from world_weather import CITIES
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import json
import math
import sys

ROOT=Path(__file__).resolve().parents[1]
MAX_BYTES=2_000_000


def date(value):
    result=datetime.fromisoformat(value.replace('Z','+00:00'))
    if result.tzinfo is None:raise ValueError('Forecast timestamp lacks a timezone')
    return result.astimezone(timezone.utc)


def number(value,minimum,maximum):
    if isinstance(value,bool) or not isinstance(value,(float,int)) or not math.isfinite(value) or not minimum<=value<=maximum:
        raise ValueError('Invalid forecast measurement')
    return float(value)


def parse_forecast(payload,now,city_key='da-nang'):
    city,latitude,longitude=CITIES[city_key]
    source_url=f'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={latitude}&lon={longitude}'
    properties=payload['properties'];meta=properties['meta'];units=meta['units']
    if units.get('air_temperature')!='celsius' or units.get('precipitation_amount')!='mm' or units.get('wind_speed')!='m/s':
        raise ValueError('Unsupported forecast units')
    updated=date(meta['updated_at'])
    if not now-timedelta(hours=48)<=updated<=now+timedelta(hours=1):raise ValueError('Forecast model is stale or future-dated')
    records=[];seen=set()
    for entry in properties['timeseries']:
        timestamp=date(entry['time'])
        if timestamp<now-timedelta(hours=1) or timestamp>now+timedelta(days=7) or timestamp in seen:continue
        instant=entry['data']['instant']['details']
        temperature=number(instant['air_temperature'],-80,65)
        wind=number(instant['wind_speed'],0,150)
        amount=None;hours=None;symbol='unknown'
        for interval in (1,6,12):
            period=entry['data'].get(f'next_{interval}_hours')
            if not period:continue
            symbol=period.get('summary',{}).get('symbol_code','unknown')
            value=period.get('details',{}).get('precipitation_amount')
            if value is not None:amount=number(value,0,5000);hours=interval
            break
        if not isinstance(symbol,str) or len(symbol)>64 or not all(c.isalpha() or c=='_' for c in symbol):symbol='unknown'
        seen.add(timestamp)
        records.append({'time':timestamp.isoformat(),'temperature_c':temperature,'wind_mps':wind,'precipitation_mm':amount,'precipitation_hours':hours,'symbol_code':symbol})
    records.sort(key=lambda item:item['time'])
    if len([item for item in records if date(item['time'])>=now])<5:raise ValueError('Insufficient future forecast points')
    return {'provider':'MET Norway','source_url':source_url,'license_url':'https://creativecommons.org/licenses/by/4.0/','city':city,'latitude':latitude,'longitude':longitude,'source_updated_at':updated.isoformat(),'fetched_at':now.isoformat(),'points':records}


def refresh():
    target=ROOT/'data/weather.json';previous=json.loads(target.read_text())
    cached=previous.get('cities',{'da-nang':previous})
    now=datetime.now(timezone.utc);results={};successes=0
    def fetch_city(item):
        key,(city,latitude,longitude)=item
        prior=cached.get(key,{})
        source_url=f'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={latitude}&lon={longitude}'
        headers={'User-Agent':'StayInDaNangWeather/2.0 (+https://github.com/stayinvietnamtravel/stayindanang)','Accept':'application/json'}
        if prior.get('etag') and prior.get('source_updated_at') and date(prior['source_updated_at'])>=now-timedelta(hours=24):
            headers['If-None-Match']=prior['etag']
        try:
            try:
                with urlopen(Request(source_url,headers=headers),timeout=15) as response:
                    raw=response.read(MAX_BYTES+1)
                    if len(raw)>MAX_BYTES:raise ValueError('Forecast payload too large')
                    result=parse_forecast(json.loads(raw),now,key)
                    etag=response.headers.get('ETag')
                    result['etag']=etag if etag and len(etag)<200 and '\n' not in etag and '\r' not in etag else None
            except HTTPError as error:
                if error.code==304 and prior.get('points') and date(prior['source_updated_at'])>=now-timedelta(hours=48):
                    result={**prior,'fetched_at':now.isoformat()}
                else:raise
            result.update(last_attempt_at=now.isoformat(),fetch_status='ok',failure_reason=None)
            return key,result,True

        except Exception as error:
            result={**prior,'city':city,'latitude':latitude,'longitude':longitude,'source_url':source_url,'last_attempt_at':now.isoformat(),'fetch_status':'unavailable','failure_reason':f'{type(error).__name__}: {error}'}
            print(f'{city}: unavailable; prior forecast retained.',file=sys.stderr)
            return key,result,False
    with ThreadPoolExecutor(max_workers=4) as executor:
        for key,result,ok in executor.map(fetch_city,CITIES.items()):
            results[key]=result;successes+=int(ok)
    print(f'Weather refresh: {successes}/{len(CITIES)} cities updated.')
    target.write_text(json.dumps({'provider':'MET Norway','cities':results,'last_attempt_at':now.isoformat()},ensure_ascii=False,indent=2)+'\n')
    return 0 if successes==len(CITIES) else 1


if __name__=='__main__':sys.exit(refresh())

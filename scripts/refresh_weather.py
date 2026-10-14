#!/usr/bin/env python3
"""Cache MET Norway forecasts for central Da Nang; never invent observations."""
from pathlib import Path
from datetime import datetime, timedelta, timezone
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import json
import math
import sys

ROOT=Path(__file__).resolve().parents[1]
URL='https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=16.0544&lon=108.2022'
MAX_BYTES=2_000_000


def date(value):
    result=datetime.fromisoformat(value.replace('Z','+00:00'))
    if result.tzinfo is None:raise ValueError('Forecast timestamp lacks a timezone')
    return result.astimezone(timezone.utc)


def number(value,minimum,maximum):
    if isinstance(value,bool) or not isinstance(value,(float,int)) or not math.isfinite(value) or not minimum<=value<=maximum:
        raise ValueError('Invalid forecast measurement')
    return float(value)


def parse_forecast(payload,now):
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
    return {'provider':'MET Norway','source_url':URL,'license_url':'https://creativecommons.org/licenses/by/4.0/','city':'Da Nang','latitude':16.0544,'longitude':108.2022,'source_updated_at':updated.isoformat(),'fetched_at':now.isoformat(),'points':records}


def refresh():
    target=ROOT/'data/weather.json';previous=json.loads(target.read_text())
    now=datetime.now(timezone.utc)
    headers={'User-Agent':'StayInDaNangWeather/1.0 (+https://github.com/stayinvietnamtravel/stayindanang)','Accept':'application/json'}
    if previous.get('etag') and previous.get('source_updated_at') and date(previous['source_updated_at'])>=now-timedelta(hours=24):
        headers['If-None-Match']=previous['etag']
    try:
        with urlopen(Request(URL,headers=headers),timeout=25) as response:
            raw=response.read(MAX_BYTES+1)
            if len(raw)>MAX_BYTES:raise ValueError('Forecast payload too large')
            result=parse_forecast(json.loads(raw),now)
            etag=response.headers.get('ETag')
            result['etag']=etag if etag and len(etag)<200 and '\n' not in etag and '\r' not in etag else None
    except HTTPError as error:
        if error.code==304 and previous.get('points') and date(previous['source_updated_at'])>=now-timedelta(hours=48):
            result={**previous,'fetched_at':now.isoformat()}
        else:
            print(f'Weather request failed ({error.code}); existing forecast retained.',file=sys.stderr);return 1
    except Exception as error:
        print(f'Weather unavailable ({type(error).__name__}); existing forecast retained.',file=sys.stderr);return 1
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(f'Cached {len(result["points"])} forecast points for Da Nang from MET Norway.')
    return 0


if __name__=='__main__':sys.exit(refresh())

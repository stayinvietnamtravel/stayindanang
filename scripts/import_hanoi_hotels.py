from openpyxl import load_workbook
from pathlib import Path
import json,re,unicodedata,hashlib
from urllib.parse import urlsplit
import argparse
parser=argparse.ArgumentParser(description='Import Hanoi hotel names and exact Trip.com links from workbook data.')
parser.add_argument('workbook',type=Path)
args=parser.parse_args()
src=args.workbook
w=load_workbook(src,data_only=True);records={}
for s in w:
 if 'Ha Noi' not in s.title:continue
 group='Hot Sellers' if s.title.startswith('Hot Sellers') else 'Top Deals'
 header=None
 for cells in s:
  values=[c.value for c in cells]
  if 'name' in values and 'link' in values:header={v:i for i,v in enumerate(values) if isinstance(v,str)};continue
  if not header:continue
  name=values[header['name']];link=values[header['link']]
  if not name and not link:continue
  name=name.strip();link=link.strip();u=urlsplit(link)
  assert u.scheme=='https' and u.netloc=='www.trip.com' and re.fullmatch('/w/[A-Za-z0-9]+',u.path) and not u.query and not u.fragment
  cell=cells[header['link']];assert not cell.hyperlink or cell.hyperlink.target==link
  slug=re.sub('[^a-z0-9]+','-',unicodedata.normalize('NFKD',name).encode('ascii','ignore').decode().lower()).strip('-')
  if name not in records:records[name]={'name':name,'slug':slug,'city':'hanoi','group':group,'urls':[],'source_rows':[]}
  row=records[name];assert row['group']==group
  if link not in row['urls']:row['urls'].append(link)
  row['source_rows'].append({'sheet':s.title,'row':cells[0].row})
rows=list(records.values());assert len({r['slug'] for r in rows})==len(rows)
(Path(__file__).resolve().parents[1]/'data/hanoi_hotels.json').write_text(json.dumps({'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'rows':rows},ensure_ascii=False,indent=2)+'\n')
print(len(rows),'hotels',sum(len(r['urls']) for r in rows),'affiliate links')

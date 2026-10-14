"""City-center forecast coordinates and IANA timezones for curated destinations."""
from world_destinations import COUNTRIES
# Coordinates follow the same city order as each country's editorial selector.
COORDINATES={
'VN':[(16.0544,108.2022),(21.0285,105.8542),(22.3364,103.8438),(10.8231,106.6297),(10.2899,103.9840),(15.8801,108.3380),(16.4637,107.5909),(12.2388,109.1967),(11.9404,108.4583),(20.9500,107.0800)],
'TH':[(13.7563,100.5018),(18.7883,98.9853),(7.8804,98.3923),(8.0863,98.9063)],
'JP':[(35.6762,139.6503),(34.6937,135.5023),(35.0116,135.7681),(33.5902,130.4017)],
'CN':[(39.9042,116.4074),(31.2304,121.4737),(30.5728,104.0668),(23.1291,113.2644),(22.3193,114.1694)],
'KR':[(37.5665,126.9780),(35.1796,129.0756),(33.4996,126.5312)],'SG':[(1.3521,103.8198)],
'ID':[(-8.5069,115.2625),(-6.2088,106.8456),(-7.7956,110.3695)],
'MY':[(3.1390,101.6869),(5.4141,100.3288),(6.3500,99.8000)],
'PH':[(14.5995,120.9842),(10.3157,123.8854),(11.2027,119.4169)],
'IN':[(28.6139,77.2090),(19.0760,72.8777),(26.9124,75.7873),(27.1767,78.0081)],
'AE':[(25.2048,55.2708),(24.4539,54.3773)],'KH':[(13.3671,103.8448),(11.5564,104.9282)],
'LA':[(17.9757,102.6331),(19.8833,102.1333)],'NP':[(27.7172,85.3240)],
'FR':[(48.8566,2.3522),(43.7102,7.2620),(45.7640,4.8357)],
'GB':[(51.5074,-0.1278),(55.9533,-3.1883),(53.4808,-2.2426)],
'IT':[(41.9028,12.4964),(45.4408,12.3155),(43.7696,11.2558)],
'ES':[(41.3851,2.1734),(40.4168,-3.7038),(37.3891,-5.9845)],
'DE':[(52.5200,13.4050),(48.1351,11.5820),(50.1109,8.6821)],
'GR':[(37.9838,23.7275),(36.3932,25.4615)],'CH':[(47.3769,8.5417),(47.0502,8.3093)],
'NL':[(52.3676,4.9041)],'PT':[(38.7223,-9.1393),(41.1579,-8.6291)],
'AT':[(48.2082,16.3738),(47.8095,13.0550)],'CZ':[(50.0755,14.4378),(49.1951,16.6068)],
'RU':[(55.7558,37.6173),(59.9311,30.3609)],
'US':[(40.7128,-74.0060),(34.0522,-118.2437),(37.7749,-122.4194),(36.1699,-115.1398),(21.3099,-157.8581)],
'CA':[(43.6532,-79.3832),(49.2827,-123.1207),(45.5017,-73.5673)],
'MX':[(19.4326,-99.1332),(21.1619,-86.8515),(17.0732,-96.7266)],
'BR':[(-22.9068,-43.1729),(-23.5505,-46.6333)],'AR':[(-34.6037,-58.3816)],
'PE':[(-12.0464,-77.0428),(-13.5320,-71.9675)],'CL':[(-33.4489,-70.6693)],
'AU':[(-33.8688,151.2093),(-37.8136,144.9631),(-27.4698,153.0251),(-31.9505,115.8605),(-28.0167,153.4000)],
'NZ':[(-36.8485,174.7633),(-45.0312,168.6626),(-41.2865,174.7762)],'FJ':[(-17.7765,177.4356)],
}
ZONES=dict(zip(['VN','TH','JP','CN','KR','SG','ID','MY','PH','IN','AE','KH','LA','NP','FR','GB','IT','ES','DE','GR','CH','NL','PT','AT','CZ','RU','US','CA','MX','BR','AR','PE','CL','AU','NZ','FJ'],['Asia/Ho_Chi_Minh','Asia/Bangkok','Asia/Tokyo','Asia/Shanghai','Asia/Seoul','Asia/Singapore','Asia/Jakarta','Asia/Kuala_Lumpur','Asia/Manila','Asia/Kolkata','Asia/Dubai','Asia/Phnom_Penh','Asia/Vientiane','Asia/Kathmandu','Europe/Paris','Europe/London','Europe/Rome','Europe/Madrid','Europe/Berlin','Europe/Athens','Europe/Zurich','Europe/Amsterdam','Europe/Lisbon','Europe/Vienna','Europe/Prague','Europe/Moscow','America/New_York','America/Toronto','America/Mexico_City','America/Sao_Paulo','America/Argentina/Buenos_Aires','America/Lima','America/Santiago','Australia/Sydney','Pacific/Auckland','Pacific/Fiji']))
OVERRIDES={'hong-kong':'Asia/Hong_Kong','bali':'Asia/Makassar','los-angeles':'America/Los_Angeles','san-francisco':'America/Los_Angeles','las-vegas':'America/Los_Angeles','honolulu':'Pacific/Honolulu','vancouver':'America/Vancouver','cancun':'America/Cancun','melbourne':'Australia/Melbourne','brisbane':'Australia/Brisbane','perth':'Australia/Perth','gold-coast':'Australia/Brisbane'}
CITIES={};TIMEZONES={}
for region,code,en,vi,cities in COUNTRIES:
    assert len(cities)==len(COORDINATES[code]),code
    for city,coordinates in zip(cities,COORDINATES[code]):
        CITIES[city[0]]=(city[1],*coordinates)
        TIMEZONES[city[0]]=OVERRIDES.get(city[0],ZONES[code])

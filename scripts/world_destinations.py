"""Curated country/city selectors; independent of the five-city forecast cache."""
# Region, ISO country, English/ Vietnamese country names, city keys and labels.
COUNTRIES=[
('asia','VN','Vietnam','Việt Nam',[('da-nang','Da Nang','Đà Nẵng'),('hanoi','Hanoi','Hà Nội'),('sapa','Sa Pa','Sa Pa'),('ho-chi-minh-city','Ho Chi Minh City','TP. Hồ Chí Minh'),('phu-quoc','Phu Quoc','Phú Quốc'),('hoi-an','Hoi An','Hội An'),('hue','Hue','Huế'),('nha-trang','Nha Trang','Nha Trang'),('da-lat','Da Lat','Đà Lạt'),('ha-long','Ha Long','Hạ Long')]),
('asia','TH','Thailand','Thái Lan',[('bangkok','Bangkok','Bangkok'),('chiang-mai','Chiang Mai','Chiang Mai'),('phuket','Phuket','Phuket'),('krabi','Krabi','Krabi')]),
('asia','JP','Japan','Nhật Bản',[('tokyo','Tokyo','Tokyo'),('osaka','Osaka','Osaka'),('kyoto','Kyoto','Kyoto'),('fukuoka','Fukuoka','Fukuoka')]),
('asia','CN','China','Trung Quốc',[('beijing','Beijing','Bắc Kinh'),('shanghai','Shanghai','Thượng Hải'),('chengdu','Chengdu','Thành Đô'),('guangzhou','Guangzhou','Quảng Châu'),('hong-kong','Hong Kong','Hồng Kông')]),
('asia','KR','South Korea','Hàn Quốc',[('seoul','Seoul','Seoul'),('busan','Busan','Busan'),('jeju','Jeju','Jeju')]),
('asia','SG','Singapore','Singapore',[('singapore','Singapore','Singapore')]),
('asia','ID','Indonesia','Indonesia',[('bali','Bali','Bali'),('jakarta','Jakarta','Jakarta'),('yogyakarta','Yogyakarta','Yogyakarta')]),
('asia','MY','Malaysia','Malaysia',[('kuala-lumpur','Kuala Lumpur','Kuala Lumpur'),('penang','George Town / Penang','George Town / Penang'),('langkawi','Langkawi','Langkawi')]),
('asia','PH','Philippines','Philippines',[('manila','Manila','Manila'),('cebu','Cebu','Cebu'),('el-nido','El Nido','El Nido')]),
('asia','IN','India','Ấn Độ',[('new-delhi','New Delhi','New Delhi'),('mumbai','Mumbai','Mumbai'),('jaipur','Jaipur','Jaipur'),('agra','Agra','Agra')]),
('asia','AE','United Arab Emirates','Các Tiểu vương quốc Ả Rập Thống nhất',[('dubai','Dubai','Dubai'),('abu-dhabi','Abu Dhabi','Abu Dhabi')]),
('asia','KH','Cambodia','Campuchia',[('siem-reap','Siem Reap','Siem Reap'),('phnom-penh','Phnom Penh','Phnom Penh')]),
('asia','LA','Laos','Lào',[('vientiane','Vientiane','Viêng Chăn'),('luang-prabang','Luang Prabang','Luang Prabang')]),
('asia','NP','Nepal','Nepal',[('kathmandu','Kathmandu','Kathmandu')]),
('europe','FR','France','Pháp',[('paris','Paris','Paris'),('nice','Nice','Nice'),('lyon','Lyon','Lyon')]),
('europe','GB','United Kingdom','Vương quốc Anh',[('london','London','London'),('edinburgh','Edinburgh','Edinburgh'),('manchester','Manchester','Manchester')]),
('europe','IT','Italy','Ý',[('rome','Rome','Rome'),('venice','Venice','Venice'),('florence','Florence','Florence')]),
('europe','ES','Spain','Tây Ban Nha',[('barcelona','Barcelona','Barcelona'),('madrid','Madrid','Madrid'),('seville','Seville','Seville')]),
('europe','DE','Germany','Đức',[('berlin','Berlin','Berlin'),('munich','Munich','Munich'),('frankfurt','Frankfurt','Frankfurt')]),
('europe','GR','Greece','Hy Lạp',[('athens','Athens','Athens'),('santorini','Santorini','Santorini')]),
('europe','CH','Switzerland','Thụy Sĩ',[('zurich','Zurich','Zurich'),('lucerne','Lucerne','Lucerne')]),
('europe','NL','Netherlands','Hà Lan',[('amsterdam','Amsterdam','Amsterdam')]),
('europe','PT','Portugal','Bồ Đào Nha',[('lisbon','Lisbon','Lisbon'),('porto','Porto','Porto')]),
('europe','AT','Austria','Áo',[('vienna','Vienna','Vienna'),('salzburg','Salzburg','Salzburg')]),
('europe','CZ','Czechia','Séc',[('prague','Prague','Prague'),('brno','Brno','Brno')]),
('europe','RU','Russia','Nga',[('moscow','Moscow','Moskva'),('saint-petersburg','Saint Petersburg','Saint Petersburg')]),
('americas','US','United States','Hoa Kỳ',[('new-york','New York','New York'),('los-angeles','Los Angeles','Los Angeles'),('san-francisco','San Francisco','San Francisco'),('las-vegas','Las Vegas','Las Vegas'),('honolulu','Honolulu','Honolulu')]),
('americas','CA','Canada','Canada',[('toronto','Toronto','Toronto'),('vancouver','Vancouver','Vancouver'),('montreal','Montreal','Montréal')]),
('americas','MX','Mexico','Mexico',[('mexico-city','Mexico City','Mexico City'),('cancun','Cancún','Cancún'),('oaxaca','Oaxaca','Oaxaca')]),
('americas','BR','Brazil','Brazil',[('rio-de-janeiro','Rio de Janeiro','Rio de Janeiro'),('sao-paulo','São Paulo','São Paulo')]),
('americas','AR','Argentina','Argentina',[('buenos-aires','Buenos Aires','Buenos Aires')]),
('americas','PE','Peru','Peru',[('lima','Lima','Lima'),('cusco','Cusco','Cusco')]),
('americas','CL','Chile','Chile',[('santiago','Santiago','Santiago')]),
('oceania','AU','Australia','Úc',[('sydney','Sydney','Sydney'),('melbourne','Melbourne','Melbourne'),('brisbane','Brisbane','Brisbane'),('perth','Perth','Perth'),('gold-coast','Gold Coast','Gold Coast')]),
('oceania','NZ','New Zealand','New Zealand',[('auckland','Auckland','Auckland'),('queenstown','Queenstown','Queenstown'),('wellington','Wellington','Wellington')]),
('oceania','FJ','Fiji','Fiji',[('nadi','Nadi','Nadi')]),
]
REGIONS={
 'vi':['Châu lục','Quốc gia','Thành phố / điểm đến','Tất cả','Châu Á','Châu Âu','Châu Mỹ','Châu Úc & châu Đại Dương'],
 'en':['Continent','Country','City / destination','All','Asia','Europe','Americas','Australia & Oceania'],
 'fr':['Continent','Pays','Ville / destination','Tous','Asie','Europe','Amériques','Australie et Océanie'],
 'de':['Kontinent','Land','Stadt / Reiseziel','Alle','Asien','Europa','Amerika','Australien und Ozeanien'],
 'es':['Continente','País','Ciudad / destino','Todos','Asia','Europa','América','Australia y Oceanía'],
 'zh':['洲','国家','城市 / 目的地','全部','亚洲','欧洲','美洲','澳大利亚与大洋洲'],
 'zh-Hant':['洲','國家','城市 / 目的地','全部','亞洲','歐洲','美洲','澳洲與大洋洲'],
 'ru':['Континент','Страна','Город / направление','Все','Азия','Европа','Америка','Австралия и Океания'],
 'ko':['대륙','국가','도시 / 여행지','전체','아시아','유럽','아메리카','호주 및 오세아니아'],
 'ja':['大陸','国','都市 / 目的地','すべて','アジア','ヨーロッパ','南北アメリカ','オーストラリア・オセアニア'],
 'hi':['महाद्वीप','देश','शहर / गंतव्य','सभी','एशिया','यूरोप','अमेरिका','ऑस्ट्रेलिया और ओशिनिया'],
 'th':['ทวีป','ประเทศ','เมือง / จุดหมาย','ทั้งหมด','เอเชีย','ยุโรป','อเมริกา','ออสเตรเลียและโอเชียเนีย'],
 'id':['Benua','Negara','Kota / destinasi','Semua','Asia','Eropa','Amerika','Australia dan Oseania'],
}
REGION_KEYS=('asia','europe','americas','oceania')
CITY_KEYS={key for _,_,_,_,cities in COUNTRIES for key,_,_ in cities}
assert len(CITY_KEYS)==sum(len(cities) for *_,cities in COUNTRIES)

def country_name(country,lang):return country[3] if lang=='vi' else country[2]
def city_name(city,lang):
    if city[0] in ('da-nang','hanoi','sapa','ho-chi-minh-city','phu-quoc'):
        from destinations import CITIES,DESTINATIONS
        return DESTINATIONS[lang][3][list(CITIES).index(city[0])]
    return city[2] if lang=='vi' else city[1]

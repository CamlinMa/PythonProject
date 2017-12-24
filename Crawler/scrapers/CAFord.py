# -*- coding:utf-8 -*-

from crawler.crawler import *
import time
import json
from urllib.parse import quote
import re

brand = 'CAFORD'

dealer_head = [
    [brand, 'DEALERNAME', 'ADDRESS', 'FAX', 'PROV', 'CITY', 'LATITUDE', 'LONGITUDE', 'PHONE']
]

create_time = str(time.strftime("%Y%m%d"))
create_csv(dealer_head, brand + '_' + create_time)

BASE_URL = 'http://www.ford.com.cn/content/ford/cn/zh_cn/configuration/application-and-services-config/provinceCityDropDowns.multiFieldDropdown.data'
page = get_page(BASE_URL)
prov_list = json.loads(page)
count = 0

for prov_match in prov_list:
    prov = prov_match['provinceKey']
    prov2 = quote(prov)
    for city_match in prov_match['cityList']:
        city = city_match['cityKey']
        city2 = quote(city)
        geo_url = 'http://restapi.amap.com/v3/geocode/geo?key=1891d0f847c0a210a88015fdd4c3bc46&s=rsv3&callback=jsonp_232&platform=JS&logversion=2.0&sdkversion=1.3&appname=http://www.ford.com.cn/dealer/locator?intcmp=hp-return-fd&csid=D6C889F7-2FF1-4EA5-8D60-494D42872518&address=' + str(
            prov2) + str(city2) + '&callback=jsonp_232'

        geo_str = get_page_nosave(geo_url)
        try:
            geo = re.search(r'location\":\"([^\"]+)\"', geo_str).group(1)
        except:
            continue
        dealer_url = 'http://yuntuapi.amap.com/datasearch/around?s=rsv3&key=1891d0f847c0a210a88015fdd4c3bc46&extensions=base&language=en&enc=utf-8&output=jsonp&sortrule=_distance:1&keywords=&limit=100&tableid=55adb0c7e4b0a76fce4c8dd6&radius=35000&callback=jsonp_333&platform=JS&logversion=2.0&sdkversion=1.3&appname=http://www.ford.com.cn/dealer/locator?intcmp=hp-return-fd&csid=C0F2C0C7-D2A2-4730-9618-5B2C060C3DDD&center=' + str(
            geo) + '&filter=AdministrativeArea:' + str(prov2) + '&Locality:' + str(city2) + '&callback=jsonp_333'
        dealer_page = get_page_nosave(dealer_url)
        dealer_list = json.loads(re.search(r'\{(.+)\}', dealer_page).group(0))
        for dealer in dealer_list['datas']:
            if dealer['DealerAffiliation'] == 'Category3':
                continue
            name = dealer['_name'].strip()
            address = dealer['_address'].strip()
            phone = '#' + str(dealer['PrimaryPhone']).strip()
            fax = str(dealer['Fax']).strip()
            location = str(dealer['_location']).strip().split(',')
            lat = location[1]
            lng = location[0]
            city = str(dealer['_city']).strip()
            prov = str(dealer['_province']).strip()
            dealer_data = [[brand, name, address, fax, prov, city, lat, lng, phone]]
            count += 1
            save_csv(dealer_data, brand + '_' + create_time)

            print(str(count) + '  OK')

print('total   ' + str(count))

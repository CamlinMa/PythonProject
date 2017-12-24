# -*- coding:utf-8 -*-

from crawler.crawler import *
import re
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests
import json

file_name = 'BRAND' + '_' + str(time.strftime("%Y%m%d"))  # 文件保存格式    BMW_20170913.csv

# 定义字段
dealer_head = [
    ['BRAND', 'DEALERNAME', 'ADDRESS', 'SUBURB', 'POSTCODE', 'STATE', 'SALES', 'SERVICE', 'VEHICLESTYPE', 'CATEGORY',
     'LATITUDE', 'LONGITUDE', 'PHONE']
]
# 创建文件 会覆盖已存在文件
# create_csv(dealer_head, file_name)

count = 0


'''
code 

url 为必须参数 encoding 默认 utf-8  headers 默认 Chrome 浏览器PC 版
get_page(url='',encoding='utf-8',headers={}) 
get_page_nosave(url='',encoding='utf-8',headers={})


list_ss=string2list(instr='',start_str='',end_str='')  

'''
dealer_list = []
for info in dealer_list:
    dealer_name = ''
    address = ''
    suburb = ''
    pc = ''
    state = ''
    sales = ''
    service = ''
    vehiclesitype = ''
    category = ''
    lat = ''
    lng = ''
    phone = ''
    data = [
        ['BRAND', dealer_name, address, suburb, pc, state, sales, service, vehiclesitype, category, lat, lng, phone]
    ]
    # 写入文件
    # save_csv(data, file_name)
    count += 1
    print('OK    ' + str(count))

# -*- coding:utf-8 -*-

from download.web import get_page,get_new_page,save_data
from bs4 import BeautifulSoup
import re
import json

import datetime

def tencent_data(yestoday):

    n = 60
    data_name='tencent'
    index_url = 'http://auto.qq.com/comment.htm'

    count = 0
    page=get_new_page(index_url,'gbk')
    soup=BeautifulSoup(page,'html.parser')
    for art in soup.find_all('div','newTxt'):

        article_info={}

        url='http://auto.qq.com'+art.h3.a.attrs['href']
        page2=get_page(url,'gb2312')
        sou2=BeautifulSoup(page2,'html.parser')
        try:
            title=sou2.find('div','hd').h1.get_text()
            times=sou2.find('span','a_time').get_text()
        except:
            continue

        tmp_time2 = str(times).split(' ')[0]
        tmp_time3 = tmp_time2.split('-')
        year = tmp_time3[0].replace('\n', '').replace('\t', '').replace('_', '')
        month = tmp_time3[1]
        days = tmp_time3[2]
        content=''
        for con in sou2.find('div','Cnt-Main-Article-QQ').find_all('p'):
            content=content+str(con.get_text())

        article_info['url'] = url
        article_info['year'] = year
        article_info['month'] = month
        article_info['day'] = days
        article_info['title'] = title
        article_info['content'] = content
        article_info['source'] = 'tencent'
        if yestoday==year + '-' + month + '-' + days:
            file_name = year + '-' + month + '-' + days + '_' + data_name
            save_data(json.dumps(article_info, ensure_ascii=False), file_name)
            count += 1
            print('ok    ' + str(count))
    print('save successful!')



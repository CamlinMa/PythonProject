# -*- coding:utf-8 -*-


from download.web import get_page,get_new_page,save_data
from bs4 import BeautifulSoup
import re
import json

import datetime

index_url=['http://auto.sina.com.cn/news/',
           'http://auto.sina.com.cn/news/hy/',
           'http://auto.sina.com.cn/news/ct/',
           'http://auto.sina.com.cn/news/f/',
           'http://auto.sina.com.cn/service/n/',
           'http://auto.sina.com.cn/newcar/h/']
data_name='sina'
file_name = str(datetime.date.today()) + '_'+data_name

def sina_auto(yestoday):
    count=0
    article_collection=[]

    for urlt in index_url:

        urls = urlt
        page = get_new_page(urls, 'utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        for infos in soup.find('div','content').find_all('div','con'):
            info=infos.find('h3')
            article_info = {}
            try:
                url = info.a.attrs['href']
                article = get_page(url,'utf-8')
                soup2 = BeautifulSoup(article, 'html.parser')
                tmp_time = soup2.find('span', 'time-source').get_text()
                tmp_time2 = str(tmp_time).split(' ')[0]
                tmp_time3 = tmp_time2.split('-')
                year = tmp_time3[0].replace('\n', '').replace('\t', '').replace('_', '')
                month = tmp_time3[1]
                days = tmp_time3[2]
                content = ''
                for con in soup2.find('div', 'page-content clearfix').find_all('p'):
                    content += con.get_text()
                title = soup2.find('div', 'page-head').h1.get_text()
            except:
                continue

            article_info['url'] = url
            article_info['year'] = year
            article_info['month'] = month
            article_info['day'] = days
            article_info['title'] = title
            article_info['content'] = content
            article_info['source'] = 'autohome'

            if str(yestoday) == year + '-' + month + '-' + days:
                file_name = year + '-' + month + '-' + days + '_' + data_name
                save_data(json.dumps(article_info, ensure_ascii=False), file_name)
                count += 1
                print('ok    ' + str(count))

if __name__=='__main__':
    sina_auto()
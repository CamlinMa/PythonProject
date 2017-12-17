# -*- coding:utf-8 -*-

from download.web import get_page,get_new_page,save_data
from bs4 import BeautifulSoup
import re
import json

import datetime

def autohome_data(yestoday):

    n = 60
    data_name='autohome'
    index_url = 'http://www.autohome.com.cn/news/'

    count = 0

    for i in range(1, n):
        if i == 1:
            c_url = index_url
        else:
            c_url = index_url + str(i) + '/#liststart'
        try:
            index_page = get_new_page(c_url, 'gb2312')
            soup = BeautifulSoup(index_page, 'html.parser')
            article_list = soup.find_all('ul', 'article')

            for article_list2 in article_list:
                for article in article_list2.find_all('li'):
                    try:
                        article_info = {}
                        url = str('http:' + str(article.a.attrs['href']))
                        title = str(article.h3.get_text())
                        content_page = str(get_page(url, 'gb2312'))
                        soup2 = BeautifulSoup(content_page, 'html.parser')
                        content_time = str(soup2.find('div', 'article-info').span.get_text()).replace('\r\n', '')
                        content = str(soup2.find('div', 'article-content').get_text()).replace('\n', '')
                        year = re.search(r'([0-9]+)年', str(content_time)).group(1)
                        month = re.search(r'年([0-9]+)月', str(content_time)).group(1)
                        days = re.search(r'月([0-9]+)日', str(content_time)).group(1)
                        article_info['url'] = url
                        article_info['year'] = year
                        article_info['month'] = month
                        article_info['day'] = days
                        article_info['title'] = title
                        article_info['content'] = content
                        article_info['source']='autohome'
                        if str(yestoday) == year + '-' + month + '-' + days:
                            file_name = year + '-' + month + '-' + days + '_' + data_name
                            save_data(json.dumps(article_info, ensure_ascii=False), file_name)
                            count += 1
                            print('ok    ' + str(count))

                    except:
                        print('something wrong go next')
        except:
            continue

if __name__=='__main__':
    autohome_data()
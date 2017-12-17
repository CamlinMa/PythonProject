# -*- coding:utf-8 -*-

from download.web import get_page,get_new_page,save_data
from bs4 import BeautifulSoup
import re
import json
import time
import datetime

def sohu(yestoday):
    max_page=21
    article_collection=[]

    count=0
    index_url='http://api.db.auto.sohu.com/restful/news/list/news/%s/20.json'
    data_name = 'sohu'

    for i in range(1,max_page):

        stamp=str(int(time.time()*1000))
        url=index_url % (str(i))

        page=get_new_page(url,'UTF-8').replace('news(','').replace(');','')
        data=json.loads(page)['result']
        for info in data:
            url=info['url']
            tmps=re.search(r'http://auto.sohu.com/([0-9]+)/n',str(url)).group(1)
            year=str(tmps[0:4])
            month=str(tmps[4:6])
            days=str(tmps[6:8])
            title=info['title']
            page2=get_page(url,'GBK')
            if page2=='':
                continue
            sou2=BeautifulSoup(page2,'html.parser')
            infos=sou2.find('div','left')
            content=''
            try:
                for p in infos.find('div','text clear').find_all('p'):
                    content=content+p.get_text()
            except:
                continue


            article_info={}

            article_info['url'] = url
            article_info['year'] = year
            article_info['month'] = month
            article_info['day'] = days
            article_info['title'] = title
            article_info['content'] = content
            article_info['source'] = 'sohu'
            if str(yestoday) == year + '-' + month + '-' + days:
                file_name = year + '-' + month + '-' + days + '_' + data_name
                save_data(json.dumps(article_info, ensure_ascii=False), file_name)
                count += 1

            # test=json.dumps(article_collection,ensure_ascii=False)
                print('ok    ' + str(count))

    print('save successful!')

if __name__=='__main__':
    # index_url = 'http://auto.sohu.com/qichexinwen.shtml'
    # souhu(index_url)
    sohu()
# _*_ coding:utf-8 _*_

from download.web import *
from bs4 import BeautifulSoup
import re

class Everything:
    def __init__(self,start_url,max_page,encoding='utf-8'):
        self.encoding=encoding
        self.start_url=start_url
        self.new_url_set=[]
        self.old_url_set=[]
        self.new_url_set.append(self.start_url)
        self.site_name=self.get_site_name(self.start_url)
        self.page_list=[]
        self.max_page_num=30
        self.page_count=0
        while len(self.new_url_set)>0 and self.page_count< self.max_page_num:
            tmp_page_list=self.get_page_list(self.new_url_set,self.encoding)
            self.update_url_set(tmp_page_list,self.site_name)
            self.page_list.extend(tmp_page_list)

    def get_page_list(self, new_url_set, encoding):
        page_list=[]
        for url in new_url_set:
            page=get_page(url,encoding)
            self.old_url_set.append(url)
            self.new_url_set.remove(url)
            page_list.append(page)
            self.page_count+=1
            if self.page_count>self.max_page_num:
                return page_list
        return page_list

    def get_url(self, page_list,site_name):
        url_list=[]
        for page in page_list:
            try:
                soup=BeautifulSoup(page,'html.parser')
            except:
                print('something wrong at get soup')
                continue
            for item in soup.find_all('a'):
                try:
                    url_tmp=item.attrs['href']
                except:
                    continue
                if site_name in url_tmp:
                    url_list.append(url_tmp)
        return url_list

    def get_site_name(self, start_url):
        site_name = start_url.replace('http://www.', '').replace('https://www.', '').replace('http://', '').replace(
            'https://', '')
        pattern=re.search(r'(.+)\.',site_name).group(1)
        return pattern

    def update_url_set(self,page_list,site_name):
        new_url_list=self.get_url(page_list,site_name)
        for url in new_url_list:
            if url not in self.old_url_set:
                self.new_url_set.append(url)


# if __name__=='__main__':
#     myspider=Spider('http://news.bitauto.com/')
#     print(myspider.page_list)
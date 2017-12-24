# _*_ coding:utf-8 _*_

# from urllib.request import urlopen,Request
from crawler.file import *
import requests
import re

class Web(object):
    def __init__(self):
        self.Save=Save()
        self.Read=Read()
    def _url_format(self, url):
        if len(url)>220:
            return url.replace('://', '').replace('/', '_').replace('?', '_').replace('.', '')[0:220]
        else:
            return url.replace('://', '').replace('/', '_').replace('?', '_').replace('.','')
    def get_new_page(self, url, encoding,headers):


        # url2=Request(url,headers=headers)
        # #req = urlopen(url)
        req=requests.get(url,headers=headers)
        page = req.content.decode(encoding=encoding,errors='ignore')
        file_name = self._url_format(url)

        self.Save.save_temp(file_name, page)
        return page

    def get_page(self, url, encoding,headers):
        # 下载网页并写入缓存
        file_name = self._url_format(url)
        path = self.Read.check_temp(file_name)
        if path:
            page = self.Read.load_temp_file(path)
            return page
        else:
            page = self.get_new_page(url, encoding=encoding,headers=headers)
            return page

    def get_page_nosave(self, url, encoding,headers):
        # 不保存网页

        req = requests.get(url,headers=headers)
        page = req.content.decode(encoding=encoding, errors='ignore')
        return page
    def post_page(self,url,data,encoding,headers):

        page_res=requests.post(url=url,data=data,headers=headers)
        page=page_res.content.decode(encoding=encoding,errors='ignore')
        return page

    def string2list(self,instr, start_str, end_str):
        # 字符串切为list
        result_list = []
        start_index_tmp = [m.start() for m in re.finditer(start_str, instr)]
        end_index_tmp = [m.start() for m in re.finditer(end_str, instr)]
        index_list = []
        for ss in start_index_tmp:
            for ee in end_index_tmp:
                if ss<ee:
                    index_list.append([ss,ee])
                    end_index_tmp.remove(ee)
                    break



        for li in index_list:
            start = int(li[0])
            end = int(li[1])
            if start<end:
                result_list.append(instr[start:end + len(end_str)])
        return result_list
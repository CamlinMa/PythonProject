# _*_ coding:utf-8 _*_

from urllib.request import urlopen,Request
from crawler.file import *

class Web(object):
    def __init__(self):
        self.Save=Save()
        self.Read=Read()
    def _url_format(self, url):
        return url.replace('://', '').replace('/', '_').replace('?', '_')[:120]

    def get_new_page(self, url, encoding):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            #'Cookie': 's_ria=flash%20not%20detected%7C; s_sv_sid=939829075958; cp_aone_tuuid=c438c4a1-b2b0-4250-8968-5881e7fc5e45; _a1_u=c438c4a1-b2b0-4250-8968-5881e7fc5e45; unit=passengercars; model=2040; _gali=pref_select; utag_main=v_id:015dc2a3ebb700215e00d7561e3c04073002d06b0086e$_sn:1$_ss:0$_st:1502212380388$ses_id:1502209108922%3Bexp-session$_pn:7%3Bexp-session$dc_visit:1$dc_event:8%3Bexp-session$dc_region:ap-northeast-1%3Bexp-session; _tdim=52a03fc1-5dca-4a8d-bbc8-6c629d016e46; _ga=GA1.2.1429794810.1502209317; _gid=GA1.2.1813743088.1502209317; s_cpc=1; s_cc=true; s_sq=%5B%5BB%5D%5D',
            'Referer': 'http://www.smart-j.com/dealer/',
        }
        url2=Request(url,headers=headers)
        req = urlopen(url2)
        page = req.read().decode(encoding=encoding)
        file_name = self._url_format(url)

        self.Save.save_temp(file_name, page)
        return page

    def get_page(self, url, encoding):
        file_name = self._url_format(url)
        path = self.Read.check_temp(file_name)
        if path:
            page = self.Read.load_temp_file(path)
            return page
        else:
            page = self.get_new_page(url, encoding=encoding)
            return page

    def get_page_nosave(self, url, encoding='utf-8'):
        response = urlopen(url)
        page = response.read().decode(encoding=encoding)
        return page
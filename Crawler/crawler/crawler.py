# _*_ coding:utf-8 _*_

from crawler.web import Web
from crawler.file import Save, Read

web = Web()
save = Save()
read = Read()

headers_default = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
}


def get_page(url, encoding='utf-8',headers=headers_default):
    return web.get_page(url, encoding, headers)

def get_page_nosave(url, encoding='utf-8',headers=headers_default):
    return web.get_page_nosave(url, encoding,headers)

def post_page(url, data, encoding='utf-8', headers=headers_default):
    return web.post_page(url=url, data=data, encoding=encoding, headers=headers)

def get_citycode():
    return read.get_citycode()

def create_csv(data_head, file_name):
    save.create_csv(data_head, file_name)

def save_csv(data, file_name):
    save.save_csv(data, file_name)

def string2list(instr,start_str,end_str):
    return web.string2list(instr,start_str,end_str)

def save_txt(data, name):
    save_txt(data, name)

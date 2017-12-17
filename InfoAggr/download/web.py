# -*- coding:utf-8 -*-

from urllib.request import urlopen,Request
from config import *


def create_data(data, file_name):
    path=get_content_path()+file_name+'txt'
    try:
        f = open(path, 'w', encoding='utf-8')
        f.write(data)
        f.close()
    except:
        print('wrong in save data')


def save_data(data, file_name):
    path = get_content_path() +file_name + '.txt'
    try:
        f = open(path, 'a+', encoding='utf-8')
        f.write(data)
        f.close()
    except:
        print('wrong in save data')


def _url_format(url):
    formated_url = url.replace('/', '').replace('?', '').replace(':', '').replace('*', '').replace('<', '').replace('>',
                                                                                                                    '').replace(
        '"', '')
    return formated_url


def get_page(url, encoding='utf-8'):
    page = check_tmp(url)
    if page is None:
        page = get_new_page(url, encoding=encoding)
        save_tmp(url, page)
    return page


def get_new_page(url, encoding):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
    }
    url2 = Request(url,headers=headers)

    try:
        req = urlopen(url2)
        page = req.read().decode(encoding=encoding)
    except:
        try:
            page = req.read().decode(encoding='gb2312')
        except:
            try:
                page = req.read().decode(encoding='gbk')
            except:
                try:
                    page = req.read().decode(encoding='utf-8')
                except:
                    print('error at decode webpage')
                    return
    return page


def check_tmp(url):
    try:
        tmp_path = get_web_tmp_path()
        formated_url = _url_format(url)
        tmp_file_path = tmp_path + formated_url + '.txt'
        if os.path.exists(tmp_file_path):
            f = open(tmp_file_path, 'r', encoding='utf-8')
            page = f.read()
            f.close()
            print('load data from local')
            return page
        else:
            return None
    except:
        print('error at read local temp file')


def save_tmp(url, page):
    #try:
    tmp_path = get_web_tmp_path()
    formated_url = _url_format(url)
    tmp_file_path = tmp_path + formated_url + '.txt'
    try:
        f = open(tmp_file_path, 'w', encoding='utf-8')
        f.write(page)
        f.close()
        print('save web tmp successful')
    except Exception as e:
        print(e)
        print('error at save web tmp')


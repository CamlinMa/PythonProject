# _*_ coding:utf-8 _*_

from crawler.web import Web
from crawler.file import Save, Read

web = Web()
save = Save()
read = Read()


def get_page(url,encoding='utf-8'):
	return web.get_page(url,encoding)


def get_page_nosave(url,encoding):
	return web.get_page_nosave(url,encoding)

def get_citycode():
	return read.get_citycode()


def create_csv(data_head, file_name):
	save.create_csv(data_head, file_name)


def save_csv(data, file_name):
	save.save_csv(data, file_name)

def save_txt(data,name):
	save_txt(data,name)
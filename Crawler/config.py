# _*_ coding:utf-8 _*_

import os

WORK_DIR = os.getcwd().replace('\\', '/').replace('/scrapers','').replace('/scrapers/AU','').replace('/scrapers/CN','').replace('/scrapers/JP','').replace('/scrapers/other','').replace('/scrapers/TW','')


def get_temp_path():
    return WORK_DIR + '/temp'

def get_result_path():
    return WORK_DIR + '/result'

def get_work_path():
    return WORK_DIR

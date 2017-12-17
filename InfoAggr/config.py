# -*- coding:utf-8 -*-

import os

work_dir = (str(os.getcwd()).replace('\\', '/') + '/').replace('InfoAggr/download/','InfoAggr/')


def get_content_path():
    return work_dir + 'local/content/'

def get_web_tmp_path():
    return work_dir + 'local/webTmp/'

def get_templates_path():
    return work_dir + 'templates/'

def get_report_path():
    return work_dir + 'report/'

def get_custom_key_word_path():
    return work_dir+'local/custom_keyword.csv'
def get_keyword_path():
    return work_dir+'local/keysWords/'

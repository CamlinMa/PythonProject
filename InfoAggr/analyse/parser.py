# -*- coding:utf-8 -*-

from config import get_custom_key_word_path,get_content_path,get_keyword_path
import json
import jieba
import pandas as pd
import os
import datetime

class Parser:
    def __init__(self,theday):
        self.auto_keyword=[]
        file_name=str(theday)+'_autoword'
        self.file_list=self.get_file_list(theday)
        for file in self.file_list:
            file_path=get_content_path()+file
            contents=json.loads(self.load_content(file_path),encoding='utf-8')
            self.auto_keyword.extend(self.get_auto_keyword(contents))
        self.save_parser(self.auto_keyword,file_name)



    def __sum_word(self, content, word_list):
        ''' 关键词统计 暂时弃用'''
        word_sum = []
        for word in word_list:
            word_count = str(content).count(word)
            if word_count > 0:
                word_sum.append([word, word_count])
        return word_sum

    def load_content(self, file_path):
        f = open(file_path, 'r', encoding='utf-8')
        content = '['+str(f.read()).replace('}{','},{')+']'
        f.close()
        return content

    def sum_word(self,key_word):
        count=0
        for file_path in self.file_list:
            content_str=self.load_content(file_path)
            try:
                contents = json.loads(content_str)
                for content in contents:
                    if str(key_word) in str(content['content']):
                        count += 1
            except:
                if str(key_word) in content_str:
                    count+=1
        return count

    def get_auto_keyword(self,contents):
        auto_word_list=[]
        tmp=[]
        for content in contents:
            for item in jieba.cut(str(content['content']), cut_all=True):
                if item != '':
                    tmp.append(str(item))

        for word in tmp:
            if len(word)>1:
                auto_word_list.append(word)
        return auto_word_list

    def load_custom_key_word(self):
        ''' 加载自定义关键词 '''
        custom_key_word = []
        path = get_custom_key_word_path()
        data = pd.read_csv(path, encoding='gbk')
        label_list = data.columns.tolist()
        for label in label_list:
            keywords = data[label].tolist()
            for key in keywords:
                custom_key_word.append([key, label])
        return custom_key_word

    def save_parser(self, word_list, file_name):
        path=get_keyword_path()+file_name+'.txt'
        f=open(path,'a+')
        for item in word_list:
            f.write(str(item))
            f.write(',')
        f.close()

    def get_file_list(self, theday):
        file_list=[]
        for file in os.listdir(get_content_path()):
            if str(theday) in str(file):
                file_list.append(file)
        return file_list

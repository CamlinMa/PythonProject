# -*- coding:utf-8 -*-

from config import get_templates_path,get_report_path,get_keyword_path,get_custom_key_word_path
import datetime
import pandas as pd
import webbrowser

class Report:
    def __init__(self, date_range):
        self.word_lists=self.load_word_list(date_range)
        self.file_name=date_range[0]+'-'+date_range[-1]
        self.custom_key_word = self.load_custom_key_word()
        keyword_list_nore=set(self.word_lists)

        self.final_word=[]
        for item in self.custom_key_word:
            word=item[0]
            count=self.word_lists.count(word)
            if count>2:
                self.final_word.append([word,item[1],count])


        for item2 in keyword_list_nore:
            count2=self.word_lists.count(item2)
            if count2>2:
                self.final_word.append([item2,'auto',count2])

        self.final_word=sorted(self.final_word, key=lambda x: x[2], reverse=True)
        self.label=self.get_label(self.final_word)
        self.table = self.create_table(self.final_word)
        self.html=self.load_templates('report.html')
        self.report=self.html % (self.table)
        self.save_report()

    def get_label(self, word_list):
        label = []
        for word_info in word_list:
            label_tmp = word_info[1]
            if label_tmp not in label:
                label.append(label_tmp)
        # label=list(set(label))
        return label

    def load_templates(self,file_name):
        path=get_templates_path()+file_name
        f=open(path,'r',encoding='utf-8')
        html=f.read()
        return html

    def create_table(self,word_list):
        tables=''
        for label in self.label:
            column_1='<td valign="top">'+label +'&nbsp&nbsp <br><br>'
            column_2='<td valign="top">频次 &nbsp&nbsp <br><br>'
            for word in word_list:
                if str(word[0])=='nan' or str(word[2])=='0' or str(word[2])=='1':
                    continue
                if word[1]==label:
                    column_1+=str(word[0])+'&nbsp<br>'
                    column_2+=str(word[2])+'&nbsp<br>'
            column_1+='</td>'
            column_2 += '</td>'
            tables+=column_1+column_2
        return tables

    def save_report(self):
        file_name=str(self.file_name)
        path=get_report_path()+file_name+'_'+'.html'
        f=open(path,'w',encoding='utf-8')
        f.write(self.report)
        f.close()
        webbrowser.open(path)

    def load_word_list(self, date_list):
        dirs=get_keyword_path()
        word_list=[]
        for dat in date_list:
            try:
                path=dirs+dat+'_autoword.txt'
                word_list_tmp=self.get_word_from_file(path)
                word_list.extend(word_list_tmp)
            except:
                continue
        return word_list

    def get_word_from_file(self, path):
        try:
            f=open(path,'r')
            strs=f.read()
            f.close()
        except:
            return
        return strs.split(',')

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
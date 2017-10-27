# -*- coding:utf-8 -*-

from config import *
import csv
import os

color_dict = {
    '1': 'red',
    '2': 'lime ',
    '3': 'blue',
    '4': 'deeppink',
    '5': 'darkorange',
    '6':'gold',
    '7':'black',
    '8':'cyan'
}

def load_data_csv(file_name):
    ''' 加载原始数据'''
    source_data = []
    f = open(get_data_path() + file_name + '.csv', 'r')
    csv_reader = csv.reader(f)
    for item in csv_reader:
        source_data.append(item)
    data_mat, line_index, column_index = formated_data(source_data)
    return data_mat, line_index, column_index


def formated_data(source_data):
    ''' 格式化数据 '''
    data_mat = []
    line_index = []
    for item in source_data:
        line_index.append(item[0])
    line_index.pop(0)
    column_index = source_data[0]
    column_index.pop(0)
    source_data.pop(0)
    for item in source_data:
        item.pop(0)
        tmp = []
        for cells in item:
            tmp.append(float(cells))
        data_mat.append(tmp)
    return data_mat, line_index, column_index


def load_templates(file_name='Report'):
    ''' 加载报告模板 '''
    path = get_templates_path() + file_name + '.html'
    f = open(path, 'r', encoding='utf-8')
    content = f.read()
    f.close()
    return content


def create_report(file_name, html):
    ''' 创建报告 '''
    path = get_rusult_path() + file_name + '.html'
    f = open(path, 'w', encoding='utf-8')
    f.write(html)
    f.close()


def load_mark(file_name):
    ''' 加载标记数据 '''
    path = get_rusult_path() + 'mark/' + file_name + '.txt'
    if os.path.exists(path):
        f = open(path, 'r', encoding='utf-8')
        mark_dict = {}
        mark_dict2 = {}
        mark_list = []
        for item in f.readlines():
            tmp = item.split('	')
            color = int(str(tmp[1]).replace('\n', ''))
            if color in range(1, 7):
                mark_dict[str(tmp[0]).replace('\ufeff', '')] = color_dict[str(color)]
                mark_dict2[str(tmp[2]).replace('\n', '')] = color_dict[str(color)]
            else:
                mark_dict[str(tmp[0]).replace('\ufeff', '')] = 'black'
                mark_dict2[str(tmp[2]).replace('\n', '')] = 'black'
        for it in mark_dict2.keys():
            mark_list.append([mark_dict2[it], it])
        return mark_dict, mark_list
    else:
        return None,None

if __name__=='__main__':
    file_name='2016年竞品上险'
    a,b=load_mark(file_name)
    print(a)
    print(b)

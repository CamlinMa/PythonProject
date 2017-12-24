# _*_ coding:utf-8 _*_

from config import *
import os
import csv
# import time


class Read(object):
    def check_temp(self, file_name):
        # 检查本地缓存
        file_full_name = file_name + '.txt'
        file_list = self.get_file_list()
        if file_full_name in file_list:
            file_path = get_temp_path() + '/' + file_full_name
            return file_path

    def load_temp_file(self, file_path):
        # 加载已缓存文件
        temp_file = open(file_path, 'r')
        page = temp_file.read()
        temp_file.close()
        print('load temp file successful')
        return page

    def read_file(self, file_name):
        file_path = get_temp_path() + '/' + file_name
        page_file = open(file_path, 'r', encoding='utf-8')
        page = page_file.read()
        page_file.close()
        print('load page from temp successful')
        return page

    def get_file_list(self):
        # 获取为缓存文件列表
        dir = get_temp_path()
        return os.listdir(dir)

    def get_citycode(self):
        # 城市代码
        path = get_work_path() + '/lib/citycode.txt'
        try:
            file = open(path, 'r')
            data = file.read()
            file.close()
            citycode_dict = eval(data)
            return citycode_dict
        except:
            print('no citycode.txt file')
            return None


class Save(object):
    def save_csv(self, data, file_name):
        result_file_name = get_result_path() + '/' + file_name + '.csv'
        try:
            result_file = open(result_file_name, 'a+', newline='')
            result_file_writer = csv.writer(result_file)
            result_file_writer.writerows(data)
            result_file.close()
            print('Save: successful')
        except:
            print('failed to save result ')

    def create_csv(self, data_head, file_name):
        result_file_name = get_result_path() + '/' + file_name + '.csv'
        try:
            result_file = open(result_file_name, 'w', newline='')
            result_file_writer = csv.writer(result_file)
            result_file_writer.writerows(data_head)
            result_file.close()
            print('Save: successful')
        except:
            print('failed to save result ')

    def save_temp(self, file_name, page):
        file_path = get_temp_path() + '/' + file_name + '.txt'
        temp_file = open(file_path, 'w')
        temp_file.write(page)
        temp_file.close()

    # print('save temp file successful')
'''
    def save_txt(self, data, file_name):
        result_file_name = get_result_path() + '/' + file_name + '_' + str(time.strftime("%Y%m%d")) + '.txt'

        try:
            result_file = open(result_file_name, 'w+')
        except:
            os.mkdir(get_result_path())
            result_file = open(result_file_name, 'w+')
            print('ok')
        for items in data:
            for item in items:
                result_file.write(item)
                result_file.write(',')
                result_file.write('\n')
            result_file.close()
        print("okkkkkkkk")
'''
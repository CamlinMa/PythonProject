# _*_ coding:utf-8 _*_

from data.file import load_data_csv
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
from matplotlib.font_manager import FontProperties
from config import get_image_path, get_rusult_path
import csv

class Hie:
    def __init__(self, file_name):
        data_mat, line_index, column_index = load_data_csv(file_name)
        data_np = np.mat(data_mat)
        num = 0
        maps = []
        for line in line_index:
            maps.append([line,num])
            #print(line + '  ' + str(num))
            num += 1

        Z = linkage(data_np, 'ward')  # ward  离差平方和

        font = FontProperties(fname="C:\\WINDOWS\\Fonts\\msyh.ttc", size=14)
        plt.figure(figsize=(50, 10))

        plt.title('层次聚类', fontproperties=font)
        plt.xlabel('样本', fontproperties=font)
        plt.ylabel('距离', fontproperties=font)
        dendrogram(Z, leaf_rotation=90, leaf_font_size=8)
        plt.savefig(get_image_path() + file_name + '.png')
        print('聚类完成  已保存为   ' + get_image_path() + file_name + '.png')
        self.create_csv(maps,file_name)
        plt.show()

    def create_csv(self, data_head,file_name ):
        result_file_name = get_rusult_path() + '/' + file_name + '_Map.csv'
        try:
            result_file = open(result_file_name, 'w', newline='')
            result_file_writer = csv.writer(result_file)
            result_file_writer.writerows(data_head)
            result_file.close()
            print('对应表保存成功 ')
        except:
            print('failed to save result ')

#
# h=Hie
# h(file_name='市场分类省份数据2')

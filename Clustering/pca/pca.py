# -*- coding:utf-8 -*-

from sklearn.decomposition import PCA
import numpy as np


class MyPCA:
    def __init__(self, data, components='mle'):
        self.n_components = components
        self.pca = PCA(components)
        self.new_data_list = self.get_data_list(data)
        self.column_index = self.get_column(data)

    def get_data_list(self, data):
        new_data = self.pca.fit_transform(data)
        new_data = new_data.tolist()
        return new_data

    def get_column(self, data):
        column_index = []
        for i in range(len(data[0])):
            column_index.append("第" + str(i + 1) + "主成分")
        return column_index

    def restore_data(self, new_data):
        restored = self.pca.inverse_transform(new_data)
        return restored

# if __name__ == '__main__':
#     data = [
#
#         [1, 2,3],
#         [2, 3,3],
#         [2, 4,5],
#         [1, 2,5]
#     ]
#     datas=np.mat(data)
#     a=MyPCA(datas,components=2)
#     new_data=a.new_data_list
#     res_data=a.restore_data(new_data)
#     print('ddd')

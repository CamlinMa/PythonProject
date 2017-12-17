# _*_ coding:utf-8 _*_

from clustering.kmeans_api import KMeansClustering
from clustering.hierarchical import Hie

# 样本数据文件名  位于 data 文件夹下 文件为 csv 格式
file_name = '城市坐标'

# 聚类任务描述
description = '城市坐标'

flag = 1  # 1 K-means聚类  0 层次聚类
k = 8  # 聚类数
num = 1  # 保留小数

initial_centroids = None  # 初始聚类点
# initial_centroids = ['上海', '阜新市', '商丘市', '大连市', '日照市']

KMeansClustering(
        file_name=file_name,
        k=k,
        description=description,
        weight=None,
        pca=False,
        components=None,
        initialCentroids=initial_centroids,
        num=num)

# _*_ coding:utf-8 _*_

from clustering.kmeans_api import KMeansClustering
from clustering.hierarchical import Hie

# 样本数据文件名  位于 data 文件夹下 文件为 csv 格式
file_name = 'test'

# 聚类任务描述
description = '聚类任务描述'

flag = 1  # 1 K-means聚类（以html形式展示）  0 层次聚类（以图片展示）
k = 6  # 聚类数
num = 1  # 结果保留小数
weight = None  # 聚类权重 None 则不加权重     仅 作用于K-Mean 聚类
initial_centroids = None  # 初始聚类点
# initial_centroids = [] # 直接指定样本名称即可，长度需与聚类数 k 保持一致

# 主成分分析
pca = False  # pca为False 则不进行主成分分析   True
components = None  # 指定保留主成分个数   None 则自动确定

if flag == 1:
    KMeansClustering(
        file_name=file_name,
        k=k,
        description=description,
        weight=weight,
        pca=pca,
        components=components,
        initialCentroids=initial_centroids,
        num=num)
else:
    Hie(file_name=file_name)

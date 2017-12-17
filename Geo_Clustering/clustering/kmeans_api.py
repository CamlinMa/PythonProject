# _*_ coding:utf-8 _*_

import webbrowser
from data.file import *
from data.process import *
from clustering.kmeans import Kmeans
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from config import *
from pca.pca import *
from sklearn.cluster import k_means
from mpl_toolkits.basemap import Basemap
import numpy as np


class Graph:
    def __init__(self, result_data, file_name, column_index):
        self.data = result_data
        self.color_list= ['red','lime','blue','deeppink','darkorange','gold','black','cyan']
        if len(result_data[0][0]) == 2:
            self.path = self.draw2(result_data, file_name, column_index)
        else:
            self.path = self.draws(result_data, file_name)

    def draw2_bk(self, source_data, result_data, file_name, column_index):
        '''绘制二维数据的散点图 '''
        x_axis = str(column_index[0])
        y_axis = str(column_index[1])
        x_list_re = []
        y_list_re = []
        x_list_src = []
        y_list_src = []
        for item in result_data:
            x_list_re.append(float(item[0]))
            y_list_re.append(float(item[1]))
        for item in source_data:
            x_list_src.append(float(item[0]))
            y_list_src.append(float(item[1]))
        font = FontProperties(fname="C:\\WINDOWS\\Fonts\\msyh.ttc", size=14)
        plt.xlabel(x_axis, fontproperties=font)
        plt.ylabel(y_axis, fontproperties=font)
        plt.title('    黄色点为原始数据分布，红色点为聚类质心点 ', fontproperties=font)
        plt.scatter(x_list_src, y_list_src, color='yellow')
        plt.scatter(x_list_re, y_list_re, color='red')
        # plt.show()
        image_path = 'images/' + str(file_name) + '.png'
        plt.savefig(get_data_path() + image_path)
        return image_path

    def draws(self, data, file_name):
        return ''
    def draw2(self,result_data,file_name,column_index):
        '''绘制二维数据的散点图 '''
        x_axis = str(column_index[0])
        y_axis = str(column_index[1])

        font = FontProperties(fname="C:\\WINDOWS\\Fonts\\msyh.ttc", size=14)
        plt.xlabel(x_axis, fontproperties=font)
        plt.ylabel(y_axis, fontproperties=font)
        color_count = 0
        for class_list in result_data:
            x_list=[]
            y_list=[]
            for point in class_list:
                x_list.append(point[0])
                y_list.append(point[1])

            plt.scatter(x_list, y_list, color=self.color_list[color_count])
            #plt.hold()
            color_count+=1

        # plt.show()
        image_path = 'images/' + str(file_name) + '.png'
        plt.savefig(get_data_path() + image_path)
        return image_path

class MapMark:
    ''' 绘制地图并标记坐标 '''
    def __init__(self, coords_class_list,file_name):
        self.color_list = ['red', 'lime', 'blue', 'darkorange', 'gold', 'cyan','magenta','darksage']
        plt.figure(figsize=(16, 8))
        m = Basemap(llcrnrlon=77, llcrnrlat=14, urcrnrlon=140, urcrnrlat=51, projection='lcc', lat_1=33, lat_2=45,
                    lon_0=100)
        m.drawcoastlines()
        m.readshapefile(get_shape(), 'states', drawbounds=True)
        m.drawcountries(linewidth=1.5)
        parallels = np.arange(0., 90, 10.)
        m.drawparallels(parallels, labels=[1, 0, 0, 0], fontsize=10)  # 绘制纬线
        meridians = np.arange(80., 140., 10.)
        m.drawmeridians(meridians, labels=[0, 0, 0, 1], fontsize=10)  # 绘制经线
        color_order=0
        for coords_class in coords_class_list:
            lat, lng = self.get_lat_lng(coords_class)
            x, y = m(lng, lat)
            m.scatter(x, y, edgecolors=self.color_list[color_order], facecolors=self.color_list[color_order], marker='.', s=120)
            color_order+=1
        image_path = 'images/' + str(file_name) + '.png'
        plt.savefig(get_data_path() + image_path)
        self.img_path=image_path

    def get_lat_lng(self, coords_list):
        lat = []
        lng = []
        for coords in coords_list:
            lat.append(coords[0])
            lng.append(coords[1])
        return np.array(lat), np.array(lng)

class KMeansClustering:
    def __init__(self, file_name, k, description, weight, pca, components, initialCentroids, num):
        data_mat, line_index, column_index = load_data_csv(file_name)  # 加载原始数据
        self.file_name = file_name
        self.k = k
        self.mark_dict, self.mark_list = load_mark(self.file_name)
        if weight is None:
            tmp_weight = []
            for yb in data_mat[0]:
                tmp_weight.append(1)
            weight = tmp_weight
        elif len(weight) != len(data_mat[0]):
            print(' 聚类权重错误 ！')
            return
        data_mat_normalized, maxV, minV = data_normalized(data_mat)  # 数据归一化

        # 初始聚类质心
        if initialCentroids is not None:
            initialCentroids2 = []
            for item in initialCentroids:
                init_index = line_index.index(item)
                initialCentroids2.append(data_mat_normalized[init_index])
        else:
            initialCentroids2 = None

        cluster = Kmeans(k, data_mat_normalized, weight, kmeansThreshold=0, initialCentroids=initialCentroids2)  # 聚类
        point = cluster.centroidList

        # 使用sklearn 的k mean 算法
        # cluster_info = k_means(np.mat(data_mat_normalized), k)
        # point2 = cluster_info[0].tolist()
        # label = cluster_info[1].tolist()
        # results, line_index_list = self.get_result2(point2, label, line_index, minV, maxV)  # 获取分类信息

        results, line_index_list,pointset = self.get_result(point, data_mat_normalized, line_index, minV, maxV)  # 获取分类信息
        self.info_A = self.get_info_A(description, column_index, line_index, k, weight)  # 原始数据信息 及 聚类参数
        self.info_B = self.get_info_B(results, column_index, line_index_list, len(line_index), num)  # 聚类结果
        self.info_C = self.get_info_C(line_index_list, len(line_index))  # 聚类点分组
        graph = MapMark(pointset, file_name)  # 绘图
        image_path = graph.img_path  # 图片相对路径

        if pca is True:
            self.pca = MyPCA(np.mat(data_mat), components=components)
            new_data = self.pca.new_data_list
            line_index_pca = line_index
            weight_pca = []
            for i in range(len(column_index)):
                weight_pca.append(1)
            # weight_pca=[70, 10,10,10]
            data_mat_normalized_pca, maxV_pca, minV_pca = data_normalized(new_data)  # 数据归一化

            if initialCentroids is not None:
                initialCentroids3 = []  # 初始聚类质心
                for item in initialCentroids:
                    init_index = line_index.index(item)
                    initialCentroids3.append(data_mat_normalized_pca[init_index])
            else:
                initialCentroids3 = None

            cluster_pca = Kmeans(k, data_mat_normalized_pca, weight_pca, kmeansThreshold=0,
                                 initialCentroids=initialCentroids3)  # 聚类
            point_pca = cluster_pca.centroidList

            results_pca, line_index_list_pca,pointset_pca = self.get_result(point_pca, data_mat_normalized_pca, line_index_pca,
                                                               minV_pca, maxV_pca)  # 获取分类信息

            results_pca_src = self.pca.restore_data(np.mat(results_pca)).tolist()  # 将降维数据还原到原始数据

            self.info_A_pca = self.get_info_A(description, column_index, line_index_pca, k, weight_pca,
                                              pca_num=len(new_data[0]))  # 原始数据信息 及 聚类参数
            self.info_B_pca = self.get_info_B(results_pca_src, column_index, line_index_list_pca, len(line_index_pca),
                                              num)  # 聚类结果
            self.info_C_pca = self.get_info_C(line_index_list_pca, len(line_index_pca))  # 聚类点分组
            graph_pca = Graph(pointset_pca, file_name + "_pca", column_index)  # 绘图
            image_path_pca = graph_pca.path  # 图片相对路径
            self.create_html_pca(self.info_A, self.info_B, self.info_C, file_name + '_' + str(k) + '_', image_path,
                                 image_path_pca, self.info_A_pca, self.info_B_pca, self.info_C_pca)  # 所有结果数据写入html文件
        else:
            self.create_html(self.info_A, self.info_B, self.info_C, file_name + '_' + str(k) + '_',
                             image_path)  # 所有结果数据写入html文件

    def get_info_A(self, description, column_index, line_index, k, weight, pca_num=None):
        '''生成聚类信息和参数设置表格'''
        sample_num = len(line_index)  # 样本数
        features = ''
        for column in column_index:
            features = features + str(column) + '</br>'
        clusters_num = k  # 聚类数
        i = 0
        weight_info = ''
        for feat in column_index:
            weight_info += str(feat) + '&nbsp;&nbsp;' + str(weight[i]) + '</br>'
            i += 1
        if pca_num is None:
            info_A = tuple([description, sample_num, features, weight_info, clusters_num])
        else:
            info_A = tuple([description, sample_num, features, clusters_num, str(pca_num)])
        return info_A

    def get_info_B(self, results, column_index, line_index_list, sums, numss):
        '''生成分类信息表格'''
        # info_B = '<tr><th scope="row">序号</th><td>特征1</td><td>特征2</td><td>特征3</td><td nowrap="nowrap">特征4</td></tr>'
        num = 1
        info_B = '<tr><th scope="row">序号</th>'
        for column in column_index:
            cells = '<td>' + str(column) + '<br></td>'
            info_B += cells
        info_B = info_B + '<td class="info_B_desc">&nbsp;&nbsp;代表样本&nbsp;&nbsp;<br></td>'
        info_B = info_B + '<td class="info_B_desc">&nbsp;&nbsp;样本分布&nbsp;&nbsp;<br></td></tr>'
        i = 0
        for data in results:
            info_B += '<tr><th scope="row">' + str(num) + '</th>'
            for item in data:
                if numss == 0:
                    info_B += '<td>&nbsp' + str(int(item)) + '</td>'
                else:
                    info_B += '<td>&nbsp' + str(round(item, numss)) + '</td>'

            try:
                info_B = info_B + '<td class="info_B_desc"><br>' + str(line_index_list[i][-1]) + '<br>' + str(
                    line_index_list[i][-2]) + '<br></td>'
            except:
                info_B = info_B + '<td class="info_B_desc"><br>' + str(line_index_list[i][-1]) + '<br></td>'
            info_B = info_B + '<td class="info_B_desc"><br>(共' + str(len(line_index_list[i])) + '个样本<br>占比' + str(
                round((len(line_index_list[i]) / float(sums)) * 100, 1)) + '&nbsp%)<br></td></tr>'
            i += 1
            num += 1
        return info_B

    def get_info_C(self, line_index_list, sums):
        '''生成详细分类表格'''
        if self.mark_list is not None:
            info_C = '<tr><th><span style="color:red">备注</span></th><td>'
            for mark in self.mark_list:
                info_C = info_C + '<span style="color:' + str(mark[0]) + '">' + str(mark[1]) + '</span>&nbsp;'
            info_C = info_C + '</td></tr>'

            info_C = info_C + '<tr><th scope="row">序号</th><td>包含的样本</td></tr>'
        else:
            info_C = '<tr><th scope="row">序号</th><td>包含的样本</td></tr>'
        num = 1
        for data in line_index_list:
            info_C += '<tr><td>' + str(num) + '<br>(共' + str(len(data)) + '个样本<br>占比' + str(
                round((len(data) / float(sums)) * 100, 1)) + '&nbsp%)' + '</th><td>'
            num += 1
            count = 1
            if self.mark_dict is None:
                for item in data:
                    info_C += str(item) + ','
                    if count % 5 == 0:
                        info_C += '<br>'
                    count += 1
                info_C += '</td></tr>'
            else:
                for item in data:
                    if item in self.mark_dict.keys():
                        info_C += '<span style="color:' + str(self.mark_dict[item]) + '">' + str(item) + '</span>,'
                    else:
                        info_C += str(item) + ','
                    if count % 5 == 0:
                        info_C += '<br>'
                    count += 1
                info_C += '</td></tr>'
        return info_C

    def create_html(self, info_A, info_B, info_C, file_name, image_path):
        frame = load_templates('frame')  # 框架
        info_A_template = load_templates('info_A')
        info_B_template = load_templates('info_B')  # 加载模板
        info_C_template = load_templates('info_C')
        info_A_html = info_A_template % info_A  # 原始数据信息 及 聚类参数
        info_B_html = info_B_template % info_B  # 分类信息
        info_C_html = info_C_template % info_C  # 详细分组
        image = '<div align="center"><img src="' + str(image_path) + '"></div>'
        html = frame % (info_A_html, info_B_html, image, info_C_html)  # 最终html文件
        create_report(file_name, html)
        print('生成分析报告 成功')
        img_path = get_rusult_path() + file_name + '.html'
        webbrowser.open(img_path, new=1, autoraise=True)

    def get_result(self, point, data_mat_normalized, line_name, minV, maxV):
        '''
        由聚类结果解析信息
        :param point: 聚类点信息
        :param data_mat_normalized: 归一化的数据
        :param line_name: 字段名
        :param minV: 原始数据最小值列表
        :param maxV: 原始数据最大值列表  用以还原归一化的数据
        :return: result1 为聚类质心列表   line_index_list 为每个类包含的样本名
        '''
        line_index_list = []  # 每个分类包含的样本名
        result1 = []  # 每个分类包含的样本特征数据
        pointset = []
        for p in point:
            p2 = p.point.coordinates
            result_p = []
            j = 0
            for p4 in p2:
                tmp = float(p4) * (float(maxV[j]) - minV[j]) + float(minV[j])  # 数据反归一化
                tmp_cells = round(tmp, 5)  # 保留5位有效数字
                j += 1
                result_p.append(tmp_cells)
            result1.append(result_p)
            plist = []
            for pl in p.pointList:
                plist.append(pl.coordinates)
            pointset.append(plist)
        pointset_src=[]
        for p3 in pointset:
            tmp = []
            tmp_pointset2=[]
            for p4 in p3:
                tmp.append(self.get_line_name(p4, data_mat_normalized, line_name))  # 由样本数据信息获取样本名
                j = 0
                tmp_pointset1=[]
                for p5 in p4:
                    src_data = float(p5) * (float(maxV[j]) - minV[j]) + float(minV[j])
                    tmp_pointset1.append(src_data)
                    j+=1
                tmp_pointset2.append(tmp_pointset1)
            pointset_src.append(tmp_pointset2)
            line_index_list.append(tmp)
        return result1, line_index_list,pointset_src

    def get_result2(self, point, label, line_name, minV, maxV):
        '''
        测试 sklearn 算法用
        由聚类结果解析信息
        :param point: 聚类点信息
        :param data_mat_normalized: 归一化的数据
        :param line_name: 字段名
        :param minV: 原始数据最小值列表
        :param maxV: 原始数据最大值列表  用以还原归一化的数据
        :return: result1 为聚类质心列表   line_index_list 为每个类包含的样本名
        '''
        line_index_list = []  # 每个分类包含的样本名
        result1 = []  # 每个分类包含的样本特征数据
        pointset = []
        for p in point:
            result_p = []
            j = 0
            for p4 in p:
                tmp = float(p4) * (float(maxV[j]) - minV[j]) + float(minV[j])  # 数据反归一化
                tmp_cells = round(tmp, 5)  # 保留5位有效数字
                j += 1
                result_p.append(tmp_cells)
            result1.append(result_p)

        for count_class in range(self.k):
            order = 0
            tmp = []
            for label_class in label:
                if count_class == label_class:
                    tmp.append(line_name[order])
                order += 1
            line_index_list.append(tmp)

        return result1, line_index_list

    def compare_list(self, List1, List2):
        ''' 比较列表，相同返回 1 '''
        flag = 1
        if len(List1) == len(List2):
            for i in range(0, len(List1)):
                if List1[i] != List2[i]:
                    flag = 0
                    break
        else:
            flag = 0
        return flag

    def get_line_name(self, info, data_mat_normalized, line_index):
        '''根据样本数据信息获取样本名'''
        count = 0
        for tmp in data_mat_normalized:
            if self.compare_list(info, tmp) == 1:
                line_name = line_index[count]
                return line_name
            else:
                count += 1

    def create_html_pca(self, info_A, info_B, info_C, file_name, image_path, image_path_pca, info_A_pca, info_B_pca,
                        info_C_pca):
        frame = load_templates('demo')  # 框架
        info_A_template = load_templates('info_A')
        info_A_template_pca = load_templates('info_A_pca')
        info_B_template = load_templates('info_B')  # 加载模板
        info_C_template = load_templates('info_C')
        info_A_html = info_A_template % info_A  # 原始数据信息 及 聚类参数
        info_B_html = info_B_template % info_B  # 分类信息
        info_C_html = info_C_template % info_C  # 详细分组

        info_A_html_pca = info_A_template_pca % info_A_pca  # 原始数据信息 及 聚类参数
        info_B_html_pca = info_B_template % info_B_pca  # 分类信息
        info_C_html_pca = info_C_template % info_C_pca  # 详细分组
        image = '<div align="center"><img src="' + str(image_path) + '"></div>'
        image_pca = '<div align="center"><img src="' + str(image_path_pca) + '"></div>'
        html = frame % (info_A_html, info_B_html, image, info_C_html, info_A_html_pca, info_B_html_pca, image_pca,
                        info_C_html_pca)  # 最终html文件
        create_report(file_name, html)

        print('生成分析报告 成功')
        img_path = get_rusult_path() + file_name + '.html'
        webbrowser.open(img_path, new=1, autoraise=True)

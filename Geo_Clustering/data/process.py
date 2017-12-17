# _*_ coding:utf-8 _*_

import numpy as np

'''
def load_data_df(file_name,encoding):
    file_path=get_data_path()+file_name+'.csv'
    data=pd.read_csv(file_path,encoding=encoding,header=0,index_col=0)
    return data
'''
def data_normalized(data_mat):
    '''按特征归一化'''
    normalized_mat = []
    data_mat_t = np.array(np.mat(data_mat).T).tolist()
    max_list = []
    min_list = []
    for i in range(len(data_mat[0])):
        max_list.append(max(data_mat_t[i]))
        min_list.append(min(data_mat_t[i]))
    for line in data_mat_t:
        tmp_line_data = []
        for cells in line:
            if min(line)==max(line):
                v=1
            else:
                v = float(float(cells) - float(min(line))) / (float(max(line)) - float(min(line)))
            tmp_line_data.append(v)
        normalized_mat.append(tmp_line_data)
    normalized_mat = np.array(np.mat(normalized_mat).T).tolist()
    return normalized_mat, max_list, min_list

def data_normalized2(data_mat):
    '''整体归一化'''
    normalized_mat = []
    maxV=float(data_mat[0][0])
    minV = float(data_mat[0][0])
    for line in data_mat:
        if maxV<float(max(line)):
            maxV=float(max(line))
        if minV>float(min(line)):
            minV=float(min(line))
    for item in data_mat:
        tmp=[]
        for cells in item:
            tmp_cells=float((float(cells)-minV)/float(maxV-minV))
            tmp.append(tmp_cells)
        normalized_mat.append(tmp)
    return normalized_mat,minV,maxV





# test_data=[[1,9,3,4],
#            [3,4,5,6],
#            [2,6,3,5]]
#
# data=data_normalized(test_data)
# print('dddd')
# print(data)




# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
import numpy as np


f=open('C:/1__MaQiming/Python/Map/data/city.txt','r')
lat0=[]
lng0=[]
for c in f.readlines():
    tmp=str(c).split('	')
    lat0.append(tmp[0])
    lng0.append(tmp[1])
f.close()
plt.figure(figsize=(16,8))
m = Basemap(llcrnrlon=77, llcrnrlat=14, urcrnrlon=140, urcrnrlat=51, projection='lcc', lat_1=33, lat_2=45, lon_0=100)
m.drawcoastlines()
#m.readshapefile('C:/1__MaQiming/Python/IPython/CHN_adm_shp/CHN_adm1', 'states', drawbounds=False)
m.drawcountries(linewidth=1.5)

lat=np.array(lat0)
lng=np.array(lng0)


parallels = np.arange(0.,90,10.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10) # 绘制纬线

meridians = np.arange(80.,140.,10.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10) # 绘制经线


x,y=m(lng,lat)
m.scatter(x,y,edgecolors='red',facecolors='red',marker='.',s=240)
plt.show()
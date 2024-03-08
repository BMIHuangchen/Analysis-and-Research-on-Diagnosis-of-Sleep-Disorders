# -*- coding:utf-8 -*-
import sys
reload(sys)
import matplotlib
print(matplotlib.matplotlib_fname())
sys.setdefaultencoding('utf-8')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()-0.2, 1.01*height, '%s' % float(height))

#构造区域1
X=np.arange(0, 1, step=1)#X轴的坐标
Y=np.arange(0, 5, step=1)#Y轴的坐标
Z=np.zeros(shape=(1, 5))#设置每一个（X，Y）坐标所对应的Z轴的值，在这边Z（X，Y）=X+Y

#构造区域2
X2=np.arange(1, 2, step=1)
Y2=np.arange(0, 5, step=1)
Z2=np.zeros(shape=(1, 5))
#构造区域3
X3=np.arange(2, 3, step=1)
Y3=np.arange(0, 5, step=1)
Z3=np.zeros(shape=(1, 5))

#定义柱状图的值

list1=[67,89,87,92,85]
list2=[51,60,66,92,75]
list3=[51,60,66,92,75]

#定义Z坐标的值
for i in range(5):
    Z[0,i]=list1[i]
for i in range(5):
    Z2[0,i]=list2[i]
for i in range(5):
    Z3[0,i]=list3[i]

#将坐标网格化
xx, yy=np.meshgrid(X, Y)
xx2,yy2=np.meshgrid(X2, Y2)
xx3,yy3=np.meshgrid(X3, Y3)
#将矩阵扁平化
X, Y,Z=xx.ravel(), yy.ravel(),Z.ravel()
X2,Y2,Z2=xx2.ravel(), yy2.ravel(),Z2.ravel()
X3,Y3,Z3=xx3.ravel(), yy3.ravel(),Z3.ravel()

#每一个柱子的长和宽
width=height=0.5

#绘图设置
fig=plt.figure()
ax=fig.gca(projection='3d')#三维坐标轴
p1=ax.bar3d(X, Y, np.zeros_like(X), width, height, Z, shade=True, color='#9AFF9A',label='A')
p2=ax.bar3d(X2, Y2, np.zeros_like(X2), width, height, Z2, shade=True,color='#1E90FF',label='B')
p3=ax.bar3d(X3, Y3, np.zeros_like(X3), width, height, Z3, shade=True,color='#FFFF00',label='C')

#柱状图上的数字
for xx, yy,zz ,list in zip(X,Y,Z,list1):
	    ax.text(xx+0.2,yy+0.3,zz,list)


#坐标轴设置
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# handles, labels = ax.get_legend_handles_labels()
# ax.legend(handles, labels)
#显示图
plt.show()

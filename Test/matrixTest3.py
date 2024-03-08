#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
# plt.rcParams两行是用于解决标签不能显示汉字的问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

confusion = np.array(([305, 40, 4, 0, 26], [13,  169  , 30   , 0  , 91],[ 1 ,  37 ,1005  ,  1  , 90],[ 1  ,  0 , 106 ,  40  ,  0],[ 2 ,   6  ,  2  ,  0  ,456]))
confusion2 = np.array(([352 ,  7 ,  3 ,  0  ,25],[ 36 , 38  ,12 ,  0,  72],[  6 , 49, 717 ,  4 , 57],[  1 , 15, 174,  53 ,  6],[  0  , 0  , 8 ,  0, 240]))
confusion3 = np.array(([ 85 , 13 ,114  , 1  ,31],[  0  , 2 ,244  , 2  ,30],[  0 ,  0, 929 ,  4 , 14],[  0  , 0 ,111 ,103  , 0],[  0 ,  0 ,276 ,  0 , 66]))
# 热度图，后面是指定的颜色块，可设置其他的不同颜色
plt.imshow(confusion, cmap=plt.cm.Blues)
# ticks 坐标轴的坐标点
# label 坐标轴标签说明
indices = range(len(confusion))

plt.xticks(indices, ['Wake', 'N1', 'N2','N3','REM'],fontsize=20)
plt.yticks(indices, ['Wake', 'N1', 'N2','N3','REM'],fontsize=20)

plt.colorbar()

font1={'size':20,'weight' : 'normal',}
font2={'size':15,'weight' : 'normal',}
plt.xlabel('预测睡眠阶段',font1)
plt.ylabel('真实睡眠阶段',font1)
plt.title('Fpz-Cz混淆矩阵',font1)


# 显示数据
for first_index in range(len(confusion)):    #第几行
    for second_index in range(len(confusion[first_index])):    #第几列
        plt.text(first_index, second_index, confusion[first_index][second_index],font2,ha='center')
plt.show()
###############
# 热度图，后面是指定的颜色块，可设置其他的不同颜色
plt.imshow(confusion, cmap=plt.cm.Blues)
# ticks 坐标轴的坐标点
# label 坐标轴标签说明
indices = range(len(confusion2))

plt.xticks(indices, ['Wake', 'N1', 'N2','N3','REM'],fontsize=20)
plt.yticks(indices, ['Wake', 'N1', 'N2','N3','REM'],fontsize=20)

plt.colorbar()

font1={'size':20,'weight' : 'normal',}
font2={'size':15,'weight' : 'normal',}
plt.xlabel('预测睡眠阶段',font1)
plt.ylabel('真实睡眠阶段',font1)
plt.title('Pz-Oz混淆矩阵',font1)


# 显示数据
for first_index in range(len(confusion2)):    #第几行
    for second_index in range(len(confusion2[first_index])):    #第几列
        plt.text(first_index, second_index, confusion2[first_index][second_index],font2,ha='center')
plt.show()
#######################

# 热度图，后面是指定的颜色块，可设置其他的不同颜色
plt.imshow(confusion3, cmap=plt.cm.Blues)
# ticks 坐标轴的坐标点
# label 坐标轴标签说明
indices = range(len(confusion3))

plt.xticks(indices, ['Wake', 'N1', 'N2','N3','REM'],fontsize=20)
plt.yticks(indices, ['Wake', 'N1', 'N2','N3','REM'],fontsize=20)

plt.colorbar()

font1={'size':20,'weight' : 'normal',}
font2={'size':15,'weight' : 'normal',}
plt.xlabel('预测睡眠阶段',font1)
plt.ylabel('真实睡眠阶段',font1)
plt.title('EOG混淆矩阵',font1)


# 显示数据
for first_index in range(len(confusion3)):    #第几行
    for second_index in range(len(confusion3[first_index])):    #第几列
        plt.text(first_index, second_index, confusion3[first_index][second_index],font2,ha='center')
plt.show()
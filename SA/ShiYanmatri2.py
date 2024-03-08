# -*- coding:utf-8 -*-
import sys
reload(sys)
import matplotlib
print(matplotlib.matplotlib_fname())
sys.setdefaultencoding('utf-8')
import matplotlib.pyplot as plt
import numpy as np
# plt.rcParams两行是用于解决标签不能显示汉字的问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(dpi=200,figsize=(15, 5))
plt.subplot(1, 2, 1)
confusion = np.array(([0, 1], [9, 110]))
# 热度图，后面是指定的颜色块，可设置其他的不同颜色
plt.imshow(confusion, cmap=plt.cm.Blues)
# ticks 坐标轴的坐标点
# label 坐标轴标签说明
indices = range(len(confusion))
# 第一个是迭代对象，表示坐标的显示顺序，第二个参数是坐标轴显示列表 
#plt.xticks(indices, [0, 1, 2])
#plt.yticks(indices, [0, 1, 2])
plt.xticks(indices, ['A', 'N'],fontsize=20)
plt.yticks(indices, ['A', 'N'],fontsize=20)

plt.colorbar()

font1={'size':20,'weight' : 'normal',}
font2={'size':15,'weight' : 'normal',}
fontNeibu={'size':28,'weight' : 'normal',}
plt.xlabel(u'真实睡眠状态\n N：正常，A：呼吸暂停',font1)
plt.ylabel(u'预测睡眠状态',font1)
plt.title('Subject04',font1)



# 显示数据
for first_index in range(len(confusion)):    #第几行
    for second_index in range(len(confusion[first_index])):    #第几列
        plt.text(first_index, second_index, confusion[first_index][second_index],fontNeibu,ha='center')

###################2#####################
plt.subplot(1, 2, 2)
confusion = np.array(([1, 0], [16, 103]))
plt.imshow(confusion, cmap=plt.cm.Blues)

indices = range(len(confusion))

plt.xticks(indices, ['A', 'N'],fontsize=20)
plt.yticks(indices, ['A', 'N'],fontsize=20)

plt.colorbar()

font1={'size':20,'weight' : 'normal',}
font2={'size':15,'weight' : 'normal',}
fontNeibu={'size':28,'weight' : 'normal',}
plt.xlabel(u'真实睡眠状态\n N：正常，A：呼吸暂停',font1)
plt.ylabel(u'预测睡眠状态',font1)
plt.title('Subject05',font1)



# 显示数据
for first_index in range(len(confusion)):    #第几行
    for second_index in range(len(confusion[first_index])):    #第几列
        plt.text(first_index, second_index, confusion[first_index][second_index],fontNeibu,ha='center')
# 在matlab里面可以对矩阵直接imagesc(confusion)
# 显示

plt.show()
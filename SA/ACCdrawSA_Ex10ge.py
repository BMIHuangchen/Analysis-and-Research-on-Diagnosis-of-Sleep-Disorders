# -*- coding:utf-8 -*-
import sys
reload(sys)
import matplotlib
print(matplotlib.matplotlib_fname())
sys.setdefaultencoding('utf-8')
import numpy as np
import matplotlib.pyplot as plt
# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x1=[1,2,3,4,5,6,7,8,9,10]
font1={'size':20,'weight' : 'normal',}

y1 = [85,86.3,85.6,87.1,89.1,86.2,88.9,87.3,87.2,87.3]
y2 = [83.8,84.5,84.1,84.4,85.3,87.2,87.1,86.4,86.1,87.2]
y3 = [83.1,84.6,87.1,86.4,86.3,86.1,86.2,86.1,85.2,85.0]
y4 = [81.5,80.9,83.5,83.4,85.4,82.3,82.1,80.9,83.2,81.9]

plt.figure(figsize=(10, 5))
plt.plot(x1,y1,label='准确率(ACC)', marker='p', ms=5, alpha=1)
plt.plot(x1,y2,label='特异性(SPEC)', marker='p', ms=5, alpha=1)
plt.plot(x1,y3,label='F1值(F1-score)', marker='p', ms=5, alpha=1)
plt.plot(x1,y4,label='灵敏度(SEN)', marker='p', ms=5, alpha=1)

# x轴标签
plt.xlabel(u'实验次数',font1)
# y轴标签
plt.ylabel(u'表现分数(%)',font1)
plt.xticks(fontsize=15)
plt.yticks([80,85,90],fontsize=15)
plt.grid(alpha=0.5,linestyle=':')

# 显示图例
plt.legend(fontsize=14)

plt.show()

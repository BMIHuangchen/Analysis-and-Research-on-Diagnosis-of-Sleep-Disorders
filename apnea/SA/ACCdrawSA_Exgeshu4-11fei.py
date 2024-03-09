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

# 第一组数据
#x1=np.arange(0,10,1)
x1=[1,2,3,4,5,6,7,8,9,10]
font1={'size':20,'weight' : 'normal',}
plt.figure(figsize=(10, 5))
y1 = [86,82.3,84.6,87.1,86.1,86.2,87.2,87.3,87.2,87.3]
y2 = [77.1,87.5,91.1,89.4,88.3,92.2,91.8,91.5,92.8,90.1]
y3 = [69.5,87.6,90.1,91.4,94.3,94.1,94.2,94.1,94.2,94.0]
y4 = [60.5,72.5,75.5,77.4,82.3,81.3,79.8,80.1,80.2,79.9]


plt.plot(x1,y1,label='准确率(ACC)', marker='*', ms=5, alpha=1)
plt.plot(x1,y2,label='特异度(SPEC)', marker='*', ms=5, alpha=1)
plt.plot(x1,y3,label='F1值(F1-score)', marker='*', ms=5, alpha=1)
plt.plot(x1,y4,label='灵敏度(SEN)', marker='*', ms=5, alpha=1)
#plt.plot(x1,y3,label='MA-GP', marker='p', ms=7, alpha=0.7)
# marker='p' 标记为五边形
# mfc='orange'  标记为黄色
# ms=20 标记大小为20
# mec='c' 标记边框颜色为 'c' cyan(青色)
# alpha=0.7 透明度为0.7

# x轴标签
plt.xlabel(u'特征提取层数',font1)
# y轴标签
plt.ylabel(u'表现分数(%)',font1)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.grid(alpha=0.5,linestyle=':')

# 显示图例
plt.legend(fontsize=15)
# 显示图形
plt.show()

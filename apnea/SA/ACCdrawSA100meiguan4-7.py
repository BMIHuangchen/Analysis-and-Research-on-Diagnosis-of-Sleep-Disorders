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
font1={'size':20,'weight' : 'normal',}
plt.figure(dpi=200,figsize=(10, 5))
plt.subplot(1, 2, 1)


y1 = [0.74233658,0.74517807,0.76066228,0.77132463,0.77712562,0.78266019,0.78705275,0.79062075,0.79641615,0.79718189,0.80237466,0.80555734,0.80774522,0.81179217,0.81567221,0.81894709,0.82170551,0.82593363,0.82780391,0.83115842,0.83417887,0.83797574,0.83976787,0.84554661,0.850125,0.85180812,0.85492722,0.85665857,0.85997556,0.86425852,0.8671816,0.87049127,0.87114264,0.87587789,0.87773862,0.88065583,0.88326362,0.88574215,0.88906293,0.88753275,0.89196851,0.89283897,0.89413234,0.89759869,0.90020434,0.90260826,0.90167614,0.9045267,0.90801301,0.9089093,0.90927803,0.91155316,0.91239645,0.91349,0.91577495,0.91824903,0.91803769,0.91935134,0.92143484,0.92280885,0.92308904,0.92403611,0.92535655,0.92617629,0.92740002,0.9291038,0.92942503,0.93089359,0.93215574,0.93220901,0.93302134,0.93432209,0.93588273,0.9355195,0.93596013,0.93785204,0.9384918,0.93901161,0.94001728,0.94015004,0.94076025,0.94334387,0.94273533,0.94381945,0.94442433,0.94490207,0.94557607,0.94751173,0.94647892,0.94740005,0.94836454,0.94938263,0.94895602,0.95022953,0.94997738,0.9516451,0.95209384,0.9526499,0.95341672,0.95475769]
y2 = [0.8055,0.812,0.8145,0.818,0.8115,0.8165,0.82,0.8385,0.84,0.848,0.8485,0.847,0.8405,0.8475,0.8415,0.849,0.849,0.859,0.853,0.857,0.858,0.8565,0.8485,0.859,0.854,0.859,0.855,0.855,0.8555,0.8585,0.8515,0.857,0.8795,0.857,0.874,0.878,0.865,0.873,0.8585,0.8605,0.8705,0.8715,0.8625,0.878,0.8695,0.8705,0.874,0.858,0.8555,0.877,0.866,0.8675,0.8655,0.8705,0.865,0.8705,0.887,0.8555,0.883,0.8715,0.886,0.878,0.8655,0.867,0.873,0.869,0.8675,0.8595,0.875,0.8685,0.8875,0.8885,0.8785,0.8805,0.8845,0.8685,0.885,0.887,0.8745,0.8805,0.8755,0.879,0.8785,0.8765,0.877,0.8715,0.877,0.868,0.877,0.871,0.8565,0.8515,0.8655,0.8745,0.88,0.887,0.8805,0.886,0.895,0.8845]
x = np.arange(len(y1))
#y3 = [14.89476725,12.03964652,11.16210891,10.57985179,10.16923423,9.85444629,9.59059433,9.3908235,9.16442973,8.89937192,8.80710309,8.57262165,8.42878042,8.26285349,8.06949098,7.89601062,7.73197957,7.6635407,7.48665103,7.24342876,7.15322602,7.06384012,6.91652637,6.71802597,6.60428538,6.44255999,6.26388825,6.20023001,5.98137479,5.93144126,5.77197796,5.67147447,5.54695278,5.45624671,5.27994346,5.23126411,5.01971422,5.02263414,4.91223639,4.80187305,4.64230794,4.64332292,4.52991351,4.38761829,4.34034935,4.22472091,4.15998303,4.12877657,4.12264447,3.97188299,3.89099569,3.90125692,3.66737849,3.71102868,3.65447591,3.59254706,3.48644542,3.44091185,3.34439599,3.32284089,3.31693947,3.28550363,3.16230764,3.13717509,3.07896402,2.95739818,2.94080114,2.98481054,2.87863036,2.82303846,2.7942905,2.82505456,2.71788439,2.74147582,2.62783366,2.58771003,2.54786163,2.53713493,2.49595039,2.48934266,2.39329137,2.35316312,2.40353093,2.34642335,2.32072381,2.23295852,2.31393097,2.23717297,2.2033951,2.0981241,2.14514496,2.10777142,2.10229213,2.08735907,2.06814765,2.0659166,2.01400388,1.9732847,1.95753299,1.95094031]
train_loss = [(1-i)   for i in y1]
val_loss = [(1-i)   for i in y2]

# y4 = [60.5,72.5,75.5,77.4,82.3,81.3,79.8,80.1,80.2,79.9]

plt.plot(x,y1,label='训练准确率', ms=5, alpha=1)
plt.plot(x,y2,label='验证准确率', ms=5, alpha=1)
# plt.plot(x1,y3,label='AUC', marker='p', ms=5, alpha=0.7)
# plt.plot(x1,y4,label='Sen', marker='p', ms=5, alpha=0.7)
#plt.plot(x1,y3,label='MA-GP', marker='p', ms=7, alpha=0.7)

# x轴标签
plt.xlabel(u'训练轮数',font1)
plt.ylabel(u'表现分数(%)',font1)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.grid(alpha=0.5,linestyle=':')

# 显示图例
plt.legend(fontsize=15)


####################
# 显示图形
plt.subplot(1, 2, 2)

x = np.arange(len(y1))

plt.plot(x,train_loss,label='训练损失', color='#00FF00',ms=5, alpha=1)
plt.plot(x,val_loss,label='验证损失',color='#FF0000', ms=5, alpha=1)

# x轴标签
plt.xlabel(u'训练轮数',font1)
plt.ylabel(u'表现分数(%)',font1)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.grid(alpha=0.5,linestyle=':')

# 显示图例
plt.legend(fontsize=15)
plt.show()

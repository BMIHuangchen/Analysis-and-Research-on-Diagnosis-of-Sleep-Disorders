import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

font1={'size':15,'weight' : 'normal',}
#82个点
aqn_amp=[1.365, 1.36, 1.305, 1.39, 1.235, 1.14, 1.065, 0.915, 1.13, 0.96, 1.01, 1.245, 1.265, 1.16, 1.07, 1.385, 1.37, 1.33, 1.33, 1.375, 1.22]
plt.figure(dpi=200,figsize=(7,5))
plt.subplot(2, 1, 1)
x = range(0,6300,300)

#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
#pl.xlim(-1, 11)  # 限定横轴的范围
#pl.ylim(-1, 110)  # 限定纵轴的范围
plt.plot(x,aqn_amp, marker='^', mec='r', mfc='r',label=u'心电电压幅值')

plt.legend()  # 让图例生效
plt.xticks(fontsize=15) #设置坐标轴字体
plt.yticks(fontsize=15)
plt.yticks([0,1,1.2,1.4],[0,1,1.2,1.4],fontsize=20)
plt.xticks( rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)

plt.ylabel("电压(mV)",font1) #Y轴标签
plt.xlabel(u"(b)提取的RR间隔",font1) #X轴标签
plt.title("心电电压幅值",font1) #标题

#####################################
rri_ms=[890., 890., 910., 910., 930., 940., 930., 920., 920., 920., 910., 910., 910., 880., 870., 860., 870., 880., 880., 890., 850.]


new_rri_ms = [i /1000  for i in rri_ms]
plt.subplot(2, 1, 2)


x = range(0,6300,300)

plt.plot(x,new_rri_ms, marker='^', mec='r', mfc='r',label=u'心跳间隔')

plt.legend()  # 让图例生效
plt.xticks(fontsize=15) #设置坐标轴字体
plt.yticks(fontsize=15)
plt.xticks( rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)

plt.xlabel(u"(c)提取峰值振幅",font1) #X轴标签
plt.ylabel("时间间隔(s)",font1) #Y轴标签
plt.title("心电电压间隔",font1) #标题

plt.show()


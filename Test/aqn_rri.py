import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

rri_ms=[1110,1160,1030,1110,1150,1090,1140,1160,1110,1160,1170,1110,
 1200,1130,980,890,840,850,950,1010,860,810,790,770,
  750,740,730,700,690,680,670,670,700,720,730,730,
  710,710.,  700.,  750.,  800.,  800.,  780.,  810.,  870.,  970.,  990.,  930.,
  870.,  890.,  950., 1010., 1050., 1020.,  970., 1000.,  990., 1040.,  980., 1020.,
 1160., 1130.,1060., 1050., 1060.,  990., 1010., 1070., 1050. , 950. , 870. , 870.,
 1020., 1090.,  930.,  850.,  800.,  800.,  790.,  800. , 830. , 830.  ,820. , 820.,
  810.,  790.]


new_rri_ms = [i /1000  for i in rri_ms]


plt.figure(figsize=(10, 5))
x = range(len(new_rri_ms))

#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
#pl.xlim(-1, 11)  # 限定横轴的范围
#pl.ylim(-1, 110)  # 限定纵轴的范围
font1={'size':20,'weight' : 'normal',}
plt.plot(new_rri_ms, marker='*', mec='r', mfc='w',label=u'心跳间隔')

plt.legend()  # 让图例生效
plt.xticks(fontsize=20) #设置坐标轴字体
plt.yticks(fontsize=20)
plt.xticks( rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)

plt.xlabel(u"时间(s)",font1) #X轴标签
plt.ylabel("时间间隔(s)",font1) #Y轴标签
plt.title("心电电压间隔",font1) #标题

plt.show()
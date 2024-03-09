import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
import numpy as np

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()-0.2, 1.01*height, '%s' % float(height),size=15)
shops = ["1", "2", "3", "4", "5","6","7","8"]
# w=[96.4,91.63,93.95]
# n1=[65.21,42.45,51.42]
# n2=[92.77,87,89.79]
# n3=[70.41,89.89,78.97]
# rem=[86.76,98.03,92.05]
#
# rem1=[86.76,98.03,92.05]
# rem2=[86.76,98.03,92.05]
# rem3=[86.76,98.03,92.05]
#
# sales_product_1 = [w[0], n1[0], n2[0], n3[0], rem[0],rem1[0],rem2[0],rem3[0]]
# sales_product_2 = [w[1], n1[1], n2[1], n3[1], rem[1],rem1[1],rem2[1],rem3[1]]
# sales_product_3 = [w[2], n1[2], n2[2], n3[2], rem[2],rem1[2],rem2[2],rem3[2]]
sales_product_1 = [72,82.3,84.6,87.1,87.3,87.5,84.2,83.3]
sales_product_2 = [60.5,72.5,75.5,82.1,82.5,82.3,80.8,80.1]
sales_product_3 = [69.5,73.6,82.1,83.4,84.3,84.1,80.2,77.1]
font1 = {'size': 23, 'weight': 'normal', }
# 创建分组柱状图，需要自己控制x轴坐标
xticks = np.arange(len(shops))

fig, ax = plt.subplots(dpi=200,figsize=(15, 8))

a= ax.bar(xticks, sales_product_1, width=0.25, label="准确率", color="#FF6347")
b= ax.bar(xticks + 0.25, sales_product_2, width=0.25, label="灵敏度", color="#00688B")
c= ax.bar(xticks + 0.5, sales_product_3, width=0.25, label="F1值", color="#9AC0CD")

autolabel(a)
autolabel(b)
autolabel(c)

ax.set_title("性能指标",font1)
ax.set_xlabel("特征提取层数",font1)
ax.set_ylabel("表现分数(%)",font1)
ax.legend( loc='lower right',fontsize=15)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)


# 最后调整x轴标签的位置
ax.set_xticks(xticks + 0.25)
ax.set_xticklabels(shops)

zhe=[3.5,4.1,6.1,7.2,9.3,10.4,12.7,14.3]
ax2 =ax.twinx();

d=ax2.plot(xticks+0.25,zhe, 'r',marker='p',ms=10,color="#00FF00",linewidth = 2.5)
ax2.set_ylabel('折线表示训练时长/小时',fontsize=25,color="#00FF00")
ax2.tick_params(labelsize=25)

for tl in ax2.get_yticklabels():
    tl.set_color('#00FF00')



max_times = max(zhe)
for x,y in zip(xticks+0.25, zhe):
    # if(y<=10):
    #     ax2.text(x, y + max_times * 0.01, y, ha='center', va= 'bottom',size=13)
    # else:
    #     ax2.text(x, y - max_times * 0.05, y, ha='center', va='bottom', size=13)
    if (y > 12):
        ax2.text(x+0.2, y - max_times * 0.03, y, ha='center', va= 'bottom',size=15,color = "#00FF00")
    else:
        ax2.text(x, y + max_times * 0.01, y, ha='center', va='bottom', size=15,color = "#00FF00")
plt.show()

# -*- coding:utf-8 -*-
import sys
reload(sys)
import matplotlib
print(matplotlib.matplotlib_fname())
sys.setdefaultencoding('utf-8')
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import roc_curve, auc  ###计算roc和auc
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fpr = [0.2,0.4,0.4,0.6,0.8,0.8,0.8,0.8,1.0,1.0]
tpr = [0,0,0.2,0.2,0.2,0.4,0.6,0.8,0.8,1.0]


plt.plot(fpr,tpr,linewidth=2,label="ROC")

plt.xlabel("false presitive rate")

plt.ylabel("true presitive rate")

plt.ylim(0,1.05)

plt.xlim(0,1.05)

plt.legend(loc=4)#图例的位置

plt.show()


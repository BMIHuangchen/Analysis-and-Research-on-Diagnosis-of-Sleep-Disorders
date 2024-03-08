# -*- coding:utf-8 -*-
import sys
reload(sys)
import matplotlib
print(matplotlib.matplotlib_fname())
sys.setdefaultencoding('utf-8')
from sklearn import datasets
import numpy as np
from sklearn.preprocessing import label_binarize
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, accuracy_score,recall_score, f1_score,roc_auc_score, precision_recall_fscore_support, roc_curve, classification_report
import matplotlib.pyplot as plt

iris = datasets.load_iris()
x, y = iris.data, iris.target
print("label:", y)
n_class = len(set(iris.target))
y_one_hot = label_binarize(y, np.arange(n_class))

# alpha = np.logspace(-2, 2, 20) #设置超参数范围
# model = LogisticRegressionCV(Cs = alpha, cv = 3, penalty = 'l2') #使用L2正则化
model = LogisticRegression() # 内置了最大迭代次数了，可修改
model.fit(x, y)
y_score = model.predict(x) # 输出的是整数标签
mean_accuracy = model.score(x, y)
print("mean_accuracy: ", mean_accuracy)
print("predict label:", y_score)
print(y_score==y)
print(y_score.shape)
y_score_pro = model.predict_proba(x) # 输出概率
print(y_score_pro)
print(y_score_pro.shape)
y_score_one_hot = label_binarize(y_score, np.arange(n_class)) # 这个函数的输入必须是整数的标签哦
print(y_score_one_hot.shape)

obj1 = confusion_matrix(y, y_score) # 注意输入必须是整数型的，shape=(n_samples, )
print('confusion_matrix\n', obj1)

print(y)
print('accuracy:{}'.format(accuracy_score(y, y_score))) # 不存在average
print('precision:{}'.format(precision_score(y, y_score,average='micro')))
print('recall:{}'.format(recall_score(y, y_score,average='micro')))
print('f1-score:{}'.format(f1_score(y, y_score,average='micro')))
print('f1-score-for-each-class:{}'.format(precision_recall_fscore_support(y, y_score))) # for macro
# print('AUC y_pred = one-hot:{}\n'.format(roc_auc_score(y_one_hot, y_score_one_hot,average='micro'))) # 对于multi-class输入必须是proba，所以这种是错误的

# AUC值
auc = roc_auc_score(y_one_hot, y_score_pro,average='micro') # 使用micro，会计算n_classes个roc曲线，再取平均
print("AUC y_pred = proba:", auc)
# 画ROC曲线
print("one-hot label ravelled shape:", y_one_hot.ravel().shape)
fpr, tpr, thresholds = roc_curve(y_one_hot.ravel(),y_score_pro.ravel()) # ravel()表示平铺开来,因为输入的shape必须是(n_samples,)
print("threshold： ", thresholds)
plt.plot(fpr, tpr, linewidth = 2,label='AUC=%.3f' % auc)
plt.plot([0,1],[0,1], 'k--') # 画一条y=x的直线，线条的颜色和类型
plt.axis([0,1.0,0,1.0]) # 限制坐标范围
plt.xlabel('False Postivie Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()

# p-r曲线针对的是二分类，这里就不描述了
ans = classification_report(y, y_score,digits=5) # 小数点后保留5位有效数字
print(ans)

from sklearn.metrics import confusion_matrix    # 生成混淆矩阵函数
import matplotlib.pyplot as plt    # 绘图库
import numpy as np


'''
def plot_confusion_matrix(cm, labels_name, title):
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]    # 归一化
    plt.imshow(cm, interpolation='nearest')    # 在特定的窗口上显示图像
    plt.title(title)    # 图像标题
    plt.colorbar()
    num_local = np.array(range(len(labels_name)))
    plt.xticks(num_local, labels_name, rotation=90)    # 将标签印在x轴坐标上
    plt.yticks(num_local, labels_name)    # 将标签印在y轴坐标上
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

'''
# 生成混淆矩阵：
# 其中pred_y为预测值，y_为网络输出预测值，test_x为测试输入值，test_y为测试真实值。
# （本程序中标签为one-hot形式，故使用tf.argmax(y_, 1)和tf.argmax(test_y, 1)，若标签为普通列表形式，请直接使用y_和test_y）
'''

pred_y = session.run(tf.argmax(y_, 1), feed_dict={X: test_x})
cm = confusion_matrix(np.argmax(test_y, 1), pred_y,)
print(cm)
# [[100   1   0   1   6   0   0]
#  [  2 111   3   0   2   1  24]
#  [  0   2  68   5   4   3   2]
#  [  2   0   1 120   7  26   0]
#  [  2   5   3   2 120  11  14]
#  [  2   0   2  12   8 115   1]
#  [  2  25   0   1  14   4 302]]



plot_confusion_matrix(cm, labels_name, "HAR Confusion Matrix")
# plt.savefig('/HAR_cm.png', format='png')
plt.show()
'''



'''
    cm - 混淆矩阵的数值， 是一个二维numpy数组
    classes - 各个类别的标签（label）
    title - 图片标题
    cmap - 颜色图
'''
def plot_Matrix(cm, classes, title=None, cmap=plt.cm.Greys):
    plt.rc('font', family='Times New Roman', size='8')  # 设置字体样式、大小

    # 按行进行归一化
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    print("Normalized confusion matrix")
    str_cm = cm.astype(np.str).tolist()
    for row in str_cm:
        print('\t'.join(row))
    # 占比1%以下的单元格，设为0，防止在最后的颜色中体现出来
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            if int(cm[i, j] * 100 + 0.5) == 0:
                cm[i, j] = 0

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    # ax.figure.colorbar(im, ax=ax) # 侧边的颜色条带

    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='Actual',
           xlabel='Predicted')

    # 通过绘制格网，模拟每个单元格的边框
    ax.set_xticks(np.arange(cm.shape[1] + 1) - .5, minor=True)
    ax.set_yticks(np.arange(cm.shape[0] + 1) - .5, minor=True)
    ax.grid(which="minor", color="gray", linestyle='-', linewidth=0.2)
    ax.tick_params(which="minor", bottom=False, left=False)

    # 将x轴上的lables旋转45度
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # 标注百分比信息
    fmt = 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            if int(cm[i, j] * 100 + 0.5) > 0:
                ax.text(j, i, format(int(cm[i, j] * 100 + 0.5), fmt) + '%',
                        ha="center", va="center",
                        color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    # plt.savefig('cm.jpg', dpi=300)
    plt.show()

cm=np.array([ [5022, 577, 188, 19, 395], [407, 2468, 989, 4, 965],[130, 630, 27254, 1021, 763],[13, 0, 1236, 6399, 5],[103, 258, 609, 0, 9611]])
lable = np.array([1,2,3,4,5])
plot_Matrix(cm,lable)


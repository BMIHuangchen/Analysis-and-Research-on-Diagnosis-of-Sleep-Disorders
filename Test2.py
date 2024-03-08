import wfdb as wfdb
import matplotlib.pyplot as plt
import numpy as np


# 画心电图
def draw_ecg(x):
    plt.plot(x)
    plt.title('Raw_ECG')
    plt.show()


# 画心电图及其R波位置
def draw_ecg_R(record, annotation):
    plt.plot(record.p_signal)  # 绘制心电信号
    R_v = record.p_signal[annotation.sample]  # 获取R波峰值
    plt.plot(annotation.sample, R_v, 'or')  # 绘制R波
    plt.title('Raw_ECG And R Position')
    plt.show()


def selData(record, annotation, label, R_left):
    a = annotation.symbol
    f = [k for k in range(len(a)) if a[k] == label]  # 找到对应标签R波位置索引
    signal = record.p_signal
    R_pos = annotation.sample[f]
    res = []
    for i in range(len(f)):
        if (R_pos[i] - R_left > 0):
            res.append(signal[R_pos[i] - R_left:R_pos[i] - R_left + 250])
    return res


# 读取心电图数据
def read_ecg_data(filePath, channel_names):
    '''
    读取心电信号文件
    sampfrom: 设置读取心电信号的 起始位置，sampfrom=0表示从0开始读取，默认从0开始
    sampto：设置读取心电信号的 结束位置，sampto = 1500表示从1500出结束，默认读到文件末尾
    channel_names：设置设置读取心电信号名字，必须是列表，channel_names=['MLII']表示读取MLII导联线
    channels：设置读取第几个心电信号，必须是列表，channels=[0, 3]表示读取第0和第3个信号，注意信号数不确定
    record = wfdb.rdrecord('../ecg_data/102', sampfrom=0, sampto = 1500) # 读取所有通道信号
    record = wfdb.rdrecord('../ecg_data/203', sampfrom=0, sampto = 1500,channel_names=['MLII']) # 仅仅读取“MLII”信号
    record = wfdb.rdrecord('../ecg_data/101', sampfrom=0, sampto=3500, channels=[0]) # 仅仅读取第0个信号（MLII）
    print(type(record)) # 查看record类型
    print(dir(record)) # 查看类中的方法和属性
    print(record.p_signal) # 获得心电导联线信号，本文获得是MLII和V1信号数据
    print(record.n_sig) # 查看导联线条数
    print(record.sig_name) # 查看信号名称（列表），本文导联线名称['MLII', 'V1']
    print(record.fs) # 查看采用率
    '''

    record = wfdb.rdrecord(filePath, channel_names=[channel_names])
    print('导联线条数:')
    print(record.n_sig)  # 查看导联线条数
    print('信号名称（列表）')
    print(record.sig_name)  # 查看信号名称（列表），本文导联线名称['MLII', 'V1']

    '''
    读取注解文件
    sampfrom: 设置读取心电信号的 起始位置，sampfrom=0表示从0开始读取，默认从0开始
    sampto：设置读取心电信号的 结束位置，sampto = 1500表示从1500出结束，默认读到文件末尾
    print(type(annotation)) # 查看annotation类型
    print(dir(annotation))# 查看类中的方法和属性
    print(annotation.sample) # 标注每一个心拍的R波的尖锋位置，与心电信号对应
    annotation.symbol  #标注每一个心拍的类型N，L，R等等
    print(annotation.ann_len) # 被标注的数量
    print(annotation.record_name) # 被标注的文件名
    print(wfdb.show_ann_labels()) # 查看心拍的类型
    '''
    annotation = wfdb.rdann(filePath, 'apn')
    print(annotation.symbol)
    return record, annotation


if __name__ == "__main__":
    filePath = 'data/a01'
    Channel_Name = 'ECG'
    record, annotation = read_ecg_data(filePath, Channel_Name)
    #     draw_ecg(record.p_signal)

    draw_ecg_R(record, annotation)
    res = selData(record, annotation, 'N', 100000)
    print(len(res))
    plt.plot(res[0])

    plt.show()


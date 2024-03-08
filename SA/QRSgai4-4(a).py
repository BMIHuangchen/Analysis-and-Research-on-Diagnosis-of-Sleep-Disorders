# -*- coding:utf-8 -*-
import sys
reload(sys)
import matplotlib
print(matplotlib.matplotlib_fname())
sys.setdefaultencoding('utf-8')
import matplotlib.pyplot as plt
import numpy as np
import wfdb
from wfdb import processing
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# Use the gqrs detection algorithm and correct the peaks使用gqrs检测算法并校正峰

def peaks_hr(sig, peak_inds, fs, title, figsize=(15, 5), saveto=None):
    font1 = {'size': 25, 'weight': 'normal', }
    plt.figure(dpi=200,figsize=(10, 4))
    #fig, ax_left = plt.subplots(figsize=figsize)

    plt.plot(sig, color='#2a5caa', label='Signal')
    plt.plot(peak_inds,sig[peak_inds] , 'rx', marker='^', color='red', label='Peak', markersize=15)

    plt.title(title,font1)

    plt.xlabel(u'采样点\n (a)确定R峰位置',font1)
    plt.ylabel('ECG (mV)',font1)
    plt.xticks(fontsize=20)
    plt.yticks([-0.4,0,0.4,0.8],[-0.6,0,0.6,1.2],fontsize=20)
    #ax_left.set_xticklabels(fontsize='15')


    # Make the y-axis label, ticks and tick labels match the line color.
    plt.tick_params('y', colors='#000000')

    plt.show()


#  加载wfdb记录和physical样本
record = wfdb.rdrecord('../mit/100', sampfrom=0000, sampto=6000, channels=[0])

# Use the gqrs algorithm to detect qrs locations in the first channel   使用gqrs算法检测第一个通道中的qrs位置
qrs_inds = processing.gqrs_detect(sig=record.p_signal[:, 0], fs=record.fs)

# Plot results
#peaks_hr(sig=record.p_signal, peak_inds=qrs_inds, fs=record.fs,title="原GQRS波峰")

# Correct the peaks shifting them to local maximum   校正峰，将其移动到局部最大值
min_bpm = 20
max_bpm = 230
# min_gap = record.fs * 60 / min_bpm
# Use the maximum possible bpm as the search radius     使用最大可能的bpm作为搜索半径
search_radius = int(record.fs * 60 / max_bpm)
corrected_peak_inds = processing.correct_peaks(record.p_signal[:, 0], peak_inds=qrs_inds,
                                               search_radius=search_radius, smooth_window_size=150)

# Display results
print('Corrected gqrs detected peak indices:', sorted(corrected_peak_inds))
peaks_hr(sig=record.p_signal, peak_inds=sorted(corrected_peak_inds), fs=record.fs,
         title=u"ECG波峰检测")

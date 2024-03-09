#coding=utf-8
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
import wfdb
from wfdb import processing

# Use the gqrs detection algorithm and correct the peaks  使用gqrs检测算法并校正峰

def peaks_hr(sig, peak_inds, fs, title, figsize=(20, 10), saveto=None):
    "Plot a signal with its peaks and heart rate"
    # Calculate heart rate
    hrs = processing.compute_hr(sig_len=sig.shape[0], qrs_inds=peak_inds, fs=fs)

    N = sig.shape[0]

    fig, ax_left = plt.subplots(figsize=figsize)
    ax_right = ax_left.twinx()

    ax_left.plot(sig, color='#3979f0', label='Signal')
    ax_left.plot(peak_inds, sig[peak_inds], 'rx', marker='x', color='#8b0000', label='Peak', markersize=12)
    ax_right.plot(np.arange(N), hrs, label='Heart rate', color='m', linewidth=2)

    ax_left.set_title(title)

    ax_left.set_xlabel('Time (ms)')
    ax_left.set_ylabel('ECG (mV)', color='#3979f0')
    ax_right.set_ylabel('Heart rate (bpm)', color='m')
    # Make the y-axis label, ticks and tick labels match the line color.
    ax_left.tick_params('y', colors='#3979f0')
    ax_right.tick_params('y', colors='m')
    if saveto is not None:
        plt.savefig(saveto, dpi=600)
    plt.show()


# rdrecord使用
record = wfdb.rdrecord('data/a02')
plt.plot(record.p_signal[0: 1000, 0])
plt.show()

#rdsamp使用
#使用简化的“ rdsamp”函数,读取WFDB记录的某些通道和部分，该函数返回一个numpy数组和一个字典。 显示数据。
signals, fields = wfdb.rdsamp('data/a02', channels=[0], sampfrom=0, sampto=1500)
display(signals)
display(fields)

record = wfdb.rdheader('data/a01')
display(record.__dict__)

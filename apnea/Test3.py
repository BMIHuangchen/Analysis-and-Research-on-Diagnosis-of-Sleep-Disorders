import wfdb
import matplotlib.pyplot as plt

signal, fields=wfdb.rdsamp('mit/100',channels=[0, 1], sampfrom=0, sampto=1500,)
#mitdb数据库的是数据是两导联，格式是[650000,2]的数据，channels是选择读取哪一个导联的

print('signal:',signal)
print('fields:',fields)
plt.plot(signal)
plt.ylabel(fields['units'][0])
plt.legend([fields['sig_name'][0],fields['sig_name'][1]])
plt.show()




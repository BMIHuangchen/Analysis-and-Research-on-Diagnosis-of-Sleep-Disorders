import matplotlib.pyplot as plt
import wfdb
from wfdb import processing

# ======================地址：https://blog.csdn.net/weixin_44191286/article/details/86305591======================
record=wfdb.rdrecord('mit/100', sampto=3600, )
annotation=wfdb.rdann('mit/100', 'atr',sampto=3600, )

wfdb.plot_wfdb(record=record, annotation=annotation,
               title='Record 100 from MIT-BIH Arrhythmia Database', time_units='seconds')


print('annotation:',annotation.__dict__)
print('record:',record.__dict__)
print('signal:',record.p_signal)#这个record其实并不是字典需要用点操作符取出值


# ======================使用XQRS检测算法，并将结果与参考注释进行比较======================
sig, fields=wfdb.rdsamp('mit/100', channels=[0], sampto=15000)
ann_ref=wfdb.rdann('mit/100', 'atr', sampto=1500)

#使用XQRS算法
xqrs=processing.XQRS(sig=sig[:,0], fs=fields['fs'])
xqrs.detect()
#这里还可以直接使用xqrs_detection
#qrs_inds=processing.xqrs_detect(sig=sig[:,0], fs=fields['fs'])

#下面进行算法的结果和注释中的结果相对比
#注意：在100.atr中的qrs注释第一个数是18，而18这个位置上并没有峰值，真正的第一个峰值是在第二个数77开始的所以是[1:]
comparitor=processing.compare_annotations(ref_sample=ann_ref.sample[1:],#见上面注释
                                          test_sample=xqrs.qrs_inds,
                                          window_width=int(0.1*fields['fs']),
                                          signal=sig[:,0])

#输出结果
comparitor.print_summary()
fig=comparitor.plot(title='XQRS detected QRS vs reference annotations',return_fig=True)
# display(fig[0])
plt.show(fig[0])#这一步必须加，不然图片会一闪而逝

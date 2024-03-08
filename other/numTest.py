# -*- coding:utf-8 -*-
import sys
reload(sys)
import matplotlib
print(matplotlib.matplotlib_fname())
sys.setdefaultencoding('utf-8')
import numpy as np
import tensorflow as tf
v_c = np.array([[4]])
print(v_c)
print(v_c.shape)

a=v_c.T[0]
print(a)
print(v_c.T.shape)
y_true=np.array([0,1,1,1])
y_pred=np.array([1,0,1,1])
TP=tf.reduce_sum(y_true*tf.round(y_pred))
TN=tf.reduce_sum((1-y_true)*(1-tf.round(y_pred)))
FP=tf.reduce_sum((1-y_true)*tf.round(y_pred))
FN=tf.reduce_sum(y_true*(1-tf.round(y_pred)))
precision=TP/(TP+FP)
print(precision)

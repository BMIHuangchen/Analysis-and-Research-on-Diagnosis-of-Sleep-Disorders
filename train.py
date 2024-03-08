import keras
import matplotlib.pyplot as plt
import numpy as np
import time
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.layers.recurrent import GRU
from keras.models import Sequential
import keras.backend as K
import wfdb
from sklearn.utils import class_weight
from sklearn.model_selection import train_test_split
from keras.layers import Merge
from keras.layers.convolutional import Conv1D, MaxPooling1D
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.metrics import precision_score, recall_score, f1_score
# import os
# import tensorflow as tf
# import keras.backend.tensorflow_backend as KTF
#
# #进行配置，每个GPU使用90%上限现存
# os.environ["CUDA_VISIBLE_DEVICES"]="0" # 使用编号为0，1号的GPU
# config = tf.ConfigProto()
# config.gpu_options.per_process_gpu_memory_fraction = 0.9 # 每个GPU上限控制在90%以内
# session = tf.Session(config=config)
# # 设置session
# KTF.set_session(session)



# Hyper-parameters
sequence_length = 240
epochs = int(input('Enter Number of Epochs (or enter default 1000): '))
FS = 100.0

class LossHistory(keras.callbacks.Callback):
    def init(self):
        self.losses = []

    def on_epoch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))

def z_norm(result):
    result_mean = np.mean(result)
    result_std = np.std(result)
    result = (result - result_mean) / result_std
    return result

def split_data(X):
    X1 = []
    X2 = []
    for index in range(len(X)):
        X1.append([X[index][0], X[index][1]])
        X2.append([X[index][2], X[index][3]])

    return np.array(X1).astype('float64'), np.array(X2).astype('float64')

def get_data():
    X_train = np.load('train_input.npy', allow_pickle=True)
    y_train = np.load('train_label.npy', allow_pickle=True)

    X_test = np.load('test_input.npy', allow_pickle=True)
    y_test = np.load('test_label.npy', allow_pickle=True)

    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
    '''
    X_train = X_train[:, 0, :]
    X_test = X_test[:, 0, :]
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    '''
    X_train1, X_train2 = split_data(X_train)
    X_test1, X_test2 = split_data(X_test)

    X_train1 = np.transpose(X_train1, (0, 2, 1))
    #X_train2 = np.reshape(X_train2, (X_train2.shape[0], X_train2.shape[1], 1))
    X_test1 = np.transpose(X_test1, (0, 2, 1))
    #X_test2 = np.reshape(X_test2, (X_test2.shape[0], X_test2.shape[1], 1))

    return X_train1, X_train2, y_train, X_test1, X_test2, y_test



def build_model():
    model1 = Sequential()
    layers = {'input': 2, 'hidden1': 128, 'hidden2': 128, 'hidden3': 256,'hidden4': 256,'output': 1}       # 隐含层的特征数
    model1.add(LSTM(layers['hidden1'],
                   input_shape= (sequence_length, layers['input']),
                    recurrent_dropout=0.5,
                   return_sequences=True))

    model1.add(LSTM(
            layers['hidden2'],
            recurrent_dropout=0.5,
            return_sequences=True))

    model1.add(GRU(
        layers['hidden3'],
        recurrent_dropout=0.5,
        return_sequences=True))

    model1.add(GRU(
            layers['hidden4'],
            recurrent_dropout=0.5,
            return_sequences=False))

    model1.summary()

    model2 = Sequential()
    model2.add(Dense(32, input_dim=2))

    model2.summary()

    merged = Merge([model1, model2], mode='concat')

    model = Sequential()

    model.add(merged)
    model.add(Dense(8))
    model.add(Dense(
        output_dim=layers['output'],
        kernel_initializer='normal'))
    model.add(Activation("sigmoid"))

    start = time.time()
    model.compile(loss="binary_crossentropy", optimizer="adam",
                  metrics = ['accuracy'])
    print ("Compilation Time : ", time.time() - start)

    model.summary()
    return model

def plot_acc_loss(acc, loss, val_acc, val_loss):
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 2, 1)
    plt.plot(acc, label='Training Accuracy')
    plt.plot(val_acc, label='Validation Accuracy')
    plt.title(' Accuracy')
    plt.legend()
    # plt.grid()

    plt.subplot(1, 2, 2)

    plt.plot(loss, label='Training Loss')
    plt.plot(val_loss, label='Validation Loss')
    plt.title(' Loss')
    plt.legend()
    # plt.grid()

    plt.show()

def metric_precision(y_true,y_pred):
    TP=tf.reduce_sum(y_true*tf.round(y_pred))
    TN=tf.reduce_sum((1-y_true)*(1-tf.round(y_pred)))
    FP=tf.reduce_sum((1-y_true)*tf.round(y_pred))
    FN=tf.reduce_sum(y_true*(1-tf.round(y_pred)))
    precision=TP/(TP+FP)
    return precision


def roc(y_test, y_pre):
    from sklearn.metrics import roc_curve
    from sklearn.metrics import roc_auc_score as AUC
    import matplotlib.pyplot as plt

    # 利用roc_curve函数获得假阳性率FPR，和真阳性率recall，都是一系列值
    FPR, recall, thresholds = roc_curve(y_test, y_pre)
    # 计算AUC面积
    area = AUC(y_test, y_pre)

    # 画图
    plt.figure()
    plt.plot(FPR, recall, label='ROC curve (area = %0.2f)' % area)
    plt.legend(loc="lower right")
    plt.show()


def run_network(model=None, data=None):
    global_start_time = time.time()

    print ('\nData Loaded. Compiling...\n')
    print('Loading data... ')
    X_train1, X_train2, y_train, X_test1, X_test2, y_test = get_data()

    class_w = class_weight.compute_class_weight('balanced',
                                                     np.unique(y_train),
                                                     y_train)

    print (class_w)

    if model is None:
        model = build_model()
        a = model.get_layer(index=0)
        print(a)
    try:
        print("Training")
        history = LossHistory()
        history.init()
        # metrics=Metrics()
        history = model.fit([X_train1, X_train2], y_train, epochs=epochs, batch_size=256, callbacks=[history], validation_split=0.1, class_weight=class_w)
        train_pred=model.predict([X_train1, X_train2])

        a=train_pred.T[0]
        # s=metric_precision(y_train,a)
        # print(s)
        #f1_left = f1_score(train_pred, y_train, pos_label=0, average='weighted')
        #print(f1_left)

        # Evaluate Model
        y_pred = model.predict([X_test1, X_test2])
        np.savetxt('3jutiPred.txt', y_pred, newline=',', fmt='%s')
        scores = model.evaluate([X_test1, X_test2], y_test)
        roc(y_test,y_pred)
        np.savetxt('1pred.txt', np.around(y_pred), newline=',', fmt='%s')
        np.save
        # train_pred.argmax(axis=1)
        np.savetxt('2zhunque.txt', y_test, newline=',', fmt='%s')

        print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
        val_loss=history.history.get("val_loss")
        val_acc=history.history.get("val_acc")
        loss=history.history.get("loss")
        acc=history.history.get("acc")
        plot_acc_loss(acc, loss, val_acc, val_loss)

        # print(val_loss)
        # print(val_acc)
        # print(loss)
        # print(acc)


    except KeyboardInterrupt:
        print("prediction exception")
        print ('Training duration (s) : ', time.time() - global_start_time)
        return model


    print ('Training duration (s) : ', time.time() - global_start_time)

    return model
from sklearn.metrics import roc_auc_score, classification_report,f1_score,recall_score,precision_score
from keras.callbacks import Callback
class Metrics(Callback):
    def on_train_begin(self, logs={}):
        self.val_f1s = []
        self.val_recalls = []
        self.val_precisions = []


    def on_epoch_end(self, epoch, logs={}):
        val_predict = (np.asarray(self.model.predict(self.model.validation_data[0]))).round()
        val_targ = self.model.validation_data[1]
        _val_f1 = f1_score(val_targ, val_predict,average="weighted")
        _val_recall = recall_score(val_targ, val_predict, average='macro')
        _val_precision = precision_score(val_targ, val_predict, average='macro')
        self.val_f1s.append(_val_f1)
        self.val_recalls.append(_val_recall)
        self.val_precisions.append(_val_precision)
        print("val_f1:% f — val_precision: % f — val_recall % f" % (_val_f1, _val_precision, _val_recall))
        return

run_network()
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def plot_acc_loss(acc, loss, val_acc, val_loss):
    font1 = {'size': 20, 'weight': 'normal', }
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.plot(acc, label='训练正确率',marker='p', alpha=0.7,ms=10)
    plt.plot(val_acc, label='验证正确率', marker='p',alpha=0.7,ms=10)
    plt.title(' 2类',font1)
    plt.legend()
    # plt.grid()


    plt.subplot(1, 3, 2)
    plt.plot(loss, label='训练正确率')
    plt.plot(val_loss, label='训练正确率')
    plt.title(' 3类',font1)
    plt.legend()
    # plt.grid()


    plt.subplot(1, 3, 3)
    plt.plot(loss, label='训练正确率')
    plt.plot(val_loss, label='训练正确率')
    plt.title(' 5类',font1)
    plt.legend()
    plt.show()

acc =[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.91]
loss =[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.91]
val_acc =[0.1,0.5,0.6,0.7,0.8,0.9,0.91,0.92,0.93,0.94]
val_loss =[0.1,0.5,0.6,0.7,0.8,0.9,0.91,0.92,0.93,0.94]
plot_acc_loss(acc, loss, val_acc, val_loss)

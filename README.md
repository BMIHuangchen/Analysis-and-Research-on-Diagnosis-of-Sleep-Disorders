# Analysis-and-Research-on-Diagnosis-of-Sleep-Disorders
基于电生理信号与深度学习 的睡眠障碍诊断分析与研究

1、在睡眠分期阶段， 提出一种睡眠分期网络(Multi-Scale Residual SleepNet，MSR-SleepNet)模型。 该模型结合多尺度残差特征学习网络和时间序列网络将经过散射变换等预处理的生理电信号输入模型中， 得到平均准确率 85.4%和 81.2%的科恩系数与之前报道的原始多导睡眠图(Polysomnography， PSG)睡眠分期的结果相比有所改善， 有利于早期发现存在睡眠障碍的患者。  

2、在睡眠呼吸暂停阶段， 提出了一种呼吸暂停检测网络(Sleep Apean SleepNet，SA-SleepNet)模型。 该模型基于递归神经网络中长短记忆网络(LSTM)和门控制循环器(GRU)并结合心电信号自动检测睡眠呼吸暂停的方法。 利用倾向得分匹配机制对睡眠呼吸暂停样本进行采样， 平衡阳性样本与阴性样本类不平衡问题， 得到准确率 88.9%和82.1%的灵敏度， 有利于发现睡眠障碍患者的呼吸暂停问题。  

3、使用脑机设备和心电采集设备， 进行简单自采集数据实验， 拥有平均 70.17%准确率。 同时从计量经济学中使用向量自回归模型(Vector Autoregression， VAR)对不同设备、 不同采集位置的生理信号进行关联分析， 查看睡眠数据中的时间序列分析， 表明心率、 脑电和眼电对睡眠是有影响的， 各类电信号之间也有影响， 同时也表明计量经济学领域的方法和理论是可行的。  

# 心电图睡眠呼吸暂停检测

用于心电图睡眠呼吸暂停检测的 Keras 实现

## 先决条件

- Keras：在 2.0 以上的 Keras 版本中，"Merge"层已被弃用。本代码保留了 "Merge"层，因此需要旧版本的 Keras。安装 Keras 2.0 版本（仍运行 "Merge"层）：

```py
pip install keras==2.0
```

- [ECG Sleep Apnea Dataset](https://physionet.org/physiobank/database/apnea-ecg/)

## 心电图睡眠呼吸暂停数据集

- 目录中的数据由德国马尔堡菲利普斯大学的Dr. Thomas提供。
- 35 条记录（a01 至 a20、b01 至 b05 和 c01 至 c10）
- 7 至 10 小时的心电图信号、一组呼吸暂停注释、一组机器生成的 QRS 注释
- .dat 文件：心电图信号（每个采样 16 位，Fs=100Hz）
- .apn文件：二进制注释文件，包含对每次记录的每分钟是否出现呼吸暂停的注释
- .qrs 文件：机器生成的二进制注释文件，使用 [sqrs125](https://physionet.org/physiotools/wag/sqrs-1.htm) 制作

```py
wget -r -np http://www.physionet.org/physiobank/database/apnea-ecg/
```

## 开始

### 预处理

- RR 间隔：提取连续心跳之间的时间间隔
- QRS 振幅：计算 R 峰的振幅
- [Age and Sex](https://physionet.org/physiobank/database/apnea-ecg/additional-information.txt)

```py
python pre_proc.py
```

### 训练

- 训练模型

```py
python train.py 
```




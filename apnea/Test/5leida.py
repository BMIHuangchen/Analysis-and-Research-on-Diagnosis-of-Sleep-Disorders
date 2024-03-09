import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
schema = [
("销售", 6000),
("管理", 16000),
("信息技术", 30000),
("客户服务", 38000),
("研发", 52000),
("市场", 25000)
]
v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]

# 拆分schema到标签labs与总分full_marks
labs = []
full_marks = []
for value in schema:
    labs.append(value[0])
    full_marks.append(value[1])

# v1,v2进行归一处里
Y = np.vstack((v1,v2))
Y = Y/np.array(full_marks)

print('labs = {}'.format(labs))
print('Y = {}'.format(Y))
N = len(labs)
r = np.arange(N)
theta = np.linspace(0, 360, N, endpoint=False)

# 调整角度使得正中在垂直线上
adj_angle = theta[-1] + 90 - 360
theta += adj_angle


# 将角度转化为单位弧度
X_ticks = np.radians(theta) # x轴标签所在的位置

# 首尾相连
X = np.append(X_ticks,X_ticks[0])
Y = np.hstack((Y, Y[:,0].reshape(2,1)))

print(' N = {:d}, \n r = {}, \n theta = {}, \n X_ticks = {}'.format(N, r, theta, X_ticks))

fig, ax = plt.subplots(figsize=(5, 5),
                             subplot_kw=dict(projection='polar'))
# 画图
ax.plot(X, Y[0], marker='o')
ax.plot(X, Y[1], marker='o')
ax.set_xticks(X)

# 设置背景坐标系
ax.set_xticklabels(labs, fontproperties = 'labFont', fontsize = 'large') # 设置标签
ax.set_yticklabels([])
ax.spines['polar'].set_visible(False) # 将轴隐藏
ax.grid(axis='y') # 只有y轴设置grid


# 设置X轴的grid
n_grids = np.linspace(0,1, 6, endpoint=True) # grid的网格数
grids = [[i] * (len(X)) for i in n_grids] #grids的半径

for i, grid in enumerate(grids[:-1]): # 给grid 填充间隔色
    ax.plot(X, grid, color='grey', linewidth=0.5)
    if (i>0) & (i % 2 == 0):
        ax.fill_between(X, grids[i], grids[i-1], color='grey', alpha=0.1)

plt.show()


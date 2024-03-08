import matplotlib.pyplot as plt
import numpy as np

# 产生10*10维矩阵
a = np.random.uniform(0.5, 1.0, 400).reshape([20,20])

# 绘制热力图
from matplotlib import cm
plt.imshow(a, interpolation='nearest', cmap=cm.coolwarm, origin='lower')
plt.colorbar(shrink=.92)

plt.xticks(())
plt.yticks(())
plt.show()

# -*- coding:utf-8 -*-
# import sys
# reload(sys)
# import matplotlib
# print(matplotlib.matplotlib_fname())
# sys.setdefaultencoding('utf-8')
import numpy as np
import matplotlib.pyplot as plt

H = np.array([
[6,0,6,0,6],
[0,6,1,6,0],
[6,1,2,1,6],
[0,6,0,6,1],
[6,0,1,0,1],
])  # added some commas and array creation code


fig = plt.figure(figsize=(6, 3.2))

ax = fig.add_subplot(111)
# ax.set_title('colorMap')

# 绘制热力图
from matplotlib import cm
plt.imshow(H,cmap=cm.YlOrRd,vmin=0, vmax=6)
ax.set_aspect('equal')

cax = fig.add_axes([0.12, 0.1, 0.9, 0.8])

# 不要刻度线
plt.axis('off')
ax.axis('off')

cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax.patch.set_alpha(0)
cax.set_frame_on(False)

plt.colorbar(orientation='vertical')
plt.axis('off')
fig = plt.gcf()
fig.set_size_inches(7.0/2,7.0/3)
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())
plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
plt.margins(20,20)
# fig.savefig('./test.png', transparent=True, dpi=2000, pad_inches = 0)


# fig.savefig('./test.svg' , bbox_inches='tight', dpi = 2000)
plt.show()
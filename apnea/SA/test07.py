import os
import numpy as np
import mne
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

sample_data_folder = mne.datasets.sample.data_path()
sample_data_evk_file = os.path.join(sample_data_folder, 'MEG', 'sample',
                                    'sample_audvis-ave.fif')
evokeds_list = mne.read_evokeds(sample_data_evk_file, baseline=(None, 0),
                                proj=True, verbose=False)


# Show the condition names, and reassure ourselves that baseline correction has been applied.
for e in evokeds_list:
    print(f'Condition: {e.comment}, baseline: {e.baseline}')

# convert that list of Evoked objects into a dictionary
conds = ('aud/left', 'aud/right', 'vis/left', 'vis/right')
evks = dict(zip(conds, evokeds_list))

# 指定time = 0.09
fig = evks['aud/left'].plot_topomap(ch_type='mag', times=0.09, average=0.1)

# 标题，由于轴不对称，不能用center，只能自己手动调前俩参数
fig.text(0.2, 0.05, 'Fpz-Cz通道脑地形图')
# dpi切换清晰度，bbox_inches擦边，pad_inches相当于margin
fig.savefig('./test.png', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.show()


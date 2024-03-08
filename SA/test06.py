import os
import numpy as np
import mne
from matplotlib import pyplot as plt

# 如果没有数据则用这个自动下载
# sample_data_folder = mne.datasets.sample.data_path()
# 已有数据，则直接加载即可
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
#      ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ this is equivalent to:
# {'aud/left': evokeds_list[0], 'aud/right': evokeds_list[1],
#  'vis/left': evokeds_list[2], 'vis/right': evokeds_list[3]}

# # signal trace
# evks['aud/left'].plot(exclude=[])
# plt.show()
#
# # pick spatial_color gfp
# evks['aud/left'].plot(picks='mag', spatial_colors=True, gfp=True)
# plt.show()

# 头皮地形图
times = np.linspace(0.05, 0.13, 5)
evks['aud/left'].plot_topomap(ch_type='mag', times=times, colorbar=True)
plt.show()
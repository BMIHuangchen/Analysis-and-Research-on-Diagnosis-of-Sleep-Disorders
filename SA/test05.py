import numpy as np
import matplotlib.pyplot as plt

from mne.datasets import sample
from mne import read_evokeds


path = sample.data_path()
fname = path + '/MEG/sample/sample_audvis-ave.fif'

# load evoked corresponding to a specific condition
# from the fif file and subtract baseline
condition = 'Left Auditory'
evoked = read_evokeds(fname, condition=condition, baseline=(None, 0))

times = np.arange(0.05, 0.151, 0.02)
evoked.plot_topomap(times, ch_type='mag', time_unit='s')
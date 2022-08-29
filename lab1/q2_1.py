import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import math

# Lower and upper bound for the plots
plt_low_bound = 0
plt_up_bound = 0.1

# Frequency of sine wave
freq = 100 	

t1 = np.linspace(plt_low_bound,plt_up_bound,200)
y1 = np.sin(2 * np.pi * freq * t1 + np.pi/6) #Sine wave

fs_min = 2*freq		# Minimum sampling rate
fs_low = fs_min * 0.6
fs_high = fs_min * 3

# Function for sampling values with sampling freq = fs
def get_samples(fs, x1, y1):
	sample_x = np.arange(plt_low_bound,plt_up_bound*fs)/fs
	sample_y = np.empty_like(sample_x)
	idx = 0
	for idx_x in range(len(x1)):
		if idx >= len(sample_x):
			break
		if abs(sample_x[idx] - t1[idx_x]) < 1/fs_min:
			sample_y[idx] = y1[idx_x]
			idx += 1
	return sample_x, sample_y

t_low, y_low = get_samples(fs_low, t1, y1)		# < Minimum sampling rate
t_min, y_min = get_samples(fs_min, t1, y1)		# = Minimum sampling rate
t_high, y_high = get_samples(fs_high, t1, y1)	# > Minimum sampling rate

wave_names = ['Sine wave', 'Discrete time signal x(n) with fs = ' + str(fs_low), \
		'Discrete time signal x(n) with fs = ' + str(fs_min), \
		'Discrete time signal x(n) with fs = ' + str(fs_high)]
plot_colors = ['red', 'blue', 'blue', 'blue']

x = [t1, t_low, t_min, t_high]
y = [y1, y_low, y_min, y_high]

fig, ax = plt.subplots(1, 4,figsize=(15, 2),constrained_layout=True)
for i in range(len(x)):
	ax[i].plot(x[i], y[i], color=plot_colors[i])
	ax[i].set_title(wave_names[i])
	ax[i].set_ylabel('y(t)')
	ax[i].set_xlabel('t in secs')
plt.tight_layout()
plt.show()
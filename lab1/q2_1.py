import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import math

plt_low_bound = 0
plt_up_bound = 0.1
freq = 100 #Frequency of sine wave
t1 = np.linspace(plt_low_bound,plt_up_bound,200)
y1 = np.sin(2 * np.pi * freq * t1 + np.pi/6) #Sine wave
# fig, ax = plt.subplots(1, 2,figsize=(10, 4),constrained_layout=True)
# ax[0].plot(t1,y1,label = 'continuous')
# ax[0].set_title("Sine wave")
# ax[0].set_xlabel('time in sec')
# ax[0].set_ylabel('y(t)')

fs_min = 2*freq
fs_low = fs_min * 0.6
fs_high = fs_min * 3

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

t_min, y_min = get_samples(fs_min, t1, y1)
t_low, y_low = get_samples(fs_low, t1, y1)
t_high, y_high = get_samples(fs_high, t1, y1)

wave_name = ['Sine wave', 'Discrete time signal x(n) with fs = ' + str(fs_min), \
		'Discrete time signal x(n) with fs = ' + str(fs_low), \
		'Discrete time signal x(n) with fs = ' + str(fs_high)]

x = [t1, t_min, t_low, t_high]
y = [y1, y_min, y_low, y_high]

plt.figure(figsize=(10,10))
for i in range(len(x)):
	plt.subplot(5,2,i+1)
	plt.plot(x[i], y[i])
	plt.title(wave_name[i])
	plt.ylabel('Amplitude')
	plt.xlabel('Time')
plt.tight_layout()
plt.show()
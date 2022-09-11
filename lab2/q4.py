import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import math
import random

# 4.1
times = np.arange(0, 40, 0.1)
n_time_points = len(times)

signal = np.zeros(n_time_points)
signal[40] = 2
signal[100] = 1
signal[200] = 3

plt.figure(figsize=(12,12))
plt.subplot(3,2,1)
plt.plot(times, signal)
plt.title('Neural model for three impulses')
plt.ylabel('Neural signal')
plt.xlabel('Time(seconds)')

# 4.2
def hrf(t):
	return t**8.6 * np.exp(-t / 0.547)

hrf_times = np.arange(0, 20, 0.1)
hrf_signal = hrf(hrf_times)
n_hrf_points = len(hrf_signal)

plt.subplot(3,2,2)
plt.plot(hrf_times, hrf_signal)
plt.title('Estimated BOLD signal for event at time 0')
plt.xlabel('Time(seconds)')
plt.ylabel('BOLD signal')

# 4.3
bold_signal = np.zeros(n_time_points)

bold_signal[40:40 + n_hrf_points] = hrf_signal * signal[40]
bold_signal[100:100 + n_hrf_points] += hrf_signal * signal[100]
bold_signal[200:200 + n_hrf_points] += hrf_signal * signal[200]

plt.subplot(3,2,3)
plt.plot(times, bold_signal)
plt.title('Output BOLD signal for three impulses')
plt.xlabel('Time(seconds)')
plt.ylabel('BOLD signal')

# 4.4
N = n_time_points
M = n_hrf_points
bold_signal = np.zeros(N + M - 1)
for i in range(N):
	input_value = signal[i]
	# Adding the shifted, scaled[i]
	bold_signal[i : i + n_hrf_points] += hrf_signal * input_value
# We have to extend 'times' to deal with more points in 'bold_signal'
extra_times = np.arange(n_hrf_points - 1) * 0.1 + 40
times_and_tail = np.concatenate((times, extra_times))
plt.subplot(3,2,4)
plt.plot(times_and_tail, bold_signal)
plt.title('Output BOLD signal using general algorithm')
plt.xlabel('Time(seconds)')
plt.ylabel('BOLD signal')

# 4.5
bold_signal = np.convolve(signal, hrf_signal)
plt.subplot(3,2,5)
plt.plot(times_and_tail, bold_signal)
plt.title('Output BOLD signal using np.convolve')
plt.xlabel('Time(seconds)')
plt.ylabel('BOLD signal')
plt.tight_layout()
plt.show()
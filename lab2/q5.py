import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import math
import random

impulseH = []
impulseH.append(np.asarray([0.06523, 0.14936, 0.21529, 0.2402, 0.21529, 0.14936, 0.06523]))
impulseH.append(np.asarray([-0.06523, -0.14936, -0.21529, 0.7598, -0.21529, -0.14936, -0.06523]))
impulseH.append(np.convolve(impulseH[0], impulseH[1]))

x1 = np.zeros(30)
x1[0] = 1

def plot_graph(plt, y, idx, title, xlabel, ylabel):
	plt.subplot(3, 3, idx)
	plt.xlim(-1, 36)
	plt.stem(y, linefmt='r--')
	plt.plot(y, 'g-+')
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)


y_list = []
titles = []
xlabels = []
ylabels = []

# y_list.append(np.convolve(x1, impulseH[0]))
# # y_float2s.append(signal.lfilter(impulseH[0], [1], x1))

# titles.append('Impulse response of H1')
# xlabels.append('Sample n')
# ylabels.append('H1[n]')
# ^^^ showing that convolution can be realised by np.convolve and scipy.signal.lfilter(BCoeff, [1], impulseX)

# 5.1
for i in range(3):
	y_list.append(np.convolve(x1, impulseH[i]))
	titles.append('Impulse response of H%d' % (i + 1))
	xlabels.append('Sample n')
	ylabels.append('H%d[n]' % (i + 1))

# 5.2
def func_x(y):
	# Generate using np.convolve
	kernel = np.zeros(16)
	kernel[0] = 1
	kernel[15] = -2
	return np.convolve(y, kernel)

	# Manual version of the same function below:
	# y_new = np.zeros(len(y) + 15)
	# y_new[0:len(y)] = y
	# for i in range(len(y) + 15):
	# 	if i >= 15:
	# 		y_new[i] += -2*y[i-15]
	# print(len(y_new))
	# return y_new

for i in range(3):
	y_list.append(np.convolve(x1, func_x(impulseH[i])))
	titles.append('X convolve with H%d' % (i + 1))
	xlabels.append('Sample n')
	ylabels.append('y[n]')

# 5.3
# Returns x1[n] = delta[n]
def func_x1(y):
	kernel = np.zeros(1)
	kernel[0] = 1
	return np.convolve(y, kernel)
# Returns x2[n] = -2delta[n - 15]
def func_x2(y):
	kernel = np.zeros(16)
	kernel[15] = -2
	return np.convolve(y, kernel)

# (h3[n] * x1[n]) + (h3[n] * x2[n])
y1 = func_x1(impulseH[2])
y2 = func_x2(impulseH[2])
y_sum = np.zeros(max(len(y1), len(y2)))
y_sum[0:len(y1)] += y1
y_sum[0:len(y2)] += y2

y_list.append(np.convolve(x1, y_sum))
titles.append('y1[n] + y2[n]')
xlabels.append('Sample n')
ylabels.append('')

# h3[n] * (x1[n] + x2[n])
y = func_x(impulseH[2])
y_list.append(np.convolve(x1, y))
titles.append('h3[n] * (x1[n] + x2[n])')
xlabels.append('Sample n')
ylabels.append('')

plt.figure(figsize=(15,8))
for i in range(len(y_list)):
	plot_graph(plt, y_list[i], i+1, titles[i], xlabels[i], ylabels[i])


plt.tight_layout()
plt.show()


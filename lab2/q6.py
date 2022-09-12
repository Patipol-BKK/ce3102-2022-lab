import pandas as pd
import scipy.fftpack
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import math

dataset = pd.read_csv('ECG.csv')
y = [e for e in dataset.hart]

N = len(y) # Number of samplepoints
Fs = 1000 # Sample spacing
T = 1.0 / Fs
x = np.linspace(0.0, N*T, N)

def plot_graph(plt, x, y, idx, title, xlabel, ylabel, color):
	plt.subplot(3, 2, idx)
	plt.plot(x, y, color = color)
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)

x_list = []
y_list = []
titles = []
xlabels = []
ylabels = []
colors = []

# 6.1
x_list.append(x)
y_list.append(y)
titles.append('ECG signal')
xlabels.append('')
ylabels.append('')
colors.append('red')

xf = np.linspace(0, int(1/(2*T)), int(N/2))
yf = scipy.fftpack.fft(y)
x_list.append(xf)
y_list.append(2.0/N * np.abs(yf[:N//2]))
titles.append('Frequency spectrum')
xlabels.append('')
ylabels.append('')
colors.append('red')

# 6.2
b, a = signal.butter(4, 50/(Fs/2), 'low')
y_filt = signal.filtfilt(b, a, y)

x_list.append(x)
y_list.append(y_filt)
titles.append('ECG signal (Filtered out 50hz noise)')
xlabels.append('')
ylabels.append('')
colors.append('green')

yff = scipy.fftpack.fft(y_filt)
x_list.append(xf)
y_list.append(2.0/N * np.abs(yff[:N//2]))
titles.append('Frequency spectrum')
xlabels.append('')
ylabels.append('')
colors.append('green')

plt.figure(figsize=(15,8))
for i in range(len(y_list)):
	plot_graph(plt, x_list[i], y_list[i], i+1, titles[i], xlabels[i], ylabels[i], colors[i])

plt.tight_layout()
plt.show()
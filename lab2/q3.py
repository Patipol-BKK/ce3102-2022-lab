import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import math
import random

# 3.2
n_samples = 100

signal = np.zeros(n_samples)
signal[np.random.randint(0, n_samples, 5)] = 1

x = np.linspace(0, n_samples - 1, n_samples)
plt.figure(figsize=(10,10))
plt.subplot(5,2,1)
plt.plot(x, signal)
plt.title('Signal')
plt.ylabel('Signal Intensity')
plt.xlabel('Time')

kernel_n_samples = 10
kernel = np.zeros(kernel_n_samples)
kernel[2:8] = 1

# 3.3
kernel_x = np.linspace(0, kernel_n_samples - 1, kernel_n_samples)
plt.subplot(5,2,2)
plt.plot(kernel_x, kernel, color='red')
plt.title('Kernel')
plt.ylabel('Intensity')
plt.xlabel('Time')

# a =np.random.randint(1,10,20)
# b =np.random.randint(1,10,20)
# print('Dot Product: %s'%np.dot(#Fill,#Fill))#dot product

# 3.5
shifted_kernel = np.zeros((n_samples, n_samples + len(kernel) - 1))
rev_kernel = kernel[::-1]# Reversing the kernel
for i in range(n_samples):
	shifted_kernel[i, i:i + len(kernel)] = rev_kernel
#we multiply the shifted kernal and the signal to perform convolution
convolved_signal = np.dot(signal, shifted_kernel)
convolved_x = np.linspace(0, n_samples + len(kernel) - 1, n_samples + len(kernel) - 1)
plt.subplot(5,2,3)
plt.plot(convolved_x, convolved_signal)
plt.title('Signal concolved with boxcar kernel')
plt.ylabel('Intensity')
plt.xlabel('Time')

plt.tight_layout()
plt.show()
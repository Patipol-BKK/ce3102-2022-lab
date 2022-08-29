import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import math

# define gcd function
def gcd(x, y):
	"""
	This function implements the Euclidian algorithm to find G.C.D. of two numbers
	"""
	while(y):
		x, y = y, x % y
	return x

# define lcm function
def lcm(x, y):
	"""
	This function takes two integers and returns the L.C.M.
	"""
	lcm = (x*y)//gcd(x,y)
	return lcm

# define the main function
def main():
	A=0.5; F1=10; Phi = 0; Fs=60; sTime=0; eTime = 1;
	t1 = np.arange(sTime,eTime,1.0/Fs)
	y1 = A*np.cos(2 * np.pi * F1 * t1 + Phi)

	B=0.3; F2=15;
	t2 = np.arange(sTime,eTime,1.0/Fs)
	y2 = B*np.cos(2 * np.pi * F2 * t2 + Phi)

	t3 = np.arange(sTime,eTime,1.0/Fs)
	y3 = y1 + y2

	# how many samples in one cycle
	nSamplesPeriod1 = int(Fs/F1)
	nSamplesPeriod2 = int(Fs/F2)
	nSamplesPeriod_LCM = lcm( int(nSamplesPeriod1),int(nSamplesPeriod2))
	s = 'Number of samples per cycle N1='+ repr(nSamplesPeriod1)+' N2='+ \
		repr(nSamplesPeriod2) + ' LCM = '+ repr(nSamplesPeriod_LCM)
	print(s)
	nSamplesPeriod_int = int(nSamplesPeriod_LCM)

	J = 3 # lets plot J cycles

	fig, ax = plt.subplots(1, 2,figsize=(10, 3),constrained_layout=True)
	ax[0].plot(t1,y1,label = 'continuous', color='red', linestyle='--', marker='.')
	ax[0].plot(t2,y2,label = 'continuous', color='green', linestyle='--', marker='.')
	ax[0].set_ylabel('y(n)')
	ax[0].grid(True)

	ax[1].plot(t3,y3,label = 'continuous', color='blue', linestyle='--', marker='.')
	ax[1].set_ylabel('y(n)')
	ax[1].grid(True)
	plt.show()

if __name__ == '__main__':
	main()
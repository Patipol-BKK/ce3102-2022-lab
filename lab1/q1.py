import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import math

x = np.linspace(-12.5, 12.5, 101)
plt.figure()

# Frequency for generated waves
freq = 0.1

# Wave equations
y_sine 		= np.sin(2*math.pi*freq*x)					# Sine wave
y_cos 		= np.cos(2*math.pi*freq*x)					# Cosine wave
y_unit_imp	= signal.unit_impulse(x.shape, idx='mid')	# Unit impulse
y_unit_step	= x > 0										# Unit step
y_square	= (x > -3)*(x < 3)							# Square wave
y_tri		= signal.sawtooth(2*math.pi*freq*x, 0.5)	# Tringular wave
y_exp		= np.exp(x)									# Exponential wave
y_sawtooth	= signal.sawtooth(2*math.pi*freq*x)			# Sawtooth wave
y_signum	= -1*(x < 0) + (x > 0)						# Signum function
y_sinc		= np.sinc(x)								# Sinc wave
wave_name = ['Sine wave', 'Cosine wave', 'Unit Impulse wave', 'Unit step wave','Squarewave',\
	'Triangular wave','Exponential wave','Sawtooth wave','Sign function','Sincfucntion']

y = [y_sine,y_cos,y_unit_imp,y_unit_step,y_square,y_tri,y_exp,y_sawtooth,y_signum,y_sinc]
plt.figure(figsize=(10,10))
for i in range(10):
 plt.subplot(5,2,i+1)
 plt.plot(x, y[i])
 plt.title(wave_name[i])
 plt.ylabel('Amplitude')
 plt.xlabel('Time')
plt.tight_layout()
plt.show()
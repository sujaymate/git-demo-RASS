import numpy as np
import matplotlib.pyplot as plt

theta = np.deg2rad(np.arange(0, 360, 1))

A = 100
B = 10
sin = A*np.cos(theta - phi) + B

plt.plot(theta, sin)
plt.xlabel("$\\theta$")
plt.ylabel("Amplitude")
plt.show()

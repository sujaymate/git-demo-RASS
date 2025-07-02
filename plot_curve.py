import numpy as np
import matplotlib.pyplot as plt

theta = np.deg2rad(np.arange(0, 360, 1))

A = 200
B = 10
phi = np.deg2rad(30)

sin = A*np.cos(theta - phi) + B

plt.plot(theta, sin)
plt.xlabel("$\\theta$")
plt.ylabel("Amplitude")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

ITERATION = 1000
CAPACITY = 100

ALPHA = 1
exponent1 = 2
exponent2 = 0.5

x1Values = np.zeros(ITERATION)
x2Values = np.zeros(ITERATION)

x1 = 1
x2 = 5
alpha1 = 0
alpha2 = 0
beta1 = 0
beta2 = 0

for i in range(ITERATION):
  if (x1 + x2 <= CAPACITY):
    alpha1 = ALPHA
    alpha2 = ALPHA
    x1 += alpha1
    x2 += alpha2
  else:
    beta1 = exponent2
    beta2 = exponent2
    x1 *= beta1
    x2 *= beta2
  x1Values[i] = x1
  x2Values[i] = x2

plt.plot(x1Values, x2Values, marker=".", linewidth=0.5, markersize=1)
plt.xlim([0, 80])
plt.xlabel('X1 Window size')
plt.ylim([0, 80])
plt.ylabel('X2 Window size')
plt.axline((0, 0), slope=1, color="black", linewidth=0.5)
plt.show()

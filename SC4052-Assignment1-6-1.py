import numpy as np
import matplotlib.pyplot as plt
import math

ITERATION = 1000
CAPACITY = 100
LEARN_RATE_ALPHA = 1
LEARN_RATE_BETA = 0.01

alpha = 1
beta = 0.5

remainX1 = 2000
remainX2 = 1000

x1Values = np.zeros(ITERATION)
x2Values = np.zeros(ITERATION)
network_performance = np.zeros(ITERATION)

x1 = 1
x2 = 10

x1End = 0
x2End = 0

for i in range(ITERATION):
  network_performance[i] = CAPACITY - x1 - x2
  if (i > 0):
    gradient_alpha = (network_performance[i]) * LEARN_RATE_ALPHA
    gradient_beta = (network_performance[i]) * LEARN_RATE_BETA
    alpha += gradient_alpha
    beta += gradient_beta
  if (x1 + x2 <= CAPACITY):
    x1 += alpha
    x2 += alpha
  else:
    x1 *= beta
    x2 *= beta
  x1Values[i] = x1
  x2Values[i] = x2
  remainX1 -= x1 - (0 if x1 + x2 <= CAPACITY else math.ceil((x1 + x2 - CAPACITY) / 2))
  remainX2 -= x2 - (0 if x1 + x2 <= CAPACITY else math.ceil((x1 + x2 - CAPACITY) / 2))
  if remainX1 < 0 and x1End == 0:
    x1End = i
    # x2End = i + (math.ceil(remainX2 / CAPACITY))
    # break
  elif remainX2 < 0 and x2End == 0:
    # x1End = i + (math.ceil(remainX1 / CAPACITY))
    x2End = i
    # break
  if remainX1 < 0 and remainX2 < 0:
    break

print(f"END X1: {x1End} X2: {x2End}")

plt.plot(x1Values, x2Values, marker=".", linewidth=0.5, markersize=1)
plt.xlim([0, 120])
plt.xlabel('X1 Window size')
plt.ylim([0, 120])
plt.ylabel('X2 Window size')
plt.axline((0, 0), slope=1, color="black", linewidth=0.5)
plt.show()


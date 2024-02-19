import numpy as np
import matplotlib.pyplot as plt

ITERATION = 1000
CAPACITY = 100

ALPHA = 1

x1Values = np.zeros(ITERATION)
x2Values = np.zeros(ITERATION)

x1 = 1
x2 = 50

def getIncrement(w):
  if (w <= 20):
    return 20
  elif (w > 120):
    return 220
  else:
    return 20 + (2 * (w - 20))

for i in range(ITERATION):
  if (x1 + x2 <= CAPACITY):
    increment = 1
    x1 += increment
    x2 += increment
  else:
    if (x1 > x2 and (x1 * 0.5) + x2 <= CAPACITY):
      x1 *= 0.5
    elif (x2 > x1 and (x2 * 0.5) + x1 <= CAPACITY):
      x2 *= 0.5
    else:
      x1 *= 0.5
      x2 *= 0.5
  x1Values[i] = x1
  x2Values[i] = x2

plt.plot(x1Values, x2Values, marker=".", linewidth=0.5, markersize=1)
plt.xlim([0, 80])
plt.xlabel('X1 Window size')
plt.ylim([0, 80])
plt.ylabel('X2 Window size')
plt.axline((0, 0), slope=1, color="black", linewidth=0.5)
plt.show()


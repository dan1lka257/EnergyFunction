import matplotlib.pyplot as plt
import numpy as np
n = int(input())
x = np.arange(-5, 5, 0.01)
y = x ** n
graph = plt.plot(x, y)
plt.show()
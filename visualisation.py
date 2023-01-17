
import matplotlib.pyplot as plt
import numpy as np
a = int(input())
x = np.arange(-5, 5, 0.01)
y = a*x*x 
func = plt.plot(x, y)
plt.show()

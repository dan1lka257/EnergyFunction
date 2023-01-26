import matplotlib.pyplot as plt 
import numpy as np
a = int(input())
x=np.arange(0, 1, 0.01)
y = abs(x-0.5)**a
func = plt.plot(x,y)
plt.show()

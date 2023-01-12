import numpy as np
from matplotlib import pyplot as plt
n = int(input())
domain = np.arange(-5, 5, 0.1)
graph = plt.plot(domain, domain**n)
plt.show()
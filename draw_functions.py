import matplotlib.pyplot as plt
import numpy as np
def print_function():
    n = int(input())
    figure = plt.figure(num=2, figsize=(6, 6))
    ax = figure.add_subplot(1, 1, 1)
    lowerLimF = -5
    upperLimF = 5
    x = np.arange(lowerLimF, upperLimF, 0.01)
    y = x ** n
    ax.plot(x, y)
    ax.set_yticks(np.arange(min(0, lowerLimF**n), upperLimF**n + 1, upperLimF**n//10))
    ax.set_xticks(np.arange(-5, 5 + 1, 1))
    ax.grid(color="lightgray", linestyle=":")
    ax.set_title(f"y = x^{n} function", fontsize=20)
    ax.set_ylabel("Axe Y")
    ax.set_xlabel("Axe X")
    plt.show()

print_function()
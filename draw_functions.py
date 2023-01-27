import matplotlib.pyplot as plt
import numpy as np
import argparse

def argparser():
    parser = argparse.ArgumentParser(description='Enter a natural number to draw a graph of the form y = x^n')
    parser.add_argument('number', type=int, help='Natural number')
    args = parser.parse_args()
    return args

def print_function(n):
    figure = plt.figure(num=2, figsize=(6, 6))
    ax = figure.add_subplot(1, 1, 1)
    lowerLimF = -5
    upperLimF = 5
    x = np.arange(lowerLimF, upperLimF, 0.1)
    y = x ** n
    ax.plot(x, y)
    ax.spines['bottom'].set_position(('data',0))
    ax.spines['left'].set_position(('data',0))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_title(f'y = x^{n} function', fontsize=20)
    plt.show()

def isCorrectNumber(num):
    if num > 0:
        print_function(num)
    else:
        print('Natural Numbers contains only positive integers such as 1, 2, 3, 4, 5, 6, and so on.')


num = argparser().number
isCorrectNumber(num)
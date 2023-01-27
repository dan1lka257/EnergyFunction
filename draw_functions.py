import matplotlib.pyplot as plt
import numpy as np
import argparse

def argparser():
    parser = argparse.ArgumentParser(description='Enter a natural number to draw a graph of the form y = x^n')
    parser.add_argument('number', type=int, help='Natural number')
    args = parser.parse_args()
    return args

def print_function(n):
    # figure and axes
    fig = plt.figure(num=2, figsize=(12, 6))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    radius = 1
    # 2d axes
    x1 = np.linspace(0, radius, 1000)
    y1 = abs(x1 - 1/2)**n
    # parameter
    t = 2 * np.pi * x1
    # 3d axes
    x2 = radius * np.cos(t)
    y2 = radius * np.sin(t)
    z2 = np.linspace(0, 0, 1000)
    z3 = abs(x1 - 1/2)**n
    # print all of axes
    ax1.plot(x1, y1, color='black')
    ax2.plot(x2, y2, z2, color='black', alpha=0.5)
    ax2.plot(x2, y2, z3, color='black')
    # move coordinate axes into center
    ax1.spines['bottom'].set_position(('data',0))
    ax1.spines['left'].set_position(('data',0))
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    # text marks on the axes
    ax1.set_xlabel('X', fontweight = 'bold', fontsize = 14)
    ax1.set_ylabel('Y', fontweight = 'bold', fontsize = 14)
    ax1.set_title(f'y = |x - 1/2|^{n} function', fontsize=16)
    ax2.set_xlabel('X', fontweight = 'bold', fontsize = 14)
    ax2.set_ylabel('Y', fontweight = 'bold', fontsize = 14)
    ax2.set_zlabel('Z', fontweight = 'bold', fontsize = 14)
    ax2.set_title(f'y = |x - 1/2|^{n} function into circle', fontsize=16)
    # limiting 3d axes
    ax2.set_xlim(-radius, radius)
    ax2.set_ylim(-radius, radius)
    ax2.set_zlim(0, max(z3))
    plt.show()

def isCorrectNumber(num):
    if num > 0:
        print_function(num)
    else:
        print('Natural Numbers contains only positive integers such as 1, 2, 3, 4, 5, 6, and so on.')


num = argparser().number
isCorrectNumber(num)
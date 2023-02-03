import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
import numpy as np
import argparse
import time

def argparser():
    # defence against fool
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
    y1 = abs(x1 - radius/2)**n
    # parameter
    t = 2 * np.pi * x1 / radius
    # 3d axes
    x2 = radius * np.cos(t)
    y2 = radius * np.sin(t)
    z2 = np.linspace(0, 0, 1000)
    z3 = y1
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
    ax1.set_xlabel('X', fontsize=14)
    ax1.set_ylabel('Y', fontsize=14)
    ax1.set_title(f'y = |x - {radius}/2|^{n} function', fontweight = 'bold', fontsize=16)
    ax2.set_xlabel('X', fontsize=14)
    ax2.set_ylabel('Y', fontsize=14)
    ax2.set_zlabel('Z', fontsize=14)
    ax2.set_title(f'y = |x - {radius}/2|^{n} function into circle', fontweight = 'bold', fontsize=16)
    # limiting 3d axes
    ax2.set_xlim(-radius, radius)
    ax2.set_ylim(-radius, radius)
    ax2.set_zlim(0, max(z3))
    # making animation
    frames1 = []
    frames2 = []
    for i in range(0, 1000, 10):
        line1 = ax1.scatter(x1[i], y1[i], color='black', marker='*', s=100)
        line2 = ax2.scatter(x2[i], y2[i], z3[i], color='black', marker='*', s=100)
        frames1.append([line1])
        frames2.append([line2])
    animation1 = ArtistAnimation(
        fig,
        frames1,
        interval=1000//60,
        repeat=True
    )
    animation2 = ArtistAnimation(
        fig,
        frames2,
        interval=1,
        repeat=True
    )
    plt.show()

def isNaturalNumber(num):
    # Naturality check
    if num > 0:
        print_function(num)
    else:
        print('Natural Numbers contains only positive integers such as 1, 2, 3, 4, 5, 6, and so on.')


num = argparser().number
isNaturalNumber(num)
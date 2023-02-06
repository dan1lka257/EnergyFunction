import numpy as np
import matplotlib.pyplot as plt
import argparse
import mpl_toolkits.mplot3d as Axes3D
def argparser():
    parser = argparse.ArgumentParser(description='Enter a natural number to draw a graph of the form y = |x-0.5|^n')
    parser.add_argument('number', type=int, help='Natural number')
    args = parser.parse_args()
    return args


def print_function(n):
    fig = plt.figure(num=2, figsize=(12, 6))
    ax1 =fig.add_subplot(1,2,1)
    ax2=fig.add_subplot(1,2,2,projection='3d')
    #2d
    x1 = np.linspace(0,1,2000)
    y1 = np.abs(x1-0.5)**n
    #parametr
    par = 2*np.pi* x1
    #3d
    x2 = np.cos(par)
    y2 = np.sin(par)
    z2 = np.linspace(0,0,2000)
    z3 = np.abs(x1-0.5)**n
    #show 
    ax1.plot(x1,y1,color='blue')
    ax2.plot(x1,y2,z2,color='black',alpha=0.3)
    ax2.plot(x2,y2,z3,color='blue')
    # beautiful
    ax1.set_xlabel('X',fontweight='bold',fontsize=14)
    ax1.set_ylabel('Y',fontweight='bold',fontsize=14)
    ax1.set_title(f'y=|x-0.5|^n',fontsize=14)
    ax2.set_xlabel('X',fontweight='bold',fontsize=14)
    ax2.set_ylabel('Y',fontweight='bold',fontsize=14)
    ax2.set_zlabel('Z',fontweight='bold',fontsize=14)
    ax2.set_title(f'y=|x-0.5|^n into circle',fontsize=14)
    plt.show()

def isCorrectNumber(num):
    if num > 0:
        print_function(num)
    else:
        print('Natural Numbers is such as 1, 2, 3, 4, 5, 6, and so on.')


num = argparser().number
isCorrectNumber(num)

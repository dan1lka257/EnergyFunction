import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
import numpy as np
import tkinter as tk
from tkinter import ttk

def print_function(n):
    # figure and axes
    fig = plt.figure(figsize=(12, 6))
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
        interval=1000//60,
        repeat=True
    )
    plt.show()

def isNaturalNumber():
    # Naturality check
    try:
        num = int(entry_1.get())
    except:
        num = -1
    if num > 0 and isinstance(num, int) and combo_1.get() == '|x - 0.5| ^ n':
        print_function(num)
    else:
        print('Natural Numbers contains only positive integers such as 1, 2, 3, 4, 5, 6, and so on.')


win = tk.Tk()
photo = tk.PhotoImage(file='icon.png')
win.iconphoto(False, photo)
win.title('Graph application')
win.config(bg='white')
win.geometry('500x300+1000+150')
win.resizable(False, False)

types_of_graphics = ['|x - 0.5| ^ n', '1', '2', '3', '4']
combo_1 = ttk.Combobox(win, values=types_of_graphics)
button_1 = tk.Button(win, text='Draw', command=isNaturalNumber)
entry_1 = tk.Entry(win)
combo_1.grid(row=0, column=0)
entry_1.grid(row=1, column=0)
button_1.grid(row=2, column=0)

win.grid_columnconfigure(0, minsize=80)
win.grid_columnconfigure(1, minsize=80)

win.mainloop()
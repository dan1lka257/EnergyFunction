import tkinter as tk
from tkinter import ttk
import matplotlib
from matplotlib.animation import ArtistAnimation
import numpy as np
from time import sleep as sleep

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

def start_application():
    n = 3
    # figure and axes
    fig = Figure(figsize=(12, 6))
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
    ax2.set_title(f'y = |x - {radius}/2|^{n} function into circle', fontweight = 'bold',   fontsize=16)
    # limiting 3d axes
    ax2.set_xlim(-radius, radius)
    ax2.set_ylim(-radius, radius)
    ax2.set_zlim(0, max(z3))
    k = 0
    scat1 = ax1.scatter(x1[k], y1[k], color='black', marker='*')
    scat2 = ax2.scatter(x2[k], y2[k], z3[k], color='black', marker='*')
    def running_dot():
        nonlocal k
        if k >= 1000:
            k %= 1000
        k += 25
        scat1 = ax1.scatter(x1[k], y1[k], color='black', marker='*')
        scat2 = ax2.scatter(x2[k], y2[k], z3[k], color='black', marker='*')
        canvas.draw()
        win.after(100, running_dot)
    button_start = tk.Button(win, text="Start", command=running_dot)
    button_start.pack(side=tk.BOTTOM)
    # create FigureCanvasTkAgg object
    canvas = FigureCanvasTkAgg(fig, win)
    # create the toolbar
    toolbar = NavigationToolbar2Tk(canvas, win)
    toolbar.update()
    toolbar.pack(side=tk.BOTTOM, fill=tk.X)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=0)
    canvas.draw()

win = tk.Tk()
photo = tk.PhotoImage(file='icon.png')
win.iconphoto(False, photo)
win.title('Graph application')
win.config(bg='white')
win.geometry('1000x500+150+150')
win.resizable(False, False)

button_1 = tk.Button(win, text='Draw', command=start_application)
button_quit = tk.Button(win, text="Quit", command=win.destroy)
button_1.pack(side=tk.TOP)
button_quit.pack(side=tk.BOTTOM)

win.mainloop()
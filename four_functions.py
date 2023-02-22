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
    if combo_1.get() == '1':
        t = 2 * np.pi * np.linspace(0, 20, 100000)
        x1 = 1 * np.cos(t)
        y1 = 1 * np.sin(t)
    if combo_1.get() == '2':
        t = 2 * np.pi * np.linspace(0, 20 * np.sqrt(2), 100000)
        x1 = 1 * np.cos(t)
        y1 = 1 * np.sin(t)
    if combo_1.get() == '3':
        t = np.linspace(-100, 100, 10000)
        alpha = np.pi - 2 * np.arctan(t / 2)
        x1 = np.sin(alpha)
        y1 = np.cos(alpha) + 1
        print(x1, y1)
    if combo_1.get() == '4':
        t = np.linspace(10, -10, 10000)
        alpha = np.arctan(t)
        x1 = np.cos(alpha)
        y1 = np.sin(alpha)
        x2 = -np.cos(alpha)
        print(x1, y1)
    # figure and axes
    fig = Figure(figsize=(12, 6))
    ax1 = fig.add_subplot(1, 1, 1)
    # 2d axes
    # print all of axes
    ax1.plot(x1, y1, color='black')
    ax1.plot(x2, y1, color='black')
    #ax1.axis('off')
    # text marks on the axes
    ax1.set_xlabel('X', fontsize=14)
    ax1.set_ylabel('Y', fontsize=14)
    ax1.set_title(f'---', fontweight = 'bold', fontsize=16)
    k = 0
    scat1 = ax1.scatter(x1[k], y1[k], color='black', marker='o')
    def running_dot():
        nonlocal k
        k += 100
        if k >= len(x1):
            k %= len(x1)
        scat1 = ax1.scatter(x1[k], y1[k], color='black', marker='o')
        if combo_1.get() == '4':
            ax1.scatter(x2[k], y1[k], color='black', marker='o')
        canvas.draw()
        #scat1.remove()
        win.after(10, running_dot)
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
win.geometry('500x500+150+150')
win.resizable(False, False)

types_of_graphics = ['1', '2', '3', '4']

combo_1 = ttk.Combobox(win, values=types_of_graphics)
combo_1.pack(side=tk.TOP)
button_1 = tk.Button(win, text='Draw', command=start_application)
button_quit = tk.Button(win, text="Quit", command=win.destroy)
button_1.pack(side=tk.TOP)
button_quit.pack(side=tk.BOTTOM)

win.mainloop()
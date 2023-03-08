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
    button_1['state'] = tk.DISABLED
    button_2['state'] = tk.NORMAL
    if combo_1.get() == types_of_graphics[0]:
        firstFunctionStart()
    if combo_1.get() == types_of_graphics[1]:
        secondFunctionStart()
    if combo_1.get() == types_of_graphics[2]:
        thirdFunctionStart()
    if combo_1.get() == types_of_graphics[3]:
        fourthFunctionStart()

def firstFunctionStart():
    # figure and axes
    fig = Figure(figsize=(6, 4))
    ax1 = fig.add_subplot(1, 1, 1)
    p = 2 * np.pi * np.linspace(0, 1, 1000)
    x0 = 1 * np.cos(p)
    y0 = 1 * np.sin(p)
    ax1.plot(x0, y0, color='black')
    t = 3/5 * 2 * np.pi * np.linspace(0, 200, 10000)
    x1 = 1 * np.cos(t)
    y1 = 1 * np.sin(t)
    # text marks on the axes
    ax1.set_xlabel('X', fontsize=14)
    ax1.set_ylabel('Y', fontsize=14)
    ax1.set_title(combo_1.get(), fontweight = 'bold', fontsize=16)
    ax1.axis('off')
    k = 1
    def running_dot():
        nonlocal k
        kmod = k % 1000
        scat1 = ax1.scatter(x1[kmod], y1[kmod], color='black', marker='*')
        canvas.draw()
        k += 10
        if combo_2.get() == 'Yes':
            scat1.remove()
            if k >= 1000:
                k %= 1000
        if combo_2.get() == 'No':
            if k >= 1000:
                return 0
        if button_1['state'] == tk.NORMAL: return 0
        win.after(20, running_dot)
    # create FigureCanvasTkAgg object
    canvas = FigureCanvasTkAgg(fig, win)
    canvas.get_tk_widget().grid(row=0, column=2, rowspan=2000, stick='n')
    canvas.draw()
    running_dot()

def secondFunctionStart():
    # figure and axes
    fig = Figure(figsize=(6, 4))
    ax1 = fig.add_subplot(1, 1, 1)
    p = 2 * np.pi * np.linspace(0, 1, 1000)
    x0 = 1 * np.cos(p)
    y0 = 1 * np.sin(p)
    ax1.plot(x0, y0, color='black')
    t = 2 * np.pi * np.linspace(0, 2000, 100000) * np.sqrt(2)
    x1 = 1 * np.cos(t)
    y1 = 1 * np.sin(t)
    # text marks on the axes
    ax1.set_xlabel('X', fontsize=14)
    ax1.set_ylabel('Y', fontsize=14)
    ax1.set_title(combo_1.get(), fontweight = 'bold', fontsize=16)
    ax1.axis('off')
    k = 1
    def running_dot():
        nonlocal k
        kmod = k % 100000
        scat1 = ax1.scatter(x1[kmod], y1[kmod], color='black', marker='*')
        canvas.draw()
        k += 10
        if combo_2.get() == 'Yes':
            scat1.remove()
            if k >= 100000:
                scat1 = []
                k %= 100000
        if combo_2.get() == 'No':
            if k >= 100000:
                return 0
        if button_1['state'] == tk.NORMAL: return 0
        win.after(20, running_dot)
    # create FigureCanvasTkAgg object
    canvas = FigureCanvasTkAgg(fig, win)
    canvas.get_tk_widget().grid(row=0, column=2, rowspan=2000, stick='n')
    canvas.draw()
    running_dot()

def thirdFunctionStart():
    # figure and axes
    fig = Figure(figsize=(6, 4))
    ax1 = fig.add_subplot(1, 1, 1)
    p = 2 * np.pi * np.linspace(0, 1, 1000)
    x0 = 1 * np.cos(p)
    y0 = 1 * np.sin(p) + 1
    ax1.plot(x0, y0, color='black')
    # figure and axes
    t = np.linspace(-100, 100, 10000)
    alpha = np.pi - 2 * np.arctan(t / 2)
    x1 = np.sin(alpha)
    y1 = np.cos(alpha) + 1
    # text marks on the axes
    ax1.set_xlabel('X', fontsize=14)
    ax1.set_ylabel('Y', fontsize=14)
    ax1.set_title(combo_1.get(), fontweight = 'bold', fontsize=16)
    ax1.axis('off')
    k = 1
    def running_dot():
        nonlocal k
        kmod = k % 10000
        scat1 = ax1.scatter(x1[kmod], y1[kmod], color='black', marker='*')
        canvas.draw()
        k += 25
        if combo_2.get() == 'Yes':
            scat1.remove()
            if k >= 10000:
                scat1 = []
                k %= 10000
        if combo_2.get() == 'No':
            if k >= 10000:
                return 0
        if button_1['state'] == tk.NORMAL: return 0
        win.after(20, running_dot)
    # create FigureCanvasTkAgg object
    canvas = FigureCanvasTkAgg(fig, win)
    canvas.get_tk_widget().grid(row=0, column=2, rowspan=2000, stick='n')
    canvas.draw()
    running_dot()

def fourthFunctionStart():
    # figure and axes
    fig = Figure(figsize=(6, 4))
    ax1 = fig.add_subplot(1, 1, 1)
    p = 2 * np.pi * np.linspace(0, 1, 1000)
    x0 = 1 * np.cos(p)
    y0 = 1 * np.sin(p)
    ax1.plot(x0, y0, color='black')
    t = np.linspace(10, -10, 10000)
    alpha = np.arctan(t)
    x1 = np.cos(alpha)
    y1 = np.sin(alpha)
    x2 = -np.cos(alpha)
    # text marks on the axes
    ax1.set_xlabel('X', fontsize=14)
    ax1.set_ylabel('Y', fontsize=14)
    ax1.set_title(combo_1.get(), fontweight = 'bold', fontsize=16)
    ax1.axis('off')
    k = 1
    def running_dot():
        nonlocal k
        kmod = k % 10000
        scat1 = ax1.scatter(x1[kmod], y1[kmod], color='black', marker='*')
        canvas.draw()
        k += 50
        if combo_2.get() == 'Yes':
            scat1.remove()
            if k >= 10000:
                scat1 = []
                k %= 10000
        if combo_2.get() == 'No':
            if k >= 10000:
                return 0
        if button_1['state'] == tk.NORMAL: return 0
        win.after(20, running_dot)
    # create FigureCanvasTkAgg object
    canvas = FigureCanvasTkAgg(fig, win)
    canvas.get_tk_widget().grid(row=0, column=2, rowspan=2000, stick='n')
    canvas.draw()
    running_dot()

def errorCheck():
    # Yes or No check
    if combo_2.get() != 'Yes' and combo_2.get() != 'No':
        errorWin2 = tk.Tk()
        tk.Label(errorWin2, text='Choose "Yes" or "No"').pack()
        return 0
    start_application()

def clearCanvas():
    button_1['state'] = tk.NORMAL
    button_2['state'] = tk.DISABLED
    for label in win.grid_slaves():
        if int(label.grid_info()["row"]) == 0 and int(label.grid_info()["column"]) == 2:
            label.grid_forget()

win = tk.Tk()
photo = tk.PhotoImage(file='icon.png')
win.iconphoto(False, photo)
win.title('Graph application')
win.config(bg='white')
win.geometry('1000x450+50+50')
win.resizable(False, False)

types_of_graphics = ['Rotating on circumference by a rational angle', 'Circumference filling', 'Unpassable baby', 'System Sink-Source']

combo_1 = ttk.Combobox(win, values=types_of_graphics)
combo_2 = ttk.Combobox(win, values=['Yes', 'No'])
button_1 = tk.Button(win, text='Draw', command=errorCheck)
button_2 = tk.Button(win, text='Clear Canvas', command=clearCanvas)
button_quit = tk.Button(win, text="Quit", command=win.destroy)
combo_1.grid(row=0, column=1, stick='we')
combo_2.grid(row=1, column=1, stick='we')
button_1.grid(row=2, column=1, stick='we')
button_2.grid(row=3, column=1, stick='we')
button_quit.grid(row=4, column=1, stick='we')
combo_1.current(0)
combo_2.current(0)
button_2['state'] = tk.DISABLED
tk.Label(win, text='Choose graph: ', bg='white', anchor='e').grid(row=0, column=0, stick='we')
tk.Label(win, text='One moving dot? ', bg='white', anchor='e').grid(row=1, column=0, stick='we')
win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=270)

win.mainloop()
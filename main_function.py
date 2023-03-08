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

def start_application(n):
    button_1['state'] = tk.DISABLED
    button_2['state'] = tk.NORMAL
    # figure and axes
    fig = Figure(figsize=(12, 4))
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
    k = 1
    def running_dot():
        nonlocal k
        kmod = k % 1000
        scat1 = ax1.scatter(x1[kmod], y1[kmod], color='black', marker='*')
        scat2 = ax2.scatter(x2[kmod], y2[kmod], z3[kmod], color='black', marker='*')
        canvas.draw()
        k += 25
        if combo_1.get() == 'Yes':
            scat1.remove()
            scat2.remove()
            if k >= 1000:
                k %= 1000
        if combo_1.get() == 'No':
            if k >= 1000:
                return 0
        if button_1['state'] == tk.NORMAL: return 0
        win.after(50, running_dot)
    # create FigureCanvasTkAgg object
    canvas = FigureCanvasTkAgg(fig, win)
    canvas.get_tk_widget().grid(row=0, column=2, rowspan=2000, stick='n')
    canvas.draw()
    running_dot()

def errorCheck():
    # Naturality check
    try:
        num = int(entry_1.get())
    except:
        num = -1
    if num <= 0 and isinstance(num, int):
        errorWin1 = tk.Tk()
        tk.Label(errorWin1, text='Natural Numbers contains only positive integers such as 1, 2, 3, 4, 5, 6, and so on.').pack()
        return 0
    # Yes or No check
    if combo_1.get() != 'Yes' and combo_1.get() != 'No':
        errorWin2 = tk.Tk()
        tk.Label(errorWin2, text='Choose "Yes" or "No"').pack()
        return 0
    start_application(num)
        
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
win.geometry('1350x450+50+50')
win.resizable(True, True)

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)

entry_1 = tk.Entry(win)
combo_1 = ttk.Combobox(win, values=['Yes', 'No'])
button_1 = tk.Button(win, text='Draw', command=errorCheck)
button_2 = tk.Button(win, text='Clear Canvas', command=clearCanvas)
button_quit = tk.Button(win, text="Quit", command=win.destroy)
entry_1.grid(row=0, column=1, stick='we')
combo_1.grid(row=1, column=1, stick='we')
button_1.grid(row=2, column=1, stick='we')
button_2.grid(row=3, column=1, stick='we')
button_quit.grid(row=4, column=1, stick='we')
combo_1.current(0)
button_2['state'] = tk.DISABLED
tk.Label(win, text='Enter natural number: ', bg='white', anchor='e').grid(row=0, column=0, stick='we')
tk.Label(win, text='One moving dot? ', bg='white', anchor='e').grid(row=1, column=0, stick='we')

win.mainloop()
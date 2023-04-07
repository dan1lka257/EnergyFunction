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
    dim = 10000
    fig = Figure(figsize=(12, 4))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    # fake round
    alpha = np.linspace(0, 2 * np.pi, dim)
    x0 = np.cos(alpha)
    y0 = np.sin(alpha)
    # 2d axes
    t = np.linspace(10, -10, 10000)
    beta = np.arctan(t)
    x1 = np.cos(beta)
    y1 = np.sin(beta)
    x2 = -np.cos(beta)
    # 3d axes
    z2 = np.linspace(0, 0, dim)
    z3 = np.sin(np.linspace(-np.pi, np.pi, dim) + np.pi / 2) + 1
    # print all of axes
    ax1.plot(x0, y0, color='gray')
    ax2.plot(x0, y0, z2, color='black', alpha=0.5)
    ax2.plot(x0, y0, z3, color='black')
    # move coordinate axes into center
    ax1.spines['bottom'].set_position(('data',0))
    ax1.spines['left'].set_position(('data',0))
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    # text marks on the axes
    ax1.set_xlabel('X', fontsize=14)
    ax1.set_ylabel('Y', fontsize=14)
    ax1.set_title('', fontweight = 'bold', fontsize=16)
    ax2.set_xlabel('X', fontsize=14)
    ax2.set_ylabel('Y', fontsize=14)
    ax2.set_zlabel('Z', fontsize=14)
    ax2.set_title('Lyapunov function', fontsize=16)
    ax1.axis('off')
    ax2.axis('off')
    # limiting 3d axes
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.set_zlim(0, max(z3))
    k = 1
    def running_dot():
        per = 100
        nonlocal k
        kmod = k % dim
        newkmod = (kmod + dim//per) % dim

        scat1 = ax1.scatter(x1[kmod], y1[kmod], color='black', marker='*')
        scat2 = ax2.scatter(x1[kmod], y1[kmod], z3[kmod], color='black', marker='*')
        scat3 = ax2.scatter(x1[kmod], y1[kmod], z2[kmod], color='black', marker='*')

        red_scat1 = ax1.scatter(x1[newkmod], y1[newkmod], color='red', marker='*')
        red_scat2 = ax2.scatter(x1[newkmod], y1[newkmod], z3[newkmod], color='red', marker='*')
        red_scat3 = ax2.scatter(x1[newkmod], y1[newkmod], z2[newkmod], color='red', marker='*')
        
        canvas.draw()

        red_scat1.remove()
        red_scat2.remove()
        red_scat3.remove()

        k += dim//per
        if combo_1.get() == 'No':
            scat1.remove()
            scat2.remove()
            scat3.remove()
            if k >= dim:
                k %= dim
        if combo_1.get() == 'Yes':
            if k >= dim:
                return 0
        if button_1['state'] == tk.NORMAL: return 0
        win.after(10, running_dot)
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
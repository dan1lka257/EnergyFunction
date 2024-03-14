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
    if combo_1.get() == types_of_graphics[4]:
        fifthFunctionStart()
    if combo_1.get() == types_of_graphics[5]:
        sixthFunctionStart()
    if combo_1.get() == types_of_graphics[6]:
        seventhFunctionStart()

def firstFunctionStart():
    # figure and axes
    dim = 10000
    per = 1000
    fig = Figure(figsize=(13, 6))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    # fake round
    alpha = np.linspace(0, 2 * np.pi, dim)
    x0 = np.cos(alpha)
    y0 = np.sin(alpha)
    # 2d axes
    t = 3/5 * 2 * np.pi * np.linspace(0, 200, dim)
    x1 = 1 * np.cos(t)
    y1 = 1 * np.sin(t)
    # 3d axes
    z2 = np.linspace(0, 0, dim)
    z3 = np.linspace(1/2, 1/2, dim)
    # print all of axes
    ax1.plot(x0, y0, color='gray', linewidth=1.5)
    ax2.plot(x0, y0, z2, color='black', alpha=0.5, linewidth=1.5)
    ax2.plot(x0, y0, z3, color='black', linewidth=1.5)
    # move coordinate axes into center
    ax1.spines['bottom'].set_position(('data',0))
    ax1.spines['left'].set_position(('data',0))
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    # text marks on the axes
    ax1.set_title('', fontweight = 'bold', fontsize=16)
    ax2.set_title('Lyapunov function', fontsize=16)
    ax1.axis('off')
    ax2.axis('on')
    ax2.grid(visible=0)
    tmp_planes = ax2.zaxis._PLANES 
    ax2.xaxis._PLANES = (tmp_planes[0], tmp_planes[1],
                             tmp_planes[1], tmp_planes[3],
                             tmp_planes[4], tmp_planes[5])
    ax2.yaxis._PLANES = (tmp_planes[1], tmp_planes[0],
                             tmp_planes[2], tmp_planes[3],
                             tmp_planes[4], tmp_planes[5])
    ax2.zaxis._PLANES = (tmp_planes[1], tmp_planes[0],
                             tmp_planes[2], tmp_planes[3],
                             tmp_planes[4], tmp_planes[5])
    view_2 = (25, 25)
    init_view = view_2
    ax2.view_init(*init_view)
    # limiting 3d axes
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.set_zlim(0, max(z3))
    k = 1
    def running_dot():
        nonlocal k
        kmod = k % dim
        newkmod = (kmod + dim//per) % dim

        scat1 = ax1.scatter(x1[kmod], y1[kmod], color='black', marker='o', s=10)
        scat2 = ax2.scatter(x1[kmod], y1[kmod], z3[kmod], color='black', marker='o', s=10)
        scat3 = ax2.scatter(x1[kmod], y1[kmod], z2[kmod], color='black', marker='o', s=10)

        red_scat1 = ax1.scatter(x1[newkmod], y1[newkmod], color='red', marker='o', s=30)
        red_scat2 = ax2.scatter(x1[newkmod], y1[newkmod], z3[newkmod], color='red', marker='o', s=30)
        red_scat3 = ax2.scatter(x1[newkmod], y1[newkmod], z2[newkmod], color='red', marker='o', s=30)
        
        canvas.draw()

        red_scat1.remove()
        red_scat2.remove()
        red_scat3.remove()

        k += dim//per
        if combo_2.get() == 'No':
            scat1.remove()
            scat2.remove()
            scat3.remove()
            if k >= dim:
                k %= dim
        if combo_2.get() == 'Yes':
            if k >= dim:
                return 0
        if button_1['state'] == tk.NORMAL: return 0
        win.after(10, running_dot)
    # create FigureCanvasTkAgg object
    canvas = FigureCanvasTkAgg(fig, win)
    canvas.get_tk_widget().grid(row=0, column=2, rowspan=2000, stick='n')
    canvas.draw()
    running_dot()

def secondFunctionStart():
    # figure and axes
    dim = 10000
    per = 3000
    fig = Figure(figsize=(13, 6))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    # fake round
    alpha = np.linspace(0, 2 * np.pi, dim)
    x0 = np.cos(alpha)
    y0 = np.sin(alpha)
    # 2d axes
    t = np.sqrt(2) * 2 * np.pi * np.linspace(0, 200, dim)
    x1 = 1 * np.cos(t)
    y1 = 1 * np.sin(t)
    # 3d axes
    z2 = np.linspace(0, 0, dim)
    z3 = np.linspace(1/2, 1/2, dim)
    # print all of axes
    ax1.plot(x0, y0, color='gray', linewidth=1.5)
    ax2.plot(x0, y0, z2, color='black', alpha=0.5, linewidth=1.5)
    ax2.plot(x0, y0, z3, color='black', linewidth=1.5)
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
    ax2.axis('on')
    # limiting 3d axes
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.set_zlim(0, max(z3))
    k = 1
    def running_dot():
        nonlocal k
        kmod = k % dim
        newkmod = (kmod + dim//per) % dim

        scat1 = ax1.scatter(x1[kmod], y1[kmod], color='black', marker='o', s=10)
        scat2 = ax2.scatter(x1[kmod], y1[kmod], z3[kmod], color='black', marker='o', s=10)
        scat3 = ax2.scatter(x1[kmod], y1[kmod], z2[kmod], color='black', marker='o', s=10)

        red_scat1 = ax1.scatter(x1[newkmod], y1[newkmod], color='red', marker='o', s=30)
        red_scat2 = ax2.scatter(x1[newkmod], y1[newkmod], z3[newkmod], color='red', marker='o', s=30)
        red_scat3 = ax2.scatter(x1[newkmod], y1[newkmod], z2[newkmod], color='red', marker='o', s=30)
        
        canvas.draw()

        red_scat1.remove()
        red_scat2.remove()
        red_scat3.remove()

        k += dim//per
        if combo_2.get() == 'No':
            scat1.remove()
            scat2.remove()
            scat3.remove()
            if k >= dim:
                k %= dim
        if combo_2.get() == 'Yes':
            if k >= dim:
                return 0
        if button_1['state'] == tk.NORMAL: return 0
        win.after(10, running_dot)
    # create FigureCanvasTkAgg object
    canvas = FigureCanvasTkAgg(fig, win)
    canvas.get_tk_widget().grid(row=0, column=2, rowspan=2000, stick='n')
    canvas.draw()
    running_dot()

def thirdFunctionStart():
    # figure and axes
    dim = 10000
    per = 100
    fig = Figure(figsize=(13, 6))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    # fake round
    alpha = np.linspace(0, 2 * np.pi, dim)
    x0 = np.cos(alpha)
    y0 = np.sin(alpha)
    # 2d axes
    t = np.linspace(-100, 100, dim)
    beta = np.pi - 2 * np.arctan(t / 2)
    x1 = np.sin(beta)
    y1 = np.cos(beta)
    # 3d axes
    z2 = np.linspace(0, 0, dim)
    z3 = np.linspace(1/2, 1/2, dim)
    # print all of axes
    ax1.plot(x0, y0, color='gray', linewidth=1.5)
    ax2.plot(x0, y0, z2, color='black', alpha=0.5, linewidth=1.5)
    ax2.plot(x0, y0, z3, color='black', linewidth=1.5)
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
    ax2.axis('on')
    # limiting 3d axes
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.set_zlim(0, max(z3))
    k = 1
    def running_dot():
        nonlocal k
        kmod = k % dim
        newkmod = (kmod + dim//per) % dim

        scat1 = ax1.scatter(x1[kmod], y1[kmod], color='black', marker='o', s=10)
        scat2 = ax2.scatter(x1[kmod], y1[kmod], z3[kmod], color='black', marker='o', s=10)
        scat3 = ax2.scatter(x1[kmod], y1[kmod], z2[kmod], color='black', marker='o', s=10)

        red_scat1 = ax1.scatter(x1[newkmod], y1[newkmod], color='red', marker='o', s=30)
        red_scat2 = ax2.scatter(x1[newkmod], y1[newkmod], z3[newkmod], color='red', marker='o', s=30)
        red_scat3 = ax2.scatter(x1[newkmod], y1[newkmod], z2[newkmod], color='red', marker='o', s=30)
        
        canvas.draw()

        red_scat1.remove()
        red_scat2.remove()
        red_scat3.remove()

        k += dim//per
        if combo_2.get() == 'No':
            scat1.remove()
            scat2.remove()
            scat3.remove()
            if k >= dim:
                k %= dim
        if combo_2.get() == 'Yes':
            if k >= dim:
                return 0
        if button_1['state'] == tk.NORMAL: return 0
        win.after(30, running_dot)
    # create FigureCanvasTkAgg object
    canvas = FigureCanvasTkAgg(fig, win)
    canvas.get_tk_widget().grid(row=0, column=2, rowspan=2000, stick='n')
    canvas.draw()
    running_dot()

def fourthFunctionStart():
    # figure and axes
    dim = 10000
    per = 100
    fig = Figure(figsize=(13, 6))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    # fake round
    alpha = np.linspace(0, 2 * np.pi, dim)
    x0 = np.sin(alpha)
    y0 = np.cos(alpha)
    # 2d axes
    t = np.linspace(10, -10, dim)
    beta = np.arctan(t)
    x1 = np.cos(beta)
    y1 = np.sin(beta)
    x2 = -np.cos(beta)
    # 3d axes
    z2 = np.linspace(0, 0, dim)
    z3 = np.sin(np.linspace(-np.pi, np.pi, dim) + 3/2*np.pi) + 1
    z4 = np.sin(beta) + 1
    z5 = np.sin(beta - 4 * np.pi) + 1
    # print all of axes
    ax1.plot(x0, y0, color='gray', linewidth=1.5)
    ax2.plot(x0, y0, z2, color='black', alpha=0.5, linewidth=1.5)
    ax2.plot(x0, y0, z3, color='black', linewidth=1.5)
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
    ax2.axis('on')
    # limiting 3d axes
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.set_zlim(0, max(z4))
    k = 1
    counter = 1
    def running_dot():
        nonlocal k, counter
        kmod = k % dim
        newkmod = (kmod + dim//per) % dim


        
        if counter % 2 == 1:
            scat1 = ax1.scatter(x1[kmod], y1[kmod], color='black', marker='o', s=10)
            scat2 = ax2.scatter(x1[kmod], y1[kmod], z4[kmod], color='black', marker='o', s=10)
            scat3 = ax2.scatter(x1[kmod], y1[kmod], z2[kmod], color='black', marker='o', s=10)
            red_scat1 = ax1.scatter(x1[newkmod], y1[newkmod], color='red', marker='o', s=30)
            red_scat2 = ax2.scatter(x1[newkmod], y1[newkmod], z4[newkmod], color='red', marker='o', s=30)
            red_scat3 = ax2.scatter(x1[newkmod], y1[newkmod], z2[newkmod], color='red', marker='o', s=30)
        else:
            scat1 = ax1.scatter(x2[kmod], y1[kmod], color='black', marker='o', s=10)
            scat2 = ax2.scatter(x2[kmod], y1[kmod], z5[kmod], color='black', marker='o', s=10)
            scat3 = ax2.scatter(x2[kmod], y1[kmod], z2[kmod], color='black', marker='o', s=10)
            red_scat1 = ax1.scatter(x2[newkmod], y1[newkmod], color='red', marker='o', s=30)
            red_scat2 = ax2.scatter(x2[newkmod], y1[newkmod], z5[newkmod], color='red', marker='o', s=30)
            red_scat3 = ax2.scatter(x2[newkmod], y1[newkmod], z2[newkmod], color='red', marker='o', s=30)


        canvas.draw()

        red_scat1.remove()
        red_scat2.remove()
        red_scat3.remove()

        k += dim//per
        if combo_2.get() == 'No':
            scat1.remove()
            scat2.remove()
            scat3.remove()
            if k >= dim:
                k %= dim
        if combo_2.get() == 'Yes':
            if k >= dim:
                return 0
        if button_1['state'] == tk.NORMAL: return 0
        counter += 1
        win.after(30, running_dot)
    # create FigureCanvasTkAgg object
    canvas = FigureCanvasTkAgg(fig, win)
    canvas.get_tk_widget().grid(row=0, column=2, rowspan=2000, stick='n')
    canvas.draw()
    running_dot()

def fifthFunctionStart():
    # figure and axes
    dim = 5000
    per = 100
    fig = Figure(figsize=(13, 6))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    # fake round
    alpha = np.linspace(0, 2 * np.pi, dim)
    x0 = np.sin(alpha)
    y0 = np.cos(alpha)
    # 2d axes
    t = np.linspace(10, -10, dim)
    beta = np.arctan(t)
    x1 = np.cos(beta)
    y1 = np.sin(beta)
    x2 = -np.cos(beta)
    # 3d axes
    z2 = np.linspace(0, 0, dim)
    z31 = (np.sin(np.linspace(np.pi, 0, dim//2) + 3/2*np.pi) + 1)/2
    z32 = ((np.sin(np.linspace(0, -np.pi, dim//2) + 3/2*np.pi) + 1)/2)**3
    z = np.hstack([z31, z32])
    z4 = (np.sin(beta + 2 * np.pi) + 1)/2
    z5 = ((np.sin(beta - 2 * np.pi) + 1)/2)**3
    # print all of axes
    ax1.plot(x0, y0, color='gray', linewidth=1.5)
    ax2.plot(x0, y0, z2, color='black', alpha=0.5, linewidth=1.5)
    ax2.plot(x0, y0, z, color='black', linewidth=1.5)
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
    ax2.axis('on')
    # limiting 3d axes
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.set_zlim(0, max(z4))
    k = 1
    def running_dot():
        nonlocal k
        kmod = k % dim
        newkmod = (kmod + dim//per) % dim

        scat1 = ax1.scatter(x1[kmod], y1[kmod], color='black', marker='o', s=10)
        scat2 = ax2.scatter(x1[kmod], y1[kmod], z4[kmod], color='black', marker='o', s=10)
        scat3 = ax2.scatter(x1[kmod], y1[kmod], z2[kmod], color='black', marker='o', s=10)
        scat4 = ax1.scatter(x2[kmod], y1[kmod], color='black', marker='o', s=10)
        scat5 = ax2.scatter(x2[kmod], y1[kmod], z5[kmod], color='black', marker='o', s=10)
        scat6 = ax2.scatter(x2[kmod], y1[kmod], z2[kmod], color='black', marker='o', s=10)
        red_scat1 = ax1.scatter(x1[newkmod], y1[newkmod], color='red', marker='o', s=30)
        red_scat2 = ax2.scatter(x1[newkmod], y1[newkmod], z4[newkmod], color='red', marker='o', s=30)
        red_scat3 = ax2.scatter(x1[newkmod], y1[newkmod], z2[newkmod], color='red', marker='o', s=30)
        red_scat4 = ax1.scatter(x2[newkmod], y1[newkmod], color='red', marker='o', s=30)
        red_scat5 = ax2.scatter(x2[newkmod], y1[newkmod], z5[newkmod], color='red', marker='o', s=30)
        red_scat6 = ax2.scatter(x2[newkmod], y1[newkmod], z2[newkmod], color='red', marker='o', s=30)

        canvas.draw()

        red_scat1.remove()
        red_scat2.remove()
        red_scat3.remove()
        red_scat4.remove()
        red_scat5.remove()
        red_scat6.remove()

        k += dim//per
        if combo_2.get() == 'No':
            scat1.remove()
            scat2.remove()
            scat3.remove()
            scat4.remove()
            scat5.remove()
            scat6.remove()
            if k >= dim:
                k %= dim
        if combo_2.get() == 'Yes':
            if k >= dim:
                return 0
        if button_1['state'] == tk.NORMAL: return 0
        win.after(30, running_dot)
    # create FigureCanvasTkAgg object
    canvas = FigureCanvasTkAgg(fig, win)
    canvas.get_tk_widget().grid(row=0, column=2, rowspan=2000, stick='n')
    canvas.draw()
    running_dot()

def sixthFunctionStart():
    # figure and axes
    dim = 10000
    per = 100
    fig = Figure(figsize=(13, 6))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    # fake round
    alpha = np.linspace(0, 2 * np.pi, dim)
    x0 = np.sin(alpha)
    y0 = np.cos(alpha)
    # 2d axes
    t = np.linspace(20, -20, dim)
    beta = np.arctan(t) / 4 + np.pi / 4
    x11 = np.cos(beta)
    y11 = np.sin(beta)
    x12 = -np.cos(beta)
    y12 = -np.sin(beta)
    x13 = np.cos(beta)
    y13 = -np.sin(beta)
    x14 = -np.cos(beta)
    y14 = np.sin(beta)
    # 3d axes
    z2 = np.linspace(0, 0, dim)
    z31 = (np.sin(np.linspace(-np.pi, 0, dim//4) + 3/2*np.pi) + 1)/2
    z32 = ((np.sin(np.linspace(0, np.pi, dim//4) + 3/2*np.pi) + 1)/2)**3
    z3 = np.hstack([z31, z32, z31, z32])
    z5 = (np.sin(beta * 2 + 3/2*np.pi) + 1)/2
    z4 = ((np.sin(beta * 2 + 3/2*np.pi) + 1)/2)**3
    # print all of axes
    ax1.plot(x0, y0, color='gray', linewidth=1.5)
    ax2.plot(x0, y0, z2, color='black', alpha=0.5, linewidth=1.5)
    ax2.plot(x0, y0, z3, color='black', linewidth=1.5)
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
    ax2.axis('on')
    # limiting 3d axes
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.set_zlim(0, max(z3))
    k = 1
    counter = 1
    def running_dot():
        nonlocal k, counter
        kmod = k % dim
        newkmod = (kmod + dim//per) % dim

        if counter % 2 == 1:
            scat1 = ax1.scatter(x11[kmod], y11[kmod], color='black', marker='o', s=10)
            scat2 = ax2.scatter(x11[kmod], y11[kmod], z5[kmod], color='black', marker='o', s=10)
            scat3 = ax2.scatter(x11[kmod], y11[kmod], z2[kmod], color='black', marker='o', s=10)
            red_scat1 = ax1.scatter(x11[newkmod], y11[newkmod], color='red', marker='o', s=30)
            red_scat2 = ax2.scatter(x11[newkmod], y11[newkmod], z5[newkmod], color='red', marker='o', s=30)
            red_scat3 = ax2.scatter(x11[newkmod], y11[newkmod], z2[newkmod], color='red', marker='o', s=30)
            scat4 = ax1.scatter(x13[kmod], y13[kmod], color='black', marker='o', s=10)
            scat5 = ax2.scatter(x13[kmod], y13[kmod], z4[kmod], color='black', marker='o', s=10)
            scat6 = ax2.scatter(x13[kmod], y13[kmod], z2[kmod], color='black', marker='o', s=10)
            red_scat4 = ax1.scatter(x13[newkmod], y13[newkmod], color='blue', marker='o', s=30)
            red_scat5 = ax2.scatter(x13[newkmod], y13[newkmod], z4[newkmod], color='blue', marker='o', s=30)
            red_scat6 = ax2.scatter(x13[newkmod], y13[newkmod], z2[newkmod], color='blue', marker='o', s=30)
        else:
            scat1 = ax1.scatter(x12[kmod], y12[kmod], color='black', marker='o', s=10)
            scat2 = ax2.scatter(x12[kmod], y12[kmod], z5[kmod], color='black', marker='o', s=10)
            scat3 = ax2.scatter(x12[kmod], y12[kmod], z2[kmod], color='black', marker='o', s=10)
            red_scat1 = ax1.scatter(x12[newkmod], y12[newkmod], color='red', marker='o', s=30)
            red_scat2 = ax2.scatter(x12[newkmod], y12[newkmod], z5[newkmod], color='red', marker='o', s=30)
            red_scat3 = ax2.scatter(x12[newkmod], y12[newkmod], z2[newkmod], color='red', marker='o', s=30)
            scat4 = ax1.scatter(x14[kmod], y14[kmod], color='black', marker='o', s=10)
            scat5 = ax2.scatter(x14[kmod], y14[kmod], z4[kmod], color='black', marker='o', s=10)
            scat6 = ax2.scatter(x14[kmod], y14[kmod], z2[kmod], color='black', marker='o', s=10)
            red_scat4 = ax1.scatter(x14[newkmod], y14[newkmod], color='blue', marker='o', s=30)
            red_scat5 = ax2.scatter(x14[newkmod], y14[newkmod], z4[newkmod], color='blue', marker='o', s=30)
            red_scat6 = ax2.scatter(x14[newkmod], y14[newkmod], z2[newkmod], color='blue', marker='o', s=30)

        canvas.draw()

        red_scat1.remove()
        red_scat2.remove()
        red_scat3.remove()
        red_scat4.remove()
        red_scat5.remove()
        red_scat6.remove()

        k += dim//per
        if combo_2.get() == 'No':
            scat1.remove()
            scat2.remove()
            scat3.remove()
            scat4.remove()
            scat5.remove()
            scat6.remove()
            if k >= dim:
                k %= dim
        if combo_2.get() == 'Yes':
            if k >= dim:
                return 0
        if button_1['state'] == tk.NORMAL: return 0
        counter += 1
        win.after(30, running_dot)
    # create FigureCanvasTkAgg object
    canvas = FigureCanvasTkAgg(fig, win)
    canvas.get_tk_widget().grid(row=0, column=2, rowspan=2000, stick='n')
    canvas.draw()
    running_dot()

def seventhFunctionStart():
    # figure and axes
    dim = 10000
    per = 100
    fig = Figure(figsize=(13, 6))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    # fake round
    alpha = np.linspace(0, 2 * np.pi, dim)
    x0 = np.sin(alpha)
    y0 = np.cos(alpha)
    # 2d axes
    t = np.linspace(-20, 20, dim)
    beta = np.arctan(t) / 8 + np.pi / 8
    x11 = np.cos(beta)
    y11 = np.sin(beta)
    x12 = -np.cos(beta)
    y12 = -np.sin(beta)
    x13 = np.cos(beta)
    y13 = -np.sin(beta)
    x14 = -np.cos(beta)
    y14 = np.sin(beta)
    x15 = np.sin(beta)
    y15 = np.cos(beta)
    x16 = -np.sin(beta)
    y16 = -np.cos(beta)
    x17 = np.sin(beta)
    y17 = -np.cos(beta)
    x18 = -np.sin(beta)
    y18 = np.cos(beta)
    # 3d axes
    z2 = np.linspace(0, 0, dim)
    z31 = (np.sin(np.linspace(-np.pi, 0, dim//8) + 3/2*np.pi) + 1)/2
    z32 = (np.sin(np.linspace(0, np.pi, dim//8) + 3/2*np.pi) + 1)/2
    z3 = np.hstack([z32, z31, z32, z31, z32, z31, z32, z31])
    z4 = (np.sin(beta * 4 + 3/2*np.pi) + 1)/2
    z5 = (np.sin(beta * 4 + 3/2*np.pi) + 1)/2
    # print all of axes
    ax1.plot(x0, y0, color='gray', linewidth=1.5)
    ax2.plot(x0, y0, z2, color='black', alpha=0.5, linewidth=1.5)
    ax2.plot(x0, y0, z3, color='black', linewidth=1.5)
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
    ax2.axis('on')
    # limiting 3d axes
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.set_zlim(0, max(z3))
    k = 1
    counter = 1
    def running_dot():
        nonlocal k, counter
        kmod = k % dim
        newkmod = (kmod + dim//per) % dim

        if counter % 2 == 1:
            scat1 = ax1.scatter(x11[kmod], y11[kmod], color='black', marker='o', s=10)
            scat2 = ax2.scatter(x11[kmod], y11[kmod], z5[kmod], color='black', marker='o', s=10)
            scat3 = ax2.scatter(x11[kmod], y11[kmod], z2[kmod], color='black', marker='o', s=10)
            red_scat1 = ax1.scatter(x11[newkmod], y11[newkmod], color='red', marker='o', s=30)
            red_scat2 = ax2.scatter(x11[newkmod], y11[newkmod], z5[newkmod], color='red', marker='o', s=30)
            red_scat3 = ax2.scatter(x11[newkmod], y11[newkmod], z2[newkmod], color='red', marker='o', s=30)
            scat4 = ax1.scatter(x13[kmod], y13[kmod], color='black', marker='o', s=10)
            scat5 = ax2.scatter(x13[kmod], y13[kmod], z4[kmod], color='black', marker='o', s=10)
            scat6 = ax2.scatter(x13[kmod], y13[kmod], z2[kmod], color='black', marker='o', s=10)
            red_scat4 = ax1.scatter(x13[newkmod], y13[newkmod], color='blue', marker='o', s=30)
            red_scat5 = ax2.scatter(x13[newkmod], y13[newkmod], z4[newkmod], color='blue', marker='o', s=30)
            red_scat6 = ax2.scatter(x13[newkmod], y13[newkmod], z2[newkmod], color='blue', marker='o', s=30)
           
        else:
            scat1 = ax1.scatter(x12[kmod], y12[kmod], color='black', marker='o', s=10)
            scat2 = ax2.scatter(x12[kmod], y12[kmod], z5[kmod], color='black', marker='o', s=10)
            scat3 = ax2.scatter(x12[kmod], y12[kmod], z2[kmod], color='black', marker='o', s=10)
            red_scat1 = ax1.scatter(x12[newkmod], y12[newkmod], color='red', marker='o', s=30)
            red_scat2 = ax2.scatter(x12[newkmod], y12[newkmod], z5[newkmod], color='red', marker='o', s=30)
            red_scat3 = ax2.scatter(x12[newkmod], y12[newkmod], z2[newkmod], color='red', marker='o', s=30)
            scat4 = ax1.scatter(x14[kmod], y14[kmod], color='black', marker='o', s=10)
            scat5 = ax2.scatter(x14[kmod], y14[kmod], z4[kmod], color='black', marker='o', s=10)
            scat6 = ax2.scatter(x14[kmod], y14[kmod], z2[kmod], color='black', marker='o', s=10)
            red_scat4 = ax1.scatter(x14[newkmod], y14[newkmod], color='blue', marker='o', s=30)
            red_scat5 = ax2.scatter(x14[newkmod], y14[newkmod], z4[newkmod], color='blue', marker='o', s=30)
            red_scat6 = ax2.scatter(x14[newkmod], y14[newkmod], z2[newkmod], color='blue', marker='o', s=30)
        
        scat7 = ax1.scatter(x15[kmod], y15[kmod], color='black', marker='o', s=10)
        scat8 = ax2.scatter(x15[kmod], y15[kmod], z5[kmod], color='black', marker='o', s=10)
        scat9 = ax2.scatter(x15[kmod], y15[kmod], z2[kmod], color='black', marker='o', s=10)
        red_scat7 = ax1.scatter(x15[newkmod], y15[newkmod], color='yellow', marker='o', s=30)
        red_scat8 = ax2.scatter(x15[newkmod], y15[newkmod], z5[newkmod], color='yellow', marker='o', s=30)
        red_scat9 = ax2.scatter(x15[newkmod], y15[newkmod], z2[newkmod], color='yellow', marker='o', s=30)
        scat10 = ax1.scatter(x17[kmod], y17[kmod], color='black', marker='o', s=10)
        scat11 = ax2.scatter(x17[kmod], y17[kmod], z4[kmod], color='black', marker='o', s=10)
        scat12 = ax2.scatter(x17[kmod], y17[kmod], z2[kmod], color='black', marker='o', s=10)
        red_scat10 = ax1.scatter(x17[newkmod], y17[newkmod], color='green', marker='o', s=30)
        red_scat11 = ax2.scatter(x17[newkmod], y17[newkmod], z4[newkmod], color='green', marker='o', s=30)
        red_scat12 = ax2.scatter(x17[newkmod], y17[newkmod], z2[newkmod], color='green', marker='o', s=30)
        scat13 = ax1.scatter(x16[kmod], y16[kmod], color='black', marker='o', s=10)
        scat14 = ax2.scatter(x16[kmod], y16[kmod], z5[kmod], color='black', marker='o', s=10)
        scat15 = ax2.scatter(x16[kmod], y16[kmod], z2[kmod], color='black', marker='o', s=10)
        red_scat13 = ax1.scatter(x16[newkmod], y16[newkmod], color='purple', marker='o', s=30)
        red_scat14 = ax2.scatter(x16[newkmod], y16[newkmod], z5[newkmod], color='purple', marker='o', s=30)
        red_scat15 = ax2.scatter(x16[newkmod], y16[newkmod], z2[newkmod], color='purple', marker='o', s=30)
        scat16 = ax1.scatter(x18[kmod], y18[kmod], color='black', marker='o', s=10)
        scat17 = ax2.scatter(x18[kmod], y18[kmod], z4[kmod], color='black', marker='o', s=10)
        scat18 = ax2.scatter(x18[kmod], y18[kmod], z2[kmod], color='black', marker='o', s=10)
        red_scat16 = ax1.scatter(x18[newkmod], y18[newkmod], color='orange', marker='o', s=30)
        red_scat17 = ax2.scatter(x18[newkmod], y18[newkmod], z4[newkmod], color='orange', marker='o', s=30)
        red_scat18 = ax2.scatter(x18[newkmod], y18[newkmod], z2[newkmod], color='orange', marker='o', s=30)

        k += dim//per
        if combo_2.get() == 'No':
            scat1.remove()
            scat2.remove()
            scat3.remove()
            scat4.remove()
            scat5.remove()
            scat6.remove()
            scat7.remove()
            scat8.remove()
            scat9.remove()
            scat10.remove()
            scat11.remove()
            scat12.remove()
            scat13.remove()
            scat14.remove()
            scat15.remove()
            scat16.remove()
            scat17.remove()
            scat18.remove()
            if k >= dim:
                k %= dim
        if combo_2.get() == 'Yes':
            if k >= dim:
                return 0
        
        canvas.draw()

        red_scat1.remove()
        red_scat2.remove()
        red_scat3.remove()
        red_scat4.remove()
        red_scat5.remove()
        red_scat6.remove()
        red_scat7.remove()
        red_scat8.remove()
        red_scat9.remove()
        red_scat10.remove()
        red_scat11.remove()
        red_scat12.remove()
        red_scat13.remove()
        red_scat14.remove()
        red_scat15.remove()
        red_scat16.remove()
        red_scat17.remove()
        red_scat18.remove()
        if button_1['state'] == tk.NORMAL: return 0
        counter += 1
        win.after(30, running_dot)
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
win.geometry('1600x850+0+0')
win.resizable(False, False)

types_of_graphics = ['Rotating on circumference by a rational angle', 'Circumference filling', 'Unpassable baby', 'System Sink-Source', '5', '6', '7']

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
tk.Label(win, text='Save last position? ', bg='white', anchor='e').grid(row=1, column=0, stick='we')
win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=270)

win.mainloop()
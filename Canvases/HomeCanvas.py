import tkinter
import pandas as pd
import numpy as np
from tkinter import filedialog
import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

def createHome(parent):
    #functions
    def Load_db_csv(event):
        global Data_base_csv
        parent.filename = filedialog.askopenfilename(initialdir = "/",
                                                     title = "Select file",
                                                     filetypes = (("CSV files","*.csv"),
                                                     ("all files","*.*")))
        Data_base_csv = pd.read_csv(parent.filename)

    def Load_threshold_csv(event):
        global Treshold_csv
        parent.filename = filedialog.askopenfilename(initialdir = "/",
                                                     title = "Select file",
                                                     filetypes = (("CSV files","*.csv"),
                                                     ("all files","*.*")))
        Treshold_csv = pd.read_csv(parent.filename)

    #colors
    canvas_bg_color="#fec5e5"
    button_bg_color="#3258EF"
    #variables that needs declaration
    weeks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]
    Data_base_csv=''
    Treshold_csv=''

    print(Data_base_csv)
    print(Treshold_csv)
    #creating the canvas
    home = tk.Canvas(parent,
                     width=1050,
                     height=800,
                     bg=canvas_bg_color,
                     highlightthickness=0,
                     relief='flat')
    home.pack(side="right", fill=tk.BOTH, expand=1)
    #adding the title lable
    Title = tk.Label(home,
                 text="Data Presentation :",
                 width=15,
                 height=2,
                 bg=canvas_bg_color,
                 fg='black',
                 highlightthickness=0,
                 relief='flat',
                 font=("Helvetica", 12))
    Title.place(x = 20, y = 10)

    Load_db = tk.Button(home,
                 text="Load Data",
                 width=15,
                 height=2,
                 bg=button_bg_color,
                 fg='white',
                 highlightthickness=0,
                 relief='flat',
                 font=("Helvetica", 12))
    Load_db.place(relx=0.4, y = 70, anchor=tk.CENTER)
    Load_db.bind('<ButtonRelease-1>', Load_db_csv)

    Load_threshold = tk.Button(home,
                 text="Load Threshold",
                 width=15,
                 height=2,
                 bg=button_bg_color,
                 fg='white',
                 highlightthickness=0,
                 relief='flat',
                 font=("Helvetica", 12))
    Load_threshold.place(relx=0.6, y = 70, anchor=tk.CENTER)
    Load_threshold.bind('<ButtonRelease-1>', Load_threshold_csv)

    np.random.seed(19680801)
    y_pos = np.arange(len(weeks))
    performance = 3 + 10 * np.random.rand(len(weeks))
    error = np.random.rand(len(weeks))

    fig = Figure()
    fig.add_subplot().bar(y_pos, performance, xerr=error, align='center')
    fig.add_subplot().set_xticks(y_pos)
    fig.add_subplot().set_xticklabels(weeks)
    fig.add_subplot().set_title('How fast do you want to go today?')
    fig.patch.set_facecolor('#fec5e5')
    fig.add_subplot().set_facecolor('#fec5e5')
    fig.tight_layout()

    plot = FigureCanvasTkAgg(fig, master=home)  # A tk.DrawingArea.
    plot.draw()
    plot.get_tk_widget().place(relx=0.005, rely=0.15, relwidth=0.990, relheight=0.7)
    return home
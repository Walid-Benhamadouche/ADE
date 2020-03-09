from tkinter import filedialog
import tkinter as tk
def createHome(parent):
    #colors
    canvas_bg_color="#0C3851"
    button_bg_color="#3258EF"
    #variables that needs declaration
    parent.filename=''
    #functions
    def OpenFile(event):
        parent.filename = filedialog.askopenfilename(initialdir = "/",
                                                     title = "Select file",
                                                     filetypes = (("CSV files","*.csv"),
                                                     ("all files","*.*")))

    def test(event):
        event.widget.configure(Load_db.pack_forget())

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
                 fg='white',
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
    Load_db.pack(side="top")
    Load_db.bind('<ButtonRelease-1>', OpenFile)

    Load_threshold = tk.Button(home,
                 text="Load Threshold",
                 width=15,
                 height=2,
                 bg=button_bg_color,
                 fg='white',
                 highlightthickness=0,
                 relief='flat',
                 font=("Helvetica", 12))
    Load_threshold.place(x = 670, y = 50)
    Load_threshold.bind('<ButtonRelease-1>', test)
    return home
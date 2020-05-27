import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import *
import Canvases.HomeCanvas as hc
import Canvases.OutlierCanvas as oc
import Canvases.AnalyseCanvas as ac
import Canvases.IncubationCanvas as ic
import Canvases.ClassificationCanvas as cc

#colors
menu_color="#3258EF"
in_use='Data Presentation'

#main window
root = tk.Tk()
root.configure(background="#fff")
root.geometry("1280x720")
button_identities = []

#hover event functions
def on_enter(event):
    event.widget.configure(bg='red')
def on_leave(event):
    event.widget.configure(bg=menu_color)

#on click event
def go_next(event):
    global outliers_canvas
    global in_use
    data_pre_canvas.pack_forget()
    in_use = 'Analysing Data'
    outliers_canvas = oc.createOutlier(root, hc.values_per_week, hc.Threshold_percent, hc.percentages)
    outliers_canvas.pack(side="right", fill=BOTH, expand=1)
    button_identities[1]['state'] = tk.NORMAL
    def go_incubation(event):
        global incubation_canvas
        global in_use
        outliers_canvas.pack_forget()
        in_use = 'Incubation Periode'
        incubation_canvas = ic.createIncubation(root, hc.values_per_day, hc.incubation_min, hc.incubation_max, hc.values_per_week, hc.Threshold_percent, hc.percentages)
        incubation_canvas.pack(side="right", fill=BOTH, expand=1)
        button_identities[2]['state'] = tk.NORMAL
        def go_analyse(event):
            global analyse_canvas
            global in_use
            incubation_canvas.pack_forget()
            in_use = 'Analysing Data'
            analyse_canvas = ac.createAnalyse(root, hc.values_per_week, hc.Threshold_percent, hc.percentages, oc.anomalies)
            analyse_canvas.pack(side="right", fill=BOTH, expand=1)
            button_identities[3]['state'] = tk.NORMAL
            def go_classification(event):
                global classification_vancas
                global in_use
                analyse_canvas.pack_forget()
                in_use = 'Classification'
                classification_vancas = cc.createOutlier(root, hc.Sexe, hc.Age, hc.Secteur, hc.Quartier, hc.Commune)
                classification_vancas.pack(side="right", fill=BOTH, expand=1)
                button_identities[4]['state'] = tk.NORMAL
            next_analyse = tk.Button(analyse_canvas,
                    text="Next Step",
                    width=15,
                    height=2,
                    bg=menu_color,
                    fg='white',
                    highlightthickness=0,
                    relief='flat',
                    font=("Helvetica", 12))
            next_analyse.place(relx=0.85, rely=0.9)
            next_analyse.bind('<ButtonRelease-1>', go_classification)

        next_home = tk.Button(incubation_canvas,
                    text="Next Step",
                    width=15,
                    height=2,
                    bg=menu_color,
                    fg='white',
                    highlightthickness=0,
                    relief='flat',
                    font=("Helvetica", 12))
        next_home.place(relx=0.85, rely=0.9)
        next_home.bind('<ButtonRelease-1>', go_analyse)
    next_incubation = tk.Button(outliers_canvas,
                    text="Next Step",
                    width=15,
                    height=2,
                    bg=menu_color,
                    fg='white',
                    highlightthickness=0,
                    relief='flat',
                    font=("Helvetica", 12))
    next_incubation.place(relx=0.85, rely=0.9)
    next_incubation.bind('<ButtonRelease-1>', go_incubation)
def switch_canvas(button):
    global in_use
    print(in_use)
    switcher = {
        'Data Presentation': lambda : root.configure(data_pre_canvas.pack_forget()),
        'Outliers Detection': lambda : root.configure(outliers_canvas.pack_forget()),
        'Incubation Periode': lambda : root.configure(incubation_canvas.pack_forget()),
        'Analysing Data': lambda : root.configure(analyse_canvas.pack_forget()),
        'Classification': lambda : root.configure(classification_vancas.pack_forget())
    }
    switcher.get(in_use, lambda : "ERROR: somthing is wrong !")()

    switcher = {
        'Data Presentation': lambda : root.configure(data_pre_canvas.pack(side="right", fill=BOTH, expand=1)),
        'Outliers Detection': lambda : root.configure(outliers_canvas.pack(side="right", fill=BOTH, expand=1)),
        'Incubation Periode': lambda : root.configure(incubation_canvas.pack(side="right", fill=BOTH, expand=1)),
        'Analysing Data': lambda : root.configure(analyse_canvas.pack(side="right", fill=BOTH, expand=1)),
        'Classification': lambda : root.configure(classification_vancas.pack(side="right", fill=BOTH, expand=1))
    }
    switcher.get(button['text'], lambda : "ERROR: somthing is wrong !")()
    in_use=button['text']

#side menu area
SideMenu = tk.Canvas(root,
                     width=250,
                     height=720,
                     bg=menu_color,
                     highlightthickness=0,
                     relief='flat')
SideMenu.pack(side="left", fill=Y)

#main window canvas
in_use='Data Presentation'
data_pre_canvas = hc.createHome(root)
print(hc.values_per_week)

next_home = tk.Button(data_pre_canvas,
                 text="Next Step",
                 width=15,
                 height=2,
                 bg=menu_color,
                 fg='white',
                 highlightthickness=0,
                 relief='flat',
                 font=("Helvetica", 12))
next_home.place(relx=0.85, rely=0.9)
next_home.bind('<ButtonRelease-1>', go_next)

#side menu items

Labels=["Data Presentation", "Outliers Detection", "Exposer Periode", "Analysing Data", "Classification"]

for i in range(5):
    side_label = tk.Button(SideMenu,
                    text=Labels[i],
                    width=30,
                    height=5,
                    bg=menu_color,
                    fg='white',
                    highlightthickness=0,
                    relief='flat',
                    font=("Helvetica", 16))
    side_label.configure(command=lambda b=side_label: switch_canvas(b))
    side_label.place(x = 1, y = 70 + (i+1)*70, width=250, height=60)
    side_label.bind("<Enter>", on_enter)
    side_label.bind("<Leave>", on_leave)
    # add the button's identity to a list:
    button_identities.append(side_label)

for i in range(1,5):
    button_identities[i]['state'] = tk.DISABLED

root.mainloop()
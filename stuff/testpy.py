def switch_to_outliers(event):
    global in_use
    switcher = {
        'home': lambda : event.widget.configure(home_canvas.pack_forget()),
        'outliers': lambda : event.widget.configure(outliers_canvas.pack_forget()),
        'analyse': lambda : event.widget.configure(analyse_canvas.pack_forget())
    }
    switcher.get(in_use, lambda : "ERROR: somthing is wrong !")()
    event.widget.configure(outliers_canvas.pack(side="right", fill=BOTH, expand=1))
    in_use='outliers'

def switch_to_analyse(event):
    global in_use
    switcher = {
        'home': lambda : event.widget.configure(home_canvas.pack_forget()),
        'outliers': lambda : event.widget.configure(outliers_canvas.pack_forget()),
        'analyse': lambda : event.widget.configure(analyse_canvas.pack_forget())
    }
    switcher.get(in_use, lambda : "ERROR: somthing is wrong !")()
    event.widget.configure(analyse_canvas.pack(side="right", fill=BOTH, expand=1))
    in_use='analyse'

    #Outliers = tk.Label(SideMenu,
#                  text="Outliers Detection",
#                  width=30,
#                  height=5,
#                  bg=menu_color,
#                  fg='white',
#                  highlightthickness=0,
#                  relief='flat',
#                  font=("Helvetica", 16))
#Outliers.place(x = 1, y = 70 + 2*70, width=250, height=60)
#Outliers.bind("<Enter>", smf.on_enter)
#Outliers.bind("<Leave>", smf.on_leave)
#Outliers.bind('<Button-1>', switch_to_outliers)

#Analyse = tk.Label(SideMenu,
#                  text="Incubation Periode",
#                  width=30,
#                  height=5,
#                  bg=menu_color,
#                  fg='white',
#                  highlightthickness=0,
#                  relief='flat',
#                  font=("Helvetica", 16))
#Analyse.place(x = 1, y = 70 + 3*70, width=250, height=60)
#Analyse.bind("<Enter>", smf.on_enter)
#Analyse.bind("<Leave>", smf.on_leave)
#Analyse.bind('<Button-1>', switch_to_analyse)

#label3 = tk.Label(SideMenu,
#                  text="Analysing Data",
#                  width=30,
#                  height=5,
#                  bg=menu_color,
#                  fg='white',
#                  highlightthickness=0,
#                  relief='flat',
#                  font=("Helvetica", 16))
#label3.place(x = 1, y = 70 + 4*70, width=250, height=60)
#label3.bind("<Enter>", smf.on_enter)
#label3.bind("<Leave>", smf.on_leave)
#label3.bind('<Button-1>', switchC)

#label4 = tk.Label(SideMenu,
#                  text="Classification",
#                  width=30,
#                  height=5,
#                  bg=menu_color,
#                  fg='white',
#                  highlightthickness=0,
#                  relief='flat',
#                  font=("Helvetica", 16))
#label4.place(x = 1, y = 70 + 5*70, width=250, height=60)
#label4.bind("<Enter>", smf.on_enter)
#label4.bind("<Leave>", smf.on_leave)
#label4.bind('<Button-1>', switchC)
import tkinter
import pandas as pd
import numpy as np
import collections
from tkinter import filedialog
import tkinter as tk
from calendar import monthrange

from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.ticker as mtick
#import Canvases.AnalyseCanvas as ac

dates = []
Sexe = []
Age = []
Secteur = []
Quartier = []
Commune = []
values_per_week = []
values_per_day = []
Threshold_percent = []
percentages = []
incubation_min=''
incubation_max=''
analyse_canvas=''
fig=''
def createHome(parent):
    #functions
    global fig
    def Load_db_csv(values_per_week, Threshold_percent, percentages, plot, fig):
        global Sexe
        global Age
        global Secteur
        global Quartier
        global Commune
        global Data_base_csv
        global values_per_day
        global incubation_min
        global incubation_max
        global dates
        parent.filename = filedialog.askopenfilename(initialdir = "/",
                                                     title = "Select file",
                                                     filetypes = (("CSV files","*.csv"),
                                                     ("all files","*.*")))
        dateparse = lambda x: pd.datetime.strptime(x, '%d/%m/%Y')
        Data_base_csv = pd.read_csv(parent.filename,parse_dates=['date_DCL'],date_parser=dateparse)
        dates = Data_base_csv.groupby(['date_DCL']).size()
        Sexe = pd.read_csv(parent.filename,usecols = ["sexe"])
        Age = pd.read_csv(parent.filename,usecols = ["age"])
        Secteur = pd.read_csv(parent.filename,usecols = ["nom_secteur"])
        Quartier = pd.read_csv(parent.filename,usecols = ["nom_quartier"])
        Commune = pd.read_csv(parent.filename,usecols = ["nom_commune"])
        Threshold = pd.read_csv(parent.filename,usecols = ["threshold"])
        incubation_min = pd.read_csv(parent.filename,usecols = ["incubation_min"])
        incubation_max = pd.read_csv(parent.filename,usecols = ["incubation_max"])
        Threshold = Threshold.iloc[0].values.tolist()
        Threshold = Threshold[0].split("/",1)
        number_of_cases = Threshold[0]
        per_person = Threshold[1]
        print(number_of_cases)
        print(per_person)
        Threshold_percent.append((int(Threshold[0])/int(Threshold[1]))*100)
        year = dates.keys()[0].year
        values_per_day = dates
        idx = pd.date_range('01-01-' + str(year), '12-31-' + str(year))
        dates = dates.reindex(idx, fill_value=0)

        day = 1
        counter = 0
        for index, value in dates.items():
            if day == 7:
                day = 0
                values_per_week.append(counter)
                counter = 0
            counter+=value
            day+=1
        values_per_week.append(counter)

        for x in values_per_week:
            temp = (x/5000)*100
            percentages.append(temp)
        # reploting
        x = np.linspace(1, len(values_per_week), len(values_per_week))

        fig = Figure()
        fig.patch.set_facecolor('#f5f5f5')
        
        #thresholdlist = [Threshold.iloc[0].values for i in range(53)]
        #print(thresholdlist)

        figu = fig.add_subplot()
        #figu.stem(x,percentages, 'b', use_line_collection=True, markerfmt='bo', label='data')
        figu.bar(x, percentages)
        #to display as %
        figu.yaxis.set_major_formatter(mtick.PercentFormatter(1))
        figu.set_title('number of cases per week')
        figu.set_facecolor('#f5f5f5')
        figu.plot(x, [Threshold_percent for i in range(53)], label='threshold')

        legend_elements = [Line2D([0], [0], color='#1f77b4', lw=2, label='threshold'),
                           Patch(facecolor='#1f77b4', edgecolor='#1f77b4',
                                    label='Cases')]
        figu.legend(handles=legend_elements)

        plot.get_tk_widget().forget()
        plot = FigureCanvasTkAgg(fig, master=home)
        plot.draw()
        plot.get_tk_widget().place(relx=0.005, rely=0.15, relwidth=0.990, relheight=0.7)
        global analyse_canvas
        #analyse_canvas = ac.createAnalyse(parent, values_per_week, Threshold_percent, percentages)

    #colors
    canvas_bg_color="#f5f5f5"
    button_bg_color="#30e3ca"
    #variables that needs declaration
    global values_per_week
    global Threshold_percent
    global percentages
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

    #adding plot
    fig = Figure()
    fig.patch.set_facecolor('#f5f5f5')

    figu = fig.add_subplot()
    figu.bar([0], [0])
    figu.set_title('number of cases per week')
    figu.set_facecolor('#f5f5f5')

    plot = FigureCanvasTkAgg(fig, master=home)  # A tk.DrawingArea.
    plot.draw()
    plot.get_tk_widget().place(relx=0.005, rely=0.15, relwidth=0.990, relheight=0.7)

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
                 fg='#000000',
                 highlightthickness=0,
                 relief='flat',
                 font=("Helvetica", 12))
    Load_db.place(relx=0.5, y = 70, anchor=tk.CENTER)
    Load_db.configure(command=lambda b=values_per_week, c=Threshold_percent, d=percentages,f=fig, plot=plot: Load_db_csv(b, c, d, plot, f))
    return home
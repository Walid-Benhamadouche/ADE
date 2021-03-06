import tkinter as tk
import numpy as np

from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.ticker as mtick

anomalies=[]
def createOutlier(parent, data, Threshold_percent, percentages):
     
    def find_anomalies(data):
        anomalies = []
        random_data_std = np.std(data)
        random_data_mean = np.mean(data)
        anomaly_cut_off = random_data_std * 3

        lower_limit = 0
        upper_limit = random_data_mean + anomaly_cut_off

        index = 0
        for idx,outlier in enumerate(data):
            if outlier > upper_limit or outlier < lower_limit:
                anomalies.append(idx)
            index +=1
        return anomalies
    
    def Affiche (data, figu,plot,fig):
        global anomalies
        anomalies = find_anomalies(data)
        for elemnt in anomalies:
            figu.get_children()[elemnt].set_color('r')

        legend_elements = [Line2D([0], [0], color='#1f77b4', lw=2, label='threshold'),
                           Patch(facecolor='#1f77b4', edgecolor='#1f77b4',label='Cases'),
                           Patch(facecolor='r', edgecolor='r',label='Outliers')]
        figu.legend(handles=legend_elements)

        plot.get_tk_widget().forget()
        plot = FigureCanvasTkAgg(fig, master=outlier)
        plot.draw()
        plot.get_tk_widget().place(relx=0.005, rely=0.15, relwidth=0.990, relheight=0.7)    
    
    #button_bg_color="#3258EF"
    canvas_bg_color='#f5f5f5'
    #button_bg_color="#3258EF"
    outlier = tk.Canvas(parent,
              width=1050,
              height=800,
              bg=canvas_bg_color,
              highlightthickness=0,
              relief='flat')

    x = np.linspace(1, len(data), len(data))
    fig = Figure()
    fig.patch.set_facecolor('#f5f5f5')
     
    figu = fig.add_subplot()
    figu.bar(x, percentages)

    figu.yaxis.set_major_formatter(mtick.PercentFormatter(1))
    figu.set_title('number of cases per week')
    figu.set_facecolor('#f5f5f5')
    figu.plot(x, [Threshold_percent for i in range(53)], label='threshold')
    
    legend_elements = [Line2D([0], [0], color='#1f77b4', lw=2, label='threshold'),
                           Patch(facecolor='#1f77b4', edgecolor='#1f77b4',
                                    label='Cases')]
    figu.legend(handles=legend_elements)

    plot = FigureCanvasTkAgg(fig, master=outlier)
    plot.draw()
    plot.get_tk_widget().place(relx=0.005, rely=0.15, relwidth=0.990, relheight=0.7)

    Title = tk.Label(outlier,
                 text="OUtliers :",
                 width=15,
                 height=2,
                 bg=canvas_bg_color,
                 fg='black',
                 highlightthickness=0,
                 relief='flat',
                 font=("Helvetica", 12))
    Title.place(x = 20, y = 10)
    
    Load_db = tk.Button(outlier,
                 text="Outlier",
                 width=15,
                 height=2,
                 bg='#30e3ca',
                 fg='white',
                 highlightthickness=0,
                 relief='flat',
                 font=("Helvetica", 12))
    Load_db.place(relx=0.5, y = 70, anchor=tk.CENTER)
    Load_db.configure(command=lambda b=data, f=figu, p=plot, fi=fig: Affiche(b, f, p, fi))          
    return outlier
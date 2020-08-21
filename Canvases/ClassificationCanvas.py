import tkinter as tk
import pandas as pd
import numpy as np
import collections
from tkinter import filedialog
import tkinter as tk
from calendar import monthrange
import shapefile as shp
import os

from matplotlib.font_manager import FontProperties
from matplotlib.patches import Patch
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

def createOutlier(parent, Sexe, Age, Secteur, Quartier, Commune):
    colors1 = ['#FFB873', '#015367', '#206676', '#04819E', '#38B2CE', '#60B9CE', '#e6e6e6']
    colors = ['#e6e6e6', '#60B9CE', '#38B2CE', '#04819E', '#206676', '#015367', '#FFB873', '#FF9F40', '#FF7F00', '#BF7730', '#A65200']
    in_use = 'Sexe'
    canvas_bg_color="#f5f5f5"
    #button_bg_color="#3258EF"
    outlier = tk.Canvas(parent,
              width=1050,
              height=800,
              bg=canvas_bg_color,
              highlightthickness=0,
              relief='flat')

    # Age
    age_label = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '60+']
    age_count = [0, 0, 0, 0, 0, 0, 0]
    age_len = len(Age.index)

    for i in range(age_len):
        if(float(Age.iloc[i]['age']) >= 0 and float(Age.iloc[i]['age']) <= 10):
            age_count[0] = age_count[0] + 1
        if(float(Age.iloc[i]['age']) >= 11 and float(Age.iloc[i]['age']) <= 20):
            age_count[1] = age_count[1] + 1
        if(float(Age.iloc[i]['age']) >= 21 and float(Age.iloc[i]['age']) <= 30):
            age_count[2] = age_count[2] + 1
        if(float(Age.iloc[i]['age']) >= 31 and float(Age.iloc[i]['age']) <= 40):
            age_count[3] = age_count[3] + 1
        if(float(Age.iloc[i]['age']) >= 41 and float(Age.iloc[i]['age']) <= 50):
            age_count[4] = age_count[4] + 1
        if(float(Age.iloc[i]['age']) >= 51 and float(Age.iloc[i]['age']) <= 60):
            age_count[5] = age_count[5] + 1
        if(float(Age.iloc[i]['age']) >= 61):
            age_count[6] = age_count[6] + 1
    # Secteur

    fig_age = Figure()
    fig_age.patch.set_facecolor('#f5f5f5')

    figu_age = fig_age.add_subplot()
    figu_age.pie(age_count, colors=colors1, shadow=True, startangle=90)
    figu_age.axis('equal')
    age_sum = np.sum(age_count)
    age_percents = []
    i = 0
    for age in age_count:
        temp = (age/age_sum)*100
        temp = round(temp, 2)
        age_percents.append("Age intervale : "+age_label[i]+" percentage : "+str(temp)+"%")
        i = i+1
    
    patches = [Patch(facecolor=colors1[0]),
                Patch(facecolor=colors1[1]),
                Patch(facecolor=colors1[2]),
                Patch(facecolor=colors1[3]),
                Patch(facecolor=colors1[4]),
                Patch(facecolor=colors1[5]),
                Patch(facecolor=colors1[6])]

    figu_age.legend(patches, age_percents, loc='upper left', bbox_to_anchor=(-0.1, 1.),
           fontsize=9)

    # Commune
    wedges=[]

    Commune_name = ["ain bia", 'ain kerma', 'ain turck', 'arzew', 'ben freha', 'bethioua', 'bir el djir', 'boufatis', 'bousfer', 'boutlelis',
     'el ancor', 'el braia', 'el kerma', 'es senia', 'gdyel', 'hassi benokba', 'hassi bounif', 'hassi mefsoukh', 'mers el hadjaj', 'mers el kbir',
     'misserghin', 'oran', 'oued tlelat', 'sidi ben yabka', 'sidi chami', 'tafraoui']
    #
    Commune = Commune.groupby('nom_commune').size()
    Commune = Commune.reindex(Commune_name, fill_value=0)
    Commune_labels = Commune.groupby('nom_commune').groups

    fig_commune = Figure()
    fig_commune.patch.set_facecolor(canvas_bg_color)

    script_dir = os.path.dirname(__file__)
    rel_path = "gadm36_DZA_shp/gadm36_DZA_2.shp"
    abs_file_path = os.path.join(script_dir, rel_path)
    sf = shp.Reader(abs_file_path) 
    figu_commune = fig_commune.add_subplot()
    figu_commune.set_facecolor(canvas_bg_color)
    
    Commune_sum = np.sum(Commune.values)
    commune_percenteges = []
    color_id = 0
    commune_id = 0

    for number in range(948,973):

        x=[i[0] for i in sf.shapeRecords()[number].shape.points[:]]
        y=[i[1] for i in sf.shapeRecords()[number].shape.points[:]]

        temp = (Commune.get(Commune_name[commune_id])/Commune_sum)*100

        if(temp == 0):
            color_id = 0
        elif(temp > 0 and temp < 10):
            color_id = 1
        elif(temp >= 10 and temp < 20):
            color_id = 2
        elif(temp >=20 and temp < 30):
            color_id = 3
        elif(temp >=30 and temp < 40):
            color_id = 4
        elif(temp >=40 and temp < 50):
            color_id = 5
        elif(temp >=50 and temp < 60):
            color_id = 6
        elif(temp >=60 and temp < 70):
            color_id = 7
        elif(temp >=70 and temp < 80):
            color_id = 8
        elif(temp >=80 and temp < 90):
            color_id = 9
        elif(temp >=90):
            color_id = 10
        temp = round(temp, 2)
        commune_percenteges.append(temp)
        wedges.append(figu_commune.fill(x, y, facecolor=colors[color_id]))
        commune_id = commune_id + 1
    
    legend_elements = [ Patch(facecolor=colors[0], edgecolor=colors[0], label='0%'),
                        Patch(facecolor=colors[1], edgecolor=colors[1], label='1-9%'),
                        Patch(facecolor=colors[2], edgecolor=colors[2], label='10-19%'),
                        Patch(facecolor=colors[3], edgecolor=colors[3], label='20-29%'),
                        Patch(facecolor=colors[4], edgecolor=colors[4], label='30-39%'),
                        Patch(facecolor=colors[5], edgecolor=colors[5], label='40-49%'),
                        Patch(facecolor=colors[6], edgecolor=colors[6], label='50-59%'),
                        Patch(facecolor=colors[7], edgecolor=colors[7], label='60-69%'),
                        Patch(facecolor=colors[8], edgecolor=colors[8], label='70-79%'),
                        Patch(facecolor=colors[9], edgecolor=colors[9], label='80-89%'),
                        Patch(facecolor=colors[10], edgecolor=colors[10], label='90-100%'),]
    fontP = FontProperties()
    fontP.set_size('small')
    figu_commune.legend(handles=legend_elements, loc='upper left', prop=fontP)

    annot = figu_commune.annotate("", xy=(-1,35.5), xytext=(-20,20),textcoords="offset points",
                bbox=dict(fc="white", ec="black", lw=1))
    annot.set_visible(False)

    def update(event):
        if event.inaxes == figu_commune:
            for i, w in enumerate(wedges):
                for j, wd in enumerate(w):
                    if wd.contains_point([event.x, event.y]):
                        wd.set_facecolor("green")
                        xy = wd.get_xy()
                        annot.xy = (xy[0,0], xy[1,1])
                        annot.set_text("commune name : "+str(Commune_name[i])+"\nnumber of cases : "+str(Commune.get(Commune_name[i]))+"\npercentage : "+str(commune_percenteges[i])+"%")
                        annot.set_visible(True)
                        fig_commune.canvas.draw_idle()
                    else:
                        #annot.set_visible(False)
                        if(commune_percenteges[i] == 0):
                            color_id = 0
                        elif(commune_percenteges[i] > 0 and commune_percenteges[i] < 10):
                            color_id = 1
                        elif(commune_percenteges[i] >= 10 and commune_percenteges[i] < 20):
                            color_id = 2
                        elif(commune_percenteges[i] >=20 and commune_percenteges[i] < 30):
                            color_id = 3
                        elif(commune_percenteges[i] >=30 and commune_percenteges[i] < 40):
                            color_id = 4
                        elif(commune_percenteges[i] >=40 and commune_percenteges[i] < 50):
                            color_id = 5
                        elif(commune_percenteges[i] >=50 and commune_percenteges[i] < 60):
                            color_id = 6
                        elif(commune_percenteges[i] >=60 and commune_percenteges[i] < 70):
                            color_id = 7
                        elif(commune_percenteges[i] >=70 and commune_percenteges[i] < 80):
                            color_id = 8
                        elif(commune_percenteges[i] >=80 and commune_percenteges[i] < 90):
                            color_id = 9
                        elif(commune_percenteges[i] >=90):
                            color_id = 10
                        wd.set_facecolor(colors[color_id])
            fig_commune.canvas.draw_idle()

    # Sexe
    Sexe = Sexe.groupby(['sexe']).size()
    labels = 'Female', 'Male'
    sizes = [Sexe['f'],Sexe['m']]
    #explode = (0, 0.1)  only "explode" the 2nd slice

    fig = Figure()
    fig.patch.set_facecolor('#f5f5f5')

    figu = fig.add_subplot()
    figu.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    figu.axis('equal')

    plot = FigureCanvasTkAgg(fig, master=outlier)  # A tk.DrawingArea.
    plot.draw()
    plot.get_tk_widget().place(relx=0.005, rely=0.15, relwidth=0.990, relheight=0.7)

    def switch_graph(button, plot, fig, fig_age, fig_commune, outlier):
        global in_use
        plot.get_tk_widget().forget()

        if (button['text'] == 'Sexe'):
            plot = FigureCanvasTkAgg(fig, master=outlier)
            plot.draw()
            plot.get_tk_widget().place(relx=0.005, rely=0.15, relwidth=0.990, relheight=0.7)
        elif (button['text'] == 'Age'):
            plot = FigureCanvasTkAgg(fig_age, master=outlier)
            plot.draw()
            plot.get_tk_widget().place(relx=0.005, rely=0.15, relwidth=0.990, relheight=0.7)
        elif (button['text'] == 'Commune'):
            plot = FigureCanvasTkAgg(fig_commune, master=outlier)
            plot.draw()
            plot.get_tk_widget().place(relx=0.005, rely=0.15, relwidth=0.990, relheight=0.7)
            fig_commune.canvas.mpl_connect("motion_notify_event", update)

        in_use=button['text']

    Labels=["Sexe", "Age", "Commune"]

    for i in range(3):
        Change_Button = tk.Button(outlier,
                        text=Labels[i],
                        width=20,
                        height=5,
                        bg=canvas_bg_color,
                        fg='#000000',
                        highlightthickness=0,
                        relief='flat',
                        font=("Helvetica", 16))
        Change_Button.configure(command=lambda b=Change_Button, p=plot, f=fig, fa=fig_age, fc=fig_commune, out=outlier: 
        switch_graph(b,p,f,fa,fc,out))
        Change_Button.place(x = 25 + (i+1)*160, y = 50, width=150, height=60)
    
    return outlier
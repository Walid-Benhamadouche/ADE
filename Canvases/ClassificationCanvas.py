import tkinter as tk
import pandas as pd
import numpy as np
import collections
from tkinter import filedialog
import tkinter as tk
from calendar import monthrange

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

def createOutlier(parent, Sexe, Age, Secteur, Quartier, Commune):
    canvas_bg_color="#0C3851"
    #button_bg_color="#3258EF"
    outlier = tk.Canvas(parent,
              width=1050,
              height=800,
              bg=canvas_bg_color,
              highlightthickness=0,
              relief='flat')

    # Age
    temp_age = Age.values.tolist()
    age_table = []
    age_table = temp_age[0]
    print(age_table)
    for val in enumerate(temp_age):
        if not(val[0] in age_table):
            age_table.append(val[0])

    Age = Age.groupby(['age']).size()
    #re:grouping ages samples
    
    #for val in enumerate(age_table):
    #    if (val <= 6):
    #        zero_six = zero_six + Age[val]
    
    # Secteur
    temp_secteur = Secteur.values.tolist()
    secteur_table = []
    secteur_table = temp_secteur[0]
    print(secteur_table)
    for val in enumerate(temp_secteur):
        if not(val[0] in secteur_table):
            secteur_table.append(val[0])

    Secteur = Secteur.groupby(['nom_secteur']).size()
    
    # Quartier
    temp_quartier = Quartier.values.tolist()
    quartier_table = []
    quartier_table = temp_quartier[0]
    print(quartier_table)
    for val in enumerate(temp_quartier):
        if not(val[0] in quartier_table):
            quartier_table.append(val[0])

    Quartier = Quartier.groupby(['nom_quartier']).size()
    
    # Commune
    temp_commune = Commune.values.tolist()
    commune_table = []
    commune_table = temp_commune[0]
    print(commune_table)
    for val in enumerate(temp_commune):
        if not(val[0] in commune_table):
            commune_table.append(val[0])

    Commune = Commune.groupby(['nom_commune']).size()

    # Sexe
    Sexe = Sexe.groupby(['sexe']).size()
    labels = 'Female', 'Male'
    sizes = [Sexe['F'],Sexe['M']]
    #explode = (0, 0.1)  only "explode" the 2nd slice

    fig = Figure()
    fig.patch.set_facecolor('#fec5e5')

    figu = fig.add_subplot()
    figu.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    figu.axis('equal')

    plot = FigureCanvasTkAgg(fig, master=outlier)  # A tk.DrawingArea.
    plot.draw()
    plot.get_tk_widget().place(relx=0.005, rely=0.15, relwidth=0.990, relheight=0.7)

    print(Sexe[0])
    print(Sexe[1])
    print(Sexe)
    
    return outlier
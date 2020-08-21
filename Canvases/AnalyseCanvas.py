from sklearn.neighbors import KNeighborsClassifier
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

def createAnalyse(parent, data, Threshold_percent, percentages, anomalies, year_dates):

    def Analyse_data(data, figu, plot, fig, anomalies):
        data_without_anomalies = []
        data_to_classify = []
        final_classes = []
        under_over = []
        for idx,dataa in enumerate(percentages):
            if not (idx in anomalies):
                if (dataa > Threshold_percent[0]):
                    under_over.append("over")
                else:
                    under_over.append("under")
        for idx,data in enumerate(data):
            if not (idx in anomalies):
                data_without_anomalies.append(idx)
            else:
                data_to_classify.append(idx)
        knn = KNeighborsClassifier(n_neighbors=2, metric='minkowski', p=2)
        knn.fit(np.array(data_without_anomalies).reshape(-1, 1),np.array(under_over))
        y_pred = knn.predict(np.array(data_to_classify).reshape(-1, 1))
        index = 0
        secindex = 0
        thirdindex = 0
        for index in range(53):
            if (index == data_without_anomalies[secindex]):
                final_classes.append(under_over[secindex])
                secindex +=1 
            elif (index == data_to_classify[thirdindex]):
                final_classes.append(y_pred[thirdindex])
                thirdindex +=1

        starting_date = []
        ending_date = []
        over_counter = 0
        start_date_temp = 0

        for idx,element in enumerate(final_classes):
            if (element == 'over'):
                if (over_counter <1):
                    start_date_temp = idx+1
                over_counter+=1
                figu.get_children()[idx].set_color('r')
            else:
                if (over_counter >= 2):
                    starting_date.append(start_date_temp)
                    ending_date.append(idx+1)
                over_counter = 0
        spans = []
        for idx,element in enumerate(starting_date):
            temp = figu.axvspan(starting_date[idx], ending_date[idx]-0.1, color='green', alpha=0.4)
            spans.append(temp)
        
        annot = figu.annotate("", xy=(0,0), xytext=(-20,20),textcoords="offset points",
                    bbox=dict(fc="white", ec="black", lw=1))

        def init_annot(start_week, end_week):
            annot.xy = (start_week, 0)
            start_week = start_week*7
            end_week = end_week * 7
            annot.set_text("start date :"+str(year_dates.keys()[start_week])+"\nend date :"+str(year_dates.keys()[end_week-1]))
            annot.set_visible(False)

        def hover(event):
            vis = annot.get_visible()
            if event.inaxes == figu:
                for index,span in enumerate(spans):
                    cont, ind = span.contains(event)
                    if cont:
                        init_annot(starting_date[index], ending_date[index])
                        annot.set_visible(True)
                        fig.canvas.draw_idle()
                        return
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()
        
        legend_elements = [Line2D([0], [0], color='#1f77b4', lw=2, label='threshold'),
                           Patch(facecolor='#1f77b4', edgecolor='#1f77b4', label='Cases'),
                           Patch(facecolor='r', edgecolor='r', label='weeks passed the threshold'),
                           Patch(facecolor='green', edgecolor='green', alpha=0.4, label='Epidemie Period')]
        figu.legend(handles=legend_elements)

        plot.get_tk_widget().forget()
        plot = FigureCanvasTkAgg(fig, master=Analyse)
        plot.draw()
        plot.get_tk_widget().place(relx=0.005, rely=0.15, relwidth=0.990, relheight=0.7)

        fig.canvas.mpl_connect("motion_notify_event", hover)
    
    canvas_bg_color="#f5f5f5"
    Analyse = tk.Canvas(parent,
              width=1050,
              height=800,
              bg='#f5f5f5',
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

    plot = FigureCanvasTkAgg(fig, master=Analyse)
    plot.draw()
    plot.get_tk_widget().place(relx=0.005, rely=0.15, relwidth=0.990, relheight=0.7)

    #adding the title lable
    Title = tk.Label(Analyse,
                 text="Analysing Data :",
                 width=15,
                 height=2,
                 bg=canvas_bg_color,
                 fg='black',
                 highlightthickness=0,
                 relief='flat',
                 font=("Helvetica", 12))
    Title.place(x = 20, y = 10)

    Load_db = tk.Button(Analyse,
                 text="Analyse",
                 width=15,
                 height=2,
                 bg='#30e3ca',
                 fg='white',
                 highlightthickness=0,
                 relief='flat',
                 font=("Helvetica", 12))
    Load_db.place(relx=0.5, y = 70, anchor=tk.CENTER)
    Load_db.configure(command=lambda b=data, f=figu, p=plot, fi=fig, ano=anomalies: Analyse_data(b, f, p, fi, ano))
    return Analyse
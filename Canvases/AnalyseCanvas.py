from sklearn.neighbors import KNeighborsClassifier
import tkinter as tk
import numpy as np

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.ticker as mtick

def createAnalyse(parent, data, Threshold_percent, percentages):

    def find_anomalies(data):
        anomalies = []
        random_data_std = np.std(data)
        random_data_mean = np.mean(data)
        anomaly_cut_off = random_data_std * 3

        lower_limit = 0
        upper_limit = random_data_mean + anomaly_cut_off

        print(upper_limit)
        print(lower_limit)
        index = 0
        for idx,outlier in enumerate(data):
            if outlier > upper_limit or outlier < lower_limit:
                anomalies.append(idx)
            index +=1
        print(data)
        return anomalies
    
    def Analyse_data(data, figu, plot, fig):
        data_without_anomalies = []
        data_to_classify = []
        final_classes = []
        anomalies = find_anomalies(data)
        print(anomalies)
        under_over = []
        print(percentages)
        for idx,dataa in enumerate(percentages):
            if not (idx in anomalies):
                print(dataa, Threshold_percent[0])
                if (dataa > Threshold_percent[0]):
                    under_over.append("over")
                else:
                    under_over.append("under")
        for idx,data in enumerate(data):
            if not (idx in anomalies):
                data_without_anomalies.append(idx)
            else:
                data_to_classify.append(idx)
        print(under_over, len(under_over))
        print(data_without_anomalies)
        print(data_to_classify)
        knn = KNeighborsClassifier(n_neighbors=2, metric='minkowski', p=2)
        knn.fit(np.array(data_without_anomalies).reshape(-1, 1),np.array(under_over))
        y_pred = knn.predict(np.array(data_to_classify).reshape(-1, 1))
        print(y_pred)
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
        print(final_classes, len(final_classes))
        for idx,element in enumerate(final_classes):
            if (element == 'over'):
                figu.get_children()[idx].set_color('r')
        
        plot.get_tk_widget().forget()
        plot = FigureCanvasTkAgg(fig, master=Analyse)
        plot.draw()
        plot.get_tk_widget().place(relx=0.005, rely=0.15, relwidth=0.990, relheight=0.7)
    

    Analyse = tk.Canvas(parent,
              width=1050,
              height=800,
              bg='#101001',
              highlightthickness=0,
              relief='flat')

    x = np.linspace(1, len(data), len(data))

    fig = Figure()
    fig.patch.set_facecolor('#fec5e5')
    
    figu = fig.add_subplot()

    figu.bar(x, percentages)

    figu.yaxis.set_major_formatter(mtick.PercentFormatter(1))
    figu.set_title('number of cases per week')
    figu.set_facecolor('#fec5e5')
    figu.plot(x, [Threshold_percent for i in range(53)], label='treshold')
    figu.legend()

    plot = FigureCanvasTkAgg(fig, master=Analyse)
    plot.draw()
    plot.get_tk_widget().place(relx=0.005, rely=0.15, relwidth=0.990, relheight=0.7)

    Load_db = tk.Button(Analyse,
                 text="Analyse",
                 width=15,
                 height=2,
                 bg='#3258EF',
                 fg='white',
                 highlightthickness=0,
                 relief='flat',
                 font=("Helvetica", 12))
    Load_db.place(relx=0.5, y = 70, anchor=tk.CENTER)
    Load_db.configure(command=lambda b=data, f=figu, p=plot, fi=fig: Analyse_data(b, f, p, fi))
    return Analyse
import tkinter as tk
import datetime
import numpy as np

from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.ticker as mtick

def createIncubation(parent, dates, values_per_day, incubation_min, incubation_max, incubation_aver, data, Threshold_percent, percentages):
    
    def find_exposer(dates, data, values_per_day, incubation_min, incubation_max, incubation_aver, plot, fig, figu):
        first_case = values_per_day.keys()[0]
        last_case = values_per_day.keys()[len(values_per_day)-1]
        peak_case = data.index(max(data))
        peak_case = (peak_case*7)+1
        peak_case = dates.keys()[peak_case]

        incubation_min = incubation_min.iloc[0]['incubation_min']
        incubation_max = incubation_max.iloc[0]['incubation_max']
        incubation_aver = incubation_aver.iloc[0]['incubation_aver']

        first_case_date  = datetime.date(int(first_case.year), int(first_case.month), int(first_case.day))
        incubation_min_dt = datetime. timedelta(incubation_min)
        exposer_period_start = first_case_date - incubation_min_dt
        print(exposer_period_start)

        last_case_date  = datetime.date(int(last_case.year), int(last_case.month), int(last_case.day))
        incubation_max_dt = datetime. timedelta(incubation_max)
        exposer_period_end = last_case_date - incubation_max_dt
        print(exposer_period_end)

        peak_case_date = datetime.date(int(peak_case.year), int(peak_case.month), int(peak_case.day))
        incubation_aver_dt = datetime. timedelta(incubation_aver)
        exposer_period_aver = peak_case_date - incubation_aver_dt
        print(exposer_period_aver)

        minn = min(exposer_period_start, exposer_period_aver, exposer_period_end)
        maxx = max(exposer_period_start, exposer_period_aver, exposer_period_end)

        exposer_time = maxx - minn
        print(exposer_time)
        start = int(minn.strftime("%j"))
        end = int(maxx.strftime("%j"))
        start = start/7
        end = end/7

        test = figu.axvspan(start, end, color='red', alpha=0.5)

        #position must be fixed
        annot = figu.annotate("", xy=(start,0), xytext=(-20,20),textcoords="offset points",
                    bbox=dict(fc="white", ec="black", lw=1))

        annot.set_text("start date :"+str(exposer_period_start)+"\naverage date :"+str(exposer_period_aver)+"\nend date :"+str(exposer_period_end)+"\nduration :"+str(exposer_time))
        annot.set_visible(False)

        def hover(event):
            vis = annot.get_visible()
            if event.inaxes == figu:
                cont, ind = test.contains(event)
                print(cont, ind)
                if cont:
                    annot.set_visible(True)
                    fig.canvas.draw_idle()
                    return
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

        legend_elements = [Line2D([0], [0], color='#1f77b4', lw=2, label='threshold'),
                           Patch(facecolor='#1f77b4', edgecolor='#1f77b4', label='Cases'),
                           Patch(facecolor='r', edgecolor='r', alpha=0.5, label='Exposer Periode')]
        figu.legend(handles=legend_elements)

        plot.get_tk_widget().forget()
        plot = FigureCanvasTkAgg(fig, master=outlier)
        plot.draw()
        plot.get_tk_widget().place(relx=0.005, rely=0.15, relwidth=0.990, relheight=0.7)
        
        fig.canvas.mpl_connect("motion_notify_event", hover)

    canvas_bg_color="#f5f5f5"
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

    #adding the title lable
    Title = tk.Label(outlier,
                 text="Exposer Periode :",
                 width=15,
                 height=2,
                 bg=canvas_bg_color,
                 fg='black',
                 highlightthickness=0,
                 relief='flat',
                 font=("Helvetica", 12))
    Title.place(x = 20, y = 10)

    Exposer_per_bt = tk.Button(outlier,
                 text="find Exposer period",
                 width=15,
                 height=2,
                 bg='#30e3ca',
                 fg='white',
                 highlightthickness=0,
                 relief='flat',
                 font=("Helvetica", 12))
    Exposer_per_bt.place(relx=0.5, y = 70, anchor=tk.CENTER)
    Exposer_per_bt.configure(command=lambda dates=dates ,data=data, v=values_per_day, min=incubation_min, max=incubation_max, aver=incubation_aver, p=plot, fi=fig, figu=figu: find_exposer(dates, data, v, min, max, aver, p, fi, figu))
    return outlier
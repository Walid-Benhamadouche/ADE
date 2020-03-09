import tkinter as tk
def createOutlier(parent):
    canvas_bg_color="#0C3851"
    #button_bg_color="#3258EF"
    outlier = tk.Canvas(parent,
              width=1050,
              height=800,
              bg=canvas_bg_color,
              highlightthickness=0,
              relief='flat')
    return outlier
import time_series_forecasting as tsf
import os
import tkinter as tk
import time
import base64
import threading
import csv
from datetime import datetime
from IPython.display import display
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from time_series_forecasting import TimeSeries

def root_clear(root):
    for element in root.winfo_children():
        element.destroy()
    return root

def _from_rgb(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'

class MainMenu:
    def __init__(self, root):
        #Sets the Title Name
        self._root = root
        root.title("Crime Predictor")        
        #This set of code creates the background
        width=1000
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root["bg"] = "#a7b688" 

        TempLabel1=tk.Label(root, bg="#a7b688", borderwidth="2px", justify="left", anchor="w", text="Temp 1:", relief="flat")
        TempLabel1.place(x=120,y=50,width=340,height=30)

        TempLabel2=tk.Label(root, bg="#a7b688", borderwidth="2px", justify="left", anchor="w", text="Temp 2:", relief="flat")
        TempLabel2.place(x=120,y=100,width=340,height=30)

        TempLabel3=tk.Label(root, bg="#a7b688", borderwidth="2px", justify="left", anchor="w", text="Temp 3:", relief="flat")
        TempLabel3.place(x=120,y=150,width=340,height=30)

        TempText1=tk.Entry(root, bg="#ffffff", fg="#333333")
        TempText1.place(x=175,y=50,width=200,height=30)

        TempText2=tk.Entry(root, bg="#ffffff", fg="#333333")
        TempText2.place(x=175,y=100,width=200,height=30)

        TempText3=tk.Entry(root, bg="#ffffff", fg="#333333")
        TempText3.place(x=175,y=150,width=200,height=30)

        CrimeTextLabel=tk.Label(root, anchor="center", bg="#FFFFFF", fg="#000000", justify="left")
        self.CrimeTextLabel=CrimeTextLabel
        CrimeTextLabel["text"] = TimeSeries.basictext()
        CrimeTextLabel.place(x=130,y=360,width=280,height=140)
        
        StartBasicButton=tk.Button(root, bg="#FFFFFF", fg="#000000", justify="center", text="Start Basic")
        StartBasicButton.place(x=150,y=250,width=100,height=25)
        StartBasicButton["command"] = self.StartBasicButton_command

        StartTestButton=tk.Button(root, bg="#FFFFFF", fg="#000000", justify="center", text="Start Test")
        StartTestButton.place(x=300,y=250,width=100,height=25)
        StartTestButton["command"] = self.StartTestButton_command

    def StartBasicButton_command(self):
        TimeSeries.basic()

    def StartTestButton_command(self):
        TimeSeries.testing()
        
def main():
    # The GUI root is created and runs it
    root = tk.Tk()
    root.configure(background='#5865F2')
    # Sets the Main Menu
    MainMenu(root)
    root.mainloop()

if __name__ == '__main__':
    main()
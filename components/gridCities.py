from tkinter import ttk
import tkinter as tk
import tkinter.scrolledtext as st 

class GridCities(): 
    
    radioButtons = []
    def __init__(self, parent, cities):
        self.selectedCity = tk.StringVar()
        for city in cities:
            r = ttk.Radiobutton(parent, text=city, variable=self.selectedCity, value=city)
            r.pack()
            self.radioButtons.append(r)
        
    def getCity(self):
        return self.selectedCity.get()

    def disableAll(self):
        for radio in self.radioButtons:
            radio.config(state='disabled')

    def enableAll(self):
        for radio in self.radioButtons:
            radio.config(state='enable')
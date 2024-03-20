from tkinter import ttk
import tkinter as tk
import tkinter.scrolledtext as st 

class LoggerScroll(st.ScrolledText):
    #mi servono poi le variabili font e dimensioni

    width = '40'
    height = '20'
    def __init__(self, parent):
        kwargs={
            'width': self.width,
            'height': self.height
        }
        super().__init__(parent, **kwargs)

        

    def addLog(self, msg):
        self.configure(state='normal')
        self.insert(tk.END,msg)
        self.yview(tk.END)
        self.configure(state='disabled')
        self.update()

    def clear(self):
        self.configure(state='normal')
        self.delete('1.0',tk.END)
        self.configure(state='disabled')
        self.update()
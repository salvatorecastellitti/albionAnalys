import tkinter as tk
from tkinter import ttk

class Table(ttk.Treeview):
    columns = ['ERROR','ERROR','ERROR','ERROR']
    height = 4
    show = 'headings'

    def update(self, data: dict):
        if(len(self.get_children())>0):
            for child in self.get_children():
                self.delete(child)
        firstExec = True
        for item in data:
            values = []
            for key,value in item.items():
                if(firstExec):
                    self.heading(key, text=key)
                values.append(value)
            self.insert("", tk.END, values=values)
            firstExec = False
    
    def getColumns(self, data: dict):
        data = data[0]
        columns = []
        for key,_ in data.items():
            columns.append(key)
        return columns
    
    def __init__(self, parent, data):
        if(len(self.getColumns(data))>0):
            self.columns = self.getColumns(data)

        kwargs={
            'columns': self.columns,
            'height': self.height,
            'show': self.show
        }
        super().__init__(parent, **kwargs)
        for col in self.columns:
            self.column(col,width=50)
        self.update(data=data)


            
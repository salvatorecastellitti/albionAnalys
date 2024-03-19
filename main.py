import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as st 
from utils.AlbiPy import sniffing_thread
from utils.AlbiPy import HEADERS
from time import sleep
import threading
from components.scrollableLog import LoggerScroll
from components.gridCities import GridCities

root = tk.Tk()
root.title('Albion Analys')
root.geometry('600x600')
root.minsize(600,600)

s = ttk.Style()
s.configure('Market.TFrame', background='blue')

root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)

market_retrieve = ttk.Frame(root,style='Market.TFrame')
market_data = ttk.Frame(root)

market_retrieve.grid(row=0)
market_data.grid(row=1)

market_cities = ttk.Frame(market_retrieve)
#market retrieve
label1 = ttk.Label(market_retrieve, text='Label1', background='red')
label1.grid(column=1, sticky='s')
market_cities.grid(column=2, row=0)

cities = ['bridgewatch','fort_sterling','tethford','lymhurst','martlock','brecilien','carleon']
radios = GridCities(market_cities, cities)

log_retriever = LoggerScroll(market_retrieve)
log_retriever.grid(column=4, row=0)

def inizioGather():
    global inizio_kill
    #thread = sniffing_thread()
    #thread.start()

    while not inizio_kill:
        startScrape.config(state='disabled')
        logs = "Waiting three seconds...\n"
        
        log_retriever.addLog(msg=logs)
        sleep(3)

        logs = "Fetching recorded orders...\n"
        
        #orders = thread.get_data()
            



def inizioGather2():
    log_retriever.clear()
    thread_gather = threading.Thread(target=inizioGather)
    global inizio_kill
    inizio_kill = False
    thread_gather.start()
    print(radios.getCity())
    radios.disableAll()
def fineGather():
    startScrape .config(state='enable')
    global inizio_kill
    inizio_kill = True
    radios.enableAll()

startScrape = ttk.Button(market_retrieve, text='Inzio', command=inizioGather2)
startScrape.grid(column=3, row=0)
endSniff = ttk.Button(market_retrieve, text='Fine', command=fineGather)
endSniff.grid(column=3, row=1)


label2 = ttk.Label(market_data, text='Label2', background='green')
label2.pack()
root.mainloop()

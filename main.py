import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as st 
from utils.AlbiPy import sniffing_thread
from utils.AlbiPy import HEADERS
from time import sleep
import threading
from components.scrollableLog import LoggerScroll

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

#radio city
city = tk.StringVar()
bridgewatch = ttk.Radiobutton(market_cities, text='Bridgewatch', variable=city, value="bridgewatch")
fort_sterling = ttk.Radiobutton(market_cities, text='Fort Sterling', variable=city, value="fort_sterling")
tethford = ttk.Radiobutton(market_cities, text='Tethford', variable=city, value="tethford")
lymhurst = ttk.Radiobutton(market_cities, text='Lymhurst', variable=city, value="lymhurst")
martlock = ttk.Radiobutton(market_cities, text='Martlock', variable=city, value="martlock")
brecilien = ttk.Radiobutton(market_cities, text='Brecilien', variable=city, value="brecilien")
carleon = ttk.Radiobutton(market_cities, text='Carleon', variable=city, value="carleon")
bridgewatch.pack()
fort_sterling.pack()
tethford.pack()
lymhurst.pack()
martlock.pack()
carleon.pack()
brecilien.pack()

log_retriever = LoggerScroll(market_retrieve)
log_retriever.grid(column=4, row=0)

def inizioGather():
    global inizio_kill
    #thread = sniffing_thread()
    #thread.start()

    while not inizio_kill:
        startScrape .config(state='disabled')
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
def fineGather():
    startScrape .config(state='enable')
    global inizio_kill
    inizio_kill = True

startScrape = ttk.Button(market_retrieve, text='Inzio', command=inizioGather2)
startScrape.grid(column=3, row=0)
endSniff = ttk.Button(market_retrieve, text='Fine', command=fineGather)
endSniff.grid(column=3, row=1)


label2 = ttk.Label(market_data, text='Label2', background='green')
label2.pack()
root.mainloop()

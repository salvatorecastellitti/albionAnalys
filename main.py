import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.scrolledtext as st 
from utils.AlbiPy import sniffing_thread
from utils.AlbiPy import HEADERS
from time import sleep
import threading
from components.scrollableLog import LoggerScroll
from components.gridCities import GridCities
from components.table import Table
from utils.invioDati import sendDataToServer
import os
import json

MAX_ROW = 4
filename = os.getcwd() + "/test.csv"
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

cities = ['bridgewatch','fort_sterling','tethford','lymhurst','martlock','brecilien','carleon', 'black_market']
radios = GridCities(market_cities, cities)

log_retriever = LoggerScroll(market_retrieve)
log_retriever.grid(column=4, row=0)
def orders_to_csv(orders, filename, city):
    # open file
    output_file = open(filename, "w")

    # write headers to file
    output_file.write("City,"+",".join(HEADERS)+"\n")

    # write parsed datapoints to file
    for order in orders:
        output_file.write(city + "," + ",".join(list(map(str, order.data)))+"\n")

    # close output file
    output_file.close()

thread_sniff = None
def inizioGather():
    global inizio_kill
    global thread_sniff
    log_retriever.addLog(msg="\nAvvio il Thread dello sniffer\n")
    thread_sniff = sniffing_thread()
    thread_sniff.start()

    while not inizio_kill:
        startScrape.config(state='disabled')
        logs = "\nWaiting three seconds...\n"
        
        log_retriever.addLog(msg=logs)
        sleep(3)

        logs = "\nFetching recorded orders...\n"
        log_retriever.addLog(msg=logs)
        orders = thread_sniff.get_data()

        orders_to_csv(orders, filename, radios.getCity())
            
def inizioGather2():
    if(radios.getCity() == ""):
        messagebox.showerror(title="Errore", message='Devi selezionare una città prima di proseguire')
        return
    log_retriever.clear()
    log_retriever.addLog(msg="\nAvvio il Thread del processo")
    thread_gather = threading.Thread(target=inizioGather)
    global inizio_kill
    inizio_kill = False
    thread_gather.start()
    radios.disableAll()
def fineGather():
    try:
        global thread_sniff
        orders = thread_sniff.get_data()
        log_retriever.addLog(msg="\nScrivo gli ordini rimasti in pancia")
        orders_to_csv(orders, filename, radios.getCity())
        log_retriever.addLog(msg="\nFinito di scrivere gli ordini")
        thread_sniff.stop()

        status = sendDataToServer(filename)
        if(status!='200'):
            log_retriever.addLog(msg="\n\nERRORE INVIO DATI SUL SERVER \n\n")
        else:
            log_retriever.addLog(msg="\n\nDATI INVIATI \n\n")
    except:
        log_retriever.addLog(msg="\n\nQualche problema \n\n")
    log_retriever.addLog(msg="\nStopppo lo sniffer...")
    startScrape .config(state='enable')
    global inizio_kill
    inizio_kill = True
    radios.enableAll()

startScrape = ttk.Button(market_retrieve, text='Inizio', command=inizioGather2)
startScrape.grid(column=3, row=0)
endSniff = ttk.Button(market_retrieve, text='Fine', command=fineGather)
endSniff.grid(column=3, row=1)


label2 = ttk.Label(market_data, text='Label2', background='green')
label2.grid(column=1, sticky='s')
data = """
[{"UnitPriceSilver": "5320000", "Amount": "100", "AuctionType": "request", "ItemTypeId": "T5_CLOTH"}, {"UnitPriceSilver": "5310000", "Amount": "849", "AuctionType": "request", "ItemTypeId": "T5_CLOTH"}]
"""


dataContainer = ttk.Frame(market_data)
data = json.loads(data)


dataContainer.grid(column=2, row=0)
singleDataMarket = [cities[x:x+4] for x in range(0, len(cities), 4)]

for x,item in enumerate(singleDataMarket):
    for y,city in enumerate(item):
        tabella = Table(dataContainer, data=data)
        tabella.update(data)
        tabella.grid(column=y, row=x)



root.mainloop()

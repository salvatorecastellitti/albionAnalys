import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as st 
from utils.AlbiPy import sniffing_thread
from utils.AlbiPy import HEADERS
from time import sleep
import threading

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
label1.grid(column=1)
market_cities.grid(column=2)

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

logs = ""
log_retrieve = st.ScrolledText(market_retrieve, width= 20, height= 20)
log_retrieve.grid(column=4)
log_retrieve.insert(tk.INSERT,logs)
#button start gather data
def inizioGather():
    print("Starting sniffing thread...\nHit ctrl-c to stop recording and save results!\n")
    #thread = sniffing_thread()
    #thread.start()

    # fetch recorded market orders and write them to file every three seconds
    try:
        while True:
            startScrape.config(state='disabled')
            logs = "Waiting three seconds...\n"
            log_retrieve.configure(state='normal')
            log_retrieve.insert(tk.END,logs)
            log_retrieve.configure(state='disabled')
            log_retrieve.update()
            sleep(3)

            logs = "Fetching recorded orders...\n"
            log_retrieve.configure(state='normal')
            log_retrieve.insert(tk.END,logs)
            log_retrieve.configure(state='disabled')
            log_retrieve.update()
            log_retrieve.yview(tk.END)
            #orders = thread.get_data()
            
    except:
        pass

thread_gather = threading.Thread(target=inizioGather)
def inizioGather2():
    thread_gather.start()
def fineGather():
    thread_gather.des
startScrape = ttk.Button(market_retrieve, text='Inzio', command=lambda: threading.Thread(target=inizioGather).start())
startScrape.grid(column=3)
startScrape = ttk.Button(market_retrieve, text='Fine', command=lambda: fineGather)
startScrape.grid(column=3)


label2 = ttk.Label(market_data, text='Label2', background='green')
label2.pack()
root.mainloop()

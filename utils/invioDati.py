import csv
import json
import requests

def sendDataToServer(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    #send data
    url = 'http://194.164.164.192/sendData'
    x = requests.post(url, json =json.dumps(data))
    return (x.status_code)    
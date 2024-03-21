import csv
import json
import requests
import gzip

def sendDataToServer(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    with open("sample.json", "w") as outfile: 
        json.dump(data, outfile)
    #send data
    url = 'http://194.164.164.192/sendData'

    headers = {
        'Content-Encoding': 'gzip'
    }
    
    x = requests.post(url, zipped_payload = gzip.compress(data.encode('utf-8')), headers=headers)
    return (x.status_code)    
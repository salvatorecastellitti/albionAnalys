import csv
import json

def sendDataToServer(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    with open("sample.json", "w") as outfile: 
        json.dump(data, outfile)
        
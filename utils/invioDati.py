import csv
import json
import requests
import gzip
import pandas as pd


def sendDataToServer(filename):
    df = pd.read_csv(filename)
    df = df.drop_duplicates()
    # Raggruppa i dati per le colonne desiderate e seleziona i primi 3 record per gruppo
    result = df.groupby(['City','AuctionType', 'ItemTypeId', 'EnchantmentLevel', 'QualityLevel']).apply(lambda x: x.nlargest(5, 'UnitPriceSilver') if x['AuctionType'].iloc[0] == 'request' else x.nsmallest(5, 'UnitPriceSilver')).reset_index(drop=True)
    result = result.fillna(value='')

    result_dict = result.to_dict(orient='records')

    with open("sample.json", "w") as outfile: 
        json.dump(result_dict, outfile, default=str)
    #send data
    url = 'http://194.164.164.192/saveMarket'

    headers = {
        'Content-Encoding': 'gzip',
        'Content-Type': 'application/x-gzip'
    }
    
    json_data = json.dumps(result_dict, default=str).encode('utf-8')
    compressed_data = gzip.compress(json_data)
    x = requests.post(url, data=compressed_data, headers=headers)
    print(x.status_code)
    return (x.status_code)    
import requests
import pandas as pd
from load import Loader
from keep_alive import keep_alive
import time

URL = 'https://covid-19-report-api.vercel.app/api/v1/cases/latest'

def Main():
    req = requests.get(URL)
    data  = req.json()
    
    country = []
    confirmed = []
    deaths = []
    
    for datum in data['data']:
        if 'countryregion' in datum and 'confirmed' in datum and 'deaths' in datum:
            country.append(datum['countryregion'])
            confirmed.append(datum['confirmed'])
            deaths.append(datum['deaths'])
    
    data_dict = {
        'country': country,
        'confirmed': confirmed,
        'deaths': deaths
    }
    
    df = pd.DataFrame(data_dict)
    df = df.groupby('country').sum()
    df.reset_index(inplace = True)
    
    loader = Loader()
    loader.createTable()
    loader.deleteData()
    loader.loadData(df)
    print('Data refreshed!')

if __name__ == '__main__':
    
    while True:
        keep_alive()
        Main()
        time.sleep(43200)
        keep_alive()

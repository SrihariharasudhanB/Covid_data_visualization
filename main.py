import requests
import pandas as pd
from datetime import date
from load_demo import Loader

req = requests.get('https://covid-19-report-api.vercel.app/api/v1/cases/latest')
data  = req.json()
today = date.today()

country = []
date = []
confirmed = []
deaths = []
recovered = [] 

for datum in data['data']:
    if 'countryregion' in datum and 'confirmed' in datum and 'deaths' in datum: #and 'recovered' in datum:
        country.append(datum['countryregion'])
        #date.append(datum['lastupdate'][:10])
        confirmed.append(datum['confirmed'])
        deaths.append(datum['deaths'])
        #recovered.append(datum['recovered'])

data_dict = {
    "country": country,
    "confirmed": confirmed,
    "deaths": deaths,
    #"recovered": recovered
}

df = pd.DataFrame(data_dict)
df = df.groupby('country').sum()
df.reset_index(inplace = True)

loader = Loader()
loader.createTable()
loader.deleteData()
loader.loadData(df)
print('Data refreshed!')
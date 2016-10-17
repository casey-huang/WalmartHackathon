import pandas as pd



dat=pd.read_csv('train.csv')
weather=pd.read_csv('weather.csv')
key=pd.read_csv('key.csv')

merge1=dat.merge(key,on='store_nbr')
merge_dat=merge1.merge(weather,on=['station_nbr','date'])

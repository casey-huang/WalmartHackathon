import pandas as pd
import numpy as np

def add_features(df, weather_df, key_df):
    df['store_nbr'] = df['store_nbr'].astype(str)
    df['item_nbr'] = df['item_nbr'].astype(str)
    df['id'] = df['store_nbr'] + '_' + df['item_nbr'] + '_' + df['date']
    df['store_item_nbr'] = df['store_nbr'] + '_' + df['item_nbr']

    df['date'] = pd.to_datetime(df['date'])
    df['month'] = [x.month for x in df['date']]
    df['dayofweek'] = df['date'].dt.dayofweek
    df['dayseries'] = [x.days for x in (df['date'] - pd.to_datetime('2012-01-01'))]
    df['is_weekend'] = [1 if x in (5,6) else 0 for x in df['dayofweek']]

    holidays = ['2012 Jan 1'
        ,'2012 Jan 2'
        ,'2012 Jan 16'
        ,'2012 Feb 14'
        ,'2012 Feb 20'
        ,'2012 Apr 8'
        ,'2012 May 13'
        ,'2012 May 28'
        ,'2012 Jun 17'
        ,'2012 Jul 4'
        ,'2012 Sep 3'
        ,'2012 Oct 8'
        ,'2012 Oct 31'
        ,'2012 Nov 6'
        ,'2012 Nov 11'
        ,'2012 Nov 12'
        ,'2012 Nov 22'
        ,'2012 Dec 24'
        ,'2012 Dec 25'
        ,'2012 Dec 31'
        ,'2013 Jan 1'
        ,'2013 Jan 21'
        ,'2013 Feb 14'
        ,'2013 Feb 18'
        ,'2013 Mar 31'
        ,'2013 May 12'
        ,'2013 May 27'
        ,'2013 Jun 16'
        ,'2013 Jul 4'
        ,'2013 Sep 2'
        ,'2013 Oct 14'
        ,'2013 Oct 31'
        ,'2013 Nov 11'
        ,'2013 Nov 28'
        ,'2013 Dec 24'
        ,'2013 Dec 25'
        ,'2013 Dec 31'
        ,'2014 Jan 1'
        ,'2014 Jan 20'
        ,'2014 Feb 14'
        ,'2014 Feb 17'
        ,'2014 Apr 13'
        ,'2014 Apr 20'
        ,'2014 May 11'
        ,'2014 May 26'
        ,'2014 Jun 15'
        ,'2014 Jul 4'
        ,'2014 Sep 1'
        ,'2014 Oct 13'
        ,'2014 Oct 31'
        ,'2014 Nov 11'
        ,'2014 Nov 27'
        ,'2014 Dec 24'
        ,'2014 Dec 25'
        ,'2014 Dec 31']
    holiday_dates = [pd.to_datetime(x) for x in holidays]
    df['is_holiday'] = [1 if x in holiday_dates else 0 for x in df['date']]
    black_friday = [pd.to_datetime('2012 Nov 23'), pd.to_datetime('2013 Nov 29'), pd.to_datetime('2014 Nov 28'), pd.to_datetime('2015 Nov 27')]
    df['is_black_friday'] = [1 if x in black_friday  else 0 for x in df['date']]

    # joining takes weirdly large memory
    # df['store_nbr'] = df['store_nbr'].astype(int)
    # features = df.merge(key_df, how = 'left', left_on='store_nbr', right_on='store_nbr')\
    #             .merge(weather_df, how = 'left', left_on='station_nbr', right_on='station_nbr')

    return df

train = pd.read_csv('items_to_train_on.csv')
test = pd.read_csv('items_to_predict.csv')
weather_df = pd.read_csv('weather.csv')
key_df = pd.read_csv('key.csv')

add_features(train, weather_df, key_df).to_csv('items_to_train_on_ft.csv')
add_features(test, weather_df, key_df).to_csv('items_to_predict_ft.csv')


import pandas as pd
from pandas import DataFrame
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import os
from dotenv import load_dotenv
import numpy as np
import matplotlib.pyplot as plt
# Importing hidden API Key.
load_dotenv()
api_key = os.getenv("API_KEY")



ts = TimeSeries(key = api_key, output_format = "pandas")
# data, meta_data = ts.get_intraday(symbol='MSFT',interval='60min', outputsize='full')
data, meta_data = ts.get_daily(symbol = 'MSFT', outputsize = 'full')
data.sort_index(ascending = True, inplace = True)
print(data)

ti = TechIndicators(key = api_key, output_format = 'pandas')
sma, sma_data = ti.get_sma(symbol='MSFT', interval='60min', time_period='60')
sma.sort_index(ascending = True, inplace = True)
print(sma)

# agg = data.join(sma, on = "date")
# agg.dropna(inplace = True)
# print(agg)


# ser1 = pd.Series(data['4. close'])
# ser2 = pd.Series(sma['SMA'])
# ser3 = pd.Series(data.reset_index()['date'])

# fig = plt.figure()
# ax1 = fig.add_subplot(111)

# ax1.plot(agg.index, agg["4. close"], c='b', label='msft')
# ax1.plot(agg.index, agg["SMA"], c='r', label='sma_msft')
# plt.legend(loc='upper left');
# plt.show()

class DataTunnel():
    def __init__():
        pass
    def get_csv():
        pass
    def extract_stockprice():
        pass



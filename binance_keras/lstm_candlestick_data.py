import pandas as pd
import numpy as np


from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense


from sklearn.preprocessing import MinMaxScaler

from binance.spot import Spot
client = Spot()

# starTime: 1640563200000 - 2021-12-27 00:00:00 GMT
# endTime: 1640649600000 - 2021-12-28 00:00:00 GMT
start_time = 1640563200000
end_time = 1640649600000

# RETRIEVE KLINE/CANDLESTICK DATA
params = {
    'symbol': 'BTCUSDT',
    'interval': '1m',
    'startTime': start_time,
    'endTime': end_time,
    'limit': 1000
}
response = client.klines(**params)
print("BTC-USDT KLINE DATA:")
print(response)

cols = ['open_time',
        'open',
        'high',
        'low',
        'close',
        'volume',
        'close_time',
        'quote_asset_volume',
        'number_of_trades',
        'taker_buy',
        'taker_quote_buy',
        'ignore']

btc_usdt_df = pd.DataFrame(response, columns=cols)
print("All data:")
print(btc_usdt_df)
from binance.spot import Spot
import pandas as pd

client = Spot()

# starTime: 1640563200000 - 2021-12-27 00:00:00 GMT
# endTime: 1640649600000 - 2021-12-28 00:00:00 GMT
start_time = 1640563200000
end_time = 1640649600000

# RETRIEVE KLINE/CANDLESTICK DATA FROM XRP AGAINST BTC (XRPBTC)
params = {
    'symbol': 'XRPBTC',
    'interval': '1m',
    'startTime': start_time,
    'endTime': end_time,
    'limit': 1000
}
xrp_btc_response = client.klines(**params)
print("XRP-BTC KLINE DATA:")
print(xrp_btc_response)

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

xrp_btc_df = pd.DataFrame(xrp_btc_response, columns=cols)
print("All data:")
print(xrp_btc_df)

simplified_xrp_btc_df = xrp_btc_df[['open_time', 'open']].copy()
simplified_xrp_btc_df.rename(columns={'open_time':'timestamp', 'open':'value'}, inplace=True)
print("Only timestamp - value data:")
print(simplified_xrp_btc_df)

from binance.spot import Spot

client = Spot()

# GET CURRENT SERVER TIME EPOCH
print(f"Time is: {client.time()}")

# RETRIEVE ALL SYMBOLS
symbols = client.exchange_info()['symbols']
symbol_names = [s['symbol'] for s in symbols]
print(f"Symbols are: {symbol_names}")

# RETRIEVE KLINE/CANDLESTICK DATA FROM XRP AGAINST BTC (XRPBTC)
params = {
    'symbol': 'XRPBTC',
    'interval': '1m'
}
response = client.klines(**params)
print("XRP-BTC KLINE DATA:")
print(response)









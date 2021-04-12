import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

#prices = client.get_all_tickers()

#for price in prices:
#     print(price)

csvfile = open('data/2021_1year_15min.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "360 days ago")

#candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2021", "11 Apr, 2021")

#candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2020", "12 Jul, 2020")
#candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2017", "12 Jul, 2020")

for candlestick in  candlesticks:
    candlestick[0] = candlestick[0] / 1000
    print(candlestick[0])
    candlestick_writer.writerow(candlestick)

csvfile.close()
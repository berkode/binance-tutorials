from flask import Flask, render_template, request, flash, redirect, jsonify
import config, csv, datetime
from binance.client import Client
from binance.enums import *

app = Flask(__name__)
app.secret_key = b'somelongrandomstring'

client = Client(config.API_KEY, config.API_SECRET, tld='com')


@app.route('/')
def index():
    title = 'CoinView'

    account = client.get_account()

    balances = account['balances']

    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']

    return render_template('index.html', title=title, my_balances=balances, symbols=symbols)


@app.route('/buy', methods=['POST'])
def buy():
    print(request.form)
    try:
        order = client.create_order(symbol=request.form['symbol'], 
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=request.form['quantity'])
    except Exception as e:
        flash(e.message, "error")

    return redirect('/')


@app.route('/sell')
def sell():
    return 'sell'


@app.route('/settings')
def settings():
    return 'settings'


@app.route('/history')
def history():
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Mar, 2021", "12 Apr, 2021")
    processed_candlesticks = []
    for data in candlesticks:
        candlestick = { 
            "time": data[0] / 1000 + 7200, 
            "open": data[1],
            "high": data[2], 
            "low": data[3], 
            "close": data[4]
        }
        processed_candlesticks.append(candlestick)
    return jsonify(processed_candlesticks)

@app.route('/history1')
def history1():
    candlesticks1 = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "360 days ago")
    processed_candlesticks1 = []
    for data1 in candlesticks1:
        candlestick1 = { 
            "time": data1[0] / 1000 + 7200, 
            "open": data1[1],
            "high": data1[2], 
            "low": data1[3], 
            "close": data1[4]
        }
        processed_candlesticks1.append(candlestick1)
    return jsonify(processed_candlesticks1)


@app.route('/history2')
def history2():
    candlesticks2 = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_4HOUR, "1 Mar, 2021", "12 Apr, 2021")
    processed_candlesticks2 = []
    for data2 in candlesticks2:
        candlestick2 = { 
            "time": data2[0] / 1000 + 7200, 
            "open": data2[1],
            "high": data2[2], 
            "low": data2[3], 
            "close": data2[4]
        }
        processed_candlesticks2.append(candlestick2)
    return jsonify(processed_candlesticks2)
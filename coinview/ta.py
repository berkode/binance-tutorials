import numpy
import talib
from numpy import genfromtxt

print("PRINTING DATA")
my_data = genfromtxt('data/2020_2021_Apr_4hours.csv', delimiter=',')
print(my_data)

close = my_data[:,4] 
print(close)

### Closing price is 4th column
#     "time": data[0] / 1000, 
#            "open": data[1],
#            "high": data[2], 
#            "low": data[3], 
#            "close": data[4]
###

print("PRINTING EMA")
moving_average = talib.EMA(close, timeperiod=7)
print(moving_average)

print("PRINTING RSI")
rsi = talib.RSI(close, timeperiod=7)
print(rsi)
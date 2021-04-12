import backtrader as bt
import datetime

class RSIStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=14)

    def next(self):
        if self.rsi < 30  and not self.position:
            self.buy(size=0.01)
        
        if self.rsi > 65 and self.position:
            self.close()


#fromdate = datetime.datetime.strptime('2020-03-01', '%Y-%m-%d')
#todate = datetime.datetime.strptime('2021-04-11', '%Y-%m-%d')

data = bt.feeds.GenericCSVData(dataname='data/2021_1year_15min.csv', dtformat=2, compression=15, timeframe=bt.TimeFrame.Minutes)

#data = bt.feeds.GenericCSVData(dataname='data/2021MarApr_15m.csv', dtformat=2, compression=15, timeframe=bt.TimeFrame.Minutes, fromdate=fromdate, todate=todate)

cerebro = bt.Cerebro()  # We initialize the `cerebro` backtester.

cerebro.broker.setcash(20000.0) # We set an initial trading capital of $20,000

cerebro.adddata(data) # We add the dataset in the Data cell.

cerebro.addstrategy(RSIStrategy) # We add the strategy described in the `Strategy class` cell


cerebro.broker.setcommission(commission=0.0075) # We set broker comissions of 0.075%

print('Starting Portfolio Value: {0:8.2f}'.format(cerebro.broker.getvalue()))
cerebro.run()
print('Final Portfolio Value: {0:8.2f}'.format(cerebro.broker.getvalue()))

cerebro.plot()
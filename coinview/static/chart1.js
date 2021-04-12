var ctx1 = LightweightCharts.createChart(document.getElementById('chart1'), {
	width: 1528,
  	height: 396,
	layout: {
		backgroundColor: '#ffffff',
		textColor: 'rgba(0, 0, 0, 0.9)',
	},
	grid: {
		vertLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
		horzLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	priceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
		timeVisible: true,
		secondsVisible: false,
	},
});


var candleSeries1 = ctx1.addCandlestickSeries({
	upColor: '#56B8B9',
	borderUpColor: 'rgba(86,184,185,1)',
	wickUpColor: 'rgba(86,184,185,1)',
	downColor: '#b95756', 
	borderDownColor: 'rgba(185,87,86,1)',
	wickDownColor: 'rgba(185,87,86,1)',
});


fetch('http://127.0.0.1:5000/history1')
	.then((r) => r.json())
	.then((response) => {
		candleSeries1.setData(response);
	})

var binanceSocket1 = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@kline_15m");

binanceSocket1.onmessage = function (event1) {	
	var message1 = JSON.parse(event1.data);

	var candlestick1 = message1.k;

    console.log(candlestick1)
    
	candleSeries1.update({
		time: candlestick1.t / 1000 + 7200,
		open: candlestick1.o,
		high: candlestick1.h,
		low: candlestick1.l,
		close: candlestick1.c
	})
}
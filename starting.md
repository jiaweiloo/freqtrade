freqtrade trade --logfile ./user_data/logs/freqtrade.log --db-url sqlite:///./user_data/tradesv3.sqlite --config ./user_data/config.json --strategy SampleStrategy

docker-compose run --rm freqtrade list-pairs --exchange binance --trading-mode spot > logs.txt
docker-compose run --rm freqtrade download-data --exchange binance -p BTC/USDT -t 1d --days 500 --trading-mode spot
docker-compose run --rm freqtrade download-data --exchange binance -p BTC/USDT -t 5m --days 500 --trading-mode spot
docker-compose run --rm freqtrade backtesting --strategy CTOLineStrategy --timerange=20200101-20201231
docker-compose run --rm freqtrade backtesting --strategy CTOLineStrategy --timeframe 1h
docker-compose run --rm freqtrade backtesting --strategy CTOLineStrategy --timeframe 1d
docker-compose run --rm freqtrade backtesting --strategy CTOLineStrategy --timeframe 5m --timerange=20200101-20240131
docker-compose run --rm freqtrade backtesting --strategy CTOLineStrategy --timeframe 1d --timerange=20200101-20240131



docker-compose run --rm freqtrade backtesting --strategy SampleStrategy --timeframe 1h
docker-compose restart freqtrade

docker-compose build
docker-compose up -d



docker-compose run --rm freqtrade backtesting --strategy SampleStrategy --timeframe 1h --timerange=20200101-20240131


docker-compose run --rm freqtrade download-data --exchange binance -p BTC/USDT -t 5m --days 500 --trading-mode spot

docker-compose run --rm freqtrade download-data --exchange binance -p BTC/USDT -t 5m --days 500 --trading-mode spot
docker-compose run --rm freqtrade download-data --exchange binance -p BTC/USDT ETH/USDT BNB/USDT XRP/USDT -t 5m 1h 1d --days 500 --trading-mode spot
docker-compose run --rm freqtrade download-data --exchange binance -p BTC/USDT ETH/USDT BNB/USDT XRP/USDT -t 5m 1h 1d --timerange=20200101-20240331 --trading-mode spot

docker-compose run --rm freqtrade backtesting --strategy CTOLineStrategy --timeframe 1d --timerange=20200101-20240331

docker-compose run --rm freqtrade plot-dataframe --strategy CTOLineStrategy --timeframe 1d --timerange=20240101-20240331

docker-compose run --rm freqtrade hyperopt --enable-protections --strategy CTOHyperoptStrategy -i 1d --hyperopt-loss SharpeHyperOptLoss -e 5000

docker-compose run --rm freqtrade backtesting --strategy Heracles --timeframe 1h --timerange=20240101-20240331


docker-compose run --rm freqtrade backtesting --strategy FixedRiskRewardLoss --timeframe 1h --timerange=20240101-20240331 --export trades

docker-compose run --rm freqtrade backtesting --strategy-list mabStra MultiMa PatternRecognition PowerTower Strategy001_custom_exit Strategy001 Strategy002 Strategy003 Strategy004 Strategy005 Supertrend SwingHighToSky UniversalMACD --timeframe 1h --timerange=20240101-20240331

docker-compose run --rm freqtrade download-data --exchange binance -p BTC/USDT -t 15m 30m --timerange=20200101-20240331 --trading-mode spot

docker-compose run --rm freqtrade trade --logfile ./user_data/logs/freqtrade.log --db-url sqlite:///./user_data/tradesv3.sqlite --config ./user_data/config.json --strategy PatternRecognition

docker-compose run --rm freqtrade backtesting --strategy PatternRecognition --timeframe 1h --timerange=20240101-20240331
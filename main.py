import src.data_loader as dl
import src.backtester as bt

TICKER = "TSLA"

prices = dl.pull_data(TICKER)
results = bt.vol_backtest(prices[TICKER])
print(results)
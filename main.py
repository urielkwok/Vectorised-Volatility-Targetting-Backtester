import src.data_loader as dl
import src.backtester as bt
import src.visualizer as vz

TICKER = "TSLA"

prices = dl.pull_data(TICKER)
results = bt.vol_backtest(prices[TICKER])
vz.create_plots(results)
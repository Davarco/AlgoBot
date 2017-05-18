from stock import Stock
from data import get_data
from visualize import graph_historical

# Constants
k = 1.5
num_days = 200
time_span = 300

# List that holds the data
stock_data = get_data("../input/company_backtest_list.txt")

# 2d arr, arr holds list of stocks throughout time span, each arr is a different stock
stock_data_list = []

# Go through backtest stocks
for key in stock_data:
    temp = []
    for start in range(0, time_span):
        temp.append(Stock(key, stock_data[key], k, start, num_days))
    stock_data_list.append(temp)

# Graph the historical data
graph_historical(stock_data_list)

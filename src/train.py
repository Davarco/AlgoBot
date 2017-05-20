from stock import Stock
from data import get_data
from visualize import graph_historical

# Constants
k = 1.5
num_days = 200
time_span = 300

# List that holds the data
stock_data = get_data("input/company_backtest_list.txt")

# 2d arr, arr holds list of stocks throughout time span, each arr is a different stock
stock_dict_list = []

# Go through backtest stocks
print("Testing algorithm on historical stock data...")
for key in stock_data:
    temp = []
    for start in range(time_span, 0, -1):
        temp.append(Stock(key, stock_data[key], k, start, num_days))
    stock_dict_list.append(temp)

# Go through all of the stock dictionaries
for stock_list in stock_dict_list:
    # Set if it should be buying (true) or selling (false), save results
    buy = True
    profit = 0
    price = 0
    total = 0
    num = 0
    day = 0
    ticker = stock_list[0].ticker
    # Go through all the stocks
    for stock in stock_list:
        # Get bands and current price
        upper = stock.upper_band
        lower = stock.lower_band
        today = stock.today_price
        # Buy stock if price is lower than lower band
        if today <= lower and buy:
            price += today
            total += today
            num += 1
            buy = False
        # Allow buying again after the lower peak
        if today > lower and not buy:
            buy = True
        # Sell stock if price is higher than upper band
        if today >= upper and num != 0:
            profit += (today*num - price)
            num = 0
            price = 0
            buy = True
        # Change to next day
        day += 1
    percent = 0
    if not profit == 0:
        percent = profit/total*100
    print("| %6s | %8.3f | %8.3f%% |" % (ticker, profit, percent), flush=True)

# Don't need all the graphs
# num_graphs = input("Number of graphs: ")
num_graphs = len(stock_dict_list)
temp_dict_list = [stock_dict_list[i] for i in range(0, int(num_graphs))]
graph_historical(temp_dict_list)

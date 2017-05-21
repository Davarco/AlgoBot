from stock import Stock
from data import retrieve_list
from datetime import datetime
from visualize import graph_historical
import pandas as pd
import os

# Constants
k = 1.5
num_days = 200
time_span = 300
LOG = "logs/"

init_moneys = 2000
moneys = init_moneys

# List that holds the data
stock_data = retrieve_list("input/companies/company_train_list.txt")

# 2d arr, arr holds list of stocks throughout time span, each arr is a different stock
stock_dict_list = []

# Go through backtest stocks
print("Testing algorithm on historical stock data...")
for key in stock_data:
    temp = []
    for start in range(time_span, 0, -1):
        temp.append(Stock(key, stock_data[key], k, start, num_days))
    stock_dict_list.append(temp)

# Prepare the pandas dataframe
df = pd.DataFrame(columns=['Ticker', 'Spent', 'Profit', 'Percent', 'K'])

# Create a new log file
path_dir = LOG + datetime.now().strftime("%m-%d-%Y")
if not os.path.exists(path_dir):
    os.makedirs(path_dir)
path = path_dir + "/" + datetime.now().strftime("%H:%M:%S")
print(path)
log = open(path, 'w')

# Go through all of the stock dictionaries
row = 0
for stock_list in stock_dict_list:
    # Set if it should be buying (true) or selling (false), save results
    buy = True
    profit = 0
    price = 0
    total = 0
    num = 0
    day = 0
    ticker = stock_list[0].ticker
    # Write title to log file
    log.write("-" * len(ticker) + "\n")
    log.write(ticker + "\n")
    log.write("-" * len(ticker) + "\n")
    # Go through all the stocks
    for stock in stock_list:
        # Get bands and current price
        upper = stock.upper_band
        lower = stock.lower_band
        today = stock.today_price
        # Buy stock if price is lower than lower band
        if today <= lower and buy:
            log.write("%-12s %-12s %-8.3f \n%-12s %-12s %-4.0f" % ("Buying!", "@price", today, "", "@day", day) + "\n")
            price += today
            total += today
            num += 1
            buy = False
        # Allow buying again after the lower peak
        if today > lower and not buy:
            log.write("%-12s" % "Resetting!" + "\n")
            buy = True
        # Sell stock if price is higher than upper band
        if today >= upper and num != 0:
            profit += (today*num - price)
            log.write("%-12s %-12s %-8.3f \n%-12s %-12s %-4.0f \n%-12s %-12s %-8.3f \n%-12s %-12s %-2s"
                      % ("Selling!", "@price", today, "", "@day", day, "", "@num_shares", profit, "", "@price", num) + "\n")
            num = 0
            price = 0
            buy = True
        # Change to next day
        day += 1
    # Calibrate moneys
    moneys += profit
    moneys -= total
    # Get the percent
    percent = 0
    if not profit == 0:
        percent = profit/total*100
    # Save data
    df.loc[row] = ['%5s' % ticker, '%8.3f' % total, '%8.3f' % profit, '%8.3f' % percent, '%4.1f' % k]
    # Increase the row
    row += 1
    log.write("\n")

# Print the backtested data
print(df)
df.to_csv(path + ".csv")

# Print moneys
if moneys > init_moneys:
    profit = moneys - init_moneys
    print("Start: %s. End: %s. Net profit: %s" % (init_moneys, moneys, profit))
if moneys < init_moneys:
    profit = init_moneys - moneys
    print("Start: %s. End: %s. Net loss: %s" % (init_moneys, moneys, profit))

# Don't need all the graphs
num_graphs = input("Graphs: ")
if num_graphs.lower() != "profitable":
    if num_graphs.lower() == "all":
        num_graphs = len(stock_dict_list)
    temp_dict_list = [stock_dict_list[i] for i in range(0, int(num_graphs))]
else:
    # Make sure something happened
    temp_dict_list = [stock_dict_list[i] for i in range(0, len(stock_dict_list)) if float(df.values[i, 1]) != 0]
graph_historical(temp_dict_list)

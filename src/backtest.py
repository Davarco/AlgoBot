from stock import Stock
from data import retrieve_list
from datetime import datetime
from visualize import graph_historical
from visualize import graph_historical_single
import pandas as pd
import numpy as np
import os

# Constants
k = 1.2
num_days = 200
time_span = 200
LOG = "logs/"


# Go through all of the stock dictionaries
def backtest(stock_dict_list, log):

    # Prepare the pandas dataframe
    df = pd.DataFrame(columns=['Ticker', 'Spent', 'Profit', 'Percent', 'K'])
    row = 0
    for stock_list in stock_dict_list:

        # Set if it should be buying (true) or selling (false), save results
        buy = True
        sell = False
        prev = 0
        profit = 0
        price = 0
        total = 0
        num = 0
        day = 1
        ticker = stock_list[0].ticker

        # Write title to log file
        log.write("-" * len(ticker) + "\n")
        log.write(ticker + "\n")
        log.write("-" * len(ticker) + "\n")

        # Go through all the stocks, each iteration represents one day
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

            # Allow selling after the first day the stock goes down
            if today > prev:
                sell = True

            # Set the previous to today
            prev = today

            # Sell stock if price is higher than upper band
            if today >= upper and num != 0 and sell:
                profit += (today*num - price)
                log.write("%-12s %-12s %-8.3f \n%-12s %-12s %-4.0f \n%-12s %-12s %-8.3f \n%-12s %-12s %-2s"
                          % ("Selling!", "@price", today, "", "@day", day, "", "@num_shares", num, "", "@profit", profit) + "\n")
                num = 0
                price = 0
                buy = True
                sell = False

            # Change to next day
            day += 1

        # Get the percent
        percent = 0
        if not profit == 0:
            percent = profit/total*100

        # Save data
        df.loc[row] = ['%5s' % ticker, '%8.3f' % total, '%8.3f' % profit, '%8.3f' % percent, '%4.1f' % k]

        # Increase the row
        row += 1
        log.write("\n")

    return df


def main():

    # List that holds the data
    stock_data = retrieve_list("input/companies/complete.txt")

    # 2d arr, arr holds list of stocks throughout time span, each arr is a different stock
    stock_dict_list = []

    # Go through backtest stocks
    print("Testing algorithm on historical stock data...")
    for key in stock_data:
        temp = []
        for start in range(time_span, 0, -1):
            temp.append(Stock(key, stock_data[key], k, start, num_days))
        stock_dict_list.append(temp)

    # Create a new log file
    path_dir = LOG + datetime.now().strftime("%m-%d-%Y")
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
    path = path_dir + "/" + datetime.now().strftime("%H_%M_%S")
    print(path + ".txt")
    log = open(path + ".txt", 'w')

    # Get the dataframe from the backtest
    df = backtest(stock_dict_list, log)

    # Print the backtested data
    print(df)
    df.to_csv(path + ".csv")

    # Store final results
    num_profitable = 0
    num_unprofitable = 0
    for i in range(0, len(stock_dict_list)):
        if float(df.values[i, 2]) > 0:
            num_profitable += 1
        elif float(df.values[i, 2]) < 0:
            num_unprofitable += 1
    log.write("Profitable: " + str(num_profitable) + "\n")
    log.write("Unprofitable: " + str(num_unprofitable))

    # Don't need all the graphs
    num_graphs = input("Graphs: ")
    if num_graphs.lower() == "active":

        # Make sure something happened
        temp_dict_list = [stock_dict_list[i] for i in range(0, len(stock_dict_list)) if float(df.values[i, 1]) != 0]

    elif num_graphs.lower() == "profitable":

        # Make sure the graphs were profitable
        temp_dict_list = [stock_dict_list[i] for i in range(0, len(stock_dict_list)) if float(df.values[i, 2]) > 0]

    elif num_graphs.lower() == "unprofitable":

        # Make sure the graphs were unprofitable
        temp_dict_list = [stock_dict_list[i] for i in range(0, len(stock_dict_list)) if float(df.values[i, 1]) < 0]

    elif num_graphs.lower() == "all":

        # Get all the graphs
        num_graphs = len(stock_dict_list)
        temp_dict_list = [stock_dict_list[i] for i in range(0, int(num_graphs))]

    elif num_graphs.lower() == "max":

        # Get the most profitable
        max_stock = stock_dict_list[0]
        max_percent = 0.0
        for i in range(0, len(stock_dict_list)):
            if float(df.values[i, 3]) > max_percent:
<<<<<<< HEAD
                max_percent = float(df.values[i, 3])    
=======
                max_percent = float(df.values[i, 3])
>>>>>>> vs
                max_stock = stock_dict_list[i]

        # Print the max percent
        print("Max percent: " + str(max_percent))

        # Only graph one stock
        graph_historical_single(max_stock)
        return

    else:

        # Get the correct number of graphs
        temp_dict_list = [stock_dict_list[i] for i in range(0, int(num_graphs)) if stock_dict_list[i].ticker == num_graphs.upper()]

    graph_historical(temp_dict_list)

    # Get the net percent
    net_percent = np.sum(float(i) for i in df.values[:, 3] if float(i) > 0)
    print("Net percent: %6.3f" % net_percent)


if __name__ == '__main__':
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> vs

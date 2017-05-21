from stock import Stock
from data import retrieve_list
import pandas as pd

# Constants
k = 1.5
num_days = 200
time_span = 1000

init_moneys = 2000

# Prepare the pandas dataframe
df = pd.DataFrame(columns=['Ticker', 'Spent', 'Profit', 'Percent', 'K'])


def run_sim(stock_list: list, row: int, func_moneys: int):
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
    # Calibrate moneys
    func_moneys += profit
    # Get the percent
    percent = 0
    if not profit == 0:
        percent = profit/total*100
    # Save data
    df.loc[row] = ['%5s' % ticker, '%8.3f' % total, '%8.3f' % profit, '%8.3f' % percent, '%4.1f' % k]

    return func_moneys


def __main__():
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

    # Go through all of the stock dictionaries
    row = 0
    for stock_list in stock_dict_list:
        # Set if it should be buying (true) or selling (false), save results
        final_moneys = run_sim(stock_list, row, init_moneys)

        # Print moneys
        if final_moneys > init_moneys:
            profit = final_moneys - init_moneys
            moneys += profit
        elif final_moneys < init_moneys:
            loss = init_moneys - final_moneys
            moneys -= loss

        # Increase the row
        row += 1

    # Print the simulation result
    print(df)

    print("Started with %s moneys. Ended with %s moneys." % (init_moneys, moneys))

__main__()
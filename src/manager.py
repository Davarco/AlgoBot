from stock import Stock
from data import retrieve_list
import pandas as pd

# Constants
k = 1.5
num_days = 200
time_span = 300
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
    # List that holds the data
    stock_data = retrieve_list("input/companies/company_train_list.txt")

    # 2d arr, arr holds list of stocks throughout time span, each arr is a different stock
    stock_dict_list = []

    init_moneys = int(input("Moneys: "))
    moneys = init_moneys

    # Go through backtest stocks
    for key in stock_data:
        stock_dict_list.append(Stock(key, stock_data[key], k, 0, num_days))

    buyables = []

    stock_dict_list[-1].today_price = 5
    stock_dict_list[-1].today_lower_diff = stock_dict_list[-1].lower_band - stock_dict_list[-1].today_price

    stock_dict_list[-2].today_price = 5
    stock_dict_list[-2].today_lower_diff = stock_dict_list[-2].lower_band - stock_dict_list[-2].today_price

    for stock in stock_dict_list:
        if stock.today_lower_diff > 0 and stock.today_price < moneys:
            buyables.append(stock)

    buyables = sorted(buyables, key=lambda stock_sorting: stock_sorting.today_lower_diff, reverse=True)

    if buyables.__len__() < 1:
        print("Don't buy stocks today. You either can't afford them or they're not in a good condition.")
    else:
        for buyable in buyables:
            if moneys <= 0:
                break
            num = 0
            while moneys > 0:
                moneys -= buyable.today_price
                num += 1

            if moneys < 0:
                moneys += buyable.today_price
                num -= 1

            print("Buy %s stocks from ticker %s. Today's price is %.2f moneys, and you have %.2f moneys. You will have %.2f moneys left." % (num, buyable.ticker, buyable.today_price, init_moneys, moneys))
            init_moneys = moneys

__main__()
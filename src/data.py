import requests
import pandas
import io
import os


# Returns list of data (pandas dataframes)
def retrieve(path):

    # Constants for downloading data
    cache = "cache"
    start_month = "Jan"
    start_day = "01"
    start_year = "2010"
    title_date = start_month + "-" + start_day + "-" + start_year

    # List of companies
    company_data_list = {}
    company_list = open(path)
    print("Getting stock ticker list...")

    for name in company_list:
        # Get data from google finance url
        name = name.strip()
        # print("Getting data from %s..." % name)
        # Use cache data if exists, otherwise download
        path = cache + "/" + name + "_" + title_date + ".csv"
        if os.path.exists(path):
            # print("Data already exists in cache.")
            data = pandas.read_csv(path)
        else:
            # print("Data does not already exist, adding to cache.")
            url = "https://www.google.com/finance/historical?q=NASDAQ:" + name + \
                  "&startdate=" + start_month + "+" + start_day + "%2C+" + start_year + "&output=csv"
            raw_data = requests.get(url).content
            with open(path, 'wb') as f:
                f.write(raw_data)
            data = pandas.read_csv(io.StringIO(raw_data.decode('utf-8')))
        # Create dictionary pair with the data
        company_data_list[name] = data

    return company_data_list


def generate():

    # Constants
    k = 1.5
    num_days = 200
    time_span = 1000

    # List that holds the data
    stock_data = retrieve("input/companies/company_train_list.txt")

    # 2d arr, arr holds list of stocks throughout time span, each arr is a different stock
    stock_dict_list = []

    # Go through backtest stocks
    print("Testing algorithm on historical stock data...")
    for key in stock_data:
        temp = []
        for start in range(time_span, 0, -1):
            temp.append(Stock(key, stock_data[key], k, start, num_days))
        stock_dict_list.append(temp)

    # Create the csv file to be written to (k, percent)
    csv_name = "input/bollinger_constant.txt"
    csv = open(csv_name, 'a')

    # Go through all of the stock dictionaries
    for stock_list in stock_dict_list:
        # Set if it should be buying (true) or selling (false), save results
        buy = True
        profit = 0
        price = 0
        total = 0
        num = 0
        day = 0
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
                profit += (today * num - price)
                num = 0
                price = 0
                buy = True
            # Change to next day
            day += 1
        # percent = 0
        if not profit == 0:
            percent = profit / total * 100
            csv.write(str(k) + "," + str(round(percent, 3)) + "\n")

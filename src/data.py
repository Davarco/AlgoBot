import requests
import pandas
import numpy
import time
import io
import os


# Returns a single piece of data (pandas dataframes)
def retrieve_single(ticker):

    # Constants for downloading data
    cache = "cache"
    start_month = "Jan"
    start_day = "01"
    start_year = "2010"
    title_date = start_month + "-" + start_day + "-" + start_year

    # Get the stock data from google finance
    print("Getting stock ticker list...")
    ticker = ticker.strip()
    path = cache + "/" + ticker + "_" + title_date + "_" + time.strftime("%d-%m-%Y") + ".csv"
    if os.path.exists(path):
        data = pandas.read_csv(path)
    else:
        url = "https://www.google.com/finance/historical?q=NASDAQ:" + ticker + \
              "&startdate=" + start_month + "+" + start_day + "%2C+" + start_year + "&output=csv"
        raw_data = requests.get(url).content
        with open(path, 'wb') as f:
            f.write(raw_data)
        data = pandas.read_csv(io.StringIO(raw_data.decode('utf-8')))

    return data


# Returns list of data (pandas dataframes)
def retrieve_list(path):

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
        path = cache + "/" + name + "_" + title_date + "_" + time.strftime("%d-%m-%Y") + ".csv"
        if os.path.exists(path):
            data = pandas.read_csv(path)
        else:
            url = "https://www.google.com/finance/historical?q=NASDAQ:" + name + \
                  "&startdate=" + start_month + "+" + start_day + "%2C+" + start_year + "&output=csv"
            raw_data = requests.get(url).content
            with open(path, 'wb') as f:
                f.write(raw_data)
            data = pandas.read_csv(io.StringIO(raw_data.decode('utf-8')))

        # Create dictionary pair with the data
        company_data_list[name] = data

    return company_data_list


# Generate data for training
def gen():

    # Constants for downloading data
    cache = "cache"
    start_month = "Jan"
    start_day = "01"
    start_year = "2010"
    title_date = start_month + "-" + start_day + "-" + start_year
    train_path = "input/train.csv"
    train_csv = open(train_path, "w+")

    # List of companies
    company_list = open("input/complete.txt")
    print("Getting stock ticker list...")

    for name in company_list:

        # Get data from google finance url
        name = name.strip()
        path = cache + "/" + name + "_" + title_date + "_" + time.strftime("%d-%m-%Y") + ".csv"
        if os.path.exists(path):
            df = pandas.read_csv(path)
        else:
            url = "https://www.google.com/finance/historical?q=NASDAQ:" + name + \
                  "&startdate=" + start_month + "+" + start_day + "%2C+" + start_year + "&output=csv"
            raw_data = requests.get(url).content
            with open(path, 'wb') as f:
                f.write(raw_data)
            df = pandas.read_csv(io.StringIO(raw_data.decode('utf-8')))
        df = df.iloc[::-1]
        print(df)

        # Create new csv with the data
        prices = numpy.array(df['Close'])
        # print(prices)

        # Append to new csv
        data = open(train_path, "a")
        row = len(prices)
        for i in range(200, row-100):

            # Parse data
            curr_200 = prices[i]/prices[i-200:i].mean()
            curr_100 = prices[i]/prices[i-100:i].mean()
            curr_50 = prices[i]/prices[i-50:i].mean()
            future = prices[i+100]

            # Write to file
            num = 0
            if future > prices[i]:
                num = 1

            # Write to csv
            data.write(str(num) + "," + str(curr_200) + "," + str(curr_100) + "," + str(curr_50) + "\n")


if __name__ == '__main__':
    gen()

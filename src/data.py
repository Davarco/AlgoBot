from stock import Stock
import numpy as np
import requests
import pandas
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
    path = cache + "/" + ticker + "_" + title_date + ".csv"
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
        path = cache + "/" + name + "_" + title_date + ".csv"
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

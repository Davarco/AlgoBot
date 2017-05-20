import requests
import pandas
import io
import os

# List of companies
company_data_list = {}

# Constants for downloading data
CACHE = "cache"
start_month = "Jan"
start_day = "01"
start_year = "2010"
title_date = start_month + "-" + start_day + "-" + start_year


def init(path):
    company_list = open(path)
    for name in company_list:
        # Get data from google finance url
        name = name.strip()
        print("Getting data from %s..." % name)
        # Use cache data if exists, otherwise download
        path = CACHE + "/" + name + "_" + title_date + ".csv"
        if os.path.exists(path):
            print("Data already exists in cache.")
            data = pandas.read_csv(path)
        else:
            print("Data does not already exist, adding to cache.")
            url = "https://www.google.com/finance/historical?q=NASDAQ:" + name + \
                  "&startdate=" + start_month + "+" + start_day + "%2C+" + start_year + "&output=csv"
            raw_data = requests.get(url).content
            with open(path, 'wb') as f:
                f.write(raw_data)
            data = pandas.read_csv(io.StringIO(raw_data.decode('utf-8')))
        # Create dictionary pair with the data
        company_data_list[name] = data


# Returns list of data (pandas dataframes)
def get_data(path):
    init(path)
    return company_data_list
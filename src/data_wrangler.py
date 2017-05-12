from yahoo_finance import Share
import numpy as np
import scipy as sp
import pandas as pd

# Hold list of companies
share_list = []


# Get the list of companies
def init():
    company_list_file = open("../input/company_list.txt", "r")
    for name in company_list_file:
        share_list.append(Share(name))


# Find deviations
def main():
    init()
    for share in share_list:
        get_historical_data(share)


def get_historical_data(share):
    print("Share: ", share.get_name())
    date_range = pd.date_range('2017-01-01', '2017-05-01')
    for date in date_range:
        str_date = str(date.strftime("%Y-%m-%d"))
        print(str_date)


def calc_diff_200(share):
    percent = round((float(share.get_price())-float(share.get_200day_moving_avg()))/(float(share.get_price()))*100, 2)
    return percent


def calc_diff_50(share):
    percent = round((float(share.get_price())-float(share.get_50day_moving_avg()))/(float(share.get_price()))*100, 2)
    return percent


main()

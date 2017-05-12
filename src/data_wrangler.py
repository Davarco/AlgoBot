from yahoo_finance import Share
from pprint import pprint
import datetime
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
        print()


def get_historical_data(share):
    print(share.get_name())
    date_range = pd.date_range('2017-04-28', '2017-05-01')
    for date in date_range:
        start_date = str(date.strftime("%Y-%m-%d"))
        get_historical_avg(share, start_date)


def get_historical_avg(share, start_date):
    # 200 day avg
    total_200 = 0
    for i in range(0, 5):
        # Get the curr day and prev
        curr_temp = ((datetime.datetime.strptime(start_date, '%Y-%m-%d') - datetime.timedelta(i)).isoformat())
        prev_temp = ((datetime.datetime.strptime(start_date, '%Y-%m-%d') - datetime.timedelta(i+1)).isoformat())
        curr_date = str(curr_temp)[0:10]
        prev_date = str(prev_temp)[0:10]
        # Get the price
        print(prev_date)
        print(curr_date)
        print(share.get_historical())


def calc_diff_200(share):
    percent = round((float(share.get_price())-float(share.get_200day_moving_avg()))/(float(share.get_price()))*100, 2)
    return percent


def calc_diff_50(share):
    percent = round((float(share.get_price())-float(share.get_50day_moving_avg()))/(float(share.get_price()))*100, 2)
    return percent


main()

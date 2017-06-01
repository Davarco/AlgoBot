import requests
import pandas
import numpy
import time
import io
import os


# Generate data for training
def gen():

    # Constants for downloading data
    cache = "cache"
    start_month = "Jan"
    start_day = "01"
    start_year = "2010"
    future_interval = 100
    percent_test = 0.3
    title_date = start_month + "-" + start_day + "-" + start_year
    train_path = "input/train.csv"
    test_path = "input/test.csv"
    train_csv = open(train_path, "w+")
    test_csv = open(test_path, "w+")

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

        # Create new csv with the data
        prices = numpy.array(df['Close'])
        # print(prices)

        # Append to new csv
        row = len(prices)
        num_test = int(row * percent_test)
        for i in range(200, row-future_interval-num_test):

            # Parse data
            curr_200 = prices[i]/prices[i-200:i].mean()
            curr_100 = prices[i]/prices[i-100:i].mean()
            curr_50 = prices[i]/prices[i-50:i].mean()
            future = prices[i+future_interval]

            # Write to file
            num = 0
            if future > prices[i]:
                num = 1

            # Write to csv
            train_csv.write(str(curr_200) + "," + str(curr_100) + "," + str(curr_50) + "," + str(num) + "\n")

        # Append to test csv as well
        for i in range(row-future_interval-num_test, row-future_interval):

            # Parse data
            curr_200 = prices[i] / prices[i - 200:i].mean()
            curr_100 = prices[i] / prices[i - 100:i].mean()
            curr_50 = prices[i] / prices[i - 50:i].mean()
            future = prices[i + future_interval]

            # Write to file
            num = 0
            if future > prices[i]:
                num = 1

            # Write to csv
            test_csv.write(str(curr_200) + "," + str(curr_100) + "," + str(curr_50) + "," + str(num) + "\n")


if __name__ == '__main__':
    gen()

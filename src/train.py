from stock import Stock
from data import retrieve_list
from datetime import datetime
import os

# Constants
k = 1.2
num_days = 200
time_span = 300
LOG = "logs/"


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

    # Get the file name
    path_dir = LOG + datetime.now().strftime("%m-%d-%Y")
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
    path = path_dir + "/" + datetime.now().strftime("%H_%M_%S")
    print(path + ".txt")
    log = open(path + ".txt", 'w')


if __name__ == '__main__':
    main()

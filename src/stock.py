import numpy as np


class Stock(object):

    # Important data for bollinger bands
    ticker = ""
    mean_price = 0
    deviation = 0

    def __init__(self, tick, data_list):
        price_list = np.array([float(data['Close']) for data in data_list])
        mean_price = price_list.mean()
        deviation = price_list.std()
        ticker = tick
        print("Ticker: ", ticker)
        print("Mean price: ", mean_price)
        print("Deviation: ", deviation)
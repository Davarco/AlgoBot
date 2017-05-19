import pandas as pd
import numpy as np


class Stock(object):

    ticker = ""
    num_days = 0
    mean_price = 0
    today_price = 0
    deviation = 0
    upper_band = 0
    lower_band = 0

    def __str__(self):
        return "\nTicker: " + self.ticker + "\nStd Deviation: " + str(self.deviation) + "\nMean Price: " + str(self.mean_price) + \
               "\nUpper Band: " + str(self.upper_band) + "\nLower Band: " + str(self.lower_band) + \
               "\nToday Price: " + str(self.today_price) + "\nDays: " + str(self.num_days)

    def __init__(self, ticker, data, k, start, num_days):
        prices = np.array(data.iloc[start:start+num_days, 4].values)
        self.ticker = ticker
        self.num_days = num_days
        self.mean_price = prices.mean()
        self.today_price = prices[0]
        self.deviation = prices.std()
        self.upper_band = self.mean_price + k*self.deviation
        self.lower_band = self.mean_price - k*self.deviation

import pandas as pd
import numpy as np


class Stock(object):

    ticker = ""
    k = 0
    num_days = 0
    mean_price = 0
    today_price = 0
    deviation = 0
    upper_band = 0
    lower_band = 0
    upper_band_diff = 0
    lower_band_diff = 0
    ma_200 = 0
    ma_50 = 0
    yest_price = 0

    def __str__(self):
        return "\nTicker: " + self.ticker + "\nStd Deviation: " + str(self.deviation) + "\nMean Price: " + str(self.mean_price) + \
               "\nUpper Band: " + str(self.upper_band) + "\nLower Band: " + str(self.lower_band) + \
               "\nToday Price: " + str(self.today_price) + "\nDays: " + str(self.num_days)

    def __init__(self, ticker, data, k, start, num_days):

        # Use numpy array to get features
        prices = np.array(data.iloc[start:start+num_days, 4].values)
        self.k = k
        self.ticker = ticker
        self.num_days = num_days
        self.mean_price = prices.mean()
        self.today_price = prices[0]
        self.yest_price = prices[1]
        self.deviation = prices.std()

        # Calculate the upper and lower band
        self.upper_band = self.mean_price + k*self.deviation
        self.lower_band = self.mean_price - k*self.deviation
        self.lower_band_diff = (self.lower_band - self.today_price) / self.today_price
        self.upper_band_diff = (self.today_price - self.upper_band) / self.today_price

        # Get the 200 and 50 day moving averages
        self.ma_200 = prices[0:200].mean()
        self.ma_50 = prices[0:50].mean()

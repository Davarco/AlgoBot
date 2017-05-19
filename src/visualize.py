import pylab as plt
import pandas as pd


def graph_historical(stock_data_list):
    # Go through all of the stocks
    for stock in stock_data_list:
        # Get the upper, lower, and price band, and curr
        upper_band = pd.DataFrame([item.upper_band for item in stock])
        lower_band = pd.DataFrame([item.lower_band for item in stock])
        price_band = pd.DataFrame([item.mean_price for item in stock])
        today_band = pd.DataFrame([item.today_price for item in stock])
        # Set index columns
        upper_band.insert(0, 'day', upper_band.index+1)
        lower_band.insert(0, 'day', lower_band.index+1)
        price_band.insert(0, 'day', price_band.index+1)
        today_band.insert(0, 'day', today_band.index+1)
        # Plot graphs
        plt.figure()
        plt.plot(upper_band.values[:, 0], upper_band.values[:, 1], color="green")
        plt.plot(lower_band.values[:, 0], lower_band.values[:, 1], color="red")
        plt.plot(price_band.values[:, 0], price_band.values[:, 1], color="blue")
        plt.plot(today_band.values[:, 0], today_band.values[:, 1], color="black")
        plt.xlabel("Day")
        plt.ylabel("Price")
        plt.title(stock[0].ticker + ": Simple Mean Reversion")
        # plt.ylim(ymin=0)
        plt.draw()
    plt.show()

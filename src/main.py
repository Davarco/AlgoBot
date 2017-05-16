from src.data_wrangler import get_data
from src.stock import Stock

# Data holding the info for bands
stock_data_dict = {}


def init():
    # Get data from data_wrangler
    stock_data = get_data()
    # Create stocks from the data
    for key in stock_data:
        stock_data_dict[key] = Stock(stock_data[key])


def main():
    init()

main()

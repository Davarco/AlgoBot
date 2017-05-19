from stock import Stock
from data import get_data


# Constants
k = 1.5
start = 0
num_days = 200

# List that holds the data
stock_data = get_data("input/company_list.txt")

# Create stock list from data
stock_list = []
for key in stock_data:
    stock_list.append(Stock(key, stock_data[key], k, start, num_days))

# Print calculated results
for stock in stock_list:
    print(stock)

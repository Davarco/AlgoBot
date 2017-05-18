from stock import Stock
from data import get_data


# Bollinger band constant
k = 1.5

# List that holds the data
stock_data = get_data()

# Create stock list from data
stock_list = []
for key in stock_data:
    stock_list.append(Stock(key, stock_data[key], k))

# Print calculated results
for stock in stock_list:
    print(stock)
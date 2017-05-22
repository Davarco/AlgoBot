from stock import Stock
from data import retrieve_list

# Constants
k = 1.5
num_days = 200
time_span = 300

def __main__():
    # List that holds the data
    stock_data = retrieve_list("input/companies/company_train_list.txt")

    # 2d arr, arr holds list of stocks throughout time span, each arr is a different stock
    stock_dict_list = []

    # Go through backtest stocks
    for key in stock_data:
        stock_dict_list.append(Stock(key, stock_data[key], k, 0, num_days))

    sellables = sorted(stock_dict_list, key=lambda stock_sorting: stock_sorting.today_lower_diff, reverse=True)

    sale_ticker = str(input("Ticker to advise: "))
    stock = None

    for sellable in sellables:
        if sellable.ticker == sale_ticker.upper():
            stock = sellable
            break

    if stock == None:
        print("Ticker not found!")
        return

    if stock.today_upper_diff <= 0:
        print("WARNING: Today's price is %.2f below the upper band, so your sale is based solely on profitability." % abs(stock.today_upper_diff))
    else:
        print("Good news! Today's price is %.2f moneys above the upper band!" % stock.today_upper_diff)

    print("%s stocks: %.2f moneys today." % (stock.ticker, stock.today_price))
    purchase_price = float(input("How much did you buy these stocks for? "))
    if purchase_price == 0:
        print("Doubtful...")
        return
    elif purchase_price > stock.today_price:
        print("Don't sell these stocks today.")
        return

    num = int(input("How many are you looking to sell? "))
    if num == 0:
        print("Then stop wasting my time!")
        return

    if purchase_price > stock.today_price:
        loss = (stock.today_price - purchase_price) * num
        print("Don't sell these stocks today. You'll lose %.2f moneys!" % loss)
    else:
        profit = (stock.today_price - purchase_price) * num
        print("Sell 'em! You'll make %.2f moneys in profit!" % profit)

__main__()
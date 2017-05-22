from stock import Stock
from data import retrieve_list

# Constants
k = 1.5
num_days = 200
time_span = 300
init_moneys = 2000

def __main__():
    # List that holds the data
    stock_data = retrieve_list("input/companies/complete.txt")

    # 2d arr, arr holds list of stocks throughout time span, each arr is a different stock
    stock_dict_list = []

    init_moneys = int(input("Moneys: "))
    moneys = init_moneys

    # Go through backtest stocks
    for key in stock_data:
        stock_dict_list.append(Stock(key, stock_data[key], k, 0, num_days))

    buyables = sorted(stock_dict_list, key=lambda stock_sorting: stock_sorting.today_lower_diff, reverse=True)

    if buyables.__len__() < 1 or buyables[0].today_lower_diff < 0:
        print("Don't buy stocks today. You either can't afford them or they're not in a profitable condition.")
    else:
        print()
        print("FIRST STOCK -- SPENDING 50% MONEYS")
        buy = buyables[0]
        spendable = init_moneys / 2

        before_spending = moneys

        num = 0
        spent = 0

        while spent < spendable:
            moneys -= buy.today_price
            spent += buy.today_price
            num += 1

        if spent > spendable:
            moneys += buy.today_price
            spent -= buy.today_price
            num -= 1

        while moneys < 0:
            moneys += buy.today_price
            spent -= buy.today_price
            num -= 1

        print("Buy %s stocks from ticker %s. Today's price is %.2f moneys, and you have %.2f moneys. "
              "You will have %.2f moneys left." %
              (num, buy.ticker, buy.today_price, before_spending, moneys))

        print()
        print("SECOND STOCK -- SPENDING 25% MONEYS")
        buy = buyables[1]
        spendable = init_moneys / 4

        before_spending = moneys

        num = 0
        spent = 0

        while spent < spendable:
            moneys -= buy.today_price
            spent += buy.today_price
            num += 1

        if spent > spendable:
            moneys += buy.today_price
            spent -= buy.today_price
            num -= 1

        while moneys < 0:
            moneys += buy.today_price
            spent -= buy.today_price
            num -= 1

        print("Buy %s stocks from ticker %s. Today's price is %.2f moneys, and you have %.2f moneys. "
              "You will have %.2f moneys left." %
              (num, buy.ticker, buy.today_price, before_spending, moneys))

        print()
        print("THIRD STOCK -- SPENDING 25% MONEYS")
        buy = buyables[2]
        spendable = init_moneys / 4

        before_spending = moneys

        num = 0
        spent = 0

        while spent < spendable:
            moneys -= buy.today_price
            spent += buy.today_price
            num += 1

        if spent > spendable:
            moneys += buy.today_price
            spent -= buy.today_price
            num -= 1

        while moneys < 0:
            moneys += buy.today_price
            spent -= buy.today_price
            num -= 1

        print("Buy %s stocks from ticker %s. Today's price is %.2f moneys, and you have %.2f moneys. "
              "You will have %.2f moneys left." %
              (num, buy.ticker, buy.today_price, before_spending, moneys))

        init_moneys = moneys

        print()
        print("FURTHER STOCKS -- SPENDING AS MUCH MONEYS AS POSSIBLE")
        for i in range(3, buyables.__len__()):
            if moneys < 1:
                break

            buyable = buyables[i]
            num = 0

            while moneys > 0:
                moneys -= buyable.today_price
                num += 1

            if moneys < 0:
                moneys += buyable.today_price
                num -= 1

            print("Buy %s stocks from ticker %s. Today's price is %.2f moneys, and you have %.2f moneys. "
                  "You will have %.2f moneys left." %
                  (num, buyable.ticker, buyable.today_price, init_moneys, moneys))

            init_moneys = moneys

__main__()
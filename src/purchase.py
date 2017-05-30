from stock import Stock
from data import retrieve_list

# Constants
k = 1.5
num_days = 200
time_span = 300


def main():

    # List that holds the data
    stock_data = retrieve_list("input/companies/complete.txt")

    # 2d arr, arr holds list of stocks throughout time span, each arr is a different stock
    stock_dict_list = []

    init_money = int(input("Initial: "))
    money = init_money

    # Go through backtest stocks
    for key in stock_data:
        stock_dict_list.append(Stock(key, stock_data[key], k, 0, num_days))

    buyables = sorted(stock_dict_list, key=lambda stock_sorting: stock_sorting.lower_band_diff, reverse=True)

    if buyables.__len__() < 1 or buyables[0].lower_band_diff < 0:
        print("Don't buy stocks today. You either can't afford them or they're not in a profitable condition.")
    else:
        print()
        print("FIRST STOCK -- SPENDING 50%!")
        buy = buyables[0]
        spendable = init_money / 2

        before_spending = money

        num = 0
        spent = 0.0

        while spent < spendable:
            money -= buy.today_price
            spent += buy.today_price
            num += 1

        if spent > spendable:
            money += buy.today_price
            spent -= buy.today_price
            num -= 1

        while money < 0:
            money += buy.today_price
            spent -= buy.today_price
            num -= 1

        if num > 0:
            print("Buy %s stocks from ticker %s. Today's price is %.2f, and you have %.2f. "
                  "You will have %.2f left." %
                  (num, buy.ticker, buy.today_price, before_spending, money))

        print()
        print("SECOND STOCK -- SPENDING 25%!")
        buy = buyables[1]
        spendable = init_money / 4

        before_spending = money

        num = 0
        spent = 0.0

        while spent < spendable:
            money -= buy.today_price
            spent += buy.today_price
            num += 1

        if spent > spendable:
            money += buy.today_price
            spent -= buy.today_price
            num -= 1

        while money < 0:
            money += buy.today_price
            spent -= buy.today_price
            num -= 1

        if num > 0:
            print("Buy %s stocks from ticker %s. Today's price is %.2f, and you have %.2f. "
                  "You will have %.2f left." %
                  (num, buy.ticker, buy.today_price, before_spending, money))

        print()
        print("THIRD STOCK -- SPENDING 25% money")
        buy = buyables[2]
        spendable = init_money / 4

        before_spending = money

        num = 0
        spent = 0.0

        while spent < spendable:
            money -= buy.today_price
            spent += buy.today_price
            num += 1

        if spent > spendable:
            money += buy.today_price
            spent -= buy.today_price
            num -= 1

        while money < 0:
            money += buy.today_price
            spent -= buy.today_price
            num -= 1

        if num > 0:
            print("Buy %s stocks from ticker %s. Today's price is %.2f, and you have %.2f. "
                  "You will have %.2f left." %
                  (num, buy.ticker, buy.today_price, before_spending, money))

        print("\nDone! Keep the remainder of your money.")

        # print("FURTHER STOCKS -- SPENDING AS MUCH money AS POSSIBLE")
        # for i in range(3, buyables.__len__()):
        #     if money < 1:
        #         break
        #
        #     buyable = buyables[i]
        #     num = 0
        #
        #     while money > 0:
        #         money -= buyable.today_price
        #         num += 1
        #
        #     if money < 0:
        #         money += buyable.today_price
        #         num -= 1
        #
        #     if num > 0:
        #         print("Buy %s stocks from ticker %s. Today's price is %.2f money, and you have %.2f money. "
        #               "You will have %.2f money left." %
        #               (num, buyable.ticker, buyable.today_price, init_money, money))
        #
        #     init_money = money

if __name__ == '__main__':
    main()

import json
from yahoo_finance import Share
from datetime import *

def isweekend(year, month, day):
    try:
        if (datetime(year,month,day).weekday() > 4):
            return True
        else:
            return False
    except:
        return True

def beforetoday(year, month, day):
    try:
        if (datetime.today().day == day and datetime.today().month == month and datetime.today().year == year):
            return False
        else:
            return True
    except:
        return True

counter = 0

tickers = ['UAL', 'AAPL', 'AMZN', 'BABA', 'CVX', 'GOOG', 'MSFT', 'VEEV']
stocklist = []

for ticker in tickers:
    yahoo = Share(ticker)
    currentstock = []

    for month in range(1, 12):
        for day in range(1, 31):

            if not beforetoday(2017, month, day):
                continue

            if not isweekend(2017, month, day):
                try:
                    jdata = yahoo.get_historical('2017-' + str(month) + '-' + str(day), '2017-' + str(month) + '-' + str(day))
                    jdata = jdata[0]

                    currentstock.append(jdata)

                    symbol = jdata['Symbol']
                    date = jdata['Date']
                    open = jdata['Open']
                    high = jdata['High']
                    low = jdata['Low']
                    close = jdata['Close']
                    volume = jdata['Volume']
                    # adjclose = jdata['Adj_Close']

                    # print("TODAY IS " + str(date) + ". WE ARE TRACKING " + symbol + ".")
                    # print("Open: " + open + "; High: " + high)
                    # print("Low: " + low + "; Close: " + close)
                    # print("Volume: " + volume + ".")
                    # print("==========================================================================")

                    counter += 1
                except:
                    continue

    stocklist.append(currentstock)

    print("PRINTED " + str(counter) + " OBJECTS FOR " + ticker)
    counter = 0

print("REPORTED " + str(stocklist.__sizeof__()) + " STOCKS.")

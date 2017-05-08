import urllib.request, json

for x in range(0, 1):
    baseurl = "http://query.yahooapis.com/v1/public/yql?q=%20select%20*%20from%20yahoo.finance.historicaldata%20where%20symbol%20=%20%22"
    ticker = "AAPL"
    startdaterequest = "%22%20and%20startDate%20=%20%22"
    startdate = "2014-09-11"
    enddaterequest = "%22%20and%20endDate%20=%20%22"
    enddate = "2014-09-11"
    extras = "%22%20&format=json%20&diagnostics=true%20&env=store://datatables.org/alltableswithkeys%20&callback="

    with urllib.request.urlopen(baseurl + ticker + startdaterequest + startdate + enddaterequest + enddate + extras) as url:
        data = json.loads(url.read().decode())['query']['results']['quote']

        print("Stock Symbol: ", data['Symbol'])
        print("Date in Question: ", data['Date'])
        print("Open: ", data['Open'])
        print("High: ", data['High'])
        print("Low: ", data['Low'])
        print("Close: ", data['Close'])
        print("Volume: ", data['Volume'])
        print("Adj Close: ", data['Adj_Close'])
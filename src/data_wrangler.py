from yahoo_finance import Share


# List of companies
company_list = ['YHOO', 'BABA', 'AMZN', 'CVX', 'GOOGL', 'MSFT', 'VEEV']
share_list = []


def init():
    for name in company_list:
        share = Share(name).get_historical('2017-01-01', '2017-05-01')
        share_list.append(share)


def get_data():
    init()
    return share_list


from yahoo_finance import Share


# List of companies
company_list = ['YHOO', 'BABA']
share_list = {}


def init():
    for name in company_list:
        print("Getting data from", name, "...")
        share = Share(name).get_historical('2016-05-01', '2017-05-01')
        share_list[name] = share


def get_data():
    init()
    return share_list


import requests
import pandas
import io

# List of companies
company_data_list = {}


def init():
    company_list = open("input/company_list.txt")
    for name in company_list:
        # Get data from google finance url
        name = name.strip()
        print("Getting data from %s..." % name)
        url = "https://www.google.com/finance/historical?q=NASDAQ:" + name + "&startdate=Jan+01%2C+2010&output=csv"
        raw_data = requests.get(url).content
        data = pandas.read_csv(io.StringIO(raw_data.decode('utf-8')))
        company_data_list[name] = data


# Returns list of data (pandas dataframes)
def get_data():
    init()
    return company_data_list

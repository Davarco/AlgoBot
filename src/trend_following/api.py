import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from flask_restful import Resource, Api
from data import retrieve_list
from stock import Stock
from trend_following.backtest import num_days, k


app = Flask(__name__)
api = Api(app)

todos = {}

# Get stock data
stock_data = retrieve_list("input/companies/complete.txt")
stock_dict_list = []
for key in stock_data:
    stock_dict_list.append(Stock(key, stock_data[key], k, 0, num_days))

# Sort stocks to buy and sell
buy_order = sorted(stock_dict_list, key=lambda stock_sorting: stock_sorting.ma_diff, reverse=False)
sell_order = sorted(stock_dict_list, key=lambda stock_sorting: stock_sorting.ma_diff, reverse=True)

buy_json = []
for stock in buy_order:
    buy_json.append(stock.__dict__)

sell_json = []
for stock in sell_order:
    sell_json.append(stock.__dict__)


class BuyOrder(Resource):
    def get(self):
        # stock = buy_order[0]
        # buy_order.remove(stock)
        # buy_order.insert(-1, stock)
        # return {"data": stock.__dict__}
        return {"data_count": len(buy_json), "data": buy_json}


class SellOrder(Resource):
    def get(self):
        # stock = sell_order[0]
        # sell_order.remove(stock)
        # sell_order.insert(-1, stock)
        # return {"data": stock.__dict__}
        return {"data_count": len(sell_json), "data": sell_json}


class GetStock(Resource):
    def get(self, ticker):
        stock = None
        for s in stock_dict_list:
            if s.ticker == ticker:
                stock = s
                break

        if stock is not None:
            return {ticker: stock.__dict__}
        else:
            return {"error": "ticker not found!"}

# Add the resources to the API
api.add_resource(BuyOrder, '/stocks/buy')
api.add_resource(SellOrder, '/stocks/sell')
api.add_resource(GetStock, '/stocks/get/<string:ticker>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

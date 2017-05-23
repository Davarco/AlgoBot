from flask import Flask, request
from flask_restful import Resource, Api
from data import retrieve_list
from stock import Stock
from backtest import num_days, k


app = Flask(__name__)
api = Api(app)

todos = {}

stock_data = retrieve_list("input/companies/complete.txt")
stock_dict_list = []

for key in stock_data:
    stock_dict_list.append(Stock(key, stock_data[key], k, 0, num_days))

buy_order = sorted(stock_dict_list, key=lambda stock_sorting: stock_sorting.today_lower_diff, reverse=True)
sell_order = sorted(stock_dict_list, key=lambda stock_sorting: stock_sorting.today_upper_diff, reverse=True)


class BuyOrder(Resource):
    def get(self):
        stock = buy_order[0]
        buy_order.remove(stock)
        buy_order.insert(-1, stock)
        return {"data": stock.__dict__}


class SellOrder(Resource):
    def get(self):
        stock = sell_order[0]
        sell_order.remove(stock)
        sell_order.insert(-1, stock)
        return {"data": stock.__dict__}

api.add_resource(BuyOrder, '/buy')
api.add_resource(SellOrder, '/sell')

if __name__ == '__main__':
    app.run(debug=True)
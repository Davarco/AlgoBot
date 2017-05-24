from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from backtest import k, num_days
from data import retrieve_list
from stock import Stock


# Flask stuff
app = Flask(__name__)
api = Api(app)


if __name__ == '__main__':
    app.run()

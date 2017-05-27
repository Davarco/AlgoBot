from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

# Flask stuff
app = Flask(__name__)
api = Api(app)


class Recommender(Resource):

    @staticmethod
    def get(self):
        pass

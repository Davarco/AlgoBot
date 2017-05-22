from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps


# Flask stuff
app = Flask(__name__)
api = Api(app)

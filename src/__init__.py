# __init__.py
# you have to activate the server all in one line on windows:
# $env:FLASK_APP = "src\__init__.py"; python manage.py run

from flask import Flask, jsonify
from flask_restx import Resource, Api

# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
# app = the Flask instance
# config is (an instance of the config.py class?)
# 'from_object' is a builtin method for taking an object from that other class?
# app.config I guess is a declared object of type config??
app.config.from_object('src.config.DevelopmentConfig'); 


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }

api.add_resource(Ping, '/ping')

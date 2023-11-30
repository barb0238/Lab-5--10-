# __init__.py
# you have to activate the server all in one line on windows:
# $env:FLASK_APP = "src\__init__.py"; python manage.py run
import os
from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy


# instantiate the app
app = Flask(__name__)

api = Api(app)




# set config
# app = the Flask instance
# config is (an instance of the config.py class?)
# 'from_object' is a builtin method for taking an object from that other class?
# app.config I guess is a declared object of type config??
app_settings = os.getenv('APP_SETTINGS')

app.config.from_object('src.config.DevelopmentConfig')

db = SQLAlchemy(app)

class User(db.model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


# this is routing apparently
class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }

api.add_resource(Ping, '/ping')

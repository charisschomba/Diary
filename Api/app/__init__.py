from flask import Flask
from flask_restful import Resource,Api,reqparse
from app.Models.entries import Entry
from app.Resources.entries import Entries, EntryList


from config import app_config

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    api = Api(app)
    api.add_resource(Entries, '/mydiary/v1/entries')
    api.add_resource(EntryList, '/mydiary/v1/entries/<int:entryId>')

    return app

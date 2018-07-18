# from flask import Flask
# from flask_restful import Resource, Api, reqparse
# from app.Models.entries import Entry
# from app.Resources.entries import Entries, EntryList
#
# app = Flask(__name__, instance_relative_config=True)
# app.config.from_object('config')
# api = Api(app)
#
# api.add_resource(Entries, '/mydiary/api/v1/entries')
# api.add_resource(EntryList, '/mydiary/api/v1/entries/<int:entryId>')
from flask import Flask
from flask_restful import Resource,Api,reqparse
from app.Models.entries import Entry
from app.Resources.entries import Entries, EntryList


from instance.config import app_config

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    api = Api(app)
    api.add_resource(Entries, '/mydiary/api/v1/entries')
    api.add_resource(EntryList, '/mydiary/api/v1/entries/<int:entryId>')

    return app

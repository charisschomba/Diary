from flask import Flask
from config import app_config
from flask_restful import Api,Resource
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from app.auth import SingUp,Login
from app.entries import Entries,EntryList

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    api = Api(app)
    jwt = JWTManager(app)
    api.add_resource(SingUp,'/mydiary/v1/auth/register')
    api.add_resource(Login,'/mydiary/v1/auth/login')
    api.add_resource(Entries, '/mydiary/v1/entries')
    api.add_resource(EntryList, '/mydiary/v1/entries/<int:entryId>')

    return app

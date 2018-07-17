from datetime import datetime
from flask import Flask,jsonify,make_response
from flask_restful import Resource,Api,reqparse

class Entries(Resource):
    """
    This resource class will have two methods,
    a post method that creates a new entry and get method that 
    fetches all items from Entry model
    
    """
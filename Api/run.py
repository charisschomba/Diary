from flask import Flask
from flask_restful import Resource, Api, reqparse
from Models.entries import Entry
from Resources.entries import Entries, EntryList

app = Flask(__name__)
api = Api(app)

api.add_resource(Entries, '/mydiary/api/v1/entries')
api.add_resource(EntryList, '/mydiary/api/v1/entries/<int:entryId>')

if __name__ == "__main__":
    app.run(debug=True)

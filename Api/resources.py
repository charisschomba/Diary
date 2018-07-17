from datetime import datetime
from flask import Flask,jsonify,make_response
from flask_restful import Resource,Api,reqparse
from entries import Entry

class Entries(Resource):
    """
    This resource class will have two methods,
    a post method that creates a new entry and get method that 
    fetches all items from Entry model

    """
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title', type=str, required=True,
                        help='Please provide title for your entry',
                        location='json')
        self.parser.add_argument('content', type=str, required=True,
                        help="Please provide content for your entry",
                        location='json')

    def get(self):
        """
        Method: GET
        Get all entries
        URL path: mydiary/api/v1/entries/
        """
        entries = Entry().all_items()
        response = {'All Entries':entries}
        return response

    def post(self):
        """
        Method: POST
        Create an Entry
        URL path: mydiary/api/v1/entries/
        """
        entries = Entry()
        data = self.parser.parse_args()
        if len(entries) == 0:
            id_ = 1
        else:
            id_ = entries[-1]['id'] + 1
        if data['title'] == '' or data['content'] == '':
            return {'Message':'title or content cannot be empty'}, 400
        else:
            try:
                new_entry = {
                    'id': id_,
                    'date':datetime.now().strftime("%d-%m-%Y"),
                    'title':data['title'],
                    'content':data['content']
                }
                Entry().save(new_entry)
            except:
                return {'Message':'An error occured while processing your request'}, 500
        return make_response(jsonify(new_entry), 201)   

    class EntryList(Resource):
        """
        This resource class will have three methods,
        a get method that get an entry by id,put method that 
        updates an entry by id if it exists and delete method that
        delete an entry by id.
        """
        def __init__(self):
            self.parser = reqparse.RequestParser()
            self.parser.add_argument('title', type=str, required=True,
                            help='No task title provided',
                            location='json')
            self.parser.add_argument('content', type=str, default="",
                            location='json') 

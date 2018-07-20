from datetime import datetime
from flask import jsonify,make_response
from flask_restful import Resource,reqparse
from app.Models.entries import Entry

class Entries(Resource):
    """
    This resource class will have two methods,a post method that creates a new entry and get method that
    fetches all items from Entry model

    """
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title',
                        type=str, required=True,
                        help='Please provide title for your entry'
                        )
        self.parser.add_argument('content',
                        type=str, required=True,
                        help="Please provide content for your entry"
                        )
    @staticmethod
    def get():
        """
        Method: GET
        Get all entries
        URL path: mydiary/v1/entries
        """
        entries = Entry().all_items()
        response = {'All Entries':entries}
        return response

    def post(self):
        """
        Method: POST
        Create an Entry
        URL path: mydiary/v1/entries
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
            except RuntimeError:
                return {'Message':'An error occured while processing your request'}, 500
        return make_response(jsonify(new_entry),201)

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
                    )
        self.parser.add_argument('content', type=str, required=True,
                    )
    @classmethod
    def get(cls,entryId):
        """
        Method: GET
        Fetches a single entry by it's Id
        URL path: mydiary/v1/entries/<int:entryId>
        """
        entry = Entry().get_by_id(entryId)
        if entry:
            return make_response(jsonify(entry),200)
        return {'Message':"Entry requested does not exist"}, 404

    def put(self,entryId):
        """
        Method: PUT
        Modifies an entry by it's Id
        URL path: mydiary/v1/entries/<int:entryId>
        """
        entry = Entry().get_by_id(entryId)
        if entry is None:
            return make_response(jsonify({'message':"Entry does not exist"}), 404)
        else:
            data = self.parser.parse_args()
            Entry().update_entry(data,entryId)
        return make_response(jsonify(entry),200)
    @classmethod
    def delete(cls,entryId):
        """
        Method: DELETE
        Deletes an entry by it's Id
        URL path: mydiary/v1/entries/<int:entryId>
        """
        entry = Entry().get_by_id(entryId)
        if entry is None:
            return make_response(jsonify({'message':"Entry does not exist"}), 404)
        else:
            Entry().delete_entry(entry)

        return make_response(jsonify({'message':'Your entry was successfully deleted'}),200)

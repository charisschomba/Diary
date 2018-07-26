from datetime import datetime
from flask_restful import Resource,reqparse
from flask_jwt_extended import (get_jwt_identity,jwt_required)
from app.models import Entry

class Entries(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.date = datetime.now().strftime("%d-%m-%Y")
        self.parser.add_argument('title',
                        type=str, required=True,
                        help='Title is required!'
                        )
        self.parser.add_argument('content',
                        type=str, required=True,
                        help="Content is required"
                        )
    @jwt_required
    def post(self):
        data = self.parser.parse_args()
        user_id =get_jwt_identity()[0]
        date = self.date
        title = data['title']
        content = data['content']
        entry = (user_id,date,title,content)
        try:
            Entry().save(entry)
            return {'id':user_id,'date':date,'title':title,'content':content},201
        except:
            return{'Server Response':"An error occured try again"},500

    @staticmethod
    @jwt_required
    def get():
        """
        Method: GET
        Get all entries of a user
        URL path: mydiary/v1/entries
        """
        user_id =get_jwt_identity()[0]
        entries = Entry().get_all_entries( user_id )
        response = {'All Entries':entries}
        return response, 200

class EntryList(Resource):
    """
    This resource class will have three methods,
    a get method that get an entry by id,put method that
    updates an entry by id if it exists and delete method that
    delete an entry by id.
    """

    def __init__(self):
            self.parser = reqparse.RequestParser()
            self.parser.add_argument('title',
                            type=str,
                            required=True,
                            help='No enty title provided',
                            )
            self.parser.add_argument('content',
                            type=str,
                            required=True,
                            help='No entry content provided'
                            )

    @staticmethod
    @jwt_required
    def get(entryId):
        user_id =get_jwt_identity()[0]
        entry = Entry().get_by_id(entryId,user_id)
        if entry:
            return {"Entry fetched Successuflly":entry[0]},200
        return {'Message':"Entry requested does not exist"}, 404

    @staticmethod
    def delete(entryId):
        """
        Method: DELETE
        Deletes an entry by it's Id
        URL path: mydiary/v1/entries/<int:entryId>
        """
        entry_id = Entry().get_entry_by_id(entryId)
        if entry_id is None:
            return {'message':"Entry does not exist"}, 404
        else:
            Entry().delete_entry(entryId)

        return {'message':'Your entry was successfully deleted'}, 200
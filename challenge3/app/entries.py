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



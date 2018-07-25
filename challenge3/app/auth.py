from datetime import datetime
from flask import Flask,jsonify,make_response
from flask_restful import Resource,reqparse
from app.models import User

class SingUp(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username',
                        type=str, required=True,
                        help='username is required!'
                        )
        self.parser.add_argument('email',
                        type=str, required=True,
                        help="Email is required"
                        )
        self.parser.add_argument('password',
                        type=str, required=True,
                        help="password is required"
                        )
        self.parser.add_argument('confirm_password',
                        type=str, required=True,
                        help="confirm Password is required"
                        )
    def post(self):
        data = self.parser.parse_args()
        username = data['username']
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']
        if not password == confirm_password:
            return {"message":"Double check your password"}
        user = User().get_user_by_email(email)
        if email in str(user):
            return{"Server Response":'User with email: {} exists'.format(email)}
        else:
            new_user = (username,email,password)
            User().save(new_user)
            return{"Server Response":"Account created"}

from datetime import datetime
from flask import Flask,jsonify,make_response
from flask_restful import Resource,reqparse
from app.models import User
from flask_jwt_extended import (create_access_token, get_jwt_identity)

class SingUp(Resource):
    """
        This is resource used to register new users
    """
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
            return {"message":"Double check your password"},400
        user = User().get_user_by_email(email)
        if email in str(user):
            return{"Server Response":'User with email: {} exists'.format(email)},400
        else:
            new_user = (username,email,password)
            User().save(new_user)
            return{"Server Response":"Account created"},200

class Login(Resource):
    """
        This is resource used to login existing users
    """
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email',
                        type=str, required=True,
                        help='email is required!'
                        )
        self.parser.add_argument('password',
                        type=str, required=True,
                        help="Password is required"
                        )
    def post(self):
        data = self.parser.parse_args()
        email = data['email']
        password = data['password']
        if not email in str(User().get_user_by_email(email)):
            return{"Server Response":"User does not exist"},400

        if password == User().get_pwd_by_email(email)[0]:
            user_id = User().get_id_by_email(email)
            access_token = create_access_token(identity=user_id)
            return {"Welcome":{"Your access token is:":access_token}},200
        return {"Server Response":"Incorrect password"},400
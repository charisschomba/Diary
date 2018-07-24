import json
from app import create_app

class BaseClass():
    """
    This class initializes our test client and hold all the required data
    """
    singin_url = '/mydiary/v1/auth/login'
    singup_url = '/mydiary/v1/auth/register'

    def SetUp(self):
        #SetUp method imtiliazes the app with testing configs
        app = create_app('testing')
        self.tester = app.test_client(self)

        self.new_user = {"username":'test',
                'email':'test@camp.com',
                'password':'test',
                'confirm_password':'test'}

        self.login_user = { 'email':'test@camp.com','password':'test'}

# this methods first sings up the user before logging
    def sing_in_user(self):
        #Sing Up the user
        self.tester.post(self.singup_url,
        data = json.dumps(self.new_user), content_type = 'application/json')

        #Logs in the user
        response = self.tester.post(self.singup_url,
        data=json.dumps(self.login_user),content_type='application/json')
        return response
    def tearDown(self):
        pass






import unittest
from app import create_app

class TestAppConfigs(unittest.TestCase):
    """
    This class tests app configuration settings such as Debug and Secret key
    """

    def test_DefaultConfig(self):
        app = create_app("production")
        self.tester = app.test_client(self)
        self.assertEqual(True,app.config['JSONIFY_PRETTYPRINT_REGULAR'])
        self.assertTrue('http://127.0.0.1:5000/',app.config["SERVER_NAME"])

    def test_productionConfig(self):
        app = create_app("production")
        self.tester = app.test_client(self)
        self.assertEqual(False,app.config['DEBUG'])
        self.assertTrue(b'\x01Q\xd5\xc7\x8d%\xff\\\xcd\xd7',app.config["SECRET"])

    def test_TestingConfig(self):
        app = create_app("testing")
        self.tester = app.test_client(self)
        self.assertEqual(True,app.config['DEBUG'])
        self.assertTrue(b'\x01Q\xd5\xc7\x8d%\xff\\\xcd\xd7',app.config["SECRET"])

    def test_DevelopmentConfig(self):
        app = create_app("development")
        self.tester = app.test_client(self)
        self.assertEqual(True,app.config['DEBUG'])
        self.assertTrue(b'\x01Q\xd5\xc7\x8d%\xff\\\xcd\xd7',app.config["SECRET"])

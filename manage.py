# import unittest
# import os

# from flask_script import Manager

# from challenge3.app import create_app

# app = create_app(config_name=os.getenv("FLASK_CONFIG"))

# manager = Manager(app)

# @manager.command
# def test():
#     test = unittest.TestLoader().discover("../challenge3/tests", pattern="test*.py")
#     unittest.TextTestRunner(verbosity=2).run(test)

# if __name__ == "__main__":
#     manager.run()

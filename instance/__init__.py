from flask import Flask

myapp=Flask(__name__)
myapp.testing=True
myapp.config['JWT_SECRET_KEY']='user_token'
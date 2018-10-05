from flask import Flask
# from instance.errors import Errors_msg


myapp=Flask(__name__)
myapp.testing=True
# error=Errors_msg()
myapp.config['JWT_SECRET_KEY']='user_token'
# myapp.register_error_handler(404, error.not_found)
# myapp.register_error_handler(400, error.bad_request)
# myapp.register_error_handler(500, error.internal_server_error)
# myapp.register_error_handler(405, error.method_not_allowed)
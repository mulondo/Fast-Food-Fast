""" runs the whole application """
from instance import myapp
from main.db import Database
from main import views


db=Database()
db.create_tables
if __name__==('__main__'):
    myapp.run(debug=True, port=5000)
    
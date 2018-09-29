""" runs the whole application """
from instance import myapp
from main import views

if __name__==('__main__'):
    myapp.run(debug=True, port=5000)

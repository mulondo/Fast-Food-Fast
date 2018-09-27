""" runs the whole application """
from api.instance import myapp
from api.main import views

if __name__==('__main__'):
    myapp.run(debug=True, port=5000)

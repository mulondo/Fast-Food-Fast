""" runs the whole application """
from instance import myapp
from app import views


myapp.run(debug=True, port=5000)

""" base tests"""
from unittest import TestCase
from flask import json
from main import views
from unittest import TestCase
from main.db import Database
from instance import myapp


class BaseTests(TestCase):
    """create a base test class"""
    def setUp(self):
      obj=Database()      
      creat_tab=obj.create_tables()
      self.apps = myapp
      self.client = self.apps.test_client
      self.default_url='/api/v1/'

    def signin_user(self,customer):
      """ method registers user """
      return self.client().post(self.default_url + "auth/signup", data=json.dumps(customer),
                content_type='application/json')
    
    def plan_login(self,login_info):
      """ method for plan login """
      return self.client().post(self.default_url+'auth/login',
                        content_type='application/json', data=json.dumps((login_info)))

    def login(self,login_info):
      """ method allows a user to login and get an access token """
      res = self.client().post(self.default_url+'auth/login',
                        content_type='application/json', data=json.dumps((login_info)))
      result = json.loads(res.data.decode())
      return result['access_token']
    
    def tearDown(self):
        """
        method destroys trial database after testing is done
        """
        trial_db = Database()
        trial_db.drop_tables()
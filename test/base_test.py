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
      self.apps = myapp
      self.client = self.apps.test_client
      self.order={'location':'kampala',
                'payment_mode':'cash',
                'order_items':[{'items':'eggs','price':'1000'}]}
      self.customer={'phone_number':'0703455445',
                      'email':'opi@gmail.com',
                      'username':'opio',
                      'password':'opioqwt'
                  }
      self.login_add={'username':'opio','password':'opioqwt'}

    def test_signup(self):
        """ test for posting an order """
        add_result = self.client().post('/api/v1/auth/signup', content_type='application/json', data=json.dumps(self.customer))
        self.assertEqual(add_result.status_code, 201)

    def login(self,tp):
        respo=add_result=self.client().post('/api/v1/auth/login',content_type='application/json', data=json.dumps(self.login_add))
        respo_data=json.loads(respo.data.decode())
        token=respo_data['access_token']
        return token
    
    # def plan_login(self,login_info):
    #   """ method for plan login """
    #   return self.client().post(self.default_url+'auth/login',
    #                     content_type='application/json', data=json.dumps(login_info))
    
    # def make_user_admin(self):
    #   return self.client().put('/make_admin/<int:user_id>',content_type='application/json',data=json.dumps(user_id))
                                                                              
    
    # def make_order(self,order,token):
    #   return self.client().post(self.default_url+'users/orders',content_type='application/json',
    #                       data=json.dumps(order),headers=({"acces_token": token}))                       
    
    # def tearDown(self):
    #     """ method destroys trial database after testing is done """
    #     trial_db = Database()
    #     trial_db.drop_tables()
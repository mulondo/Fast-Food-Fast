""" api tests"""
from unittest import TestCase
from flask import json
from app import views
from instance import myapp


class Test_api(TestCase):
    """ Api test class """
    def setUp(self):
        self.apps = myapp
        self.client = self.apps.test_client

    def test_add_order(self):
        """ test for posting an order """
        result = self.client().post('/api/v1/orders', content_type='application/json',
                                    data=json.dumps(dict(username="moses", 
                                                         phone_number="0704893645", order_items="['matooke']")))
        self.assertEqual(result.status_code, 201)

    def test_short_phone_number(self):
        """ test for short phone number """
        result = self.client().post('/api/v1/orders', content_type='application/json',
                                    data=json.dumps(dict(username="moses", phone_number="07039", order_items="['matooke']")))
        self.assertEqual(result.status_code, 403)

    def test_very_long_phone_number(self):
        """ test for very long phone number"""
        result = self.client().post('/api/v1/orders', content_type='application/json',
                                    data=json.dumps(dict(username="moses", phone_number="07039573748483", order_items="['matooke']")))
        self.assertEqual(result.status_code, 403)

    def test_incorrect_phone_number_format(self):
        """ test for incorrect phone number format """
        result = self.client().post('/api/v1/orders', content_type='application/json',
                                    data=json.dumps(dict(username="moses", phone_number="fvhjccjaksnxkjk", order_items="['matooke']")))
        self.assertEqual(result.status_code, 403)

    def test_empty_phone_number_format(self):
        """ test for empty phone number """
        result = self.client().post('/api/v1/orders', content_type='application/json',
                                    data=json.dumps(dict(username="moses", phone_number="", order_items="['matooke']")))
        self.assertEqual(result.status_code, 403)
        
    def test_get_all_orders(self):
        """ test for get all orders """
        result = self.client().get('/api/v1/orders')
        self.assertEqual(result.status_code, 200)        
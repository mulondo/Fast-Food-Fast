""" api tests"""
from unittest import TestCase
from flask import json
from main import views
from instance import myapp


class Test_api(TestCase):
    """ Api test class """
    def setUp(self):
        self.apps = myapp
        self.client = self.apps.test_client

    def test_add_order(self):
        """ test for posting an order """
        add_result = self.client().post('/api/v1/orders', content_type='application/json',
                                    data=json.dumps(dict(username="moses",
                                    phone_number="0704893645",location="kampala", payment="cash", order_items="['matooke']")))
        self.assertEqual(add_result.status_code, 201)    

    def test_get_all_orders(self):
        """ test for get all orders """
        result = self.client().get('/api/v1/orders')
        self.assertEqual(result.status_code, 200)

    def test_get_specific_order_with_existing_id(self):
        """ test for getting a specific order"""
       
        result = self.client().get('/api/v1/orders/1')
        self.assertEqual(result.status_code, 200)
        result1 = self.client().get('/api/v1/orders/8')
        self.assertEqual(result1.status_code, 404)

    def test_update_status_with_existing_id(self):
        """ test for update status """
        result = self.client().put('/api/v1/orders/1', content_type='application/json',
                                    data=json.dumps(dict(status="accepted")))
        self.assertEqual(result.status_code, 201)        


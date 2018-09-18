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
        add_result = self.client().post('/api/v1/orders', content_type='application/json',
                                    data=json.dumps(dict(username="moses",
                                                         phone_number="0704893645", order_items="['matooke']")))
        self.assertEqual(add_result.status_code, 201)

    # def test_short_phone_number(self):
    #     """ test for short phone number """
    #     result = self.client().post('/api/v1/orders', content_type='application/json',
    #                                 data=json.dumps(dict(username="peter", phone_number="07039", order_items="['matooke']")))
    #     self.assertEqual(result.status_code, 403)

    # def test_very_long_phone_number(self):
    #     """ test for very long phone number"""
    #     result = self.client().post('/api/v1/orders', content_type='application/json',
    #                                 data=json.dumps(dict(username="joan", phone_number="07039500748483", order_items="['matooke']")))
    #     self.assertEqual(result.status_code, 403)

    # def test_incorrect_phone_number_format(self):
    #     """ test for incorrect phone number format """
    #     result = self.client().post('/api/v1/orders', content_type='application/json',
    #                                 data=json.dumps(dict(username="sarah", phone_number="fvhjccjaksnxkjk", order_items="['matooke']")))
    #     self.assertEqual(result.status_code, 403)

    # def test_empty_phone_number_format(self):
    #     """ test for empty phone number """
    #     result = self.client().post('/api/v1/orders', content_type='application/json',
    #                                 data=json.dumps(dict(username="hope", phone_number="", order_items="['matooke']")))
    #     self.assertEqual(result.status_code, 403)

    def test_get_all_orders(self):
        """ test for get all orders """
        result = self.client().get('/api/v1/orders')
        self.assertEqual(result.status_code, 200)

    def test_get_specific_order_with_existing_id(self):
        """ test for getting a specific order"""
        # self.client().post('/api/v1/orders', content_type='application/json',
        #                    data=json.dumps(dict(username="tim", phone_number="0701859624", order_items="['matooke']")))
        result = self.client().get('/api/v1/orders/1')
        self.assertEqual(result.status_code, 200)
        result1 = self.client().get('/api/v1/orders/8')
        self.assertEqual(result1.status_code, 404)

    # def test_get_specific_order_with_non_existing_id(self):
    #     """ test for getting a specific order"""
    #     self.client().post('/api/v1/orders', content_type='application/json',
    #                        data=json.dumps(dict(username="Mukasa", phone_number="0701356709", order_items="['matooke']")))
    #     result = self.client().get('/api/v1/orders/8')
    #     self.assertEqual(result.status_code, 404)

    def test_update_status_with_existing_id(self):
        """ test for update status """
        # self.client().post('/api/v1/orders', content_type='application/json',
        #                     data=json.dumps(dict(username="Noah", phone_number="0705700834", order_items="['matooke']")))

        result = self.client().put('/api/v1/orders/1', content_type='application/json',
                                    data=json.dumps(dict(status="accepted")))
        self.assertEqual(result.status_code, 201)

        # result1 = self.client().put('/api/v1/orders/10', content_type='application/json',
        #                            data=json.dumps(dict(status="accepted")))
        # self.assertEqual(result1.status_code, 404)

        # result2 = self.client().put('/api/v1/orders/1', content_type='application/json',
        #                            data=json.dumps(dict(status="")))
        # self.assertEqual(result2.status_code, 403)


    # def test_validation_update_status_with_non_existing_id(self):
    #     """ test for update status """
    #     self.client().post('/api/v1/orders', content_type='application/json',
    #                        data=json.dumps(dict(username="Brian", phone_number="0705789625", order_items="['matooke']")))

        

    # def test_update_status_with_empty_status(self):
    #     """ test for empty status """
    #     self.client().post('/api/v1/orders', content_type='application/json',
    #                        data=json.dumps(dict(username="james", phone_number="", order_items="['chapati']")))

    #     result = self.client().put('/api/v1/orders/1', content_type='application/json',
    #                                data=json.dumps(dict(status="")))
    #     self.assertEqual(result.status_code, 403)

    # def test_update_status_with_wrong_format(self):
    #     """ test for wrong status format"""
    #     self.client().post('/api/v1/orders', content_type='application/json',
    #                        data=json.dumps(dict(username="moses", phone_number="3453t72", order_items="['chapati']")))

    #     result = self.client().put('/api/v1/orders/1', content_type='application/json',
    #                                data=json.dumps(dict(status="")))
    #     self.assertEqual(result.status_code, 403)
                        
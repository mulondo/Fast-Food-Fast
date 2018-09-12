from unittest import TestCase
from flask import json
from app import views
from instance import myapp


class Test_api(TestCase):
    def setUp(self):
        self.apps=myapp
        self.client=self.apps.test_client
    
   
    
    def test_add_order(self):
        result = self.client().post('/api/v1/orders', content_type='application/json',
        data=json.dumps(
            dict(username="moses",phone_number="Kisitu",order_items="['matooke']")))

        self.assertEqual(result.status_code, 201)

    def test_as(self):
        pass
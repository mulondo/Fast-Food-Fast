from test.base_test import BaseTests


class Test_oders(BaseTests):

    def test_make_order(self):        
        """method tests for placing and order"""

        order={"location":"kampala","payment_mode":"cash","order_items":[{"item":"chapati","price":"1000"}]}
        result = self.client().post('/api/v1/users/orders',headers={'Authorization': 'Bearer '+ self.tok_login(self.login_add)},
                                                                                    json=dict(self.order))
        self.assertEqual(result.status_code, 201)
    
    def test_make_order_with_missing_fields(self):
        order={"location":"kampala","payment_mode":"cash","order_items":[{"item":"chapati","price":"1000"}]}
        result = self.client().post('/api/v1/users/orders',headers={'Authorization': 'Bearer '+ self.tok_login(self.login_add)},
                                                                                    json=dict(self.order))
        self.assertEqual(result.status_code, 201)
    
    def test_get_history_order(self):
        result =self.client().get('/api/v1/users/orders',headers={'Authorization': 'Bearer '+ self.tok_login(self.login_add)})
        self.assertEqual(result.status_code, 200)
    
    def test_get_all_order(self):
        result =self.client().get('/api/v1/users/orders',headers={'Authorization': 'Bearer '+ self.tok_login(self.login_add)})
        self.assertEqual(result.status_code, 200)
    


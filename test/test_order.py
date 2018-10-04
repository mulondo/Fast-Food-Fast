from test.base_test import BaseTests


class Test_oders(BaseTests):

    def test_make_order(self):        
        """method tests for placing and order"""

        order={"location":"kampala","payment_mode":"cash","order_items":[{"item":"chapati","price":"1000"}]}
        result = self.client().post('/api/v1/users/orders',headers={'Authorization': 'Bearer '+ self.tok_login(self.login_add)},
                                                                                    json=dict(self.order))
        self.assertEqual(result.status_code, 201)

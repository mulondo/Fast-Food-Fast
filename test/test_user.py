from test.base_test import BaseTests


class Test_user(BaseTests):        
    """class for testing user signup and login"""
    def test_user_signup(self):
        """method testing for sign up"""      
        reg=self.signin_user(self.customer)
        self.assertEqual(reg.status_code,200)
    def test_login(self):
        res=self.login(self.login_add)
        self.assertEqual(res.status_code,201)
    
    def test_user_login_with_invalid_inputs(self):
        login_data={'username':'opio','password':''}
        res=self.login(login_data)
        self.assertEqual(res.status_code,400)

    def test_user_with_missing_field(self):
        data={'username':'opio'}
        res=self.login(data)
        self.assertEqual(res.status_code,400)
    
    def  test_make_admin(self):
        result = self.client().put('/api/v2/make_admin/11', content_type='application/json')
        self.assertEqual(result.status_code,201)
    
    def test_make_menu(self):
        list_items={'price':2000,'item':'chapati', 'quantity':'one'}
        result = self.client().post('/api/v2/users/orders',headers={'Authorization': 'Bearer '+ self.tok_login(self.login_add)},
                                                                                    json=dict(list_items))
        self.assertEqual(result.status_code,400)
    
    def test_get_menu(self):
        result =self.client().get('/api/v2/menu',headers={'Authorization': 'Bearer '+ self.tok_login(self.login_add)})
        self.assertEqual(result.status_code, 200)
    
    def test_get_all_orders(self):
        result =self.client().get('/api/v2/menu',headers={'Authorization': 'Bearer '+ self.tok_login(self.login_add)})
        self.assertEqual(result.status_code, 200)
        

    # def test_login_with_wrong_creditials(self): 

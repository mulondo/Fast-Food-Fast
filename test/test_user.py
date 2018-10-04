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

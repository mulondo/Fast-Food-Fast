from test.base_test import BaseTests


class Test_user(BaseTests):        
    """class for testing user signup and login"""
    def test_user_signup(self):
        """method testing for sign up"""      
        reg=self.signin_user(self.customer)
        self.assertEqual(reg.status_code,200)
    
 
    

        
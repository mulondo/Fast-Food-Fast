from test.base_test import BaseTests


customer={
        "phone_number":"0709632548",
        "email":"joan23@gmail.com",
        "username":"joan",
        "password":"12345"}

class Test_user(BaseTests):
        

    def test_user_signup(self):       
        reg=self.signin_user(customer)
        self.assertEqual(reg.status_code,201)
    
    def test_user_login(self):
        self.signin_user(customer)
        customer_info={
                    "username":"joan",
                    "password":"12345"}
        res=self.plan_login(customer_info)
        self.assertEqual(res.status_code,201)

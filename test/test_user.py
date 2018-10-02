from test.base_test import BaseTests


class Test_user(BaseTests):

    def test_user_signup(self):
        customer={
        "phone_number":"0709632548",
        "email":"joan23@gmail.com",
        "username":"joan",
        "password":"12345"}
        reg=self.signin_user(customer)
        self.assertEqual(reg.status_code,201)

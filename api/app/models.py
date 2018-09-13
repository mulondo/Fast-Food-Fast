""" contains datastores and the logic to store and retrieve the data"""
class CustomerOrders:
    """ Customer_order class handles the necessary datastores"""
    def __init__(self):
        """ contains instance variables"""
        self.orders = []

    def make_order(self, username, phone_number, myitems=list()):
        """ performs the logic for addding an order to a list"""
        my_order = []
        my_order = myitems
        order_id = len(self.orders)+1
        order = {
            "username":username,
            "order_id":order_id,
            "phone_number":phone_number,
            "order_items":my_order,
            "status":"None"
        }
        return self.orders.append(order)
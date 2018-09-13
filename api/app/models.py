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
        
    def get_all_orders(self):
        """ gets a list of orders"""
        return self.orders
    def get_an_order(self, order_id):
        """ gets a specific order"""
        for order in self.orders:
            if order['order_id'] == order_id:
                return order
        return "The order id doesnot exist"

    def update_status(self, order_id, status):
        """ updates the order status"""
        for order in self.orders:
            if order['order_id'] == order_id:
                order['status'] = status
                return self.orders
        return "The order id doesnot exist"
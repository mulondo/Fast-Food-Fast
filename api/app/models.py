from flask import jsonify


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

        if not username.isalpha() or len(username) < 4 or username.strip() == "":
            return jsonify({'error':'wrong username format'}), 403 

        if not phone_number.isdigit() or phone_number.strip() == "" or len(phone_number) < 10 or len(phone_number) > 12:
            return jsonify({'error': 'wrong phone number format'}), 403

        order = {
            "username":username,
            "order_id":order_id,
            "phone_number":phone_number,
            "order_items":my_order,
            "status":"None"
        }
        return jsonify({'message':'successfully added'}),201 

    def get_all_orders(self):
        """ gets a list of orders"""
        return jsonify({'orders':self.orders}),200 

    def get_an_order(self, order_id):
        """ gets a specific order"""
        for order in self.orders:
            if order['order_id'] == order_id:
                return jsonify({'message':'order'}),200
        return jsonify({'error':'order doesnot exit'}),404

    def update_status(self, order_id, status):
        """ updates the order status"""
        if status.strip() == "":
            return jsonify({'error':'status is empty'}), 403
        if not status.isalpha():
            return jsonify({'error':'wrong stutus format'}), 403
        for order in self.orders:
            if order['order_id'] == order_id:
                order['status'] = status
                return jsonify({'status updated':self.orders}),201
        return jsonify({'error':'The order id doesnot exist'}),404

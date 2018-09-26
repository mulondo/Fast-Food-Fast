""" api routes"""
from flask import jsonify, request
from api.main.models import CustomerOrders
from api.instance import myapp



  
ORDRS = CustomerOrders()
@myapp.route('/api/v1/orders', methods=['POST'])
def place_order():
    """creates an order"""
    username = request.json['username']
    phone_number = request.json['phone_number']
    my_items = []
    my_items.append(request.json['order_items'])
    return ORDRS.make_order(username, phone_number, my_items)

@myapp.route('/api/v1/orders', methods=['GET'])
def get_order():
    """Gets all orders"""
    return ORDRS.get_all_orders()

@myapp.route('/api/v1/orders/<int:order_id>', methods=['GET'])
def get_specific_order(order_id):
    """ gets a specific order given an id"""
    return ORDRS.get_an_order(order_id)

@myapp.route('/api/v1/orders/<int:order_id>', methods=['PUT'])
def update_status(order_id):
    """ Updates the status"""
    status = request.json['status']
    return ORDRS.update_status(order_id, status)
    
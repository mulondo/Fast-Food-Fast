""" api routes"""
from flask import jsonify, request
from app.models import CustomerOrders
from instance import myapp


ORDRS = CustomerOrders()
@myapp.route('/api/v1/orders', methods=['POST'])
def add_order():
    """creates an order"""
    username = request.json['username']
    phone_number = request.json['phone_number']
    my_items = []
    my_items.append(request.json['order_items'])

    ORDRS.make_order(username, phone_number, my_items)
    return jsonify({'message': 'succussfully created'}), 201
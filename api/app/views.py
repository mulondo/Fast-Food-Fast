""" api routes"""
from flask import jsonify, request
from app.models import CustomerOrders
from instance import myapp


ORDRS = CustomerOrders()
@myapp.route('/api/v1/orders', methods=['POST'])
def place_order():
    """creates an order"""
    username = request.json['username']
    phone_number = request.json['phone_number']
    my_items = []
    my_items.append(request.json['order_items'])

    # order items validation check
    if my_items is None:
        return jsonify({'error':'No item is ordered'}), 403

    # user name validation check
    if username.strip() == "":
        return jsonify({'error':'customer name is empty'}), 403
    if not username.isalpha():
        return jsonify({'error':'wrong username format'}), 403
    if len(username) < 4:
        return jsonify({'error':'username is too short'}), 403


    # phone number
    if phone_number.strip() == "":
        return jsonify({'error': 'phone number is empty'}), 403
    if not phone_number.isdigit():
        return jsonify({'error': 'wrong phone number type'}), 403
    if len(phone_number) < 10:
        return jsonify({'error': 'phone number is too short'}), 403
    if len(phone_number) > 12:
        return jsonify({'error': 'phone number is too long'}), 403

    ORDRS.make_order(username, phone_number, my_items)
    return jsonify({'message': 'succussfully created'}), 201

@myapp.route('/api/v1/orders', methods=['GET'])
def get_order():
    """Gets all orders"""
    return jsonify({'orders made':ORDRS.get_all_orders()}), 200

@myapp.route('/api/v1/orders/<int:order_id>', methods=['GET'])
def get_specific_order(order_id):
    """ gets a specific order given an id"""
    if type(order_id) is not int:
        return jsonify({'error':'the id must be an integer'}), 403

    return jsonify({'Order':ORDRS.get_an_order(order_id)}), 201

@myapp.route('/api/v1/orders/<int:order_id>', methods=['PUT'])
def update_status(order_id):
    """ Updates the status"""
    status = request.json['status']
    return jsonify({'status updated':ORDRS.update_status(order_id, status)}), 201    
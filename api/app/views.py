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
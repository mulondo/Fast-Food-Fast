from app.models import Customer_Orders
from flask import Flask,json,jsonify,request
from instance import myapp

ordrs=Customer_Orders()
@myapp.route('/api/v1/orders', methods=['POST'])
def add_order(): 
    username=request.json['username']
    phone_number=request.json['phone_number']
    my_items=[]
    my_items.append(request.json['order_items'])

    # order items validation check
    if my_items is None:
        return jsonify({'error':'No item is ordered'}),403

    # # user name validation check
    if username.strip()=="":
        return jsonify({'error':'customer name is empty'}),403    
    elif not username.isalpha():
        return jsonify({'error':'wrong username format'}),403
    elif len(username)<4:
        return jsonify({'error':'username is too short'}),403


    # phone number 
    if phone_number.strip()=="":
        return jsonify({'error': 'phone number is empty'}),403
    elif not phone_number.isdigit():
        return jsonify({'error': 'wrong phone number type'}),403
    elif len(phone_number)<10:
        return jsonify({'error': 'phone number is too short'}),403
    elif len(phone_number)>12:
        return jsonify({'error': 'phone number is too long'}),403    
    
    ordrs.make_order(username,phone_number,my_items)
    return jsonify({'message': 'succussfully created'}),201

@myapp.route('/api/v1/orders',methods=['GET'])
def get_order():
    return jsonify({'orders made':ordrs.get_all_orders()}),200

@myapp.route('/api/v1/orders/<int:order_id>',methods=['GET'])
def get_specific_order(order_id):
    if type(order_id) is not int:
        return jsonify({'error':'the id must be an integer'}),403

    return jsonify({'Order':ordrs.get_an_order(order_id)}),200

@myapp.route('/api/v1/orders/<int:order_id>',methods=['PUT'])
def update_status(order_id):
    status=request.json['status']
    # status validation check
    if status.strip()=="":
        return jsonify({'error':'status is empty'}),403    
    elif not status.isalpha():
        return jsonify({'error':'wrong stutus format'}),403
    
    return jsonify({'status updated':ordrs.update_status(order_id,status)}),201


   

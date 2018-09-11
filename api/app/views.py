from app.models import Customer_Orders
from flask import Flask,json,jsonify,request
from instance import myapp


@myapp.route('/api/v1/oders', methods=['POST'])
def add_order():
    username=request.json['username']
    phone_number=request.json['phone_number']
    my_items=[]
    my_items.append(request.json['order_items'])
    ordrs.make_order(username,phone_number,my_items)
    return jsonify({'message': 'succussfully created'}),201 
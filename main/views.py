""" api routes"""
from flask import jsonify, request
from functools import wraps
import psycopg2
from flask_jwt_extended import (JWTManager,verify_jwt_in_request, jwt_required, create_access_token,get_jwt_identity, get_jwt_claims)
from main.models import CustomerOrders
from instance import myapp
from main.db import Database
import datetime

my_db=Database()
ORDRS = CustomerOrders()
myapp.config['JWT_SECRET_KEY']='user_token'
jwt=JWTManager(myapp)


def admain_only(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_id=get_jwt_identity()
        if user_id['user_role'] != 'admin':
            return jsonify({'msg':'Admins only!'}), 403
        else:
            return fn(*args, **kwargs)
    return wrapper

@myapp.route('/api/v1/auth/signup', methods=['POST'])
def signp():   
    phone=request.json['phone_number']
    email=request.json['email']
    username=request.json['username']
    password=request.json['password']
    return ORDRS.create_account(username,phone,email,password)

@myapp.route('/api/v1/auth/login', methods=['POST'])
def login():
    username=request.json['username']
    password=request.json['password']
    if username.strip() == "" or password.strip() == "":
            return jsonify({'error':'password or username is missing'}),400
    user_details=ORDRS.login_check(username,password)
    for user in user_details:
        if user[0]==username and user[1]==password: 
            details= {'user_role':user[2],'user_id':user[3]}       
            access_token=create_access_token(identity=details)            
            return jsonify({'access_token':access_token}),201
    return jsonify({'error':'user is not known'}), 404

@myapp.route('/api/v1/users/orders', methods=['POST'])
@jwt_required
def place_order():
    """creates an order"""
    user_identity=get_jwt_identity()
    customer_id=user_identity['user_id']
    order_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_location = request.json['location']
    payment=request.json['payment_mode']
    my_items = []
    my_items.append(request.json['order_items'])
    return ORDRS.make_order(customer_id, order_date, payment, current_location, my_items)

@myapp.route('/api/v1/users/orders', methods=['GET'])
@jwt_required
def get_history_order():    
    """ gets a specific order given an id""" 
    user_identity=get_jwt_identity()  
    user_id=user_identity['user_id']
    return ORDRS.get_history_orders(user_id)

@myapp.route('/api/v1/orders', methods=['GET'])
@admain_only
def get_order():
    """Gets all orders"""
    return ORDRS.get_all_orders()

@myapp.route('/api/v1/orders/<int:orderId>', methods=['GET'])
@admain_only
def get_an_order(orderId):   
    return ORDRS.get_specific_order(orderId)

@myapp.route('/api/v1/orders/<int:orderId>',methods=['PUT'])
@admain_only
def update_order_status(orderId):
    status=request.json['status']
    return ORDRS.update_status(status,orderId)

@myapp.route('/api/v1/menu', methods=['GET'])
def get_menu_items():
    return ORDRS.get_menu_items()

@myapp.route('/api/v1/menu', methods=['POST'])
@admain_only
def add_menu_items():   
    price=request.json['price']
    item=request.json['item']
    quantity=request.json['quantity']
    return ORDRS.add_menu_items(item,price,quantity)

@myapp.route('/api/v1/make_admin/<int:user_id>',methods=['PUT'])
def create_admin(user_id):
    return ORDRS.make_admin(user_id)



    
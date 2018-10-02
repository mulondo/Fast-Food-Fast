""" api routes"""
from flask import jsonify, request,session
from functools import wraps
import psycopg2
from flask_jwt_extended import (JWTManager,verify_jwt_in_request, jwt_required, create_access_token,get_jwt_identity, get_jwt_claims)
from main.models import CustomerOrders
from instance import myapp
from main.db import Database
import datetime
import os

my_db=Database()
ORDRS = CustomerOrders()
myapp.config['JWT_SECRET_KEY']='user_token'
myapp.secret_key=os.urandom(24)
jwt=JWTManager(myapp)

@myapp.route('/api/v1/auth/login', methods=['POST'])
def login():
    users=request.json['username']
    passwrd=request.json['password']
    my_db.cur.execute("select username,password,user_type,user_id from users")
    user_details=my_db.cur.fetchall()
    for user in user_details:
        if user[0]==users and user[1]==passwrd:
            user_id=str(user[3])
            session['user_id']=user[3]
            access_token=create_access_token(identity=user[2])            
            return jsonify({'access_token':access_token}),201
    return jsonify({'error':'user is not known'}), 404

@jwt.user_claims_loader
def user_claims(identity):
    if identity=='admin':
        return {'role':'admin'}
    else:
        return {'role':'customer'}

def admain_only(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['role'] != 'admin':
            return jsonify({'msg':'Admins only!'}), 403
        else:
            return fn(*args, **kwargs)
    return wrapper

@myapp.route('/api/v1/orders', methods=['GET'])
@jwt_required
def get_order():
    """Gets all orders"""
    return jsonify({'id':session['user_id']})
    #return ORDRS.get_all_orders()

@myapp.route('/api/v1/orders/<int:order_id>', methods=['GET'])
@admain_only
def get_specific_order(order_id):
    """ gets a specific order given an id"""
    return ORDRS.get_an_order(order_id)

@myapp.route('/api/v1/auth/signup', methods=['POST'])
def signp():   
    phone=request.json['phone_number']
    email=request.json['email']
    username=request.json['username']
    password=request.json['password']
    return ORDRS.create_account(username,phone,email,password)

@myapp.route('/make_admin/<int:user_id>',methods=['PUT'])
def create_admin(user_id):
    return ORDRS.make_admin(user_id)

@myapp.route('/api/v1/users/orders', methods=['POST'])
def place_order():
    """creates an order"""
    customer_id=session['user_id']
    order_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_location = request.json['location']
    payment=request.json['payment_mode']
    my_items = []
    my_items.append(request.json['order_items'])
    return ORDRS.make_order(customer_id, order_date, payment, current_location, my_items)

# @myapp.route('/api/v1/orders/<int:order_id>', methods=['PUT'])
# def update_status(order_id):
#     """ Updates the status"""
#     status = request.json['status']
#     return ORDRS.update_status(order_id, status)
    
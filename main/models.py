from flask import jsonify
from main.db import Database
import psycopg2


db_content=Database()
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
        self.orders.append(order)
        return jsonify({'message':'successfully added'}),201 

    def get_all_orders(self):
        """ gets a list of orders"""
        return jsonify({'orders':self.orders}),200 

    def get_an_order(self, order_id):
        """ gets a specific order"""
        for order in self.orders:
            if order['order_id'] == order_id:
                return jsonify({'order':order}),200
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

    def create_account(self,username,phone,email,password):
        try:
            sql="INSERT INTO users(username,phone_number,email,password) VALUES(%s,%s,%s,%s)"
            db_content.cur.execute(sql,(username,phone,email,password))
        except psycopg2.Error as err:
            return jsonify({'error':str(err)})        
        return jsonify({'message':'succussfully registered'}),201

    def make_admin(user_id):
        adm='admin'
        sql="UPDATE users SET user_type='"+adm+"' WHERE user_id=user_id"
        db_content.cur.execute(sql)
        return jsonify({'message':'changed to admin succussfully'}),201

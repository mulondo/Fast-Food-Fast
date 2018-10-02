from flask import jsonify,json
from main.db import Database
import psycopg2


db_content=Database()
""" contains datastores and the logic to store and retrieve the data"""
class CustomerOrders:
    """ Customer_order class handles the necessary datastores"""
    def __init__(self):
        """ contains instance variables"""
        self.orders = []

    def make_order(self, customer_id, order_date, payment, current_location, my_items=list()):
        """ performs the logic for addding an order to a list"""
        customer_order = []
        order_items = my_items
        
        try:
            sql="INSERT INTO orders(customer_id,date,payment_mode,order_items,location) VALUES(%s,%s,%s,%s,%s)"
            db_content.cur.execute(sql,(customer_id, order_date, payment, json.dumps(order_items),current_location))
        except psycopg2.Error as err:
            return jsonify({'error':str(err)}),400       
        return jsonify({'message':'order succussfully made '}),201                                                        

    def create_account(self,username,phone,email,password):
        try:
            sql="INSERT INTO users(username,phone_number,email,password) VALUES(%s,%s,%s,%s)"
            db_content.cur.execute(sql,(username,phone,email,password))
        except psycopg2.Error as err:
            return jsonify({'error':str(err)})        
        return jsonify({'message':'succussfully registered'}),201

    def make_admin(self,user_id):
        adm='admin'
        sql="UPDATE users SET user_type='"+adm+"' WHERE user_id=user_id"
        db_content.cur.execute(sql)
        return jsonify({'message':'changed to admin succussfully'}),201

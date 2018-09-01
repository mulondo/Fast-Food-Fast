import psycopg2
class Database:
#connect to database
    con=psycopg2.connect(host="localhost", database="fast_food_fast",user="postgres",password="angels",port="5432")

    cur=con.cursor()

    con.autocommit=True
    def create_users_table():
        user_table="""create table if not exists Users(user_id serial PRIMARY KEY NOT NULL,
                                                        username TEXT NOT NULL,
                                                        user_type TEXT DEFAULT 'customer',
                                                        phone_number TEXT NOT NULL,
                                                        email TEXT NOT NULL,
                                                        password TEXT NOT NULL
                                                        )"""
        return Database.cur.execute(user_table)
    
    def create_orders_table():
        order_table="""create table if not exists Orders(customer_id INTEGER REFERENCES Users(user_id),
                                                        order_id serial PRIMARY KEY NOT NULL,
                                                        date timestamp NOT NULL,
                                                        payment_mode TEXT,
                                                        location TEXT,
                                                        order_items json NOT NULL
                                                        )"""
        return Database.cur.execute(order_table)

create_table=Database
create_table.create_orders_table()
 
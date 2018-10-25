import psycopg2
from psycopg2.extras import RealDictCursor
class Database:
#connect to database
    con=psycopg2.connect(host="ec2-184-73-197-211.compute-1.amazonaws.com", database="df11mo103pjvn4",user="bunyqndezyzqxm",password="aac276d05879653ee9edbe8f3f73c8a24959caf1206337389929f452fca5b48b",port="5432")
    
    dict_cursor=con.cursor(cursor_factory=RealDictCursor)
    cur=con.cursor()

    con.autocommit=True
    def create_tables(self):
        user_table="""create table if not exists Users(user_id serial PRIMARY KEY NOT NULL,
                                                        username TEXT NOT NULL,
                                                        user_type TEXT DEFAULT 'customer',
                                                        phone_number TEXT NOT NULL,
                                                        email TEXT NOT NULL,
                                                        password TEXT NOT NULL
                                                        )"""
        order_table="""create table if not exists Orders(user_id INTEGER REFERENCES Users(user_id),
                                                        order_id serial PRIMARY KEY NOT NULL,
                                                        date timestamp NOT NULL,
                                                        payment_mode TEXT,
                                                        location TEXT,
                                                        status TEXT DEFAULT 'pending',
                                                        order_items TEXT NOT NULL
                                                        )"""
        menu_items="""create table if not exists Items(items_id serial PRIMARY KEY NOT NULL,
                                                        item_name TEXT NOT NULL,
                                                        price INTEGER NOT NULL,
                                                        category TEXT NOT NULL,
                                                        quantity TEXT NOT NULL                                                       
                                                        )"""
        Database.cur.execute(user_table)
        Database.cur.execute(order_table)
        Database.cur.execute(menu_items)    

    def drop_tables(self):
        """
        method drops tables
        """
        drop_tables = "DROP TABLE Users,Orders"
        drop_menu="DROP TABLE Items cascade"
        Database.cur.execute(drop_tables)
        Database.cur.execute(drop_menu)


        
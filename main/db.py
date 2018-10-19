import psycopg2
from psycopg2.extras import RealDictCursor
class Database:
#connect to database
    con=psycopg2.connect(host="ec2-23-23-80-20.compute-1.amazonaws.com", database="dfdhpj79t1i7i6",user="oahuugythatjhg",password="026d5d18df9957aa2a797b80956652fd4acf637155083327b265d1f717e3d010",port="5432")
    
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
                                                        order_items json NOT NULL
                                                        )"""
        menu_items="""create table if not exists Items(items_id serial PRIMARY KEY NOT NULL,
                                                        item_name TEXT NOT NULL,
                                                        price INTEGER NOT NULL,
                                                        category TEXT NOT NULL,
                                                        quantity TEXT NOT NULL                                                       
                                                        )"""
        # Database.cur.execute(user_table)
        # Database.cur.execute(order_table)
        Database.cur.execute(menu_items)    

    def drop_tables(self):
        """
        method drops tables
        """
        # drop_tables = "DROP TABLE Users,Orders"
        drop_menu="DROP TABLE Items cascade"
        # Database.cur.execute(drop_tables)
        Database.cur.execute(drop_menu)
        
create=Database()
create.create_tables()
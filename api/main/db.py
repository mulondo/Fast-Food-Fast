import psycopg2

#connect to database
con=psycopg2.connect(host="localhost", database="fast_food_fast",user="postgres",password="angels",port="5432")

cur=con.cursor()

con.autocommit=True

user_table="""create table if not exists Users(user_id serial PRIMARY KEY NOT NULL,
                                                username TEXT NOT NULL,
                                                user_type TEXT NOT NULL,
                                                phone_number TEXT NOT NULL,
                                                email TEXT NOT NULL,
                                                password TEXT NOT NULL
                                                )"""
cur.execute(user_table)
import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Graydon Sinclair in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab10_render_db_user:3nbt8zcuJiN8YOWYQLxxkaBbvYWQ6k3U@dpg-co0t727109ks73biivk0-a/lab10_render_db")
    conn.close()
    return "Database Connection Successful"

@app.route('db_create')
def creating():
    conn = psycopg2.connect("postgres://lab10_render_db_user:3nbt8zcuJiN8YOWYQLxxkaBbvYWQ6k3U@dpg-co0t727109ks73biivk0-a/lab10_render_db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"
"""
Flask application for demonstrating basic database interactions
with a PostgreSQL database using psycopg2. This app includes
routes for testing connectivity, creating a table, inserting data,
selecting and displaying table contents, and dropping the table.

Author: Greg VanDyne
Course: CSPB 3308
"""

import psycopg2
from flask import Flask

app = Flask(__name__)

# Connection string to remote PostgreSQL database
DB_URL = "postgresql://gregs_postgres_db_user:lGQhLBaitrrIdLVsGBuH10hzhrXHzw8G@dpg-cvlf428dl3ps738jql00-a/gregs_postgres_db"

@app.route('/')
def hello_world():
    """
    Base route that returns a simple greeting.
    """
    return 'Hello World from Greg VanDyne in 3308'

@app.route('/db_test')
def db_test():
    """
    Tests database connectivity by opening and closing a connection.
    """
    conn = psycopg2.connect(DB_URL)
    conn.close()
    return 'Database connection successful!'

@app.route('/db_create')
def db_create():
    """
    Creates a 'Basketball' table in the database if it doesn't exist.
    The table stores NBA player details.
    """
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()

    # SQL to create the table with basic player info
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
    cur.close()
    conn.close()
    return 'Basketball table successfully created!'

@app.route('/db_insert')
def db_insert():
    """
    Inserts a set of sample NBA players into the 'Basketball' table.
    """
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()

    # Insert multiple rows into the Basketball table
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')

    conn.commit()
    cur.close()
    conn.close()
    return 'Basketball Table Populated'

@app.route('/db_select')
def db_select():
    """
    Queries all records from the 'Basketball' table and returns them
    in an HTML table format.
    """
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('SELECT * FROM Basketball;')
    records = cur.fetchall()
    cur.close()
    conn.close()

    # Dynamically build an HTML table to display records
    response = "<table border='1'><tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"
    for row in records:
        response += "<tr>"
        for cell in row:
            response += f"<td>{cell}</td>"
        response += "</tr>"
    response += "</table>"
    return response

@app.route('/db_drop')
def db_drop():
    """
    Drops the 'Basketball' table from the database.
    WARNING: This deletes all data in the table.
    """
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('DROP TABLE Basketball;')
    conn.commit()
    cur.close()
    conn.close()
    return 'Basketball Table Dropped'

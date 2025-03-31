import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Greg VanDyne in 3308'

@app.route('/db_test')
def db_test():
    # Connect to the database using the internal URL
    conn = psycopg2.connect("postgresql://gregs_postgres_db_user:lGQhLBaitrrIdLVsGBuH10hzhrXHzw8G@dpg-cvlf428dl3ps738jql00-a/gregs_postgres_db")
    conn.close()
    return 'Database connection successful!'

@app.route('/db_create')
def db_create():
    # Connect to the database
    conn = psycopg2.connect("postgresql://gregs_postgres_db_user:lGQhLBaitrrIdLVsGBuH10hzhrXHzw8G@dpg-cvlf428dl3ps738jql00-a/gregs_postgres_db")
    
    # Create a cursor
    cur = conn.cursor()

    # Execute SQL to create the Basketball table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')

    # Commit the changes
    conn.commit()

    # Close the connection
    cur.close()
    conn.close()

    return 'Basketball table successfully created!'

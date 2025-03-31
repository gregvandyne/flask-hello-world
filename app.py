import psycopg2
from flask import Flask

app = Flask(__name__)

DB_URL = "postgresql://gregs_postgres_db_user:lGQhLBaitrrIdLVsGBuH10hzhrXHzw8G@dpg-cvlf428dl3ps738jql00-a/gregs_postgres_db"

@app.route('/')
def hello_world():
    return 'Hello World from Greg VanDyne in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect(DB_URL)
    conn.close()
    return 'Database connection successful!'

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect(DB_URL)
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
    cur.close()
    conn.close()
    return 'Basketball table successfully created!'

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
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
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('SELECT * FROM Basketball;')
    records = cur.fetchall()
    cur.close()
    conn.close()

    # Build HTML table response
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
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('DROP TABLE Basketball;')
    conn.commit()
    cur.close()
    conn.close()
    return 'Basketball Table Dropped'

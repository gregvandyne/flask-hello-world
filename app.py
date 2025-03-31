import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from --your name-- in 3308'

@app.route('/db_test')
def db_test():
    # Connect to the database using the internal URL
    conn = psycopg2.connect("postgresql://gregs_postgres_db_user:lGQhLBaitrrIdLVsGBuH10hzhrXHzw8G@dpg-cvlf428dl3ps738jql00-a/gregs_postgres_db")
    # Close
    conn.close()
    return 'Database connection successful and closed!'

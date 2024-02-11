from flask import Flask
from pymysql import connect

app = Flask(__name__)

# DB 연결 설정
DB_HOST = '34.47.71.74'
DB_USER = 'beyondvision-user'
DB_PASSWORD = 'fighting2024'
DB_NAME = 'beyondvision-db'

def connect_to_db():
    return connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

#conn = connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
#cursor = conn.cursor()
#cursor.execute("SELECT * FROM member")
#results = cursor.fetchall()
#for row in results:
#    print(row)
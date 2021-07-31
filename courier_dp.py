import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host,
    user,
    password,
    database
)

# A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
cursor = connection.cursor()

# Add code here to insert a new record
sql = "INSERT INTO couriers (courier_name, phone_number) VALUES (%s, %s)"
val = [('Alex', '078024702'),
       ('Oussama', '078173423'),
       ('Tom', '079667242'),
       ('Ahmed', '076945323'),
       ('Harry', '072190655'),
       ('Usain', '073652892'),
       ('Idris', '075823454'),
       ('Jeniel', '074990702'),
       ('Aliana', '074907332')
]

cursor.executemany(sql, val)
# cursor.execute('SELECT name, phone_number FROM couriers')

# rows = cursor.fetchall()
# for row in rows:
#     print(row)
#     print(f'mame:{(row[0])}, phone_number:{row[1]},')


connection.commit()
cursor.close()
connection.close()
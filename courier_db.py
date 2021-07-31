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
val = [('Alex', '07802470263'),
       ('Oussama', '07817342326'),
       ('Tom', '07966724244'),
       ('Ahmed', '07696645323'),
       ('Harry', '07214390655'),
       ('Usain', '07365287692'),
       ('Idris', '07582333454'),
       ('Jeniel', '07499980702'),
       ('Aliana', '07490347332')
]

cursor.executemany(sql, val)


####### T O   P R I N T ###########
# cursor.execute('SELECT courier_name, phone_number FROM couriers')

# # Gets all rows from the result
# rows = cursor.fetchall()
# for row in rows:
#     # print(row)
#     print(f'\n Name: {str(row[0])}, Number: {row[1]},')


connection.commit()
cursor.close()
connection.close()
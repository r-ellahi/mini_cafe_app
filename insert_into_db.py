#INSERT INTO DB
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
sql = 'INSERT INTO Products (Product_Name, Price) VALUES (%s, %s)'
val = [('Latte', 2.5),
       ('Tea', 2.5),
       ('Eggs', 2.5)
       ]


# Add code here to insert a new record
cursor.executemany(sql, val)

connection.commit()
cursor.close()
connection.close()
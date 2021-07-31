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
sql = "INSERT INTO products (product_name, price) VALUES (%s, %s)"
val = [('Coffee',3.25),
        ('Mocha',3.25),
        ('Americano',3.25),
        ('Chai',3.15),
        ('Tea',2.5),
        ('Herbal Tea',3.4),
        ('Hot Chocolate',3.5),
        ('Cake',3.1),
        ('Cookie',2.25),
        ('Cinnamon Twist',2.75),
        ('Crossiant',2.5),
        ('Pain Au Chocolat',2.75)
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
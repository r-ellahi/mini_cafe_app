import csv
from csv import DictWriter, DictReader
import pymysql
import os
from dotenv import load_dotenv

########PRETTY CODE ##########
# from prompt_toolkit import print_formatted_text, HTML

# print_formatted_text(HTML('<b> Aliana </b>'))
# print_formatted_text(HTML('<i> Oussama </i>'))
# print_formatted_text(HTML('<u> <b> Rumaanah </b </u>'))



def whitespace():
    print('\n')

# READ CSV FILES 
def read_csv_file (file_name, csv_to_read):
    with open (file_name, 'r') as csv_file:
        csv_to_read = csv.DictReader(csv_file)
        csv_list = []
        for row in csv_to_read:
            csv_list.append(row) 
        return csv_list


# SAVE CSV FILES 
def save_csv_file(file_name, list_name):
    with open(file_name, "w", newline='') as updated:
        if list_name:
            writer = csv.DictWriter(updated, fieldnames=list_name[0].keys())
            writer.writeheader()
            writer.writerows(list_name)

# Dictionary Append
def append_dict(file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)


#UPDATE CSV ITEMS
def update_items(chosen_item):
    for key, value in chosen_item.items():
        
        chosen_value = input(
            f'\n{key} Has the value of {value}. Enter new value for {key}: ')

        if chosen_value == '':
            chosen_item[key] = value
            print('\nNothing has been changed')
        else:
            chosen_item[key] = chosen_value

# PRINT CSV FILES 
def print_csv_file (file_name, *csv_file):
    with open(file_name, 'r') as csv_print:
        csv_file = csv.DictReader(csv_print)
        for row in csv_file:
            print(dict(row))




########### WEEK 5 - TO DATABASE ###############


##### OPTION 1 - TO PRINT #######
def read_products_db():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    cursor = connection.cursor()
    
    cursor.execute('SELECT product_id, product_name, price FROM products')
    
    rows = cursor.fetchall()
    for row in rows:
        print(f'\n product_id: {int(row[0])}, Product Name: {str(row[1])}, Price: {float(row[2])}')
        
    cursor.close()
    connection.close()


def read_courier_db():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    cursor = connection.cursor()
    
    cursor.execute('SELECT courier_id, courier_name, phone_number FROM couriers')
    
    rows = cursor.fetchall()
    for row in rows:
        print(f'\n courier_id: {int(row[0])}, Courier Name: {str(row[1])}, Phone Number: {row[2]}')
        
    cursor.close()
    connection.close()



##### OPTION 2 - TO CREATE #######
def new_product_db(product_name, product_price):
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    cursor = connection.cursor()
    sql = "INSERT INTO products (product_name, price) VALUES (%s, %s)"
    val = [(product_name, product_price)]
    
    cursor.executemany(sql, val)
    
    connection.commit()
    cursor.close()
    connection.close()


def new_courier_db(courier_name, courier_number):
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    cursor = connection.cursor()
    sql = "INSERT INTO couriers (courier_name, phone_number) VALUES (%s, %s)"
    val = [(courier_name, courier_number)]
    
    cursor.executemany(sql, val)
    
    connection.commit()
    cursor.close()
    connection.close()



##### OPTION 3 - TO UPDATE #######
def update_into_product_db(new_product, new_price, product_id):
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    cursor = connection.cursor()
    if new_product or new_price:
        sql = 'UPDATE products SET'
        if new_product and new_price:
            sql += ' product_name = %s, price = %s WHERE product_id = %s'
            val = (new_product, new_price, product_id)
            print("\nNothing has been updated")
            
        elif new_product:
            sql += ' product_name = %s WHERE product_id = %s'
            val = (new_product, product_id)
            print("\nNothing has been updated")
            
        elif new_price:
            sql += ' price = %s WHERE product_id = %s'
            val = (new_price, product_id)
            print("\nNothing has been updated")
            
        cursor.execute(sql, val)
        connection.commit()
        
    else:
        print("Nothing has been updated")
    cursor.close()
    connection.close()


def update_into_courier_db(new_courier, new_number, courier_id):
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    cursor = connection.cursor()
    if new_courier or new_number:
        sql = 'UPDATE couriers SET'
        if new_courier and new_number:
            sql += ' courier_name = %s, phone_number = %s WHERE courier_id = %s'
            val = (new_courier, new_number, courier_id)
            print("\nNothing has been updated")
            
        elif new_courier:
            sql += ' courier_name = %s WHERE courier_id = %s'
            val = (new_courier, courier_id)
            print("\nNothing has been updated")
            
        elif new_number:
            sql += ' phone_number = %s WHERE courier_id = %s'
            val = (new_number, courier_id)
            print("\nNothing has been updated")
            
        cursor.execute(sql, val)
        connection.commit()
        
    else:
        print("\nNothing has been updated")
        
    cursor.close()
    connection.close()



##### OPTION 4 - TO DELETE #######

def delete_product_from_db(deleted_product_id):
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )

    cursor = connection.cursor()
    sql = 'DELETE FROM products WHERE product_id = %s'
    val = [{deleted_product_id}]

    cursor.execute(sql, val)

    connection.commit()
    cursor.close()
    connection.close()


def delete_courier_from_db(deleted_courier_id):
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )

    cursor = connection.cursor()
    sql = 'DELETE FROM couriers WHERE courier_id = %s'
    val = [{deleted_courier_id}]

    cursor.execute(sql, val)

    connection.commit()
    cursor.close()
    connection.close()



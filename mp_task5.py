import csv
from mp_functions_w5 import whitespace, read_csv_file, print_csv_file, save_csv_file, append_dict, update_items, read_courier_db, update_into_courier_db
from mp_functions_w5 import read_products_db, new_product_db, new_courier_db, delete_product_from_db, delete_courier_from_db, update_into_product_db
from csv import DictWriter, DictReader
from pprint import pprint


product =
courier = []
orders = []

product = read_csv_file('product_list.csv', product)
courier = read_csv_file('courier_list.csv', courier)
orders = read_csv_file('orders.csv', orders)

order_status = ['Order Confirmed', 'Preparing', 'Quality Check', 'On Route', 'Delivered', 'Unable to Deliver']

def main_menu():
    print("""\033[33m\n\tMain Menu:\033[0m""")
    print("""
        [0] - To Exit 
        [1] - Product Options
        [2] - Courier Options
        [3] - Order Details
    """)
    
    option = int(input("""\033[33m\n\tEnter your choice here: \033[0m"""))
    
    if option == 0:
        save_csv_file('product_list.csv', product)
        save_csv_file('courier_list.csv', courier)
        save_csv_file('orders.csv', orders)
        whitespace()
        print('\tThanks for visiting!')
        whitespace()
        exit()
    
    elif option == 1:
        product_menu()   
        
    elif option == 2:
        courier_menu()
    
    elif option == 3:
        orders_details()
        
    else:
        print ('\tPlease enter a valid option')
        whitespace()
        main_menu()    


def product_menu():
    print("""\033[33m\n\tProduct Options:\033[0m""")
    print('''
        [0] - Return to Main Menu
        [1] - View Menu
        [2] - Create New Product
        [3] - Update Existing Product    
        [4] - Delete a Product''')
    whitespace()
    user_input = int(input("""\033[33m\n\tEnter your choice here: \033[0m"""))
        
        
    if user_input == 0:
        main_menu()
    
    elif user_input == 1:
        read_products_db()
        product_menu()
    
    elif user_input == 2:
        print('\n\tHere is the Product Menu:')
        read_products_db()

        new_product = input('\n\tPlease Add A New Product To The List : ')
        new_price = float(input('\n\tPlease Enter Desired Price: '))
        new_product_db(new_product, new_price)
        
        print('\n\tHere is the new product menu:\n\t')
        read_products_db()
        product_menu()
    
    elif user_input == 3:
        print('Here is the menu: ')
        read_products_db()
        product_id = int(input('Choose The Product ID: '))
        new_product = input('Enter A Name For Your Product: ')
        new_price = (input('Eneter A Price: '))

        update_into_product_db(new_product, new_price, product_id)
        print('Here is the updated menu: ')
        read_products_db()
        product_menu()

    elif user_input == 4:
        print('\n\tHere is the Product Menu:')
        read_products_db()
                
        deleted_input = int(input('\n\tSelect a product to delete: '))
                
        delete_product_from_db(deleted_input)
                    
        print('\n\tHere is the new product menu: ')
        read_products_db()
        product_menu()
    


def courier_menu():
    print("""\033[33m\n\tCourier Options:\033[0m""")
    print('''
        [0] - Return to Main Menu
        [1] - Print Courier List
        [2] - Create New Courier
        [3] - Update Courier
        [4] - Delete Courier
                        ''')
    user_input = int(input("""\033[33m\n\tEnter your choice here:  \033[0m"""))

    if user_input == 0:    
        whitespace()
        print('Thanks for visiting!')
        whitespace()
        main_menu()
    
    elif user_input == 1:
        read_courier_db()
        courier_menu()
    
    elif user_input == 2:
        print('\n\tHere is the Courier List:\n\t')
        read_courier_db()
        
        new_courier = input('\n\tPlease Enter The Name of the Courier : ')
        new_number = (float(input('\n\tPlease Enter Their Number: ')))
        new_courier_db(new_courier, new_number)
        
        print('\n\tHere is the new courier list: ')
        read_courier_db()
        courier_menu()
        
        
    elif user_input == 3:
        print('Here Is The Courier List: ')
        read_courier_db()
        courier_id = int(input('Choose Courier ID: '))
        new_courier = input('Enter A New Courier Name: ')
        new_number = (input('Enter A New Courier Number: '))

        update_into_courier_db(new_courier, new_number, courier_id)
        print('Here is the updated menu: ')
        read_courier_db()
        courier_menu()

    elif user_input == 4:        
        read_courier_db()
        deleted_input = int(input('\n\tSelect a courier to delete: '))
        
        delete_courier_from_db(deleted_input)
                    
        print('\n\tHere is the new product menu: ')
        read_courier_db()
        courier_menu()


def orders_details():
    print("""\033[33m\n\tOrder Details:\033[0m""")
    print('''
        [0] - Return to Main Menu
        [1] - View Order
        [2] - Enter Details
        [3] - Update Order Status  
        [4] - Update Existing Order
        [5] - Delete Order
        ''')
    user_input = int(input("""\033[33m\n\tEnter your choice here: \033[0m"""))
    
    
    if user_input == 0:
        main_menu()

    elif user_input == 1:
        whitespace()
        # for order in orders:
        #     print(order)
        pprint(orders)
        whitespace()
        orders_details()

    elif user_input == 2:
        customer_name = input("\tEnter your name: ")
        customer_address = input("\tEnter your address: ")
        customer_number = int(input("\tEnter your number: "))
        
        for value, index in enumerate(product):
            print(value, index)
        product_choice = input('Please select your products: ')
        
        for value, index in enumerate(courier):
            print(value, index)
        courier_choice = int(input('Who would you like to deliver your order:?  '))
        
        entry = {}
        entry['Customer Name'] = customer_name 
        entry ['Customer Address'] = customer_address
        entry ['Customer Phone Number'] = customer_number
        entry ['Courier'] = courier_choice
        entry['Status'] = order_status[1]
        entry['Products'] = product_choice
        
        titles = ['Customer Name', "Customer Address", 'Customer Phone Number','Courier', 'Status', "Products"]
        append_dict('orders.csv', entry, titles)
        
        print('Thank you for your order', entry)
        orders_details()

    elif user_input == 3:
        for key, value in enumerate(orders):
            print(key, value)

        order_index = int(input("""\033[33m\nPlease select an order to update:   \033[0m"""))
        print('')

        for key, value in enumerate(order_status):
            print(key, value)

        status_input = int(
            input("""\033[33m\nChoose an order status to update on the order list:   \033[0m"""))
        order_to_update = orders[order_index]
        
        order_to_update['Status'] = order_status[status_input]
        print("""\033[33m\nOrder status has been updated\033[0m""")
        pprint(order_to_update)
        orders_details()

    elif user_input == 4:
        for key, value in enumerate (orders):
            print(key, value)
        order_index = int(input(''' \033[33m\n\tSelect an order to update:    \033[0m'''))
        updated_order = orders[order_index] 
        old_order = updated_order.copy()
        for key, value in updated_order.items():
            print(key, value)
            chosen_order = input(f'\n{key} is currently {value}. Enter new details for {key}: ')
            if chosen_order == '':
                updated_order[key] = value
                print('\nNothing has been changed')
            else:
                updated_order[key] = chosen_order
        print(f'\n\tYour order has been updated from {old_order} to {updated_order}')
        orders_details()

    elif user_input == 5:
        for key, value in enumerate(orders):
            print(key, value)
        delete_order = int(input('''
        \033[33m\n\tSelect an order to delete:    \033[0m''')) 
        orders.pop(delete_order)
        print('''
                \033[33m\n\tOrder was deleted successfully.
                
        Remaining Orders: 
                \033[0m''')
        print(orders)
        whitespace()
        orders_details()
main_menu()
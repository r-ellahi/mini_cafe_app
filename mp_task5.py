import json
from prompt_toolkit import print_formatted_text, HTML
from mp_functions_w5 import whitespace, read_csv_file, print_csv_file, save_csv_file, append_dict, update_items, read_courier_db, update_into_courier_db
from mp_functions_w5 import read_products_db, new_product_db, new_courier_db, delete_product_from_db, delete_courier_from_db, update_into_product_db, welcome_title

product = []
courier = []
orders = []

product = read_csv_file('product_list.csv', product)
courier = read_csv_file('courier_list.csv', courier)
orders = read_csv_file('orders.csv', orders)

order_status = ['Order Confirmed', 'Preparing', 'Quality Check', 'On Route', 'Delivered', 'Unable to Deliver']

welcome_title()
def main_menu():
    whitespace()
    print('\033[96m\n\tMain Menu:\033[0m')
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
        print_formatted_text(HTML('<i> \tThanks for visiting!</i>'))
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


def product_menu()
    whitespace()
    print("""\033[96m\n\tProduct Options:\033[0m""")
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
        print('\033[95m\n\tHere is the Product Menu: \033[0m')
        read_products_db()

        new_product = input('\033[95m\n\tPlease Add A New Product To The List : \033[0m')
        new_price = float(input('\033[95m\n\tPlease Enter Desired Price: \033[0m'))
        new_product_db(new_product, new_price)
        
        print('\033[94m\n\tHere Is The New Product Menu: \033[0m')
        read_products_db()
        product_menu()
    
    elif user_input == 3:
        whitespace()
        print('\033[95m\n\t Here Is A List of The Current Product Menu: \033[0m')
        read_products_db()
        product_id = int(input('\033[96m\n\t Choose The Product ID: \033[0m'))
        new_product = input('\033[96m\n\t Enter A Name For Your Product: \033[0m')
        new_price = (input('\033[96m\n\t Enter A Price: \033[0m'))

        update_into_product_db(new_product, new_price, product_id)
        print('\033[95m\n\t Here is the updated menu: \033[0m')
        read_products_db()
        product_menu()

    elif user_input == 4:
        print('\033[95m\n\tHere is the Product Menu:\033[0m')
        read_products_db()
                
        deleted_input = int(input('\033[96m\n\tSelect a product to delete: \033[0m'))
                
        delete_product_from_db(deleted_input)
                    
        print('\033[95m\n\t Here is the new product menu: \033[0m')
        read_products_db()
        product_menu()
    
    else:
        print ('\tPlease enter a valid option')
        whitespace()
        product_menu()   
    


def courier_menu():
    whitespace()
    print("""\033[96m\n\tCourier Options:\033[0m""")
    print('''
        [0] - Return to Main Menu
        [1] - Print Courier List
        [2] - Create New Courier
        [3] - Update Courier
        [4] - Delete Courier
                        ''')
    user_input = int(input("""\033[33m\n\tEnter your choice here:  \033[0m"""))

    if user_input == 0:    
        main_menu()
    
    elif user_input == 1:
        read_courier_db()
        courier_menu()
    
    elif user_input == 2:
        print('\033[95m\n\tHere is the Courier List: \033[0m')
        read_courier_db()
        
        new_courier = input('\033[95m\n\tPlease Enter The Name of the Courier : \033[0m')
        new_number = (float(input('\033[95m\n\tPlease Enter Their Number: \033[0m')))
        new_courier_db(new_courier, new_number)
        
        print('\033[94m\n\tHere Is The New Courier List: \033[0m')
        read_courier_db()
        courier_menu()
        
        
    elif user_input == 3:
        print('\033[95m\n\t Here Is The Courier List: \033[0m')
        read_courier_db()
        courier_id = int(input('\033[96m\n\t Choose Courier ID: \033[0m'))
        new_courier = input('\033[96m\n\t Enter A New Courier Name: \033[0m')
        new_number = (input('\033[96m\n\t Enter A New Courier Number: \033[0m'))

        update_into_courier_db(new_courier, new_number, courier_id)
        print('\033[95m\n\t Here Is The Updated Courier List: \033[0m')
        read_courier_db()
        courier_menu()

    elif user_input == 4: 
        print('\033[95m\n\tHere Is The Courier List:\033[0m')
        read_courier_db()
        
        deleted_input = int(input('\033[96m\n\tSelect A Courier To Delete: \033[0m'))
        
        delete_courier_from_db(deleted_input)
                    
        print('\033[95m\n\t Here Is The New Courier List: \033[0m')
        read_courier_db()
        courier_menu()
        
    else:
        print ('\tPlease enter a valid option')
        whitespace()
        courier_menu()   


def orders_details():
    whitespace()
    print('\033[96m\n\tOrder Details:\033[0m')
    print('''
        [0] - Return to Main Menu
        [1] - View Orders
        [2] - Create A New Order
        [3] - Update Order Status  
        [4] - Update Existing Order
        [5] - Delete Order
        ''')
    user_input = int(input('\033[33m\n\tEnter your choice here: \033[0m'))
    
    
    if user_input == 0:
        main_menu()

    elif user_input == 1:
        whitespace()
        #for key, value in enumerate(orders):
        #   print(f'Order Number - {key}{value}\n\t')
        print(json.dumps(orders, sort_keys=False, indent=4))
        orders_details()

    elif user_input == 2:
        customer_name = input("\tEnter your name: ")
        customer_address = input("\tEnter your address: ")
        customer_number = int(input("\tEnter your number: "))
        whitespace()
        for value, index in enumerate(product):
            print(value, index)
            
        product_choice = input('Please select your products: ')
        
        whitespace()
        for value, index in enumerate(courier):
            print(value, index)
        courier_choice = int(input('Who would you like to deliver your order:?  '))
        
        entry = {}
        entry['Customer Name'] = customer_name 
        entry['Customer Address'] = customer_address
        entry['Customer Phone Number'] = customer_number
        entry['Courier'] = courier_choice
        entry['Status'] = order_status[1]
        entry['Products'] = product_choice
        
        titles = ['Customer Name', "Customer Address", 'Customer Phone Number','Courier', 'Status', "Products"]
        append_dict('orders.csv', entry, titles)
        whitespace()
        print(entry)
        whitespace()
        # print(orders)
        #whitespace()
        print('Thank you for your order')
        # print(json.dumps(entry, sort_keys=False, indent=4))
        orders_details()

    elif user_input == 3:
        for key, value in enumerate(orders):
            print(f'Order Number - {key}{value}\n\t')
        order_index = int(input("""\033[33m\nPlease select an order to update:   \033[0m"""))
        print('')

        for key, value in enumerate(order_status):
            print(key, value)

        status_input = int(
            input("""\033[33m\nChoose an order status to update on the order list:   \033[0m"""))
        order_to_update = orders[order_index]
        
        order_to_update['Status'] = order_status[status_input]
        print("""\033[33m\nOrder status has been updated
            The New Order List is: \033[0m""")
        
        print(json.dumps(orders, sort_keys=False, indent=4))
        orders_details()

    elif user_input == 4:
        for key, value in enumerate(orders):
            print(f'Order Number - {key}{value}\n\t')
            
        order_index = int(input(''' \033[33m\n\tSelect an order to update:    \033[0m'''))
        updated_order = orders[order_index] 
        old_order = updated_order.copy()
        
        for key, value in updated_order.items():
            print(key, value)
            chosen_order = input(f'\nThe {key} is currently {value}. Enter new details for {key}: ')
            if chosen_order == '':
                updated_order[key] = value
                print_formatted_text(HTML('<b> Nothing Has Been Changed </b>'))
                whitespace()
            else:
                updated_order[key] = chosen_order
                whitespace()
        
        # print(f'\n\tYour order has been updated from {old_order} to {updated_order}')

        print('\033[95m\n\tYour order has been updated from: \033[0m')
        print(old_order)
        
        print('\033[95m\n\t TO: \033[0m')
        
        print(updated_order)
        
        orders_details()

    elif user_input == 5:
        for key, value in enumerate(orders):
            print(f'Order Number - {key}{value}\n\t')
        delete_order = int(input('''
        \033[33m\n\tSelect an order to delete:    \033[0m''')) 
        orders.pop(delete_order)
        print('''\033[33m\n\tOrder was deleted successfully.\033[0m''')
        whitespace()
        print('''\033[33m\n\tRemaining Orders: \033[0m''')
        
        print(json.dumps(orders, sort_keys=False, indent=4))
        whitespace()
        orders_details()
    
    else:
        print ('\tPlease enter a valid option')
        whitespace()
        orders_details()   
main_menu()
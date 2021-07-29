from mini_project_functions import whitespace, read_csv_file, print_csv_file, save_csv_file, append_dict, update_items
from csv import DictWriter, DictReader
from pprint import pprint

product = []
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
        whitespace()
        pprint(product)
        whitespace()
        product_menu()
    
    elif user_input == 2:
        whitespace()
        print("""\033[33m\n\tThe current menu is: \033[0m""")
        print_csv_file('product_list.csv')
        whitespace()
        new_product = input("""\033[33m\n\tWhat would you like to create?  \033[0m""")
        product_price = float(input("""\033[33m\n\tEnter a price:   \033[0m"""))
        new_product_dict = {}
        new_product_dict['Product'] = new_product
        new_product_dict['Price'] = product_price
        product.append(new_product_dict)
        field_names = ['Product', 'Price']
        append_dict('product_list.csv', new_product_dict, field_names)
        print("""\033[33m\n\tYour new product has been created!\033[0m""")
        print(new_product_dict)
        whitespace()
        product_menu()
    
    elif user_input == 3:
        print("""\033[33m\n\tThe products available are:  \033[0m""")
        for key, value in enumerate(product):
            print(key, value)
            
        number_input = int(
            input("""\033[33m\n\tEnter the number of the product you wish to replace: \033[0m"""))
        new_variable = product[number_input]
        update_items(new_variable)

        print("""\033[33m\nHere's the new updated products menu: ", \033[0m""") 
        pprint(product)
        whitespace()
        product_menu()
        
    elif user_input == 4:
        print("""\033[33m\n\nLets delete a product\033[0m""")
        for key, value in enumerate(product):
                print(key, value)
        deleted_input = int(
            input("""\033[33m\nPlease Select The Number Of The Product You Want To Delete:  \033[0m"""))       
        del product[deleted_input]
        print("""\033[33m\nThe New Product List Is :\033[0m""") 
        pprint(product)
        whitespace()
        product_menu()
        
    else:
        whitespace()
        print ('Please enter a valid option')
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
        whitespace()
        pprint(courier)
        whitespace()
        courier_menu()  
    
    elif user_input == 2:
        whitespace()
        print("""\033[33m\n\tThe current courier list is: \033[0m""")
        print_csv_file('courier_list.csv')
        whitespace()
        new_courier_name = input("What's the name of the new courier?  ")
        new_courier_number = int(input("What is their number:   "))
        new_courier_dict = {}
        new_courier_dict['Name'] = new_courier_name
        new_courier_dict['Number'] = new_courier_number
        courier.append(new_courier_dict)
        field_names = ['Name','Number']
        append_dict('courier_list.csv', new_courier_dict, field_names)
        print("""\033[33m\n\tYour new courier has been created!\033[0m""")
        print(new_courier_dict)
        whitespace()
        courier_menu()
    
    elif user_input == 3:
        print("""\033[33m\n\tThe couriers available are:  \033[0m""")
        for key, value in enumerate(courier):
            print(key, value)
            
        number_input = int(
            input("""\033[33m\n\tSelect the number of the courier you wish to replace: \033[0m"""))
        new_variable = courier[number_input]
        update_items(new_variable)

        print("""\033[33m\nHere's the new updated courier options:  \033[0m""")
        pprint(courier)
        whitespace()
        courier_menu()  
    
    elif user_input == 4:
        print("""\033[33m\n\nLets delete a courier\033[0m""")
        for key, value in enumerate(courier):
                print(key, value)
        deleted_input = int(
            input("""\033[33m\nSelect The Number Of The Courier You Wish To Delete : \033[0m"""))       
        del product[deleted_input]
        whitespace()
        print("""\033[33m\nThe New Courier List Is :\033[0m""")
        pprint(courier)
        whitespace()
        courier_menu()
        
    else:
        whitespace()
        print ('Please enter a valid option')
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
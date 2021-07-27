from pprint import pprint
from mini_project_functions import whitespace, read_csv_file, print_csv_file, dict_append
from csv import DictWriter, DictReader

product = []
# courier = []
# orders = []

product = read_csv_file('product_list.csv', product)
# courier = read_csv_file('courier_list.csv', courier)
# orders = read_csv_file('order.csv', orders)



order_status = ['Order Confirmed', 'Preparing', 'Quality Check', 'On Route', 'Delivered', 'Unable to Deliver']


def main_menu():
    print("""\033[33m\n\tMain Menu:\033[0m""")
    print("""
        [0] - To Exit 
        [1] - Product Options
        [2] - Courier Options
        [3] - Order Details
    """)
    

    option = int(input('    Enter your choice here: '))
    
    if option == 0:
        with open('Product_list.txt', 'w') as save_p_file:
            for save_i in product_list:
                save_p_file.write(save_i + '\n')
        with open('Courier_list.txt', 'w') as save_c_file:
            for save_w in courier_list:
                save_c_file.write(save_w + '\n')
        print('Thanks for visiting!')
        exit
        
    elif option == 1:
        product()   
    
    elif option == 2:
        courier()
    
    elif option == 3:
        orders_details()
    
    

def product():
    print("""\033[33m\n\tProduct Options:\033[0m""")
    print('''
        [0] - Return to Main Menu
        [1] - View Menu
        [2] - Create New Product
        [3] - Update Existing Product    
        [4] - Delete a Product''')
    user_input = int(input('\n Enter your choice here:'))
    
    if user_input == 0:
        print('Thanks for visiting!')
        exit
        
        
    elif user_input == 1:
        print_csv_file('product_list.csv', product)
        whitespace()
        main_menu()
        
        
        
    elif user_input == 2:
        print("The current menu is: ", product)
        new_product = input("What would you like to create?  ")
        product_price = float(input("Enter a price:   "))
        new_product_dict = {}
        new_product_dict['Product'] = new_product
        new_product_dict['Price'] = product_price
        product.append(new_product_dict)
        field_names = ['Product', 'Price']
        dict_append('product_list.csv', new_product_dict, field_names)
        print('Your new product has been created!')
        print_product()
    
    
    
main_menu()
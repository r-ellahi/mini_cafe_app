from mini_project_functions import whitespace, read_csv_file, print_csv_file, save_csv_file, append_dict, update_items
from csv import DictWriter, DictReader

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
        print('Thanks for visiting!')
        exit()
        
    elif option == 1:
        product_menu()   
    
    elif option == 2:
        courier()
    
    elif option == 3:
        orders_details()
        
        
def product_menu():
    print("""\033[33m\n\tProduct Options:\033[0m""")
    print('''
        [0] - Return to Main Menu
        [1] - View Menu
        [2] - Create New Product
        [3] - Update Existing Product    
        [4] - Delete a Product''')
    user_input = int(input("""\033[33m\n\tEnter your choice here: \033[0m"""))
        
        
    if user_input == 0:
        whitespace()
        save_csv_file('product_list.csv', product)
        print('Thanks for visiting!')
        whitespace()
        exit
        
        
    elif user_input == 1:
        whitespace()
        print_csv_file('product_list.csv', product)
        main_menu()
    
    elif user_input == 2:
        whitespace()
        print("The current menu is: ")
        print_csv_file('product_list.csv')
        whitespace()
        new_product = input("What would you like to create?  ")
        product_price = float(input("Enter a price:   "))
        new_product_dict = {}
        new_product_dict['Product'] = new_product
        new_product_dict['Price'] = product_price
        product.append(new_product_dict)
        field_names = ['Product', 'Price']
        append_dict('product_list.csv', new_product_dict, field_names)
        print('Your new product has been created!')
        print(new_product_dict)
    
    elif user_input == 3:
        print("""\033[33m\n\tThe products available are:  \033[0m""")
        for key, value in enumerate(product):
            print(key, value)
            
        number_input = int(
            input("""\033[33m\n\tChoose a product by selecting the number and replace with your choice: \033[0m"""))
        new_variable = product[number_input]
        update_items(new_variable)

        print("""\033[33m\nHere's the new updated products menu: ", product \033[0m""", product)

        
    elif user_input == 4:
        print([list((i, product[i]))
            for i in range(len(product))])
        whitespace()
        delete_product_index_value = int(
            input("""\033[33m\nPlease Enter The Index value Of The Product You Want To Delete : \033[0m"""))
        whitespace()
        del product[delete_product_index_value]
        print("""\033[33m\nThe New Product List Is :\033[0m""", product)

main_menu()
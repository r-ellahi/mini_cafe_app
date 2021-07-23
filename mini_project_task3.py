import pprint
product_list = []
with open('product_list.txt') as load_p_file:
    for load_i in load_p_file:
        product_list.append(load_i.rstrip())


courier_list = []
with open('courier_list.txt') as load_c_file:
    for load_w in load_c_file:
        courier_list.append(load_w.rstrip())

        
def main_menu():
    print("""\033[33m\n\tMain Menu:\033[0m""")
    print("""
        [0] -  To Exit 
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
        main_menu()
        
    elif user_input == 1:
        print(product_list)
        product()
        
    elif user_input == 2:
        print("The current menu is: ", product_list)
        new_product = input("What would you like to create? ")
        product_list.append(new_product)
        print('Your new product has been created!')
        print(product_list)
    
    elif user_input == 3:
        for value, index in enumerate(product_list):
            print(value, index)
        product_index_value = int(input('Which product would you like to update?'))
        new_product = input('What is the name of the new product?')
        
        product_list[product_index_value] = new_product
        print(product_list)
        
    elif user_input == 4:
        print([list((i, product_list[i]))
            for i in range(len(product_list))])
        delete_product_index_value = int(
            input("Please Enter The Index value Of The Product You Want To Delete : "))
        
        del product_list[delete_product_index_value]
        print("The New Product List Is :", product_list)


def courier():
    print("""\033[33m\n\tCourier Options:\033[0m""")
    print('''
        [0] - Return to Main Menu
        [1] - Print Courier List
        [2] - Create New Courier
        [3] - Update Courier
        [4] - Delete Courier
                        ''')
    user_input = int(input('\n Enter your choice here:'))

    if user_input == 0:
        print('Thank you for visiting')
        main_menu()
    
    elif user_input == 1:
        print(courier_list)
        courier()
    
    elif user_input == 2:
        print("The current couriers are: ", courier_list)
        new_courier = input("Please enter a new courier name: ")
        courier_list.append(new_courier)
        print('Your new courier has been created!')
        print(courier_list)
        
        
    elif user_input == 3:
        for value, index in enumerate(courier_list):
            print(value, index)
        courier_index_value = int(input('Which courier would you like to update?'))
        new_courier = input('What is the name of the new courier?')
        courier_list[courier_index_value] = new_courier
        print(courier_list)
        
        
    elif user_input == 4:
        print([list((i, courier_list[i]))
        for i in range(len(courier_list))])
        delete_courier_index_value = int(
        input("Please Enter The Index value Of The Courier You Want To Delete : "))
        del courier_list[delete_courier_index_value]
        print("The New Courier List Is :", courier_list)

order_status = ['Order Confirmed', 'Preparing', 'Quality Check', 'On Route', 'Delivered', 'Unable to Deliver']

order_list = [
    {
        "Customers' Name": 'John', 
        "Customers' Address": 'Unit 2, 12 Main Street, LONDON, WH1 2ER',
        "Customers' Phone Number": '0789887334',
        "Courier": [courier_list[2]],
        "Status": [order_status[3]]
    }, 
    
    {
        "Customers' Name": 'Serena', 
        "Customers' Address": 'The Moat, 73 Alley Street, LONDON, HA6 9DW',
        "Customers' Phone Number": '07648298501',
        "Courier": [courier_list[0]],
        "Status": [order_status[2]]
    }
]              



def orders_details():
    print("""\033[33m\n\tOrder Details:\033[0m""")
    user_input = int(input('''
        [0] - Return to Main Menu
        [1] - View Order
        [2] - Enter Details
        [3] - Update Order Status  
        [4] - Update Existing Order
        [5] - Delete Courier
        
        Enter your choice here:    '''))
    
    if user_input == 0:
        main_menu()
        
    elif user_input == 1:
        print(order_list)

    elif user_input == 2:
        entry = {}
    
        customer_name = input("Enter your name: ")
        customer_address = input("Enter your address: ")
        customer_number = int(input("Enter your number: "))
        
        for value, index in enumerate(courier_list):
            print(value, index)
        courier_choice = int(input('Please select your courier: '))

        entry['customer_name'] = customer_name 
        entry ['customer_address'] = customer_address
        entry ['customer_number'] = customer_number
        entry ['courier'] = courier_choice
        entry['status'] = order_status[1]
        order_list.append(entry)
        print(order_list) 
    
    elif user_input == 3:
        for key, value in enumerate(order_list):
            print(key, value)

        order_index = int(input("""\033[33m\nPlease select an order to update:   \033[0m"""))
        print('')

        for key, value in enumerate(order_status):
            print(key, value)

        status_input = int(
            input("""\033[33m\nChoose an order status to update on the order list:   \033[0m"""))
        order_to_update = order_list[order_index]
        
        order_to_update['Status'] = order_status[status_input]
        print("""\033[33m\nOrder status has been updated\033[0m""")
        print(order_to_update)
        
    
    elif user_input == 4:
        for key, value in enumerate(order_list):
            print(key, value)
        order_index = input('''
        \033[33m\n\tSelect and order to update:    \033[0m''')
        
        for key, value in (order_index):
            if user_input ==():
                orders_details()
            
            # else: 
    
#     FOR EACH key-value pair in selected order:
#     GET user input for updated property
#     IF user input is blank:
#     do not update this property
#     ELSE:
#     update the property value with user input

        
        
        
        
main_menu()



# # ELSE IF user input is 5:
# #     # STRETCH GOAL - DELETE courier
# #     PRINT orders list
# #     GET user input for order index value
# #     DELETE order at index in order list
    
# main_menu()
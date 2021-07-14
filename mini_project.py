product_list = ['Chicken', 'Beef', 'Fish', 'Fries', 'Salad', 'Eggs']
courier_list = ['Alex', 'William', 'Tom', 'David', 'Harry', 'Usain']

def main_menu():
    option = int(input('''
        To Exit select 0
        To Enter select 1
        Enter your choice here: 
            '''))
    if option == 0:
        print('Thanks for visiting!')
        exit
        
    elif option == 1:
        product()   
    
    elif option == 2:
        courier()
    
    # elif option == 3:
    #     dictionary()


def product():
    user_input = int(input('''
        Return to Main Menu: 0
        View Menu: 1
        Create New Product: 2
        Update Existing Product: 3    
        Delete a Product: 4
        Enter your choice here: '''))
    
    if user_input == 0:
        main_menu()
        
    elif user_input == 1:
        print(product_list)
        
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
    user_input = int(input('''
        Return to Main Menu: 0
        Print Courier List: 1
        Create New Courier: 2
        Update Courier:
        Delete Courier: 4
                        '''))
    
    if user_input == 0:
        print('Thank you for visiting')
        main_menu()
    
    elif user_input == 1:
        print(courier_list)
    
    elif user_input == 2:
        
        
    # elif user_input == 3:
        
    # elif user_input == 4:
        
    

        
#     ELSE IF user input is 2:
#         # CREATE new courier
#         GET user input for courier name
#         APPEND courier name to couriers list
    
    
#     ELSE IF user input is 3:
#         # STRETCH GOAL - UPDATE existing courier
#         PRINT courier names with its index value
#         GET user input for courier index value
#         GET user input for new courier name
#         UPDATE courier name at index in couriers list
    
    
#     ELSE IF user input is 4:
#         # STRETCH GOAL - DELETE courier
# PRINT courier list
# GET user input for courier index value
# DELETE courier at index in courier list

# main_menu()
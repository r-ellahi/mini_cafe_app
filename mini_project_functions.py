import csv


def whitespace():
    print('\n')
    


#READ FILES 
def read_csv_file (file_name, csv_to_read):
    with open (file_name, 'r') as csv_file:
        csv_to_read = csv.DictReader(csv_file)
        csv_list = []
        for row in csv_to_read:
            csv_list.append(row) 
        return csv_list


#Print files
with open('Product_list.csv', 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(row)



#Dictionary Append
def dict_append(file_name, dict_elements, field_names):
    with open (file_name, 'a+', newline= '') as dict_append_file:
        dict_writer = DictWriter(dict_append_file, fieldnames = field_names)
        dict_writer.writerow(dict_elements)





# def print_product():
#     with open('product_list.csv','r+') as f:
# 	    lines=f.read().splitlines()
# 	    print(lines)



# def print_csv_file(csv_file):
#     for key, value in enumerate(csv_file):
#         print(key, value)
#     return key, value

# def print_csv_file (file_name, csv_to_read):
#     with open (file_name, 'r') as csv_file:
#         csv_to_read = csv.DictReader(csv_file)
#         csv_list = []
#         for row in csv_to_read:
#             csv_list.append(row) 
#         print(csv_list)
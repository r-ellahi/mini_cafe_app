import csv

with open('product_list.csv', 'r') as products:
    csv_reader = csv.DictReader(products)
    for prod in csv_reader:
        # print(prod)
        
    with open('courier_list.csv', 'r') as couriers:
        csv_reader = csv.DictReader(couriers)
    for cour in csv_reader:
        # print(cour)

with open('orders.csv', 'r') as orders:
    csv_reader = csv.DictReader(orders)
    for ord in csv_reader:
        # print(ord)


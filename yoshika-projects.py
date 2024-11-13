# 1. Users Data Structure
users = [
    {"id": 1, "username": "admin", "password": "admin123", "role": "admin"},
    {"id": 2, "username": "john", "password": "john123", "role": "customer"},
]

# 2. Products Data Structure
products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "stock": 10},
    {"id": 2, "name": "Smartphone", "price": 499.99, "stock": 15},
    {"id": 3, "name": "Headphones", "price": 99.99, "stock": 20},
]

# 3. Cart Data Structure
cart = [{"user_id": 2, "product_id": 1, "quantity": 2}]

# 4. Orders Data Structure
orders = [
    {
        "id": 1,
        "user_id": 2,
        "items": [{"product_id": 1, "quantity": 2}],
        "date": "2024-11-12 10:30:45",
        "total": 1999.98,
    }
]


# 1. Main Menu
# def mainMenu():
#     print(
#         """
#         === E-commerce Management System ===
#         1. Login
#         2. Exit
#             """
#     )

#     while True:
#         num = int(input("Enter your choice: "))

#         if num == 1:
#             print("welcome")
#         else:
#             print("Bye")
#             break


# mainMenu()

# 4. Product Display (Using tabulate)
from tabulate import tabulate

print("=== Products ===")
print(tabulate(products, headers="keys", tablefmt="pretty"))

# 5. Cart Display

# from tabulate import tabulate

# def cartDisplay():
#     === Your Cart ===


# +-----------+----------+---------+---------+
# | Product   | Quantity | Price   | Total   |
# +===========+==========+=========+=========+
# | Laptop    | 2        | $999.99 | $1999.98|
# +-----------+----------+---------+---------+

# Total Amount: $1999.98


# cart =[
# {"product": product, "quantity": quantity, "price": price, "Total":total},
# ]
# print(tabulate(cart, headers='keys', tablefmt='pretty'))

# print("Total Amount: "total)

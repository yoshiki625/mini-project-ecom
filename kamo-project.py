from tabulate import tabulate

# 1. Users Data Structure

users = [
    {"id": 1, "username": "admin", "password": "admin123", "role": "admin"},
    {"id": 2, "username": "john", "password": "john123", "role": "customer"},
]

# 2. Products Data Structure

products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "stock": 10},
    {"id": 2, "name": "Smartphone", "price": 499.99, "stock": 15},
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

# 2. Admin Menu After Login


def AdminMenuAfterLogin():

    while True:
        print(
            """Welcome, admin!

        1. Manage Products
        2. View All Products
        3. Logout

          """
        )

    choice = int(input("Enter your choice:"))

    if choice == 1:
        print("1")
    elif choice == 2:
        print("2")
    else:
        print("3")


# 4. Product Display (Using tabulate)


def productDisplay():

    print("=== Your Cart ===")
    print(tabulate(products, headers="keys", tablefmt="pretty"))


# productDisplay()


# 6. Order History Display
def orderHistoryDisplay():
    print(
        f"""=== Order History ===
Order ID : {orders["id"]}
Date: {orders["date"]}"""
    )
    print(tabulate(orders, headers="keys", tablefmt="pretty"))


# orderHistoryDisplay()

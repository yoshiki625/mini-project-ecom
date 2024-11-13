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

def login():
    username = input("username : ")
    password = input("password : ")

    user_info = {
                    "user" : username,
                    "pass" : password,
                    "role" : ""
                    }
    for user in users:
        if user["username"] == username and user["password"] == password:
                user_info = {
                    "user" : username,
                    "pass" : password,
                    "role" : user["role"]
                    }
    return user_info

# 1. Main Menu
def mainMenu():
    print(
        """
        === E-commerce Management System ===
        1. Login
        2. Exit
            """
    )

    num = int(input("Enter your choice: "))

    if num == 1:
        user_info = login()
        if user_info["role"] == "admin":
            AdminMenuAfterLogin()
        elif user_info["role"] == "customer":
            customer_menu_after_login(user_info) # TODO
        else :
            print(f"there is no user : {user_info["user"]}")
    else:
        print("Bye")

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
            print("Bye")
            break

# 3. Customer Menu After Login
def customer_menu_after_login(user_info):
    # for i in range(len(books)) :
    print(f"Welcome, {user_info["user"]}!")
    print(
        """\
1. View Products
2. Add to Cart
3. View Cart
4. Checkout
5. Order History
6. Logout"""
    )
    choice = int(input("Enter your choice:"))
    if choice == 1:
        productDisplay()
    elif choice == 5:
        orderHistoryDisplay()
    else:
        print("")

# 4. Product Display (Using tabulate)

def productDisplay():

    print("=== Products ===")
    print(tabulate(products, headers="keys", tablefmt="pretty"))

# 5. Cart Display
def cart_display(user_id):
    _, product_id, quantity = [
        detail for detail in cart if detail["user_id"] == user_id
    ]
    # head = ["Product","Quantity","Price","Total" ]

    # body ={"Product": }

# 6. Order History Display
def orderHistoryDisplay():
    print(
        f"""=== Order History ===
Order ID : {orders["id"]}
Date: {orders["date"]}"""
    )
    print(tabulate(orders, headers="keys", tablefmt="pretty"))



mainMenu()
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


# 3. Customer Menu After Login
def customer_menu_after_login(user_id):
    # for i in range(len(books)) :
    index_no = [i for i in range(len(users)) if users[i]["id"] == user_id]
    print(f"Welcome, {users[index_no]["username"]}!")
    print(
        """\
1. View Products
2. Add to Cart
3. View Cart
4. Checkout
5. Order History
6. Logout"""
    )
    return int(input("Enter your choice:"))


customer_menu_after_login(2)


# 5. Cart Display
def cart_display(user_id):
    _, product_id, quantity = [
        detail for detail in cart if detail["user_id"] == user_id
    ]
    # head = ["Product","Quantity","Price","Total" ]

    # body ={"Product": }

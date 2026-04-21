import re

users = {}

def is_valid_password(password):
    if (len(password) >= 6 and
        re.search("[A-Z]", password) and
        re.search("[a-z]", password) and
        re.search("[0-9]", password)):
        return True
    return False

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if is_valid_password(password):
        users[username] = password
        print("Registration successful!")
    else:
        print("Password must have uppercase, lowercase, number and be 6+ chars")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid credentials")

while True:
    print("\n1.Register 2.Login 3.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        break
    else:
        print("Invalid choice")

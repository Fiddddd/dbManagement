import functions
from functions import addVal
import hashlib

print("Sample")
print("-----------")
while True:
    email = input("Enter your email id: ")
    if email.count("@gmail.com") != 1:
        print("Invalid email.")
    else:
        break
while True:
    password = input("Enter your password: ")
    if password.count(" ") != 0:
        print("Invalid password, try again.")
    else:
        encoded = hashlib.sha256(password.encode()).hexdigest()
        password = encoded
        break

first_name = input("Enter your first name:")
last_name = input("Enter your last name: ")


addVal(email, password, first_name.capitalize(), last_name.capitalize())



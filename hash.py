import hashlib
import connection


def hash_pw(pw):
    encoded = hashlib.sha256(pw.encode()).hexdigest()
    return encoded


def get_pw():
    pw = input("Enter the password to be stored: ")
    return hash_pw(pw)


if connection.status():
    hashed = get_pw()
    check = get_pw()

    if hashed == check:
        print("Login successful!")
    else:
        print("Invalid credentials!")

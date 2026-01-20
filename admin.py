import connection
import functions

def admin():
    while True:
        print("Admin Panel")
        print("--------------")
        print("SELECT OPERATION")
        print("---------------")
        print("1. Remove User")
        print("2. View Data Stored")
        print("3. Delete Database")
        print("4. Exit")
        print("---------------")
        choice = input("Enter operation number: ")

        if choice == 1:
            functions.removeVal()
        if choice == 2:
            functions.viewDB()
        if choice == 3:
            functions.removeDB()
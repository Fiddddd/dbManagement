import psycopg2
from psycopg2 import OperationalError


def status():
    pw = input("Enter password for user: ")
    try:
        conn = psycopg2.connect(
            database= "postgres",
            user= "postgres",
            host= "localhost",
            password= f"{pw}",
            port=5432
        )
        print("connected successfully.")

        return conn
    except OperationalError:
        print("Connection failed.")


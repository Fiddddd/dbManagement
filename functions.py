import connection
import psycopg2


def viewDB():
    pass

def addVal(email, password, first_name, last_name):
    conn = connection.status()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO users(email, password, first_name, last_name)
        VALUES (%s, %s, %s, %s)
        """,
        (email, password, first_name, last_name)
    )
    conn.commit()
    cur.close()
    conn.close()

    print("User added successfully!")


def removeVal():
    pass

def admin():
    pass

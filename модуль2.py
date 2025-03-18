from sqlite3 import *
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = connect(path)
        print("Uhendus on edukalt tehtud")
    except Error as e:
        print(f"Tekkis viga'{e}'")
    return connection

conn=create_connection("C:/Users/38096/Desktop/Python/Database/SQLite/SQLite.db")

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel on loodud")
    except Error as e:
        print(f"Viga'{e}' tabeli loomisega")

        create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        nationality TEXT
        );
        """
        execute_query(conn, create_users_table)

        def execute_read_query(connection, query):
            cursor = connection.cursor()
            result = None
            try:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
            except Error as e:
                print(f"Viga'{e}'")

     create_users= """
        INSERT INTO
        users(name,age,gender,nationality)
        VALUES
        ('James',25,'mees','USA'),
        ('Leila',32,'naine','Prantsusmaa'),
        ('Henry',20,'mees','UK'),
        ('Jane',22,'naine','USA');
        """
execute_query(conn, create_users)
select_users= "SELECT * from users"
users = execute_read_query(conn, select_users)
for user in users:
        print(user)


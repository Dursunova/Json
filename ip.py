import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1707",
)

if connection.is_connected():
    print("Successfully connected to MySQL database")

    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS my_db")
    cursor.execute("USE my_db")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Computer (
        ID INT PRIMARY KEY,
        Name VARCHAR(255),
        IP VARCHAR(255)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS User (
        ID INT PRIMARY KEY,
        First_name VARCHAR(255),
        Last_name VARCHAR(255),
        Computer_id INT,
        FOREIGN KEY (Computer_id) REFERENCES Computer(ID)
    )
    """)

    cursor.execute("INSERT INTO Computer (ID, Name, IP) VALUES (1, 'first', '10.0.1.2')")
    cursor.execute("INSERT INTO Computer (ID, Name, IP) VALUES (2, 'second', '10.0.1.3')")
    
    cursor.execute("INSERT INTO User (ID, First_name, Last_name, Computer_id) VALUES (1, 'Nergiz', 'Dursunova', 1)")
    cursor.execute("INSERT INTO User (ID, First_name, Last_name, Computer_id) VALUES (2, 'Mira', 'Aliyeva', 1)")
    cursor.execute("INSERT INTO User (ID, First_name, Last_name, Computer_id) VALUES (3, 'Zarifa', 'Orucova', 2)")
    cursor.execute("INSERT INTO User (ID, First_name, Last_name, Computer_id) VALUES (4, 'Farah', 'Asadli', 2)")

    connection.commit()

    cursor.close()
    connection.close()
else:
    print("Connection failed")

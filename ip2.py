import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1707",
    database="my_db"  
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM User")
users = cursor.fetchall()
print("All Users:")
for user in users:
    print(user)

cursor.execute("""
SELECT COUNT(*) AS User_Count
FROM User
JOIN Computer ON User.Computer_id = Computer.ID
WHERE Computer.Name = 'first'
""")
count_result = cursor.fetchone()
print(f"\nNumber of users with access to first: {count_result[0]}")

cursor.execute("""
SELECT User.First_name, User.Last_name, Computer.Name, Computer.IP
FROM User
JOIN Computer ON User.Computer_id = Computer.ID
WHERE User.ID = 4
""")
fourth_user = cursor.fetchone()
print("\n4th User's Details:", fourth_user)


cursor.execute("""
SELECT User.First_name, User.Last_name
FROM User
JOIN Computer ON User.Computer_id = Computer.ID
WHERE Computer.ID = 2
""")
second_computer_users = cursor.fetchall()
print("\nUsers with access to second:")
for user in second_computer_users:
    print(user)

cursor.close()
connection.close()

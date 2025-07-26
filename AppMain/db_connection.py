import mysql.connector

cnn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "30696222",
    database = "DB_Inventory"
)


cur = cnn.cursor()
cur.execute('SELECT * FROM usersTable')
data = cur.fetchall() 
for i in data:
    print(i)
 
import mysql.connector

cnn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "30696222",
    database = "DB_Inventory"
)

cur = cnn.cursor()
id = 18
cur.execute(f'DELETE FROM Inventtorytable WHERE product_id = {id}')
table_view = cur.execute('SELECT * FROM Inventtorytable')
cnn.commit()

print(table_view)

 
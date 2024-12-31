import mysql.connector

cnn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "30696222",
    database = "DB_Inventory"
)

cur = cnn.cursor()
product_id = 0
item = 'Onions'
quantity = 1
kg_or_lt = 0.245
price = 169.05
notes = 'Regular Purchase'
cur = cnn.cursor()
cur.execute('INSERT INTO Inventtorytable (product_id, item, quantity, kg_or_lt, price, notes) VALUES(%s, %s, %s, %s, %s, %s)',  (product_id, item, quantity, kg_or_lt, price, notes))
cnn.commit()

 
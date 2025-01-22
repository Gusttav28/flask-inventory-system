from flask import Flask, render_template, redirect, url_for, request, flash
import mysql.connector

class app:
    def __init__(self, appFlaskName):
        self.appFlaskName = appFlaskName


        # Constructure of flask

        self.appFlaskName = Flask(__name__)

        self.route_home = "/"
        self.route_aboutThe_project = "/aboutThe_project"
        self.route_table = "/table"
        self.route_login = "/login"
        self.route_itemView = "/itemView"
        self.route_addItem = "/addItem"
        self.route_editItem = "/editItem/<id>"
        self.route_itemUpdate = "/itemUpdate"
        self.route_itemDelete = "/itemDelete/<id>"

        self.appFlaskName.secret_key = "mysecrettkey"


        self.cnn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "30696222",
            database = "DB_Inventory"
        )

    def app_main(self):
        self.appFlaskName.run(port=8097, debug=True)

    def app_routes(self):

        @self.appFlaskName.route(self.route_home)
        def index():
            return render_template("home.html")    
        
        @self.appFlaskName.route(self.route_aboutThe_project)
        def aboutThe_project():
            return render_template("aboutThe_project.html")    

        @self.appFlaskName.route(self.route_table)
        def table():
            # cur = self.cnn.cursor()
            # cur.execute('INSERT INTO inventorytable (product_id, ITEM, QUANTITY, KG_LT, PRICE, NOTES) VALUES(2, "ONIONS", 1, 0.245, 169, "Was 5")')
            # self.cnn.commit()
            return redirect(url_for("itemView"))    
        
        @self.appFlaskName.route(self.route_login)
        def login():
            return render_template("login.html")    
        
        @self.appFlaskName.route(self.route_itemView)
        def itemView():
            cur = self.cnn.cursor()
            cur.execute('SELECT * FROM Inventtorytable')
            data = cur.fetchall()
            for i in data:
                print(i)
            return render_template("table.html", itemInformation = data)
        
        @self.appFlaskName.route(self.route_addItem, methods=['POST', 'GET'])
        def addItem():
            try:                
                if request.method == 'POST':
                    product_id = 0
                    item = request.form['item']
                    quantity = request.form['quantity']
                    kg_or_lt = request.form['kg_or_lt']
                    price = request.form['price']
                    notes = request.form['notes']
                    print(item, quantity, kg_or_lt, price,notes)
                    cur = self.cnn.cursor()
                    cur.execute('INSERT INTO Inventtorytable (product_id, item, quantity, kg_or_lt, price, notes) VALUES(%s, %s, %s, %s, %s, %s)',(product_id, item, quantity, kg_or_lt, price, notes))
                    self.cnn.commit()
                    flash("The item was successfully add it")
                    return redirect(url_for("itemView"))
            except:
                flash("Something happens, try again")
                return redirect(url_for("itemView"))    
            return redirect(url_for("itemView"))
        
        @self.appFlaskName.route(self.route_editItem)
        def editItem(id):
            cur = self.cnn.cursor()
            cur.execute(f'SELECT * FROM Inventtorytable WHERE product_id = {id}')
            data = cur.fetchall()
            self.cnn.commit()
            print(data)
            return redirect(url_for("table", itemInformation = data[0]))
        
        @self.appFlaskName.route(self.route_itemUpdate, methods=['POST', 'GET'])
        def itemUpdate():
            try:
                if request.method == 'POST':
                    product_id = 0
                    item = request.form['item']
                    quantity = request.form['quantity']
                    kg_or_lt = request.form['kg_or_lt']
                    price = request.form['price']
                    notes = request.form['notes']
                    print(item, quantity, kg_or_lt, price,notes)
                    cur = self.cnn.cursor()
                    cur.execute(f'UPDATE Inventtorytable SET = item = %s, quantity = %s, kg_or_lt = %s, price= %s, notes = %s WHERE product_id = {id}', {item, quantity, kg_or_lt, price, notes})
                    self.cnn.commit()
                    flash("The item was successfully update it")
                    return redirect(url_for("itemUpdate"))
            except:
                flash("There was a problem with the update proccess of the item")
            return redirect(url_for("table"))
        
        @self.appFlaskName.route(self.route_itemDelete)
        def deleteItem(id):
            print("it works")
            cur = self.cnn.cursor()              
            cur.execute(f'DELETE FROM Inventtorytable WHERE product_id = {id}')
            self.cnn.commit()
            flash(f"the item with id = {id} was delete successsfully")
            return redirect(url_for("itemView"))    
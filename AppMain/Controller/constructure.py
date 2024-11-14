from flask import Flask, render_template

class app:
    def __init__(self, appFlaskName):
        self.appFlaskName = appFlaskName


        # Constructure of flask

        self.appFlaskName = Flask(__name__)

        self.route_home = "/"
        self.route_aboutThe_project = "/aboutThe_project"
        self.route_table = "/table"
        self.route_login = "/login"

    def app_main(self):
        self.appFlaskName.run(port=8094, debug=True)

    def app_routes(self):

        @self.appFlaskName.route(self.route_home)
        def index():
            return render_template("home.html")    
        
        @self.appFlaskName.route(self.route_aboutThe_project)
        def aboutThe_project():
            return render_template("aboutThe_project.html")    

        @self.appFlaskName.route(self.route_table)
        def table():
            return render_template("table.html")    
        
        @self.appFlaskName.route(self.route_login)
        def login():
            return render_template("login.html")    

        
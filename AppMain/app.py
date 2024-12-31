from Controller import constructure
 

if __name__ == "__main__":
    app = constructure.app(__name__)
    app.app_routes()
    app.app_main()   
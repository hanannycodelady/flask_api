from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from authors_app.extensions import db,migrate,bcrypt
from flask_migrate import Migrate
from authors_app.controllers.auth_controller import auth




# it enables us access or class

# enables us to import our config class
# defining the class



# creating a  factory function
def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')
    
    # initializing the third libraries .
    db.init_app(app)
    migrate.init_app(app,db)
    bcrypt.init_app(app)
    
    
   
    
    # working with migrations
    # importing and registering the models
    from authors_app.models.user import User
    # from authors_app.models.company import company
    # from authors_app.models.book import book
    
    # testing whether the application works_
    
    @app.route('/')
    
    def home ():
        return"Hello world"
    

    app.register_blueprint(auth ,url_prefix="/api/v1/auth")
    
    
    
    return app


    
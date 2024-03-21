# importing the data base 
from authors_app.extensions import db
from datetime import datetime

# creating the class user

class User(db.Model):
    __tablename__ = 'users'  # renaming the class
    # creating an instance
    # nullable means the field is either required or not
    
    id=db.Column(db.Integer,primary_key = True)
    First_name = db.Column(db.String(50),nullable = False)
    Last_name = db.Column(db.String(100),nullable = False)
    email = db.Column(db.String(100),nullable = False, unique=True)
    contact = db.Column(db.String,nullable = False, unique = True)
    password = db.Column(db.String(100), nullable =False, unique=True)
    biography=db.Column(db.String(1000))
    user_time =  db.Column(db.String,nullable = False)
    image = db.Column(db.String(255),nullable = True)
    
    
    
    # company=db.relationship('companies', back_populates='users') # the relationship between the company and the user
    # books = db.relationship('books', back_populates='users')# the relationship between the books and the user
    
    create_at=db.Column(db.DateTime, default=datetime.now())
    update_at= db.Column(db.DateTime, onupdate=datetime.now())
    
    
    def __init__(self,first_name,last_name,user_type,password,email,contact,image=None):
        self.first_name =First_name
        self.last_name = Last_name
        self.email=email
        self.contact=contact
        self.password=password
        self.user_type=user_type
        self.image=image
        
    def get_full_name(self):
        return f'{self.last_name}{self.first_name}'
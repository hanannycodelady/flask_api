# from authors_app.extensions import db
# from datetime import datetime


# class company (db.Model):
#     __tablename__ ='companies'
#     id=db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.String(255),nullable = False,unique=True)
#     origin = db.Column (db.String(1000))
#     description= db.Column(db.String(50),nullable = False)
#     user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
#     user = db.relationship('users',back_populates='companies') # creating the relationship between the user and companies
    
#     create_at=db.Column(db.DateTime, default=datetime.now())
#     update_at= db.Column(db.DateTime, onupdate=datetime.now())
    
    
    
    
    
#     # method is a special method in Python classes used to return a string representation of the object. 
    
#     def __repr__(self):
#         return f"<companies(name='{self.name}', origin='{self.origin}')>"
    
    
    
# from authors_app import db
# from datetime import datetime


# class book (db.Model):
#     __tablename__='books'
#     id=db.Column(db.Integer,primary_key = True)
#     title = db.Column(db.String(100),nullable = False)
#     description = db.Column(db.Text)
#     Price = db.Column(db.Integer)
#     number_of_pages = db.Column(db.Integer)
#     user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
#     # user = db.relationship('users',back_populates='books')
    
#     create_at=db.Column(db.DateTime ,default=datetime.now())
#     update_at= db.Column(db.DateTime, onupdate=datetime.now())
    
    
#     # This defines the initializer method for the class.
    
#     def __init__(self, title, description, number_of_pages, user_id):
#         self.Price = price
#         self.title = title
#         self.description = description
#         self.number_of_pages = number_of_pages
#         self.user_id = user_id

        
#         def __repr__ (self):
#             return f'<book{self.title}>'
    
    
    
    



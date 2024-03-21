from flask import Blueprint,request, jsonify
from authors_app.models.user import User  
from authors_app.extensions import db,bcrypt

#auth Blueprint
auth = Blueprint('auth',__name__,url_prefix='/api/v1/auth')


@auth.route('/register',methods=['POST'])
#creating a function for use register
def register():
    #storing viables
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    contact=request.json['contact']
    user_type=request.json['user_type']
    image=request.json['image']
    password = request.json['password']
    biography = request.json['biography']

    #checking the null validations and  null contraints
    # first approach for lito viables
    #it only for field/viables dat are required only, neccessary/complusary
    if not first_name:
        return jsonify({'error':"Your first_name is required"})
    if not last_name:
        return jsonify({'error':"Your last_name is required"})
    if not email:
        return jsonify({'error':"Your email is required"})
    if not contact:
        return jsonify({'error':"Your contact is required"})
    if not user_type:
        return jsonify({'error':"Your user_type is required"})
    if not image:
        return jsonify({'error':"Your image is required"})
    if len(password)<8:
        return jsonify({'error':"Your password still short"})
    #only if u are not an author
    if user_type == 'author' and not biography:
        return jsonify({'error':"Your biography is required"})
    #searching whthr the email exists 
    if User.query.filter_by(email=email).first():
        return jsonify({'error':"email already exists"})
    if User.query.filter_by(contact=contact).first():
        return jsonify({'error':"contact already exists"})
    


    try:
        #hashing the password
        hashed_password =bcrypt.generate_password_hash(password)
        #creating auser
        new_user = User(first_name=first_name,last_name=last_name,password =hashed_password,email=email,contact=contact,user_type=user_type,image=image)
        db.session.add(new_user)
        db.session.commit()
        # defining avariable that gives track to the user name
        
        username=User.get_full_name() 
        return jsonify({
            'message':username+'has been successfully created as an'+User.user_type,
            'user':{
            "id": new_user.id,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "password": new_user.password,
            "email": new_user.email,
            "contact": new_user.contact,
            "image":new_user.image,
            "User-type": new_user.user_type,
            "biography": new_user.biography,
            "created_at": new_user.created_at,
            #  "id": new_user.id,
            # "first_name": new_user.first_name,
            # "last_name": new_user.last_name,
            # "password": new_user.password,
            # "email": new_user.email,
            # "contact": new_user.contact,
            # "User-type": new_user.user_type,
            # "biography": new_user.biography,
            # "created_at": new_user.created_at,
            }
        })
    
    # except KeyError as e:
    #     # Handle the case where a required field is missing in the request body
    #     return jsonify({'error': f'Missing {e.args[0]} in request body'})

    except Exception as e:
        db.session.rollback()
        return jsonify({'error':str(e)}) 
    
    
# from flask import Blueprint, request, jsonify
# from authors_app.models.user import User, db
# from flask_bcrypt import Bcrypt

# # from email_validator import validate_email, EmailNotValidError


# # creating a blue print for the object
# auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')
# bcrypt = Bcrypt()

# # Define routes within the Blueprint
# @auth.route('/register', methods=['POST'])
# def register():
#     try:
#         # Extracting request data
#         first_name = request.json.get('first_name')
#         last_name = request.json.get('last_name')
#         contact = request.json.get('contact')
#         email = request.json.get('email')
#         user_type = request.json.get('user_type', 'author')  # Default to 'author'
#         password = request.json.get('password')
#         biography = request.json.get('biography', '') if user_type == 'author' else ''

#         # Basic input validation
#         required_fields = ['first_name', 'last_name', 'contact', 'password', 'email']
#         if not all(request.json.get(field) for field in required_fields):
#             return jsonify({'error': 'All fields are required'}), 400

#         if user_type == 'author' and not biography:
#             return jsonify({'error': 'Enter your author biography'}), 400

#         #Password validation
#         if len(password) < 6:
#             return jsonify({'error': 'Password is too short'}), 400

#         # Email validation
#         try:
#             validate_email(email)
#         except EmailNotValidError:
#             return jsonify({'error': 'Email is not valid'}), 400

#         # Check for uniqueness of email and contact separately
#         if User.query.filter_by(email=email).first() is not None:
#             return jsonify({'error': 'Email already exists'}), 409

#         if User.query.filter_by(contact=contact).first() is not None:
#             return jsonify({'error': 'Contact already exists'}), 409

#         #Creating a new user
#         hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
#         new_user = User(first_name=first_name, last_name=last_name, email=email,
#                         contact=contact, password=hashed_password, user_type=user_type,
#                         biography=biography)

#         #Adding and committing to the database
#         db.session.add(new_user)
#         db.session.commit()

#         # Building a response
#         username = f"{new_user.first_name} {new_user.last_name}"
#         return jsonify({
#             'message': f'{username} has been successfully created as an {new_user.user_type}',
#             'user': {
#                 'first_name': new_user.first_name,
#                 'last_name': new_user.last_name,
#                 'email': new_user.email,
#                 'contact': new_user.contact,
#                 'type': new_user.user_type,
#                 'biography': new_user.biography,
#                 'created_at': new_user.created_at,
#             }
#         }), 201

#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 500

# # getting all users
# @auth.route('/users', methods=['GET'])
# def get_all_users():
#     try:
#         users = User.query.all()
#         user_list = [{
#             'id': user.id,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'email': user.email,
#             'contact': user.contact,
#             'user_type': user.user_type,
#             'biography': user.biography,
#             'created_at': user.created_at
#         } for user in users]
#         return jsonify({'users': user_list}), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
# # getting a user 
# @auth.route('/users/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     try:
#         user = User.query.get_or_404(user_id)
#         user_data = {
#             'id': user.id,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'email': user.email,
#             'contact': user.contact,
#             'user_type': user.user_type,
#             'biography': user.biography,
#             'created_at': user.created_at
#         }
#         return jsonify({'user': user_data}), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
# # updating the user
# @auth.route('/users/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     try:
#         user = User.query.get_or_404(user_id)
#         data = request.json
#         # Update user attributes based on data
#         for key, value in data.items():
#             setattr(user, key, value)
#         db.session.commit()
#         return jsonify({'message': 'User updated successfully'}), 200
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 500
# # deleting the users
# @auth.route('/users/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     try:
#         user = User.query.get_or_404(user_id)
#         db.session.delete(user)
#         db.session.commit()
#         return jsonify({'message': 'User deleted successfully'}), 200
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 500
# from flask import Blueprint, request, jsonify
# from authors_app.models.user import User, db
# from flask_bcrypt import Bcrypt
# # from email_validator import validate_email, EmailNotValidError

# auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')
# bcrypt = Bcrypt()

# @auth.route('/register', methods=['POST'])
# def register():
#     try:
#         # Extracting request data
#         first_name = request.json.get('first_name')
#         last_name = request.json.get('last_name')
#         contact = request.json.get('contact')
#         email = request.json.get('email')
#         user_type = request.json.get('user_type', 'author')  # Default to 'author'
#         password = request.json.get('password')
#         biography = request.json.get('biography', '') if user_type == 'author' else ''

#         # Basic input validation
#         required_fields = ['first_name', 'last_name', 'contact', 'password', 'email']
#         if not all(request.json.get(field) for field in required_fields):
#             return jsonify({'error': 'All fields are required'}), 400

#         if user_type == 'author' and not biography:
#             return jsonify({'error': 'Enter your author biography'}), 400

#         #Password validation
#         if len(password) < 6:
#             return jsonify({'error': 'Password is too short'}), 400

#         # Email validation
#         try:
#             validate_email(email)
#         except EmailNotValidError:
#             return jsonify({'error': 'Email is not valid'}), 400

#         # Check for uniqueness of email and contact separately
#         if User.query.filter_by(email=email).first() is not None:
#             return jsonify({'error': 'Email already exists'}), 409

#         if User.query.filter_by(contact=contact).first() is not None:
#             return jsonify({'error': 'Contact already exists'}), 409

#         #Creating a new user
#         hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
#         new_user = User(first_name=first_name, last_name=last_name, email=email,
#                         contact=contact, password=hashed_password, user_type=user_type,
#                         biography=biography)

#         #Adding and committing to the database
#         db.session.add(new_user)
#         db.session.commit()

#         # Building a response
#         username = f"{new_user.first_name} {new_user.last_name}"
#         return jsonify({
#             'message': f'{username} has been successfully created as an {new_user.user_type}',
#             'user': {
#                 'first_name': new_user.first_name,
#                 'last_name': new_user.last_name,
#                 'email': new_user.email,
#                 'contact': new_user.contact,
#                 'type': new_user.user_type,
#                 'biography': new_user.biography,
#                 'created_at': new_user.created_at,
#             }
#         }), 201

#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 500






# from flask import Blueprint, request, jsonify
# from authors_app.models.user import User
# from datetime import datetime
# import bcrypt

# auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')


# @auth.route('/register', methods=['POST'])
# def register():
#     data = request.json

#     # Extracting data from request JSON
#     first_name = data.get('first_name')
#     last_name = data.get('last_name')
#     email = data.get('email')
#     contact = data.get('contact')
#     password = data.get('password')
#     biography = data.get('biography')
#     user_type = data.get('user_type')
#     image = data.get('image')




    # # creating a new user
    
    # new_user = user(first_name=first_name,last_name=last_name,email=email,
    #                 contact=contact,password=hashed_password,user_type=user_time,image=image)
    
    # #adding to the database
    # db.session.add(new_user)
    # db.session.commit()
    
    
    # #building a response
    # username=new_user.get_full_name()
    
    # return jsonify({
    #     'message': f'{username} has been successfully created as an {new_user.user_type}',
    # 'user':{
    #     'first_name': new_user.first_name,
    #     'last_name':new_user.last_name,
    #     'email':new_user.email,
    #     'contact':new_user.contact,
    #     'user_type':new_user.user_type,
    #     'created_at':new_user.created_at,
    #     }
    # }
    # )
    
    
    #         except Exception as e:
    #         db.session.rollback()
    #         return jsonify({'error':str(e)})
from flask import request, jsonify, Blueprint
from playhouse.shortcuts import model_to_dict
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user

import models

users = Blueprint('users', 'users')

#register route url localhost:8000/api/v1/users/register
@users.route('/register', methods=['POST'])
def register():
    payload = request.get_json()
    payload['email'].lower()
    
    try:
        models.User.get(models.User.email == payload['email'])
        
        return jsonify(data ={}, status = {'code: ': 400, 'message: ': 'A user with that email already exists'})
    
    except models.DoesNotExist:
        payload['password'] = generate_password_hash(payload['password'])
        print('hitting register route')
        user = models.User.create(**payload)
        login_user(user)
        user_dict = model_to_dict(user)
        
        del user_dict['password']
        return jsonify(data = user_dict, status= {'code: ': 200, 'message: ': f"Successfully registered {user_dict['email']}"})
#login route with accessibility requirement
#http://localhost:8000/api/v1/users/login
@users.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    payload['email'].lower()
    print(payload)
    
    try:
        user = models.User.get(models.User.email == payload['email'])
        
        user_dict = model_to_dict(user)
        print('hitting the login route', user_dict)
        
        if(check_password_hash(user_dict['password'], payload['password'])):
            del user_dict['password']
            login_user(user)
            return jsonify(data = user_dict, status = {'code: ': 200, 'message: ': f"Successfully logged in {user_dict['email']}"})
       
        else:
            return jsonify(data={}, status={'code: ': 401, 'message: ':'Email or password is incorrect'})
    
    except models.DoesNotExist:
            return jsonify(data={}, status= {'code: ': 401, 'message: ': 'Email or password is incorrect'})    
        
#logout route
@users.route('/logout', methods = ['GET'])
def logout():
    email = model_to_dict(current_user)['email']
    print('user logged out')
    
    logout_user()
    
    return jsonify(data = {}, status ={'code: ': 200, 'message: ': f"Successfully logged out {email}"})
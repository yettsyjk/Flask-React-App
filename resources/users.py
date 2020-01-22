from flask import request, jsonify, Blueprint
from playhouse.shortcuts import model_to_dict

import models

users = Blueprint('users', 'users')

@users.route('/register', methods=['POST'])

def register():
    payload = request.get_json()
    payload['email'].lower()
    try:
        models.User.get(models.User.email == payload['email'])
        return jsonify(data ={}, status = {'code: ': 401, 'message: ': 'A user wit that email already exists'})
    except models.DoesNotExist:
        user = models.User.create(**payload)
        user_dict = model_to_dict(user)
        del user_dict['password']
        return jsonify(data = user_dict, status= {'code: ': 200, 'message: ': f"Successfully registered {user_dict['email']}"})
#
@users.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    payload['email'].lower()
    try:
        user = models.User.get(models.User.email == payload['email'])
        user_dict = model_to_dict(user)
        if(user_dict['password'] == payload['password']):
            del user_dict['password']
            return jsonify(data = user_dict, status = {'code: ': 200, 'message: ': f"Successfully logged in {user_dict['email']}"})
        else:
            return jsonify(data={}, status={'code: ': 401, 'message: ':'Email or password is incorrect'})
    except models.DoesNotExist:
            return jsonify(data={}, status= {'code: ': 401, 'message: ': 'Email or password is incorrect'})    
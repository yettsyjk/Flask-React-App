from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

import models

birds = Blueprint('birds', 'birds')

###########INDEX ROUTE###########
#url localhost:8000/api/v1/birds
@birds.route('/', methods=["GET"])
# @login_required
#run function get all birds
def get_all_birds():
    try:
        #list of birds dict we set as data
        print('bird get hit')
        birds = [model_to_dict(bird) for bird in models.Bird.select().where(models.Bird.owner == current_user.id)]
        print(birds)
        for bird in birds:
            bird['owner'].pop('password')
        return jsonify(data=birds, status={"code: ": 200, "message: ": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code: ": 400, "message: ": "Error getting the resources"})
#############CREATE ROUTE##########http://localhost:8000/api/v1/birds/
@birds.route('/', methods=["POST"])
# @login_required
def create_bird():
    try:
        payload = request.get_json()
        payload['owner'] = (current_user.id)
        print(payload)
        bird = models.Bird.create(**payload)
        print(bird.__dict__)
        bird_dict = model_to_dict(bird)
        
        return jsonify(data= bird_dict, status={"code: ": 201, "message: ": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code: ": 400, "message: ": "Error creating the resources"})
##############SHOW ROUTE#################
@birds.route('/<id>', methods=["GET"])
def get_one_bird(id):
    print('test show')
    try:
        bird = models.Bird.get_by_id(id)
        print(bird)
        bird_dict = model_to_dict(bird)
        return jsonify(data = bird_dict, status = {
                'code: ': 200,
                'message': "Registered users can access more info about this weather"
                })
    except models.DoesNotExist:
        return jsonify(data={}, status={"code: " : 400, 'message: ': 'Error getting one resource'})
#############UPDATE ROUTE################
@birds.route('/<id>', methods=["PUT"])
# @login_required
def update_bird(id):
    try:
        payload = request.get_json()
        
        payload['owner']= current_user.id
        
        query = models.Bird.update(**payload).where(models.Bird.id == id)
        query.execute()
        updated_bird = model_to_dict(models.Bird.get_by_id(id))
        return jsonify(data= updated_bird, status={'code: ': 200, 'message: ': 'resources updated successfully'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code: ': 400, 'message: ': 'Error updating one resource'})
##########DELETE ROUTE###################
@birds.route('/<id>', methods=["DELETE"]) 
# @login_required
def delete_bird(id):
    try:
        query = models.Bird.delete().where(models.Bird.id == id)
        query.execute()
        return jsonify(data='Resources successfully deleted', status={'code: ': 200, 'message: ': 'Bird data successfully deleted'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code: ': 400, 'message: ': 'Error deleting the resource'})
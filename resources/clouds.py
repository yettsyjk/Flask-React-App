from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

import models

clouds = Blueprint('clouds', 'clouds')

###########INDEX ROUTE###########
#url localhost:8000/api/v1/clouds
@clouds.route('/', methods=['GET'])
@login_required
#run function get all clouds
def get_all_clouds():
    try:
        #list of clouds dict we set as data
        clouds = [model_to_dict(cloud) for cloud in models.Cloud.select().where(models.Cloud.owner == current_user.id)]
        print(clouds)
        for cloud in clouds:
            cloud['owner'].pop('password')
        return jsonify(data=clouds, status={"code: ": 200, "message: ": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code: ": 401, "message: ": "Error getting the resources"})
#############CREATE ROUTE##########
@clouds.route('/', methods=['POST'])
@login_required
def create_cloud():
    try:
        payload = request.get_json()
        payload['owner'] = int(current_user.id)
        print(payload)
        cloud = models.Cloud.create(**payload)
        print(cloud.__dict__)
        cloud_dict = model_to_dict(cloud)
        return jsonify(data= cloud_dict, status={"code: ": 201, "message: ": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code: ": 401, "message: ": "Error creating the resources"})
##############SHOW ROUTE#################
@clouds.route('/<id>', methods=['GET'])
def get_one_cloud(id):
    print('test show')
    try:
        cloud = models.Cloud.get_by_id(id)
        print(cloud)
        
        if not current_user.is_authenticated:
            return jsonify(data = {
                'city': cloud.city,
                'country': cloud.country,
                'weather': cloud.weather,
                'temp': cloud.temp
            }, status = {
                'code: ': 200,
                'message': "Registered users can access more info about this weather"
                })
        else: 
            cloud_dict = model_to_dict(cloud)
            cloud_dict['owner'].pop('password')
            return jsonify(data = cloud_dict, status = {
                'code: ': 200,
                'message: ': f"Found cloud with id {cloud.id}"
                })
    except models.DoesNotExist:
        return jsonify(data={}, status={"code: " : 401, 'message: ': 'Error getting the resources'})
#############UPDATE ROUTE################
@clouds.route('/<id>', methods=['PUT'])
@login_required
def update_cloud(id):
    try:
        payload = request.get_json()
        query = models.Cloud.update(**payload).where(models.Cloud.id == id)
        query.execute()
        updated_cloud = model_to_dict(models.Cloud.get_by_id(id))
        return jsonify(data= updated_cloud, status={'code: ': 200, 'message: ': 'resources updated successfully'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code: ': 400, 'message: ': 'Error updating one resource'})
##########DELETE ROUTE###################
@clouds.route('/<id>', methods=['DELETE']) 
@login_required
def deleted_cloud(id):
    try:
        query = models.Cloud.delete().where(models.Cloud.id == id)
        query.execute()
        return jsonify(data='Resources successfully deleted', status={'code: ': 200, 'message: ': 'Cloud data successfully deleted'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code: ': 400, 'message: ': 'Error deleting the resource'})
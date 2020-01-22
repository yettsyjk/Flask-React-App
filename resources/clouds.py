from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
import models

clouds = Blueprint('clouds', 'clouds')

###########INDEX ROUTE###########
#url localhost:8000/api/v1/clouds
@clouds.route('/', methods=['GET'])
#run function get all clouds
def get_all_clouds():
    try:
        #list of clouds dict we set as data
        clouds = [model_to_dict(cloud) for cloud in models.Cloud.select()]
        print(clouds)
        return jsonify(data=clouds, status={"code: ": 200, "message: ": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code: ": 401, "message: ": "Error getting the resources"})
#############CREATE ROUTE##########
@clouds.route('/', methods=['POST'])
def create_cloud():
    try:
        payload = request.get_json()
        cloud = models.Cloud.create(**payload)
        print(cloud.__dict__)
        dog_dict = model_to_dict(cloud)
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
        cloud_dict = model_to_dict(cloud)
        return jsonify(data = cloud_dict, status = {'code: ': 200, 'message: ': f"Found cloud with id {cloud.id}"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code: " : 400, 'message: ': 'Error getting the resources'})
#############UPDATE ROUTE################
@clouds.route('/<id>', methods=['PUT'])
def update_cloude(id):
    try:
        payload = request.get_json()
        query = models.Cloud.update(**payload).where(models.Cloud.id == id)
        query.execute()
        return jsonify(data= model_to_dict(models.Cloud.get_by_id(id)), status={'code: ': 200, 'message: ': 'resources updated successfully'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code: ': 401, 'message: ': 'Error deleting the resource'})
##########DELETE ROUTE###################
@clouds.route('/<id>', methods=['DELETE']) 
def deleted_cloud(id):
    try:
        query = models.Cloud.delete().where(models.CLoud.id == id)
        query.execute()
        return jsonify(data='Resources successful deleted', status={'code: ': 200, 'message: ': 'Cloud data successfully deleted'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code: ': 400, 'message: ': 'Error deleting the resource'})
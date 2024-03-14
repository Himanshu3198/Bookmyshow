from flask import Blueprint
from flask import request, jsonify

from apps.Model.userModel import userAddModel
from apps.Service.userService import userService

user_blueprint = Blueprint('user', __name__)
user_service = userService()


@user_blueprint.route('/home', methods=['GET'])
def welcome():
    return "welcome to the dev world.."


@user_blueprint.route('/create_user/', methods=['POST'])
def add_user():
    data = request.get_json()
    user = userAddModel(**data)

    try:
        user_id = user_service.add_user(user)
        response = {'message': 'User added Successfully', 'user_id': user_id}
        return jsonify(response), 201
    except Exception as e:
        response = {'error': str(e)}
        return jsonify(response), 400


@user_blueprint.route('/users/', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    if users:
        return jsonify([user.dict() for user in users])
    else:
        return jsonify({'message': 'users not found'}), 404

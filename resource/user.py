from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import create_access_token, jwt_required
from flask_jwt_extended import current_user


import json

from heplers.encoder import AlchemyEncoder
from models.user import UserModel


class User(Resource):

    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    parser.add_argument('username', type=str, required=True,
                        help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True,
                        help='This field cannot be left blank')

    def post(self):
        data = User.parser.parse_args()
        username = data['username']

        current_user = UserModel.find_by_username(username)
        if not current_user:
            return {'message': f'User {username} doesn\'t exist'}

        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(
                identity=json.dumps(current_user, cls=AlchemyEncoder))
            return jsonify(access_token=access_token)
        else:
            return {'message': 'Wrong username or password.'}, 401



class UserRegister(Resource):

    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    parser.add_argument('username', type=str, required=True,
                        help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True,
                        help='This field cannot be left blank')

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'UserModel has already been created, aborting.'}, 400

        new_user = UserModel(
            username=data['username'],
            password=UserModel.generate_hash(data['password'])
                             )


        new_user.save_to_db()

        return {'message': 'user has been created successfully.'}, 201
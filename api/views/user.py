from marshmallow import pprint

from flask_restplus import Resource
from flask import request, jsonify

from main import api
from api.utilities.model_serializers.user import UserSchema
from api.models.user import User
from api.middleware.auth_token import encode_auth_token


@api.route('/auth/user')
class UserResource(Resource):
    def post(self):
        userData = request.get_json()
        user = User(**userData)
        schema = UserSchema(exclude=['updated_at'])
        user.save()
        token = encode_auth_token(user.id)
        response = jsonify({
            'status': 'success',
            'message': 'user signup successfully',
            'token': str(token)
        })

        return response
     

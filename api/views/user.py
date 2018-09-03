from marshmallow import pprint

from flask_restplus import Resource
from flask import request

from main import api
from api.utilities.model_serializers.user import UserSchema
from api.models.user import User


@api.route('/auth/user')
class UserResource(Resource):
    def post(self):
        userData = request.get_json()
        user = User(**userData)
        schema = UserSchema()
        user.save()
        userResul = schema.dump(result)
        return userResult.data

from marshmallow import ValidationError as ValidationErrorSchema

from flask_restplus import Resource
from flask import request, jsonify

from main import api
from api.utilities.model_serializers.user import UserSchema
from api.utilities.model_serializers.user import UserSigninSchema
from api.models.user import User
from api.middleware.auth_token import encode_auth_token
from api.middleware.auth_token import decode_auth_token
from api.middleware.base_validator import ValidationError


@api.route('/auth/signup')
class UserSignup(Resource):
    def post(self):
        userData = request.get_json()

        try:
            UserSchema().load(userData)
        except ValidationErrorSchema as err:
            raise ValidationError(err.messages, 400)

        user = User(**userData)
        user_found = User.query_().filter_by(
            email=user.email).first()
        if user_found:
            return {
                'success': 'False',
                'message': 'User with that email already exist'
            }, 400

        user.save()
        token = encode_auth_token(user.id)

        response = {
            'success': 'true',
            'message': 'user signed up successfully',
            'token': token.decode('UTF-8')
        }

        return response, 201

@api.route('/auth/signin')
class UserSignin(Resource):
    def post(self):
        userData = request.get_json()

        try:
            UserSigninSchema().load(userData)
        except ValidationErrorSchema as err:
            raise ValidationError(err.messages, 400)

        user = User(**userData)
        user_found = User.query_().filter_by(
            email=user.email).first()
        if not user_found:
            return {
                'success': 'true',
                'message': 'user not found, please sign up',
            }

        # user.save()
        # token = encode_auth_token(user.id)
        token = encode_auth_token(user_found.id)

        response = {
            'success': 'true',
            'message': 'user signed in  successfully',
            'token': token.decode('UTF-8')
        }

        return response, 201

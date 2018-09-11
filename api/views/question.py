from flask_restplus import Resource
from flask import request, jsonify
from marshmallow import ValidationError as ValidationErrorSchema

from api.utilities.model_serializers.question import QuestionSchema
from main import api
from api.middleware.base_validator import ValidationError
from api.middleware.auth_token import decode_auth_token
from api.models.question import Question
from api.models.user import User


@api.route('/questions')
class QuestionResource(Resource):
    @decode_auth_token
    def post(self):
        schema = QuestionSchema()
        question = request.get_json()

        try:
            schema.load(question)
        except ValidationErrorSchema as err:
            raise ValidationError(err.messages, 400)
        
        user_id = request.decoded_token['id']

        user = User.get(user_id)
        new_question = Question(**question, user=user)
        new_question.save()
        result = schema.dump(new_question)

        return {
            'success': 'true',
            'message': 'question added successfully',
            'data': result
        }
        
        
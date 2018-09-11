from marshmallow import Schema, fields, post_load
from api.models.question import Question
from ..validators.str_length_validator import string_length_0_validator


class QuestionSchema(Schema):
    id = fields.String()
    title = fields.String(
        required=True,
        validate=string_length_0_validator,
        error_messages={'required': 'Title is required'}
    )
    body = fields.String(
        required=True,
        validate=string_length_0_validator,
        error_messages={'required': 'Body is required'}
    )
    user_id = fields.String()

    @post_load
    def make_question(self, data):
        return Question(**data)

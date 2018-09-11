from marshmallow import Schema, fields, post_load

from ..validators.str_length_validator import string_length_0_validator
from api.models.user import User


class UserSchema(Schema):
    first_name = fields.String(required=True, 
                               validate=string_length_0_validator,
                               error_messages={
                                 'required': 'First name is required'
                               })
    last_name = fields.String(required=True, 
                              validate=string_length_0_validator,
                              error_messages={
                                'required': 'Last name is required'
                              })
    email = fields.Email(required=True, 
                         validate=string_length_0_validator,
                         error_messages={
                            'required': 'Email is required'
                         })
    password = fields.String(required=True, 
                             validate=string_length_0_validator,
                             error_messages={
                               'required': 'Password is required'
                             })

    @post_load
    def make_user(self, data):
        return User()


class UserSigninSchema(Schema):
    email = fields.Email(required=True, 
                         validate=string_length_0_validator,
                         error_messages={
                            'required': 'Email is required'
                         })
    password = fields.String(required=True, 
                             validate=string_length_0_validator,
                             error_messages={
                               'required': 'Password is required'
                             })

    @post_load
    def make_user(self, data):
        return User()

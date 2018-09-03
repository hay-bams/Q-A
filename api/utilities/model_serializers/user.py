from marshmallow import Schema, fields, post_load
from api.models.user import User


class UserSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Email()
    password = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    @post_load
    def make_user(self, data):
        return User()

from marshmallow import ValidationError

def string_length_0_validator(data):
    if len(data) < 1:
        raise ValidationError('Fields cannot be empty')
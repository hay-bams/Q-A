import os
import datetime
from functools import wraps

import jwt
from flask import request


def encode_auth_token(user_id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }

        return jwt.encode(
            payload,
            os.getenv('JWT_SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        auth_token = request.headers.get('x-access-token')
        try:
            payload = jwt.decode(auth_token,  os.getenv('JWT_SECRET_KEY'))
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

        return func()
    return wrapper
        
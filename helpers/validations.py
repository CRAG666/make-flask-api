from flask import current_app as app
from flask import jsonify, request
import jwt
from functools import wraps
from models import ma
from marshmallow import ValidationError


def token_required(**parameters):
    def inner_function(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token: str = request.headers.get('x-access-token', None)

            if not token:
                return jsonify({'message': 'Token is missing!'}), 401

            table = parameters.get('table', app.config['TABLE_VALIDATE_TOKEN'])
            key = parameters.get('key', app.config['SECRET_KEY'])
            print(key)
            try:
                data = jwt.decode(token, key)
                current_user = table.query.filter_by(id=data['id']).first()
            except (jwt.ExpiredSignature, jwt.InvalidSignatureError, jwt.DecodeError):
                return jsonify({'message': 'Token is invalid!'}), 401
            return f(*args, current_user, **kwargs)
        return wrapper
    return inner_function


def validate_json(schema: ma.Schema):
    def inner_function(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                schema.load(request.json)
            except ValidationError as err:
                return err.messages
            return f(*args, **kwargs)
        return wrapper
    return inner_function

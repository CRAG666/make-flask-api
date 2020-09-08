from . import ma
from marshmallow import validate


class LoginSchema(ma.Schema):
    name = ma.Str(validate=validate.Length(min=1), required=True)
    email = ma.Email(required=True)

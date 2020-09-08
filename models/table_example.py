from . import db, ma, Standard
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import validate


class TableExample(db.Model, Standard):
    __tablename__ = 'TableExample'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, fields: dict):
        self.changes(fields)

    def changes(self, fields: dict):
        self.name = fields.get('name')
        self.password = self.__generate_password(fields.get('password'))
        self.email = fields.get('email')

    @staticmethod
    def __generate_password(password: str) -> str:
        return generate_password_hash(password)

    def compare_passwords(self, password: str) -> bool:
        return check_password_hash(self.password, password)


class TableExample_Schema(ma.Schema):
    name = ma.Str(validate=validate.Length(min=1), required=True)
    email = ma.Email(required=True)
    password = ma.Str(validate=validate.Length(min=4), load_only=True, required=True)

    class Meta:
        fields = ('id', 'name', 'email', 'password')

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import exc
from flask import current_app as app
db = SQLAlchemy()
ma = Marshmallow()


class Standard:
    def save(self) -> bool:
        db.session.add(self)
        try:
            db.session.commit()
        except exc.SQLAlchemyError:
            db.session.rollback()
            return False
        return True

    def delete(self, *args) -> bool:
        db.session.delete(self)
        try:
            db.session.commit()
        except exc.SQLAlchemyError:
            db.session.rollback()
            return False
        return True


def create_database():
    engine = db.create_engine(app.config['EGINE_URI'], {})
    engine.execute(f"CREATE DATABASE IF NOT EXISTS {app.config['DB_NAME']}")


from .table_example import TableExample

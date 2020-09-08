from os import environ
from models.table_example import TableExample


class Config:
    SECRET_KEY = "CRAG"


class DevelopmentConfig(Config):
    DEBUG = True
    EGINE_URI = 'mysql://root:' + environ['passmaria'] + '@localhost'
    # * EGINE_URI = 'mysql://root:@localhost'
    DB_NAME = 'ECU_app1'
    SQLALCHEMY_DATABASE_URI = f'{EGINE_URI}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TABLE_VALIDATE_TOKEN = TableExample

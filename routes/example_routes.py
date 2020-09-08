from . import example
from models.table_example import TableExample, TableExample_Schema
from routes.create_routesStandars import create_routes

create_routes(
    table=TableExample,
    table_schema=TableExample_Schema,
    blueprint=example,
    noun="example",
    login_endpoint=True)

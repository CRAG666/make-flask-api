from flask import Flask, jsonify
from config import DevelopmentConfig
from routes.example_routes import example
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


# * Error 404
@app.errorhandler(404)
def page_not_found(err):
    return jsonify({"Message": "This page could not be found"})


# * Error 405
@app.errorhandler(405)
def method_not_allowed(err):
    return jsonify({"Message": "The method is not allowed for the requested URL"})


# * Error 401
@app.errorhandler(401)
@cross_origin()
def method_not_allowed(err):
    return jsonify({'Authenticate': 'Could not verify'})


# * Routes
app.register_blueprint(example)

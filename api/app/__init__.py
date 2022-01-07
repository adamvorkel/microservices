from io import BytesIO
from flask import Flask
from flask_restful import Api
from app.resources.ping import PingResource 

def create_app():
    app = Flask(__name__)

    register_resources(app)
    return app


def register_resources(app):
    api = Api(app, prefix='/api')

    api.add_resource(PingResource, '/ping')

app = create_app()
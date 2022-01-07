from flask_restful import Resource
from http import HTTPStatus 

class PingResource(Resource):
    def get(self):
        return {}, HTTPStatus.OK
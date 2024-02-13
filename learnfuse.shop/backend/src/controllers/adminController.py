from flask_restful import Resource

class AdminResource(Resource):
    def get(self):
        return {'message': 'Admin endpoint'}

    # Add other methods as needed

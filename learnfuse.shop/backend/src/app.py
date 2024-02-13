from flask import Flask
from flask_restful import Api
from controllers.adminController import AdminResource
from controllers.studentController import StudentResource
from controllers.trainerController import TrainerResource

app = Flask(__name__)
api = Api(app)

# Define API endpoints
api.add_resource(AdminResource, '/admin')
api.add_resource(StudentResource, '/student')
api.add_resource(TrainerResource, '/trainer')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from db import db
from resource.car import CarListResource, CarResource
from resource.user import UserRegister, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    db.init_app(app)
    db.create_all()


api.add_resource(CarListResource, '/cars')
api.add_resource(CarResource, '/car/<int:car_id>')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)

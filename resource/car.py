from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from flask import request, jsonify

from db import db
from models.car import CarModel
from schema.car import CarSchema

car_schema = CarSchema()
cars_schema = CarSchema(many=True)


class CarListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('year', type=int, required=False,
                        help='This field cannot be string')

    def get(self):
        cars = CarModel.query.all()
        cars_data = cars_schema.dump(cars)
        return {"cars": cars_data}, 200

    @jwt_required()
    def post(self):
        new_post = CarModel(
            brand=request.json['brand'],
            year=request.json['year']
        )
        try:
            db.session.add(new_post)
            db.session.commit()
            return {"car": car_schema.dump(new_post)}, 201
        except:
            return {"error": "You send invalid request"}, 400


class CarResource(Resource):
    @jwt_required()
    def get(self, car_id):
        try:
            car = CarModel.query.get_or_404(car_id)
            return car_schema.dump(car)
        except:
            return {"error": f"car: {car_id} does not exists"}, 404

    @jwt_required()
    def patch(self, car_id):
        car = CarModel.query.get_or_404(car_id)

        if 'brand' in request.json:
            car.brand = request.json['brand']
        if 'year' in request.json:
            car.content = request.json['year']

        db.session.commit()
        return car_schema.dump(car)

    @jwt_required()
    def delete(self, car_id):
        car = CarModel.query.get_or_404(car_id)
        db.session.delete(car)
        db.session.commit()
        return '', 204

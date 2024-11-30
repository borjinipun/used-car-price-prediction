from flask import Blueprint, request, jsonify
from app.models import CarModel
from app.database import db

bp = Blueprint('car_routes', __name__)

@bp.route('/add_car', methods=['POST'])
def add_car():
    """API to add a car to the database."""
    data = request.json
    car = CarModel(make=data['make'], model=data['model'], year=data['year'])
    db.session.add(car)
    db.session.commit()
    return jsonify({"message": "Car added successfully!", "car": data}), 201

from flask import Blueprint, jsonify
from app.models import Issue, CarModel
from app.utils.score_calculator import calculate_health_score

bp = Blueprint('score_routes', __name__)

@bp.route('/calculate_health_score/<int:car_id>', methods=['GET'])
def get_health_score(car_id):
    """API to calculate the health score of a car."""
    car = CarModel.query.get_or_404(car_id)
    score = calculate_health_score(car_id)
    return jsonify({"car": {"make": car.make, "model": car.model, "year": car.year}, "health_score": score}), 200

from flask import Blueprint, request, jsonify
from app.models import Issue
from app.database import db

bp = Blueprint('issue_routes', __name__)

@bp.route('/report_issue', methods=['POST'])
def report_issue():
    """API to report an issue."""
    data = request.json
    issue = Issue(
        car_model_id=data['car_model_id'],
        description=data['description'],
        severity=data['severity'],
        user_feedback=data.get('user_feedback', '')
    )
    db.session.add(issue)
    db.session.commit()
    return jsonify({"message": "Issue reported successfully!", "issue": data}), 201

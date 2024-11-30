from app.models import Issue

def calculate_health_score(car_id):
    """Calculate the health score of a car."""
    issues = Issue.query.filter_by(car_model_id=car_id).all()
    if not issues:
        return "No data available"

    severity_sum = sum(issue.severity for issue in issues)
    total_votes = sum(issue.votes for issue in issues)
    health_score = max(100 - (severity_sum * 2 + total_votes), 0)

    return health_score

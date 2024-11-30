from app.database import db

class CarModel(db.Model):
    """Database model for car details."""
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    issues = db.relationship('Issue', backref='car_model', lazy=True)

class Issue(db.Model):
    """Database model for car issues."""
    id = db.Column(db.Integer, primary_key=True)
    car_model_id = db.Column(db.Integer, db.ForeignKey('car_model.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.Integer, nullable=False)
    votes = db.Column(db.Integer, default=0)
    user_feedback = db.Column(db.Text, nullable=True)

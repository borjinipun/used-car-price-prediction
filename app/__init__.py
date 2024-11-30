from flask import Flask
from app.database import db

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    # Initialize database
    db.init_app(app)
    
    # Register Blueprints
    from app.routes import car_routes, issue_routes, user_routes, score_routes
    app.register_blueprint(car_routes.bp)
    app.register_blueprint(issue_routes.bp)
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(score_routes.bp)

    return app

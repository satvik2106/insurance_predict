from flask import Blueprint

# Define the blueprint for routes
routes_bp = Blueprint("routes", __name__)

# Import route files after defining the blueprint to avoid circular imports
from .predict import predict_bp
from .auth import auth_bp

# Register blueprints inside this main routes blueprint
routes_bp.register_blueprint(predict_bp, url_prefix="/predict")
routes_bp.register_blueprint(auth_bp, url_prefix="/auth")

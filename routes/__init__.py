from flask import Blueprint

from .auth import auth_bp
from .delivery_routes import delivery_bp
from .medication_routes import medications_bp
from .notifications import notifications_bp
from .users_routes import users_bp
from .orders_routes import orders_bp
from .payments_routes import payments_bp
from .chatbot_routes import chatbot_bp
from .teleconsultations_routes import teleconsultations_bp

# Register all routes into a single blueprint
api_bp = Blueprint('api', __name__)

# Add all sub-blueprints
api_bp.register_blueprint(auth_bp, url_prefix='/auth')
api_bp.register_blueprint(delivery_bp, url_prefix='/delivery')
api_bp.register_blueprint(medications_bp, url_prefix='/medications')
api_bp.register_blueprint(notifications_bp, url_prefix='/notifications')
api_bp.register_blueprint(users_bp, url_prefix='/users')
api_bp.register_blueprint(orders_bp, url_prefix='/orders')
api_bp.register_blueprint(payments_bp, url_prefix='/payments')
api_bp.register_blueprint(chatbot_bp, url_prefix='/chatbot')
api_bp.register_blueprint(teleconsultations_bp, url_prefix='/teleconsultations')


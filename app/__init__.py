import os
from flask import Flask
from dotenv import load_dotenv
from models.database import db

# Load environment variables
load_dotenv()

def create_app():
    """App factory function."""
    app = Flask(__name__)

    # App configurations
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback_dev_key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///test.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    db.init_app(app)

    # Register blueprints (if any)
    # from app.routes import main
    # app.register_blueprint(main)

    return app


import os
from flask import Flask
from dotenv import load_dotenv

# Delay the import of db and models
def create_app():
    """App factory function."""
    # Load environment variables
    load_dotenv()

    app = Flask(__name__)

    # App configurations
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback_dev_key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///test.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Now import db and models here, to avoid circular import
    from models.database import db
    from models import User, Product, Order, Payment, Tracking, ChatbotInteraction, Teleconsultation

    db.init_app(app)

    # Initialize 

    return app

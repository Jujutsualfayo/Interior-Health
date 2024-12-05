import os
from flask import Flask
from dotenv import load_dotenv

# Import db 
from models.database import db

def create_app():
    """App factory function."""
    # Load environment variables
    load_dotenv()

    app = Flask(__name__)

    # App configurations
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback_dev_key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///test.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize db here
    db.init_app(app)

    # Now import models here
    from models import User, Product, Order, Payment, Tracking, ChatbotInteraction, Teleconsultation

    # Initialize any other parts of your app here, like routes or blueprints

    return app

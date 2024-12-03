from flask import Flask
from app.routes import (
    auth,
    delivery_routes,
    medication_routes,
    notifications,
)

def create_app():
    """Factory to create a Flask app."""
    app = Flask(__name__)

    # App configurations
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Register Blueprints
    app.register_blueprint(auth.bp)
    app.register_blueprint(delivery_routes.bp)
    app.register_blueprint(medication_routes.bp)
    app.register_blueprint(notifications.bp)

    return app

# Create an instance of the app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


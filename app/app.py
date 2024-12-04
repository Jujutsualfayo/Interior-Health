import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from app.database import db, reset_test_db
from models import User, Teleconsultation


# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# App configurations
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback_dev_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Routes
@app.route('/')
def home():
    return "Welcome to Interior Health!"

@app.route('/users', methods=['GET'])
def get_users():
    """Fetch all users."""
    users = User.query.all()
    user_list = [{"id": u.id, "name": u.name, "email": u.email} for u in users]
    return jsonify(user_list), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Fetch a single user by ID."""
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200

@app.route('/chatbot', methods=['POST'])
def interact_chatbot():
    """Handle chatbot interactions."""
    data = request.get_json()
    message = data.get("message", "")

    # Mock chatbot responses
    if "hello" in message.lower():
        return jsonify({"response": "Hello! How can I assist you today?"}), 200
    elif "help" in message.lower():
        return jsonify({"response": "I can assist with booking teleconsultations or finding health information."}), 200
    else:
        return jsonify({"response": "I'm sorry, I didn't understand that. Could you rephrase?"}), 200

@app.route('/teleconsultation', methods=['POST'])
def book_teleconsultation():
    """Book a teleconsultation for a user."""
    data = request.get_json()
    user_id = data.get("user_id")
    time_slot = data.get("time_slot")

    # Validate input
    if not user_id or not time_slot:
        return jsonify({"error": "Missing user_id or time_slot"}), 400

    # Create a new teleconsultation record
    teleconsultation = Teleconsultation(user_id=user_id, time_slot=time_slot)
    db.session.add(teleconsultation)
    db.session.commit()

    return jsonify({
        "message": "Teleconsultation booked successfully",
        "teleconsultation": {"user_id": user_id, "time_slot": time_slot}
    }), 201

@app.cli.command('reset-test-db')
def reset_db():
    """CLI command to reset the test database."""
    with app.app_context():
        reset_test_db()
    print("Test database has been reset.")

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)


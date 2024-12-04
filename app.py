import os
from flask import Flask, jsonify, abort
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# App configurations
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback_dev_key')

# Mock data for users (replace with database integration if needed)
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

@app.route('/')
def home():
    return "Welcome to Interior Health!"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Look for the user in the mock data
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        # Return a 404 error with a JSON message
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

if __name__ == '__main__':
    app.run(debug=True)


import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# App configurations
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback_dev_key')

# Mock data
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

teleconsultations = []

@app.route('/')
def home():
    return "Welcome to Interior Health!"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@app.route('/chatbot', methods=['POST'])
def interact_chatbot():
    data = request.get_json()
    message = data.get("message", "")
    
    # Mock chatbot response
    if "hello" in message.lower():
        return jsonify({"response": "Hello! How can I assist you today?"}), 200
    elif "help" in message.lower():
        return jsonify({"response": "I can assist with booking teleconsultations or finding health information."}), 200
    else:
        return jsonify({"response": "I'm sorry, I didn't understand that. Could you rephrase?"}), 200

@app.route('/teleconsultation', methods=['POST'])
def book_teleconsultation():
    data = request.get_json()
    user_id = data.get("user_id")
    time_slot = data.get("time_slot")
    
    # Validate input
    if not user_id or not time_slot:
        return jsonify({"error": "Missing user_id or time_slot"}), 400
    
    # Mock booking logic
    teleconsultations.append({"user_id": user_id, "time_slot": time_slot})
    return jsonify({"message": "Teleconsultation booked successfully", "teleconsultation": {"user_id": user_id, "time_slot": time_slot}}), 201

if __name__ == '__main__':
    app.run(debug=True)


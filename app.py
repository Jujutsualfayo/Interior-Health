import os
from flask import Flask, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# App configurations
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback_dev_key')

# Mock data for users 
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

if __name__ == '__main__':
    app.run(debug=True)

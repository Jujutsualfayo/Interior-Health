import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# App configurations
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback_dev_key')

@app.route('/')
def home():
    return "Welcome to Interior Health!"

if __name__ == '__main__':
    app.run(debug=True)


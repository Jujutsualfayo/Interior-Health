from flask import Blueprint, request, jsonify
from db_utils import Database

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/chatbot', methods=['POST'])
def interact_chatbot():
    """Record chatbot interaction."""
    try:
        data = request.json
        user_id = data['user_id']
        question = data['question']
        response = "Placeholder response for now."  # Replace with AI/logic later
        interaction_id = Database.create_chatbot_interaction(user_id, question, response)
        return jsonify({"message": "Chatbot interaction recorded", "interaction_id": interaction_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


from flask import Blueprint, request, jsonify
from db_utils import Database

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/payments', methods=['POST'])
def create_payment():
    """Process a payment."""
    try:
        data = request.json
        user_id = data['user_id']
        order_id = data['order_id']
        amount = data['amount']
        payment_id = Database.create_payment(user_id, order_id, amount)
        return jsonify({"message": "Payment successful", "payment_id": payment_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


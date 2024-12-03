from flask import Blueprint, request, jsonify
from db_utils import Database

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=['POST'])
def create_order():
    """Create a new order."""
    try:
        data = request.json
        user_id = data['user_id']
        product_id = data['product_id']
        quantity = data['quantity']
        order_id = Database.create_order(user_id, product_id, quantity)
        return jsonify({"message": "Order created successfully", "order_id": order_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


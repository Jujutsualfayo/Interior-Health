from flask import Blueprint, request, jsonify
from db_utils import Database

teleconsultations_bp = Blueprint('teleconsultations', __name__)

@teleconsultations_bp.route('/teleconsultations', methods=['POST'])
def book_teleconsultation():
    """Book a teleconsultation."""
    try:
        data = request.json
        user_id = data['user_id']
        doctor_name = data['doctor_name']
        appointment_time = data['appointment_time']
        teleconsultation_id = Database.create_teleconsultation(user_id, doctor_name, appointment_time)
        return jsonify({"message": "Teleconsultation booked", "teleconsultation_id": teleconsultation_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


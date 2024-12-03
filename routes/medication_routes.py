from flask import Blueprint, request, jsonify
from models.inventory import Inventory
from database import session

medication_routes = Blueprint('medication_routes', __name__)

@medication_routes.route('/medications', methods=['GET'])
def get_all_medications():
    medications = session.query(Inventory).all()
    return jsonify([{"id": med.id, "name": med.name, "stock": med.stock, "location": med.location} for med in medications])

@medication_routes.route('/medications', methods=['POST'])
def add_medication():
    data = request.json
    new_medication = Inventory(name=data['name'], stock=data['stock'], location=data['location'])
    session.add(new_medication)
    session.commit()
    return jsonify({"message": "Medication added successfully"}), 201


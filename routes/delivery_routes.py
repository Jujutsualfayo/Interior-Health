from flask import Blueprint, jsonify
from models.delivery_route import DeliveryRoute
from database import session

delivery_routes = Blueprint('delivery_routes', __name__)

@delivery_routes.route('/routes', methods=['GET'])
def get_all_routes():
    routes = session.query(DeliveryRoute).all()
    return jsonify([{"id": route.id, "start": route.start_point, "end": route.end_point, "distance": route.distance} for route in routes])


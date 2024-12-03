# routes/__init__.py

from .user_routes import user_routes
from .product_routes import product_routes
from .order_routes import order_routes
from .payment_routes import payment_routes
from .tracking_routes import tracking_routes
from .chatbot_routes import chatbot_routes
from .teleconsultation_routes import teleconsultation_routes

# Combine all route modules for easier app inclusion
routes = [
    user_routes,
    product_routes,
    order_routes,
    payment_routes,
    tracking_routes,
    chatbot_routes,
    teleconsultation_routes,
]


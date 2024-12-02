class Order:
    def __init__(self, user_id, product_id, quantity, status='pending'):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        self.status = status

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "status": self.status
        }

    @staticmethod
    def track_order(order_id):
        """Allows  for tracking an order."""
        print(f"Tracking order ID: {order_id}")


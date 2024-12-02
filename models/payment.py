class Payment:
    def __init__(self, user_id, order_id, amount, status='pending'):
        self.user_id = user_id
        self.order_id = order_id
        self.amount = amount
        self.status = status

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "order_id": self.order_id,
            "amount": self.amount,
            "status": self.status
        }

    @staticmethod
    def process_payment(user_id, order_id, amount):
        """Allows for processing a payment."""
        print(f"Processing payment of {amount} for user ID {user_id} and order ID {order_id}")
        return "Payment successful"


class Feedback:
    def __init__(self, user_id, message, rating):
        self.user_id = user_id
        self.message = message
        self.rating = rating

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "message": self.message,
            "rating": self.rating
        }


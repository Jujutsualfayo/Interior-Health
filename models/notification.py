class Notification:
    def __init__(self, user_id, message, status='unread'):
        self.user_id = user_id
        self.message = message
        self.status = status

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "message": self.message,
            "status": self.status
        }


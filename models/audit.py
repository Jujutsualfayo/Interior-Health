class AuditLog:
    def __init__(self, action, user_id, timestamp):
        self.action = action
        self.user_id = user_id
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "action": self.action,
            "user_id": self.user_id,
            "timestamp": self.timestamp
        }


class User:
    ROLES = ['patient', 'health_worker', 'admin']

    def __init__(self, name, email, password, role='patient'):
        if role not in self.ROLES:
            raise ValueError("Invalid role")
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "role": self.role
        }

    @staticmethod
    def reset_password(email):
        """Will be enabling resetting the user's password via email."""
        print(f"Password reset link sent to {email}")


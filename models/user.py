from .database import db  # Import the database instance

class User(db.Model):
    """Model for storing user details."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    username = db.Column(db.String(80), nullable=False, unique=True)  # Unique username
    email = db.Column(db.String(120), nullable=False, unique=True)  # Unique email
    password = db.Column(db.String(128), nullable=False)  # Password (hashed)

    def __init__(self, username, email, password):
        """
        Constructor to initialize a User instance.
        :param username: The username of the user.
        :param email: The email of the user.
        :param password: The hashed password of the user.
        """
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        """String representation of the User instance."""
        return f"<User {self.username}>"

    def as_dict(self):
        """
        Serialize the user object into a dictionary.
        Useful for APIs or JSON responses.
        """
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }

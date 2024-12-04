from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def reset_test_db():
    """Reset the database for testing."""
    db.drop_all()
    db.create_all()
    populate_test_data()

def populate_test_data():
    """Insert initial data into the test database."""
    from app.models import User, Teleconsultation  # Import models here to avoid circular imports

    user1 = User(id=1, name="Alice", email="alice@example.com")
    user2 = User(id=2, name="Bob", email="bob@example.com")

    teleconsultation = Teleconsultation(user_id=1, time_slot="2024-12-05T10:00")

    db.session.add_all([user1, user2, teleconsultation])
    db.session.commit()


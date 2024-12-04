from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def reset_test_db():
    """Reset the database to its initial test state."""
    # Drop all tables
    db.drop_all()

    # Recreate tables
    db.create_all()

    # Add initial test data
    populate_test_data()

def populate_test_data():
    """Insert initial test data into the database."""
    from models import User, Teleconsultation  # Import models as needed

    # Add users
    user1 = User(id=1, name="Alice", email="alice@example.com")
    user2 = User(id=2, name="Bob", email="bob@example.com")

    db.session.add_all([user1, user2])

    # Add teleconsultation data
    teleconsultation = Teleconsultation(user_id=1, time_slot="2024-12-05T10:00")
    db.session.add(teleconsultation)

    # Commit changes
    db.session.commit()

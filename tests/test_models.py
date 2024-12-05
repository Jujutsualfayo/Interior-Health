import pytest
from datetime import datetime
from app import db
from app.models import User, Drug, Order, Teleconsultation, ChatbotInteraction  # Update with correct model import path

# Test for User model
def test_user_model(test_db):
    """Test the User model."""
    user = User(name="John Doe", email="john.doe@example.com", password_hash="hashed_password", role="patient")
    db.session.add(user)
    db.session.commit()

    queried_user = User.query.filter_by(email="john.doe@example.com").first()

    # Ensure the user was saved and retrieved correctly
    assert queried_user is not None
    assert queried_user.name == "John Doe"
    assert queried_user.email == "john.doe@example.com"
    assert queried_user.role == "patient"
    assert queried_user.password_hash == "hashed_password"

# Test for Drug model
def test_drug_model(test_db):
    """Test the Drug model."""
    drug = Drug(name="Paracetamol", description="Pain reliever", price=5.0, stock=100)
    db.session.add(drug)
    db.session.commit()

    queried_drug = Drug.query.filter_by(name="Paracetamol").first()

    # Ensure the drug was saved and retrieved correctly
    assert queried_drug is not None
    assert queried_drug.name == "Paracetamol"
    assert queried_drug.description == "Pain reliever"
    assert queried_drug.price == 5.0
    assert queried_drug.stock == 100

# Test for Order model
def test_order_model(test_db):
    """Test the Order model."""
    user = User(name="Jane Doe", email="jane.doe@example.com", password_hash="hashed_password", role="patient")
    drug = Drug(name="Ibuprofen", description="Anti-inflammatory", price=10.0, stock=50)
    db.session.add(user)
    db.session.add(drug)
    db.session.commit()

    order = Order(user_id=user.id, drug_id=drug.id, quantity=2, total_price=20.0, status="pending")
    db.session.add(order)
    db.session.commit()

    queried_order = Order.query.filter_by(user_id=user.id).first()

    # Ensure the order was saved and retrieved correctly
    assert queried_order is not None
    assert queried_order.quantity == 2
    assert queried_order.total_price == 20.0
    assert queried_order.status == "pending"
    assert queried_order.user_id == user.id
    assert queried_order.drug_id == drug.id

# Test for Teleconsultation model
def test_teleconsultation_model(test_db):
    """Test the Teleconsultation model."""
    date = datetime.strptime('2024-12-05', '%Y-%m-%d')

    teleconsultation = Teleconsultation(patient_name='Test Patient', date=date, status='Scheduled')
    db.session.add(teleconsultation)
    db.session.commit()

    queried_teleconsultation = Teleconsultation.query.filter_by(patient_name='Test Patient').first()

    # Ensure the teleconsultation was saved correctly
    assert queried_teleconsultation is not None
    assert queried_teleconsultation.status == 'Scheduled'
    
    # Ensure the date comparison works with datetime objects
    assert queried_teleconsultation.date == date

# Test for ChatbotInteraction model
def test_chatbot_model(test_db):
    """Test the ChatbotInteraction model."""
    chatbot_interaction = ChatbotInteraction(query="How are you?", response="I'm good, thanks!")
    db.session.add(chatbot_interaction)
    db.session.commit()

    # Use filter() instead of filter_by() for querying by 'query' field
    queried_interaction = ChatbotInteraction.query.filter(ChatbotInteraction.query == "How are you?").first()

    # Ensure the interaction was correctly saved and retrieved
    assert queried_interaction is not None
    assert queried_interaction.query == "How are you?"
    assert queried_interaction.response == "I'm good, thanks!"


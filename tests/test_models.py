import pytest
from datetime import datetime
from app import create_app
from models import db, User, Product, Order, Payment, Tracking, ChatbotInteraction, Teleconsultation

# Create the app for testing
app = create_app()

# Initialize app context for testing
@pytest.fixture(scope='module')
def test_app():
    app_context = app.app_context()
    app_context.push()
    yield app
    app_context.pop()

# Setup the database for testing
@pytest.fixture(scope='module')
def test_db(test_app):
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()

def test_user_model(test_db):
    """Test the User model."""
    user = User(username='testuser', email='test@example.com', password='password123')
    db.session.add(user)
    db.session.commit()
    queried_user = User.query.filter_by(username='testuser').first()
    assert queried_user is not None
    assert queried_user.username == 'testuser'
    assert queried_user.email == 'test@example.com'

def test_product_model(test_db):
    """Test the Product model."""
    product = Product(name='Test Product', price=19.99, description='A test product', stock=100)
    db.session.add(product)
    db.session.commit()
    queried_product = Product.query.filter_by(name='Test Product').first()
    assert queried_product is not None
    assert queried_product.name == 'Test Product'
    assert queried_product.price == 19.99
    assert queried_product.description == 'A test product'
    assert queried_product.stock == 100

def test_order_model(test_db):
    """Test the Order model."""
    order = Order(product_id=1, user_id=1, quantity=2)
    db.session.add(order)
    db.session.commit()
    queried_order = Order.query.filter_by(product_id=1).first()
    assert queried_order is not None
    assert queried_order.quantity == 2

def test_chatbot_model(test_db):
    """Test the ChatbotInteraction model."""
    chatbot_interaction = ChatbotInteraction(query="How are you?", response="I'm good, thanks!")
    db.session.add(chatbot_interaction)
    db.session.commit()

    # Fix: Use filter() instead of filter_by for querying by 'query' field
    queried_interaction = ChatbotInteraction.query.filter(ChatbotInteraction.query == "How are you?").first()

    assert queried_interaction is not None
    assert queried_interaction.query == "How are you?"
    assert queried_interaction.response == "I'm good, thanks!"

def test_teleconsultation_model(test_db):
    """Test the Teleconsultation model."""
    # Convert string date to datetime object (to ensure comparison with datetime)
    date = datetime.strptime('2024-12-05', '%Y-%m-%d')

    teleconsultation = Teleconsultation(patient_name='Test Patient', date=date, status='Scheduled')
    db.session.add(teleconsultation)
    db.session.commit()

    queried_teleconsultation = Teleconsultation.query.filter_by(patient_name='Test Patient').first()

    assert queried_teleconsultation is not None
    assert queried_teleconsultation.status == 'Scheduled'

    # Fix: Ensure comparison works between datetime objects
    assert queried_teleconsultation.date == date

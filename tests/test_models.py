import pytest
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
    # Create a test user
    user = User(username='testuser', email='test@example.com', password='password123')
    
    # Add the user to the session and commit
    db.session.add(user)
    db.session.commit()

    # Query the user back from the database
    queried_user = User.query.filter_by(username='testuser').first()

    # Assert the user was added correctly
    assert queried_user is not None
    assert queried_user.username == 'testuser'
    assert queried_user.email == 'test@example.com'

def test_product_model(test_db):
    """Test the Product model."""
    # Create a test product
    product = Product(name='Test Product', price=19.99)
    
    # Add the product to the session and commit
    db.session.add(product)
    db.session.commit()

    # Query the product back from the database
    queried_product = Product.query.filter_by(name='Test Product').first()

    # Assert the product was added correctly
    assert queried_product is not None
    assert queried_product.name == 'Test Product'
    assert queried_product.price == 19.99

def test_order_model(test_db):
    """Test the Order model."""
    # Create a test order
    order = Order(product_id=1, user_id=1, quantity=2)
    
    # Add the order to the session and commit
    db.session.add(order)
    db.session.commit()

    # Query the order back from the database
    queried_order = Order.query.filter_by(product_id=1).first()

    # Assert the order was added correctly
    assert queried_order is not None
    assert queried_order.quantity == 2

def test_chatbot_model(test_db):
    """Test the ChatbotInteraction model."""
    # Create a test chatbot interaction
    chatbot_interaction = ChatbotInteraction(query="How are you?")
    
    # Add the interaction to the session and commit
    db.session.add(chatbot_interaction)
    db.session.commit()

    # Query the interaction back from the database
    queried_interaction = ChatbotInteraction.query.filter_by(query="How are you?").first()

    # Assert the interaction was added correctly
    assert queried_interaction is not None
    assert queried_interaction.query == "How are you?"

def test_teleconsultation_model(test_db):
    """Test the Teleconsultation model."""
    # Create a test teleconsultation
    teleconsultation = Teleconsultation(patient_name='Test Patient', date='2024-12-05', status='Scheduled')
    
    # Add the teleconsultation to the session and commit
    db.session.add(teleconsultation)
    db.session.commit()

    # Query the teleconsultation back from the database
    queried_teleconsultation = Teleconsultation.query.filter_by(patient_name='Test Patient').first()

    # Assert the teleconsultation was added correctly
    assert queried_teleconsultation is not None
    assert queried_teleconsultation.status == 'Scheduled'


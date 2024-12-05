# tests/test_models.py
import pytest
from app import db
from models import User, Product
from models.chatbot import Chatbot

# Fixture to set up and tear down the database
@pytest.fixture
def setup_db():
    # Create the tables for the test database
    db.create_all()
    yield
    # Clean up database after each test
    db.session.remove()
    db.drop_all()

def test_create_user(setup_db):
    """Test user creation."""
    user = User(name="John Doe", email="john@example.com", password="password")
    db.session.add(user)
    db.session.commit()
    
    # Query the database to check if the user was created
    created_user = User.query.filter_by(email="john@example.com").first()
    assert created_user is not None
    assert created_user.name == "John Doe"
    assert created_user.email == "john@example.com"

def test_create_product(setup_db):
    """Test product creation."""
    product = Product(name="Aspirin", description="Pain reliever", price=5.00)
    db.session.add(product)
    db.session.commit()
    
    # Query the database to check if the product was created
    created_product = Product.query.filter_by(name="Aspirin").first()
    assert created_product is not None
    assert created_product.price == 5.00
    assert created_product.description == "Pain reliever"

def test_update_user(setup_db):
    """Test user update."""
    user = User(name="John Doe", email="john@example.com", password="password")
    db.session.add(user)
    db.session.commit()

    # Update the user's name
    user.name = "Jane Doe"
    db.session.commit()

    updated_user = User.query.filter_by(email="john@example.com").first()
    assert updated_user.name == "Jane Doe"

def test_delete_user(setup_db):
    """Test user deletion."""
    user = User(name="John Doe", email="john@example.com", password="password")
    db.session.add(user)
    db.session.commit()

    user_to_delete = User.query.filter_by(email="john@example.com").first()
    db.session.delete(user_to_delete)
    db.session.commit()

    deleted_user = User.query.filter_by(email="john@example.com").first()
    assert deleted_user is None

def test_create_product_with_unique_name(setup_db):
    """Test creating two products with the same name."""
    product1 = Product(name="Aspirin", description="Pain reliever", price=5.00)
    product2 = Product(name="Aspirin", description="Pain reliever", price=6.00)
    
    db.session.add(product1)
    db.session.commit()
    
    # Trying to create another product with the same name
    with pytest.raises(Exception):  # You can specify a specific exception type based on your app's setup
        db.session.add(product2)
        db.session.commit()

def test_product_association_with_order(setup_db):
    """Test creating an order associated with a product and user."""
    user = User(name="John Doe", email="john@example.com", password="password")
    product = Product(name="Aspirin", description="Pain reliever", price=5.00)
    
    db.session.add(user)
    db.session.add(product)
    db.session.commit()

    # Assuming you have a relationship between User and Product through an Order model
    order = Order(user_id=user.id, product_id=product.id, quantity=2)
    db.session.add(order)
    db.session.commit()

    user_orders = User.query.filter_by(id=user.id).first().orders
    assert len(user_orders) == 1
    assert user_orders[0].product.name == "Aspirin"
    assert user_orders[0].quantity == 2

def test_product_price_update(setup_db):
    """Test updating product price."""
    product = Product(name="Aspirin", description="Pain reliever", price=5.00)
    db.session.add(product)
    db.session.commit()

    # Update the product's price
    product.price = 6.00
    db.session.commit()

    updated_product = Product.query.filter_by(name="Aspirin").first()
    assert updated_product.price == 6.00



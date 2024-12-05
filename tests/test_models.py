import pytest
from datetime import datetime
from models import User, Product, Order, Payment, Tracking, ChatbotInteraction, Teleconsultation
from models.database import db


@pytest.fixture
def test_db(app):
    """
    A pytest fixture to set up and tear down the test database.
    """
    with app.app_context():
        db.create_all()  # Create tables
        yield db
        db.session.remove()
        db.drop_all()  # Drop tables after the test


def test_user_model(test_db):
    """
    Test the User model.
    """
    user = User(username="testuser", email="test@example.com", password="password123")
    test_db.session.add(user)
    test_db.session.commit()

    queried_user = User.query.first()
    assert queried_user is not None, "User was not added to the database."
    assert queried_user.username == "testuser", "Username does not match."
    assert queried_user.email == "test@example.com", "Email does not match."


def test_product_model(test_db):
    """
    Test the Product model.
    """
    product = Product(name="Test Product", price=19.99, description="A test product.", stock=10)
    test_db.session.add(product)
    test_db.session.commit()

    queried_product = Product.query.first()
    assert queried_product is not None, "Product was not added to the database."
    assert queried_product.name == "Test Product", "Product name does not match."
    assert queried_product.price == 19.99, "Product price does not match."
    assert queried_product.description == "A test product.", "Product description does not match."
    assert queried_product.stock == 10, "Product stock does not match."


def test_order_model(test_db):
    """
    Test the Order model.
    """
    order = Order(product_id=1, user_id=1, quantity=2)
    test_db.session.add(order)
    test_db.session.commit()

    queried_order = Order.query.first()
    assert queried_order is not None, "Order was not added to the database."
    assert queried_order.product_id == 1, "Order product_id does not match."
    assert queried_order.user_id == 1, "Order user_id does not match."
    assert queried_order.quantity == 2, "Order quantity does not match."


def test_payment_model(test_db):
    """
    Test the Payment model.
    """
    payment = Payment(order_id=1, amount=39.98, status="Completed")
    test_db.session.add(payment)
    test_db.session.commit()

    queried_payment = Payment.query.first()
    assert queried_payment is not None, "Payment was not added to the database."
    assert queried_payment.order_id == 1, "Payment order_id does not match."
    assert queried_payment.amount == 39.98, "Payment amount does not match."
    assert queried_payment.status == "Completed", "Payment status does not match."


def test_tracking_model(test_db):
    """
    Test the Tracking model.
    """
    tracking = Tracking(order_id=1, status="In Transit")
    test_db.session.add(tracking)
    test_db.session.commit()

    queried_tracking = Tracking.query.first()
    assert queried_tracking is not None, "Tracking was not added to the database."
    assert queried_tracking.order_id == 1, "Tracking order_id does not match."
    assert queried_tracking.status == "In Transit", "Tracking status does not match."


def test_chatbot_model(test_db):
    """
    Test the ChatbotInteraction model.
    """
    chatbot_interaction = ChatbotInteraction(query="How are you?", response="I am fine.", timestamp=datetime.utcnow())
    test_db.session.add(chatbot_interaction)
    test_db.session.commit()

    queried_chatbot = ChatbotInteraction.query.first()
    assert queried_chatbot is not None, "ChatbotInteraction was not added to the database."
    assert queried_chatbot.query == "How are you?", "ChatbotInteraction query does not match."
    assert queried_chatbot.response == "I am fine.", "ChatbotInteraction response does not match."


def test_teleconsultation_model(test_db):
    """
    Test the Teleconsultation model.
    """
    teleconsultation = Teleconsultation(
        patient_name="Test Patient",
        date=datetime(2024, 12, 15, 10, 30),
        status="Scheduled",
        notes="Initial consultation for follow-up."
    )
    test_db.session.add(teleconsultation)
    test_db.session.commit()

    queried_consultation = Teleconsultation.query.first()
    assert queried_consultation is not None, "Teleconsultation was not added to the database."
    assert queried_consultation.patient_name == "Test Patient", "Patient name does not match."
    assert queried_consultation.date == datetime(2024, 12, 15, 10, 30), "Date does not match."
    assert queried_consultation.status == "Scheduled", "Status does not match."
    assert queried_consultation.notes == "Initial consultation for follow-up.", "Notes do not match."

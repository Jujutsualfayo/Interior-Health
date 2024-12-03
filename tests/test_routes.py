import unittest
import json
from app import app  
from db_utils import Database

class TestRoutes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        cls.client = app.test_client()  # Create a test client
        Database.reset_test_db()  # Reset the database for testing (Assumes a method for this)

    def test_get_users(self):
        """Test retrieving all users."""
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('users', data)

    def test_get_user(self):
        """Test retrieving a specific user."""
        # Insert a test user into the database
        user_id = Database.create_user("Joy Kamau", "joywanjiku@gmail.com", "password", "patient")
        response = self.client.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('user', data)
        self.assertEqual(data['user']['email'], "joywanjiku@gmail.com")

    def test_create_order(self):
        """Test creating an order."""
        # Insert a test user and product into the database
        user_id = Database.create_user("Festus Kip", "festuskip@gmail.com", "password", "patient")
        product_id = Database.create_product("Painkillers", "For headaches", 10.00, 100)
        response = self.client.post('/orders', json={
            "user_id": user_id,
            "product_id": product_id,
            "quantity": 2
        })
        self.assertEqual(response.status_code, 201)
        data = response.json
        self.assertIn('order_id', data)

    def test_create_payment(self):
        """Test processing a payment."""
        # Insert a test user and order into the database
        user_id = Database.create_user("Alice Brown", "alice.brown@example.com", "password", "patient")
        product_id = Database.create_product("Antibiotics", "For infections", 20.00, 50)
        order_id = Database.create_order(user_id, product_id, 1)
        response = self.client.post('/payments', json={
            "user_id": user_id,
            "order_id": order_id,
            "amount": 20.00
        })
        self.assertEqual(response.status_code, 201)
        data = response.json
        self.assertIn('payment_id', data)

    def test_interact_chatbot(self):
        """Test chatbot interaction."""
        # Insert a test user
        user_id = Database.create_user("Mark White", "mark.white@example.com", "password", "patient")
        response = self.client.post('/chatbot', json={
            "user_id": user_id,
            "question": "What medication do you recommend for flu?"
        })
        self.assertEqual(response.status_code, 201)
        data = response.json
        self.assertIn('interaction_id', data)

    def test_book_teleconsultation(self):
        """Test booking a teleconsultation."""
        # Insert a test user
        user_id = Database.create_user("Lucy Green", "lucy.green@example.com", "password", "patient")
        response = self.client.post('/teleconsultations', json={
            "user_id": user_id,
            "doctor_name": "Dr. Watson",
            "appointment_time": "2024-12-05T10:00:00"
        })
        self.assertEqual(response.status_code, 201)
        data = response.json
        self.assertIn('teleconsultation_id', data)

    def test_get_nonexistent_user(self):
        """Test retrieving a non-existent user."""
        response = self.client.get('/users/9999')  # Non-existent user ID
        self.assertEqual(response.status_code, 404)
        data = response.json
        self.assertIn('error', data)
        self.assertEqual(data['error'], "User not found")

if __name__ == '__main__':
    unittest.main()


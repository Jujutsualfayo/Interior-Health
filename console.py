#!/usr/bin/python3
"""
Interior Health app console a good one
"""

import cmd
from models import (
    User,
    Product,
    Order,
    Payment,
    Tracking,
    ChatbotInteraction,
    Teleconsultation
)
from utils.db_utils import DBUtils


class InteriorHealthConsole(cmd.Cmd):
    prompt = "(interior_health) "
    intro = "Welcome to the InteriorHealth App Console. Type help or ? to list commands."

    def do_create_user(self, args):
        """Create a new user."""
        try:
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            phone = input("Enter phone: ")
            address = input("Enter address: ")

            query = """
                INSERT INTO users (name, email, password, phone, address)
                VALUES (%s, %s, %s, %s, %s)
            """
            DBUtils.execute_update(query, (name, email, password, phone, address))
            print("User created successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def do_search_medication(self, args):
        """Search for a medication by name."""
        try:
            name = input("Enter medication name: ")
            query = "SELECT * FROM products WHERE name LIKE %s"
            results = DBUtils.execute_query(query, (f"%{name}%",))
            for product in results:
                print(product)
        except Exception as e:
            print(f"Error: {e}")

    def do_order_medication(self, args):
        """Create an order for a medication."""
        try:
            user_id = input("Enter user ID: ")
            product_id = input("Enter product ID: ")
            quantity = input("Enter quantity: ")

            query = """
                INSERT INTO orders (user_id, product_id, quantity)
                VALUES (%s, %s, %s)
            """
            DBUtils.execute_update(query, (user_id, product_id, quantity))
            print("Order placed successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def do_view_orders(self, args):
        """View all orders."""
        try:
            query = "SELECT * FROM orders"
            results = DBUtils.execute_query(query)
            for order in results:
                print(order)
        except Exception as e:
            print(f"Error: {e}")

    def do_track_delivery(self, args):
        """Track the delivery status of an order."""
        try:
            order_id = input("Enter order ID: ")
            query = "SELECT * FROM tracking WHERE order_id = %s"
            results = DBUtils.execute_query(query, (order_id,))
            for tracking in results:
                print(tracking)
        except Exception as e:
            print(f"Error: {e}")

    def do_exit(self, args):
        """Exit the console."""
        print("Exiting InteriorHealth Console. Goodbye!")
        return True


if __name__ == "__main__":
    InteriorHealthConsole().cmdloop()


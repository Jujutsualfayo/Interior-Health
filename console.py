import cmd
from models import (
    User, Product, Order, Payment, Tracking, 
    ChatbotInteraction, Teleconsultation, Inventory, 
    DeliveryRoute, DistributionCenter, HealthCampaign
)
from utils.route_optimization import optimize_route
from utils.ai_chatbot import get_chatbot_response
from database import session


class InteriorHealthConsole(cmd.Cmd):
    prompt = "InteriorHealth> "

    def do_add_user(self, args):
        """Add a new user: add_user <name> <email> <password> <phone> <address>"""
        try:
            name, email, password, phone, address = args.split()
            user = User(name=name, email=email, password=password, phone=phone, address=address)
            session.add(user)
            session.commit()
            print("User added successfully.")
        except ValueError:
            print("Invalid input. Usage: add_user <name> <email> <password> <phone> <address>")

    def do_add_product(self, args):
        """Add a new product: add_product <name> <description> <price> <stock>"""
        try:
            name, description, price, stock = args.split(maxsplit=3)
            product = Product(name=name, description=description, price=float(price), stock=int(stock))
            session.add(product)
            session.commit()
            print("Product added successfully.")
        except ValueError:
            print("Invalid input. Usage: add_product <name> <description> <price> <stock>")

    def do_create_order(self, args):
        """Create a new order: create_order <user_id> <product_id> <quantity>"""
        try:
            user_id, product_id, quantity = map(int, args.split())
            order = Order(user_id=user_id, product_id=product_id, quantity=quantity)
            session.add(order)
            session.commit()
            print("Order created successfully.")
        except ValueError:
            print("Invalid input. Usage: create_order <user_id> <product_id> <quantity>")

    def do_track_order(self, args):
        """Track an order: track_order <order_id>"""
        try:
            order_id = int(args)
            tracking = session.query(Tracking).filter_by(order_id=order_id).first()
            if tracking:
                print(f"Order Status: {tracking.status}, Last Updated: {tracking.last_updated}")
            else:
                print("Tracking information not found.")
        except ValueError:
            print("Invalid input. Usage: track_order <order_id>")

    def do_add_inventory(self, args):
        """Add inventory: add_inventory <name> <stock> <location>"""
        try:
            name, stock, location = args.split(maxsplit=2)
            inventory = Inventory(name=name, stock=int(stock), location=location)
            session.add(inventory)
            session.commit()
            print("Inventory item added successfully.")
        except ValueError:
            print("Invalid input. Usage: add_inventory <name> <stock> <location>")

    def do_manage_routes(self, args):
        """Manage delivery routes: manage_routes <start> <end> [waypoint1 waypoint2 ...]"""
        try:
            args_list = args.split()
            start, end = args_list[0], args_list[1]
            waypoints = args_list[2:]
            optimized_route = optimize_route(start, end, waypoints)
            print(f"Optimized Route: {optimized_route}")
        except ValueError:
            print("Invalid input. Usage: manage_routes <start> <end> [waypoint1 waypoint2 ...]")

    def do_start_chatbot(self, args):
        """Start a chatbot interaction: start_chatbot"""
        print("Chatbot started. Type 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Exiting chatbot.")
                break
            response = get_chatbot_response(user_input)
            print(f"Bot: {response}")

    def do_schedule_teleconsultation(self, args):
        """Schedule a teleconsultation: schedule_teleconsultation <user_id> <doctor_name> <appointment_time>"""
        try:
            user_id, doctor_name, appointment_time = args.split(maxsplit=2)
            teleconsultation = Teleconsultation(user_id=int(user_id), doctor_name=doctor_name, appointment_time=appointment_time)
            session.add(teleconsultation)
            session.commit()
            print("Teleconsultation scheduled successfully.")
        except ValueError:
            print("Invalid input. Usage: schedule_teleconsultation <user_id> <doctor_name> <appointment_time>")

    def do_list_products(self, args):
        """List all available products: list_products"""
        products = session.query(Product).all()
        for product in products:
            print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Stock: {product.stock}")

    def do_exit(self, args):
        """Exit the console."""
        print("Goodbye!")
        return True


if __name__ == "__main__":
    console = InteriorHealthConsole()
    console.cmdloop()


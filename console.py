from models.user import User
from models.medication import Medication
from models.order import Order
from models.chatbot import Chatbot
from models.payment import Payment

def main():
    print("Jambo welcome to Interior Health Console")
    while True:
        print("\n1. Create User\n2. Search Medications\n3. Track Order\n4. Chatbot Query\n5. Process Payment\n6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            password = input("Password: ")
            role = input("Role (patient/health_worker/admin): ")
            user = User(name, email, password, role)
            print(f"User created: {user.to_dict()}")
        
        elif choice == "2":
            name = input("Medication name: ")
            Medication.search(name)
        
        elif choice == "3":
            order_id = input("Order ID: ")
            Order.track_order(order_id)
        
        elif choice == "4":
            query = input("Enter your question: ")
            response = Chatbot.get_response(query)
            print(f"Chatbot: {response}")
        
        elif choice == "5":
            user_id = input("User ID: ")
            order_id = input("Order ID: ")
            amount = float(input("Amount: "))
            Payment.process_payment(user_id, order_id, amount)
        
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()


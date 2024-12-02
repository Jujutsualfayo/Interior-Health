from models.user import User
from models.medication import Medication
from models.order import Order
from models.chatbot import Chatbot
from models.payment import Payment
from models.appointment import Appointment
from models.feedback import Feedback
from utils.notification_service import send_notification
from utils.report_generator import generate_report

def main():
    print("Jambo Welcome to InteriorHealth Console")
    while True:
        print("\nOptions:")
        print("1. Create User\n2. Search Medications\n3. Track Order\n4. Chatbot Query\n5. Process Payment")
        print("6. Schedule Appointment\n7. Submit Feedback\n8. Generate Report\n9. Send Notification\n10. Exit")
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
            user_id = input("User ID: ")
            doctor_name = input("Doctor Name: ")
            time = input("Appointment Time: ")
            appointment = Appointment(user_id, doctor_name, time)
            print(f"Appointment scheduled: {appointment.to_dict()}")
        
        elif choice == "7":
            user_id = input("User ID: ")
            message = input("Feedback: ")
            rating = input("Rating (1-5): ")
            feedback = Feedback(user_id, message, rating)
            print(f"Feedback submitted: {feedback.to_dict()}")
        
        elif choice == "8":
            report_type = input("Report Type (e.g., orders, feedback): ")
            content = generate_report(report_type)
            print(f"Report Generated: {content}")
        
        elif choice == "9":
            user_id = input("User ID: ")
            message = input("Notification Message: ")
            send_notification(user_id, message)
        
        elif choice == "10":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


InteriorHealth
InteriorHealth is an innovative health management platform aimed at providing healthcare services to people in interior regions. It integrates multiple features, including searching and ordering medications, delivery tracking, an AI-powered chatbot for health queries, teleconsultations with doctors, practitioner and admin dashboards, and secure payment processing.

It is also my Alx final stretch portfolio project!!
Features
General Features
Search and Order Medications: Users can browse, search for, and order medications easily.
Delivery Tracking: Real-time updates on medication delivery status.
AI Chatbot: Provides instant answers to health-related queries.
Teleconsultation: Schedule virtual appointments with healthcare professionals.
Secure Payments: Ensure seamless payment integration for services and products.
Practitioner Dashboard: A dedicated portal for doctors to manage consultations and records.
Admin Dashboard: Manage the platform, including users, products, orders, and reports.
Project Architecture
Backend
Programming Language: Python
Framework: Custom-built console with MySQL database integration.
Database

Relational Database: MySQL

Tables:
users: Manage user data.
products: Store medication details.
orders: Track user orders.
tracking: Manage delivery status of orders.
chatbot_interactions: Log interactions with the AI chatbot.
teleconsultations: Track and manage virtual doctor appointments.
payments: Record payment details for all transactions.
Getting Started
Prerequisites
Python 3.x
MySQL Server installed and running
bash
Copy code
pip install -r requirements.txt  
Configure the Database:

Open the MySQL terminal:
bash
Copy code
mysql -u root
Create a new database:
sql
Copy code
CREATE DATABASE interior_health;
Run Database Initialization Script:

Supported commands:

create_user - Add new users.
create_product - Add medications or healthcare products.
create_order - Place an order for products.
create_tracking - Update and view order delivery status.
create_chatbot_interaction - Log AI chatbot interactions.
create_teleconsultation - Schedule appointments with doctors.
create_payment - Record payment details for transactions

License
This project is licensed under the MIT License.

Contact
For questions, feedback, or contributions, feel free to reach out:

Email: benjaminalfayo90@gmail.com
GitHub Issues: Issue Tracker









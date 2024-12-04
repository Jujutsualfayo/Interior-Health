import mysql.connector
from mysql.connector import errorcode


class Database:
    """
    Utility class for handling database operations.
    """

    @staticmethod
    def connect():
        """
        Connect to the MySQL database.

        Returns:
            Connection object if successful, None otherwise.
        """
        try:
            conn = mysql.connector.connect(
                host="localhost",  
                user="root",       
                password="Alphafemale1",       
                database="interior_health"  
            )
            return conn
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error: Invalid MySQL credentials.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Error: Database does not exist.")
            else:
                print(f"Error: {err}")
            return None

    @staticmethod
    def reset_test_db():
        """
        Resets the database for testing purposes by clearing tables and resetting them.
        """
        conn = Database.connect()
        if not conn:
            print("Failed to reset test database.")
            return
        try:
            cursor = conn.cursor()
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
            cursor.execute("TRUNCATE TABLE users;")
            cursor.execute("TRUNCATE TABLE medications;")
            cursor.execute("TRUNCATE TABLE orders;")
            cursor.execute("TRUNCATE TABLE payments;")
            cursor.execute("TRUNCATE TABLE deliveries;")
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
            conn.commit()
            print("Test database reset successfully.")
        except mysql.connector.Error as err:
            print(f"Error resetting test database: {err}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def create_user(name, email, password, role):
        """
        Create a new user.

        Args:
            name (str): Name of the user.
            email (str): Email of the user.
            password (str): Hashed password.
            role (str): User role (e.g., "patient", "health_worker", "admin").

        Returns:
            int: ID of the newly created user.
        """
        query = """
            INSERT INTO users (name, email, password, role)
            VALUES (%s, %s, %s, %s);
        """
        params = (name, email, password, role)
        conn = Database.connect()
        if not conn:
            return None
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Error creating user: {err}")
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_user_by_email(email):
        """
        Retrieve a user by email.

        Args:
            email (str): Email of the user.

        Returns:
            dict: User details if found, None otherwise.
        """
        query = "SELECT * FROM users WHERE email = %s;"
        conn = Database.connect()
        if not conn:
            return None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, (email,))
            return cursor.fetchone()
        except mysql.connector.Error as err:
            print(f"Error fetching user by email: {err}")
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def create_medication(name, description, price, stock):
        """
        Add a new medication.

        Args:
            name (str): Name of the medication.
            description (str): Description of the medication.
            price (float): Price of the medication.
            stock (int): Stock quantity.

        Returns:
            int: ID of the newly added medication.
        """
        query = """
            INSERT INTO medications (name, description, price, stock)
            VALUES (%s, %s, %s, %s);
        """
        params = (name, description, price, stock)
        conn = Database.connect()
        if not conn:
            return None
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Error adding medication: {err}")
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def create_order(user_id, medication_id, quantity):
        """
        Create a new order.

        Args:
            user_id (int): ID of the user placing the order.
            medication_id (int): ID of the medication.
            quantity (int): Quantity ordered.

        Returns:
            int: ID of the newly created order.
        """
        query = """
            INSERT INTO orders (user_id, medication_id, quantity)
            VALUES (%s, %s, %s);
        """
        params = (user_id, medication_id, quantity)
        conn = Database.connect()
        if not conn:
            return None
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Error creating order: {err}")
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def create_payment(order_id, amount, status):
        """
        Record a payment.

        Args:
            order_id (int): ID of the order.
            amount (float): Payment amount.
            status (str): Payment status (e.g., "completed", "pending").

        Returns:
            int: ID of the payment record.
        """
        query = """
            INSERT INTO payments (order_id, amount, status)
            VALUES (%s, %s, %s);
        """
        params = (order_id, amount, status)
        conn = Database.connect()
        if not conn:
            return None
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Error creating payment: {err}")
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def execute_query(query, params=None):
        """
        Execute a query on the database.

        Args:
            query (str): The SQL query to execute.
            params (tuple, optional): Parameters for the query.

        Returns:
            list: Query result rows, if any.
        """
        conn = Database.connect()
        if not conn:
            return None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, params)
            results = cursor.fetchall()
            conn.commit()
            return results
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")
            return None
        finally:
            cursor.close()
            conn.close()

# utils/db_utils.py

import mysql.connector
from mysql.connector import errorcode

class Database:
    """Utility class for handling database operations."""

    @staticmethod
    def connect():
        """
        Connect to the MySQL database.

        Returns:
            A MySQL connection object or None if the connection fails.
        """
        try:
            conn = mysql.connector.connect(
                host="localhost",  
                user="root",       
                password="Alphafemale1",       
                database="interior_health"  # Change to your database name
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

    @staticmethod
    def execute_update(query, params=None):
        """
        Execute an update/insert/delete query on the database.

        Args:
            query (str): The SQL query to execute.
            params (tuple, optional): Parameters for the query.

        Returns:
            int: Number of affected rows.
        """
        conn = Database.connect()
        if not conn:
            return 0
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount
        except mysql.connector.Error as err:
            print(f"Error executing update: {err}")
            return 0
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def execute_many(query, data):
        """
        Execute a query with multiple sets of parameters.

        Args:
            query (str): The SQL query to execute.
            data (list of tuple): List of parameter tuples.

        Returns:
            int: Number of affected rows.
        """
        conn = Database.connect()
        if not conn:
            return 0
        try:
            cursor = conn.cursor()
            cursor.executemany(query, data)
            conn.commit()
            return cursor.rowcount
        except mysql.connector.Error as err:
            print(f"Error executing batch query: {err}")
            return 0
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def reset_test_db():
        """
        Reset the database for testing purposes by dropping and recreating tables.
        This will clear all data and recreate tables for a fresh test run.
        """
        conn = Database.connect()  # Use the Database connection method
        if not conn:
            print("Failed to connect to the database.")
            return

        try:
            cursor = conn.cursor()
            # Drop existing test database if it exists
            cursor.execute("DROP DATABASE IF EXISTS interior_health_test;")
            cursor.execute("CREATE DATABASE interior_health_test;")
            cursor.execute("USE interior_health_test;")
            
            # Add table creation queries for your app's tables
            # For example, creating users table
            cursor.execute("""
                CREATE TABLE users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    email VARCHAR(100) UNIQUE,
                    password VARCHAR(100)
                );
            """)
            
            # Example of another table (you can add more based on your app's needs)
            cursor.execute("""
                CREATE TABLE medications (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    description TEXT,
                    price DECIMAL(10, 2),
                    stock INT
                );
            """)

            # Continue adding other necessary tables for orders, payments, etc.

            conn.commit()
            print("Test database reset successfully.")
        except mysql.connector.Error as err:
            print(f"Error resetting database: {err}")
        finally:
            cursor.close()
            conn.close()


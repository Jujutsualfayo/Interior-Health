import mysql.connector
from mysql.connector import errorcode
from models import user, product, order, payment, tracking, chatbot, teleconsultation  # Import existing models

class DatabaseSetup:
    @staticmethod
    def connect():
        """Establish a connection to the MySQL database."""
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
                print("Invalid username or password.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist.")
            else:
                print(err)
            return None

    @staticmethod
    def create_tables():
        """Create necessary tables in the database."""
        conn = DatabaseSetup.connect()
        if not conn:
            return
        
        cursor = conn.cursor()
        
        # Define table creation scripts
        tables = [
            user.CREATE_TABLE_SQL,
            product.CREATE_TABLE_SQL,
            order.CREATE_TABLE_SQL,
            payment.CREATE_TABLE_SQL,
            tracking.CREATE_TABLE_SQL,
            chatbot.CREATE_TABLE_SQL,
            teleconsultation.CREATE_TABLE_SQL
        ]
        
        # Execute table creation
        for table_sql in tables:
            try:
                cursor.execute(table_sql)
                print(f"Table created successfully: {table_sql.split()[2]}")
            except mysql.connector.Error as err:
                print(f"Error creating table: {err}")
        
        conn.commit()
        conn.close()

if __name__ == "__main__":
    print("Initializing database...")
    DatabaseSetup.create_tables()
    print("Database setup complete.")


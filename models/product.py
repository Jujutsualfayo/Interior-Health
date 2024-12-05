from sqlalchemy import Column, Integer, String, Float, Text  # Import
from .database import db  # Import the database instance

class Product(db.Model):
    """Model for storing product details."""
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String(100), nullable=False)  # Product name
    description = Column(Text, nullable=False)  # Detailed description of the product
    price = Column(Float, nullable=False)  # Price of the product
    stock = Column(Integer, nullable=False)  # Quantity in stock

    def __init__(self, name, description, price, stock):
        """
        Constructor to initialize a Product instance.
        :param name: The name of the product.
        :param description: The description of the product.
        :param price: The price of the product.
        :param stock: The stock count of the product.
        """
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def __repr__(self):
        """String representation of the Product instance."""
        return f"<Product {self.name}>"

    def as_dict(self):
        """
        Serialize the product object into a dictionary.
        Useful for APIs or JSON responses.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
        }

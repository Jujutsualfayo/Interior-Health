from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import db


class Order(db.Model):
    """Model for storing order details."""
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)  # Primary key
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)  # Foreign key to Product
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Foreign key to User
    quantity = Column(Integer, nullable=False)  # Quantity of the product ordered

    # Relationships
    product = relationship("Product", backref="orders")  # Establish relationship with Product
    user = relationship("User", backref="orders")  # Establish relationship with User

    def __init__(self, product_id, user_id, quantity):
        """
        Constructor to initialize an Order instance.
        :param product_id: ID of the product being ordered.
        :param user_id: ID of the user placing the order.
        :param quantity: Quantity of the product.
        """
        self.product_id = product_id
        self.user_id = user_id
        self.quantity = quantity

    def __repr__(self):
        """String representation of the Order instance."""
        return f"<Order {self.id}: Product {self.product_id}, User {self.user_id}, Quantity {self.quantity}>"

    def as_dict(self):
        """
        Serialize the order object into a dictionary.
        Useful for APIs or JSON responses.
        """
        return {
            "id": self.id,
            "product_id": self.product_id,
            "user_id": self.user_id,
            "quantity": self.quantity,
        }

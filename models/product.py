from sqlalchemy import Column, Integer, String, Float
from app.database import db


class Product(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)

    def __init__(self, name, description, price, stock):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
        }

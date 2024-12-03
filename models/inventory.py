from database import Base
from sqlalchemy import Column, Integer, String

class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    stock = Column(Integer, nullable=False)
    location = Column(String(255), nullable=False)

    def __init__(self, name, stock, location):
        self.name = name
        self.stock = stock
        self.location = location


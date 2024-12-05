from .database import Base
from sqlalchemy import Column, Integer, String

class DeliveryRoute(Base):
    __tablename__ = 'delivery_routes'

    id = Column(Integer, primary_key=True)
    start_point = Column(String(255), nullable=False)
    end_point = Column(String(255), nullable=False)
    distance = Column(Integer, nullable=False)

    def __init__(self, start_point, end_point, distance):
        self.start_point = start_point
        self.end_point = end_point
        self.distance = distance


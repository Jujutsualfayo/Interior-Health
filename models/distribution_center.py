from .database import Base
from sqlalchemy import Column, Integer, String

class DistributionCenter(Base):
    __tablename__ = 'distribution_centers'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    capacity = Column(Integer, nullable=False)

    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity


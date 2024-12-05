from .database import Base
from sqlalchemy import Column, Integer, String, Date

class HealthCampaign(Base):
    __tablename__ = 'health_campaigns'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    target_location = Column(String(255), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    def __init__(self, name, target_location, start_date, end_date):
        self.name = name
        self.target_location = target_location
        self.start_date = start_date
        self.end_date = end_date


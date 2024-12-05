from sqlalchemy import Column, Integer, String, DateTime, Text
from .database import db
from datetime import datetime


class Teleconsultation(db.Model):
    """Model for storing teleconsultation records."""
    __tablename__ = 'teleconsultations'

    id = Column(Integer, primary_key=True)  # Primary key
    patient_name = Column(String(100), nullable=False)  # Patient's name
    date = Column(DateTime, nullable=False)  # Scheduled date and time
    status = Column(String(50), nullable=False, default="Scheduled")  # Status of the teleconsultation
    notes = Column(Text, nullable=True)  # Additional notes from the consultation

    def __init__(self, patient_name, date, status="Scheduled", notes=None):
        """
        Constructor to initialize a Teleconsultation instance.
        :param patient_name: Name of the patient.
        :param date: Scheduled date and time of the teleconsultation.
        :param status: Current status of the teleconsultation (default: 'Scheduled').
        :param notes: Optional notes for the consultation.
        """
        self.patient_name = patient_name
        self.date = date
        self.status = status
        self.notes = notes

    def __repr__(self):
        """String representation of the Teleconsultation instance."""
        return f"<Teleconsultation {self.id}: Patient='{self.patient_name}', Date={self.date}, Status='{self.status}'>"

    def as_dict(self):
        """
        Serialize the teleconsultation object into a dictionary.
        Useful for APIs or JSON responses.
        """
        return {
            "id": self.id,
            "patient_name": self.patient_name,
            "date": self.date.isoformat(),
            "status": self.status,
            "notes": self.notes,
        }

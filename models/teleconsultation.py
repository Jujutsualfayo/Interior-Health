class Teleconsultation:
    def __init__(self, consultation_id, patient_id, doctor_id, date, time, status="Scheduled"):
        self.consultation_id = consultation_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        self.status = status

    def schedule_consultation(self):
        """Schedule a new teleconsultation."""
        print(f"Teleconsultation scheduled for patient {self.patient_id} with doctor {self.doctor_id} on {self.date} at {self.time}.")

    def update_status(self, new_status):
        """Update the status of the consultation (e.g., completed, canceled)."""
        self.status = new_status
        print(f"Consultation status updated to: {self.status}")

    def __repr__(self):
        return f"Teleconsultation(consultation_id={self.consultation_id}, patient_id={self.patient_id}, doctor_id={self.doctor_id}, date={self.date}, time={self.time}, status={self.status})"

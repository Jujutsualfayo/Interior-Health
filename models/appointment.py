class Appointment:
    def __init__(self, user_id, doctor_name, time, status='scheduled'):
        self.user_id = user_id
        self.doctor_name = doctor_name
        self.time = time
        self.status = status

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "doctor_name": self.doctor_name,
            "time": self.time,
            "status": self.status
        }


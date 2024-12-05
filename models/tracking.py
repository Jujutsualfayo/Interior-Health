from .database import db



class Tracking(db.Model):
    __tablename__ = 'tracking'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Tracking {self.order_id}: {self.status}>"

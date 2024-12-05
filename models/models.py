from .database import db
from datetime import datetime

class User(db.Model):
    """User model representing healthcare system users."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False, default="patient")  # e.g., 'patient', 'health_worker', 'admin'
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    teleconsultations = db.relationship('Teleconsultation', back_populates='user', lazy=True)

    def __repr__(self):
        return f"<User {self.name} ({self.role})>"

class Drug(db.Model):
    """Drug model representing available healthcare drugs."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Drug {self.name}, Price: {self.price}, Stock: {self.stock}>"

class Order(db.Model):
    """Order model for drug purchases."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    drug_id = db.Column(db.Integer, db.ForeignKey('drug.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="pending")  # e.g., 'pending', 'shipped', 'delivered'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    drug = db.relationship('Drug', backref=db.backref('orders', lazy=True))

    def __repr__(self):
        return f"<Order {self.id}, User: {self.user_id}, Drug: {self.drug_id}, Status: {self.status}>"

class Teleconsultation(db.Model):
    """Teleconsultation model representing appointments with health workers."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    health_worker_id = db.Column(db.Integer, nullable=False)  # Placeholder for health worker relationship
    time_slot = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='teleconsultations')

    def __repr__(self):
        return f"<Teleconsultation {self.id}, User: {self.user_id}, Time Slot: {self.time_slot}>"

class ChatHistory(db.Model):
    """Chat history model for interactions with the healthcare chatbot."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Nullable for anonymous chats
    message = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('chat_histories', lazy=True))

    def __repr__(self):
        return f"<ChatHistory {self.id}, User: {self.user_id}>"


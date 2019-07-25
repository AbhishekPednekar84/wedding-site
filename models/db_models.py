from app import db
from datetime import datetime


class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    posted_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Testimonial({self.id}, {self.name}, {self.message})"

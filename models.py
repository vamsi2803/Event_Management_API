from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    date=db.Column(db.Text, nullable=False)
    time=db.Column(db.Text, nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "location": self.location,
            "date": self.date,
            "time": self.time,
        }
    
    def __repr__(self):
        return f'<Event {self.name}>'
    

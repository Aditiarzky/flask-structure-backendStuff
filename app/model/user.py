from app import db
from datetime import datetime
import uuid

class User(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), index=True, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, name, email):
        self.id = str(uuid.uuid4())[:10]
        self.name = name
        self.email = email
        
    def __repr__(self):
        return "<User {}>".format(self.name)
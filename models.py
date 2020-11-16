from flaskified import db
from datetime import datetime


class students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentname = db.Column(db.String(),nullable=True)
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Task %r>' % self.id
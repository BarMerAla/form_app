from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Transaction(db.Model):
    __tablename__= 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    dateTime = db.Column(db.DateTime, default=datetime.now())
    author = db.Column(db.String(128), nullable=False)
    sum = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(32), nullable=False)
    comment = db.Column(db.String(128), nullable=False)
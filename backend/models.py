from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    read = db.Column(db.Boolean, default=False)
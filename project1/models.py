from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.String(50),primary_key=True)
    username = db.Column(db.String(40),unique=True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(66))
    created_date = db.Column(db.DateTime,default = datetime.datetime.now)
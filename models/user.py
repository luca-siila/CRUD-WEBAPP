from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'user_table'

    id = db.Column('USER_ID', db.Integer, primary_key=True)
    password_hash = db.Column('USER_PASSWORD', db.String(128))  
    level = db.Column('USER_LEVEL', db.Integer)
    username = db.Column('USER_NAME', db.String(64), index=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

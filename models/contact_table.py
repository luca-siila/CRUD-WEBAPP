from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import db

class ContactTable(db.Model):
    __tablename__ = 'contact_table'
    
    CONTACT_ID = Column(Integer, primary_key=True)
    CONTACT_NAME = Column(String(150))
    CONTACT_EMAIL = Column(String(150))
    CONTACT_PHONE = Column(String(150))

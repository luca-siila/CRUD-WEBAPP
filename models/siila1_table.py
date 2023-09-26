from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import db

class Siila1Table(db.Model):
    __tablename__ = 'siila1_table'
    
    SIILA1_ID_INT = db.Column(db.Integer, primary_key=True)
    SIILA1_ID = db.Column(db.Integer, nullable=False)
    PROPERTY_TYPE = db.Column(db.String(250))
    SIILA1_NAME = db.Column(db.String(200))
    REGION_ID = db.Column(db.Integer)
    CLASS = db.Column(db.String(150), nullable=False)

    ids_table = relationship("IdsTable", back_populates="siila1_table")
    ids_table_int = relationship("IdsTableInt", back_populates="siila1_table")
    prices_table = relationship("PricesTable", back_populates="siila1_table")  # Add this relationship

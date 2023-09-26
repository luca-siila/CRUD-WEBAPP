from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import db


class MarketTable(db.Model):
    __tablename__ = 'market_table'
    
    MARKET_ID = db.Column('MARKET_ID', db.Integer, primary_key=True)
    MARKET_NAME = db.Column('MARKET_NAME', db.String(17))
    FIRST_PERIOD = db.Column('FIRST_PERIOD', db.Integer)

    region_table = db.relationship("RegionTable", back_populates="market_table")
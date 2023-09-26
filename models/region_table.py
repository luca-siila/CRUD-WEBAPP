from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import db

class RegionTable(db.Model):
    __tablename__ = 'region_table'
    
    REGION_ID = db.Column('REGION_ID', db.Integer, primary_key=True)
    REGION_NAME = db.Column('REGION_NAME', db.String(38))
    MARKET_ID = db.Column('MARKET_ID', db.Integer, db.ForeignKey('market_table.MARKET_ID'))

    market_table = db.relationship("MarketTable", back_populates="region_table")

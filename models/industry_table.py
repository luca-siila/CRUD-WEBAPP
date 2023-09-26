from . import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class IndustryTable(db.Model):
    __tablename__ = 'industry_table'
    
    INDUSTRY_ID = Column('INDUSTRY_ID', Integer, primary_key=True)
    INDUSTRY_NAME = Column('INDUSTRY_NAME', String(150))

    cadastre_table = relationship("CadastreTable", back_populates="industry_table")

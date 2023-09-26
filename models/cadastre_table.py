from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import db
from .industry_table import IndustryTable

class CadastreTable(db.Model):
    __tablename__ = 'cadastre_table'
    
    CADASTRE_ID = Column(Integer, primary_key=True)
    CADASTRE_NAME = Column(String(255))
    CAD_GROUP = Column(String(255))
    INDUSTRY_ID = Column(Integer, ForeignKey(IndustryTable.INDUSTRY_ID))

    industry_table = relationship("IndustryTable", back_populates="cadastre_table")

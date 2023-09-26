from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import db

class PeriodTable(db.Model):
    __tablename__ = 'period_table'
    
    PERIOD_ID = Column(Integer, primary_key=True)
    PERIOD = Column(Integer, nullable=False)
    
    ids_table = relationship("IdsTable", back_populates="period_table")
    ids_table_int = relationship("IdsTableInt", back_populates="period_table")


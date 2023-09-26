from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy import Numeric
from sqlalchemy.orm import relationship
from . import db

class Siila3Table(db.Model):
    __tablename__ = 'siila3_table'
    
    SIILA3_ID_INT = Column(Integer, primary_key=True)
    SIILA3_ID = Column(String(150), nullable=False)
    SIILA3_NAME = Column(String(150))
    STATUS = Column(String(150), nullable=False)
    DELIVERY_DATE = Column(Date, nullable=False)
    AREA_BOMA = Column(Float, nullable=False)
    AREA = Column(Numeric(10, 2), nullable=False) # Use Numeric for decimal type
    REGISTRY = Column(String(150))
    MODULE_EFFICIENCY = Column(Numeric(10, 2), nullable=False) # Use Numeric for decimal type
    DOCKS_MODULE = Column(Integer, nullable=False)
    SIILA2_ID_INT = Column(Integer)
    SIILA1_ID_INT = Column(Integer)
    
    ids_table = relationship("IdsTable", back_populates="siila3_table")
    ids_table_int = relationship("IdsTableInt", back_populates="siila3_table")
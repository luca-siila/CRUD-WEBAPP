from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import db


class Siila2Table(db.Model):
    __tablename__ = 'siila2_table'
    
    SIILA2_ID_INT = Column(Integer, primary_key=True)
    SIILA2_ID = Column(String(250), nullable=False)
    SIILA2_NAME = Column(String(21))
    SIILA1_ID_INT = Column(Integer)

    ids_table = relationship("IdsTable", back_populates="siila2_table")
    ids_table_int = relationship("IdsTableInt", back_populates="siila2_table")
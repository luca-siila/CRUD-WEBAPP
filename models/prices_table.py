from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy import Numeric
from sqlalchemy.orm import relationship
from . import db

class PricesTable(db.Model):
    __tablename__ = 'prices_table'

    ID_PRICE_INT = Column(Integer, primary_key=True)
    ID_PRICE = Column(String(250), nullable=False)
    SIILA1_ID = Column(Integer, ForeignKey('siila1_table.SIILA1_ID'), nullable=False)
    PERIOD = Column(Integer, nullable=False)
    PRICE = Column(Numeric(10, 2), nullable=False)
    PRICE_BOMA = Column(Numeric(10, 2), nullable=False)
    PRICE_TEXT = Column(String(250), nullable=False)
    COND = Column(Numeric(10, 2), nullable=False)
    COND_BOMA = Column(Numeric(10, 2), nullable=False)
    COND_TEXT = Column(String(250), nullable=False)
    TAX = Column(Numeric(10, 2), nullable=False)
    TAX_BOMA = Column(Numeric(10, 2), nullable=False)
    TAX_TEXT = Column(String(250), nullable=False)

    siila1_table = relationship("Siila1Table", back_populates="prices_table")
    ids_table = relationship("IdsTable", back_populates="prices_table")
    ids_table_int = relationship("IdsTableInt", back_populates="prices_table")
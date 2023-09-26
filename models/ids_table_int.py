from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import db


class IdsTableInt(db.Model):
    __tablename__ = 'ids_table_int'
    
    ID_UNIQUE_INT = Column(Integer, ForeignKey('history_table.ID_UNIQUE_INT'), primary_key=True)
    PERIOD_ID = Column(Integer, ForeignKey('period_table.PERIOD_ID'))
    ID_PRICE_INT = Column(Integer, ForeignKey('prices_table.ID_PRICE_INT'))
    SIILA1_ID_INT = Column(Integer, ForeignKey('siila1_table.SIILA1_ID_INT'))
    SIILA2_ID_INT = Column(Integer, ForeignKey('siila2_table.SIILA2_ID_INT'))
    SIILA3_ID_INT = Column(Integer, ForeignKey('siila3_table.SIILA3_ID_INT'))

    history_table = relationship("HistoryTable", back_populates="ids_table_int", uselist=False)  # One-to-one relationship
    period_table = relationship("PeriodTable", back_populates="ids_table_int")
    prices_table = relationship("PricesTable", back_populates="ids_table_int")
    siila1_table = relationship("Siila1Table", back_populates="ids_table_int")
    siila2_table = relationship("Siila2Table", back_populates="ids_table_int")
    siila3_table = relationship("Siila3Table", back_populates="ids_table_int")

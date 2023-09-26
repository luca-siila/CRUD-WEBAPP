from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import db

class IdsTable(db.Model):
    __tablename__ = 'ids_table'
    
    ID_UNIQUE = Column(Integer, ForeignKey('history_table.ID_UNIQUE'), primary_key=True)
    PERIOD = Column(Integer, ForeignKey('period_table.PERIOD'))
    ID_PRICE = Column(Integer, ForeignKey('prices_table.ID_PRICE'))
    SIILA1_ID = Column(Integer, ForeignKey('siila1_table.SIILA1_ID'))
    SIILA2_ID = Column(Integer, ForeignKey('siila2_table.SIILA2_ID'))
    SIILA3_ID = Column(Integer, ForeignKey('siila3_table.SIILA3_ID'))

    history_table = relationship("HistoryTable", back_populates="ids_table", uselist=False)  # One-to-one relationship
    period_table = relationship("PeriodTable", back_populates="ids_table")
    prices_table = relationship("PricesTable", back_populates="ids_table")
    siila1_table = relationship("Siila1Table", back_populates="ids_table")
    siila2_table = relationship("Siila2Table", back_populates="ids_table")
    siila3_table = relationship("Siila3Table", back_populates="ids_table")

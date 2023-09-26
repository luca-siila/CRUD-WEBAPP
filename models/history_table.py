from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import db

class HistoryTable(db.Model):
    __tablename__ = 'history_table'

    ID_UNIQUE_INT = Column(Integer, primary_key=True, autoincrement=True)
    ID_UNIQUE = Column(String(250), primary_key=True)
    ID_TENANT = Column(Integer, ForeignKey('cadastre_table.CADASTRE_ID'), nullable=False)
    ID_CONT_TENANT = Column(Integer, ForeignKey('contact_table.CONTACT_ID'), nullable=False)
    ID_CONT_OWNER = Column(Integer, ForeignKey('contact_table.CONTACT_ID'), nullable=False)
    ID_OWNER = Column(Integer, ForeignKey('cadastre_table.CADASTRE_ID'), nullable=False)
    SIILA3_ID = Column(String(255))
    SIILA2_ID = Column(String(255))
    SIILA1_ID = Column(String(255))
    PERIOD = Column(String(255))
    MARKET_NAME = Column(String(255))
    PROPERTY_TYPE = Column(String(255))
    STATUS = Column(String(255))
    DELIVERY_DATE = Column(Date)
    DELIVERY_PERIOD = Column(Integer)

    owner = relationship("CadastreTable", foreign_keys=[ID_OWNER])
    tenant = relationship("CadastreTable", foreign_keys=[ID_TENANT])
    contact_owner = relationship("ContactTable", foreign_keys=[ID_CONT_OWNER])
    contact_tenant = relationship("ContactTable", foreign_keys=[ID_CONT_TENANT])
    ids_table = relationship("IdsTable", back_populates="history_table", uselist=False, foreign_keys="IdsTable.ID_UNIQUE")  # One-to-one relationship
    ids_table_int = relationship("IdsTableInt", back_populates="history_table", uselist=False, foreign_keys="IdsTableInt.ID_UNIQUE_INT")  # One-to-one relationship

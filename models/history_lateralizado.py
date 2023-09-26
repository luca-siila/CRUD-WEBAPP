from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy import Numeric
from sqlalchemy.orm import relationship
from . import db

class HistoryLateralizado(db.Model):
    __tablename__ = 'history_lateralizado'

    SIILA3_ID = Column(String(250), primary_key=True)
    SIILA1_ID = Column(Integer)
    SIILA1_NAME = Column(String(255))
    MARKET_NAME = Column(String(255))
    REGION_NAME = Column(String(255))
    SIILA2_NAME = Column(String(255))  # Added
    SIILA3_NAME = Column(String(255))  # Added
    DELIVERY_DATE = Column(Date)
    AREA = Column(Numeric(10, 2))
    PROPERTY_TYPE = Column(String(255))
    _201504 = Column('201504', String(255))
    _201601 = Column('201601', String(255))
    _201602 = Column('201602', String(255))
    _201603 = Column('201603', String(255)) # Added assuming the pattern
    _201604 = Column('201604', String(255))
    _201701 = Column('201701', String(255))
    _201702 = Column('201702', String(255))
    _201703 = Column('201703', String(255))
    _201704 = Column('201704', String(255))
    _201801 = Column('201801', String(255))
    _201802 = Column('201802', String(255))
    _201803 = Column('201803', String(255))
    _201804 = Column('201804', String(255))
    _201901 = Column('201901', String(255))
    _201902 = Column('201902', String(255))
    _201903 = Column('201903', String(255))
    _201904 = Column('201904', String(255))
    _202001 = Column('202001', String(255))
    _202002 = Column('202002', String(255))
    _202003 = Column('202003', String(255))
    _202004 = Column('202004', String(255))
    _202101 = Column('202101', String(255))
    _202102 = Column('202102', String(255))
    _202103 = Column('202103', String(255))
    _202104 = Column('202104', String(255))
    _202201 = Column('202201', String(255))
    _202202 = Column('202202', String(255))
    _202203 = Column('202203', String(255))
    _202204 = Column('202204', String(255))
    _202301 = Column('202301', String(255))
    _202302 = Column('202302', String(255))
    _202303 = Column('202303', String(255))
    _202303_INDUSTRY_NAME = Column('202303_INDUSTRY_NAME', String(255))
    _202303_CONTACT_NAME = Column('202303_CONTACT_NAME', String(255))
    _202303_CONTACT_PHONE = Column('202303_CONTACT_PHONE', String(255))
    _202303_CONTACT_EMAIL = Column('202303_CONTACT_EMAIL', String(255))
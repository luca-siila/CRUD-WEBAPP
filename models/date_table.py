from sqlalchemy import Column, Integer, String, ForeignKey, Date

from sqlalchemy.orm import relationship
from . import db

class DateTable(db.Model):
    __tablename__ = 'date_table'
    
    DATE = Column(Date, primary_key=True)
    DATE_MONTH_STRING = Column(String(15))
    DATE_YEAR_STRING = Column(String(15))
    DATE_MONTH_INTEGER = Column(Integer)
    DATE_YEAR_INTEGER = Column(Integer)
    DATE_QUARTER = Column(Integer)
    PERIOD = Column(String(10))

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import db

class LogsTable(db.Model):
    __tablename__ = 'logs_table'
    
    logs_id = db.Column('LOGS_ID', db.Integer, primary_key=True)
    table_name = db.Column('TABLE_NAME', db.String(150))
    variable_name = db.Column('VARIABLE_NAME', db.String(150))
    table_id = db.Column('TABLE_ID', db.String(150))
    old_value = db.Column('OLD_VALUE', db.String(150))
    new_value = db.Column('NEW_VALUE', db.String(150))
    user = db.Column('USER', db.String(150))
    date_update = db.Column('DATE_UPDATE', db.DateTime)  # Change to DateTime
    update_type = db.Column('UPDATE_TYPE', db.String(150))

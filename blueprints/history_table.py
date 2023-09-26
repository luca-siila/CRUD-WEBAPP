from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from models import (db, HistoryTable, Siila1Table, Siila2Table, Siila3Table, 
                    RegionTable, MarketTable, CadastreTable, ContactTable, IndustryTable)
from utils import get_menu_context
from datetime import datetime
from models.logs_table import LogsTable
from sqlalchemy import cast, String, join

history_bp = Blueprint('history_table', __name__)

@history_bp.route('/history_table')
@login_required
def history_table():
    current_table, tables = get_menu_context('History Table')
    market_names = [row.MARKET_NAME for row in db.session.query(MarketTable.MARKET_NAME).distinct()]
    return render_template('group1/history_table.html', tables=tables, current_table=current_table, market_names=market_names)

@history_bp.route('/get_history_data')
@login_required
def get_history_data():
    property_type = request.args.get('propertyType')
    market_name = request.args.get('marketName')

    # Join necessary tables to retrieve all fields
    history_data = db.session.query(
    HistoryTable.SIILA1_ID,
    HistoryTable.ID_UNIQUE,
    Siila1Table.SIILA1_NAME,
    Siila2Table.SIILA2_NAME,
    Siila3Table.SIILA3_NAME,
    RegionTable.REGION_NAME,
    HistoryTable.PERIOD,
    CadastreTable.CADASTRE_NAME.label("OWNER_NAME"),
    CadastreTable.CAD_GROUP.label("OWNER_GROUP"),
    ContactTable.CONTACT_NAME.label("CONTACT_NAME"),
    ContactTable.CONTACT_PHONE.label("CONTACT_PHONE"),
    ContactTable.CONTACT_EMAIL.label("CONTACT_EMAIL")
    ).join(
        Siila1Table, HistoryTable.SIILA1_ID == Siila1Table.SIILA1_ID
    ).join(
        RegionTable, Siila1Table.REGION_ID == RegionTable.REGION_ID
    ).join(
        MarketTable, RegionTable.MARKET_ID == MarketTable.MARKET_ID
    ).join(
        Siila2Table, HistoryTable.SIILA2_ID == Siila2Table.SIILA2_ID
    ).join(
        Siila3Table, HistoryTable.SIILA3_ID == Siila3Table.SIILA3_ID
    ).join(
        CadastreTable, HistoryTable.ID_OWNER == CadastreTable.CADASTRE_ID
    ).join(
        ContactTable, HistoryTable.ID_CONT_OWNER == ContactTable.CONTACT_ID
    ).filter(
        Siila1Table.PROPERTY_TYPE == property_type,
        MarketTable.MARKET_NAME == market_name
    ).all()

    # Convert the data to a list of dictionaries to be sent as JSON
    history_data = [{
        'SIILA1_ID': row.SIILA1_ID,
        'ID_UNIQUE': row.ID_UNIQUE,
        'SIILA1_NAME': row.SIILA1_NAME,
        'SIILA2_NAME': row.SIILA2_NAME,
        'SIILA3_NAME': row.SIILA3_NAME,
        'REGION_NAME': row.REGION_NAME,
        'PERIOD': row.PERIOD,
        'OWNER_NAME': row.OWNER_NAME,
        'OWNER_GROUP': row.OWNER_GROUP,
        'CONTACT_NAME': row.CONTACT_NAME,
        'CONTACT_PHONE': row.CONTACT_PHONE,
        'CONTACT_EMAIL': row.CONTACT_EMAIL
    } for row in history_data]

    return jsonify(history_data)

@history_bp.route('/update_history_table', methods=['POST'])
@login_required
def update_history_table():
    try:
        # Extract data from form
        table_id = request.form.get('table_id')
        column_name = request.form.get('column_name')
        new_value = request.form.get('new_value')
        user = current_user.username

        # Get the old value before updating
        old_value = db.session.query(HistoryTable).filter(HistoryTable.HISTORY_ID == table_id).first().__getattribute__(column_name)

        # Perform the update operation
        db.session.query(HistoryTable).filter(HistoryTable.HISTORY_ID == table_id).update({column_name: new_value})

        # Log the update operation
        log = LogsTable(
            table_name='History Table', 
            variable_name=column_name, 
            table_id=table_id, 
            old_value=old_value, 
            new_value=new_value, 
            user=user, 
            date_update=datetime.now(), 
            update_type="Update"
        )
        db.session.add(log)

        # Commit the changes
        db.session.commit()

        return jsonify(success=True)
    except Exception as e:
        # Log the exception for debugging
        print(str(e))
        return jsonify(success=False, message="An unexpected error occurred.")

@history_bp.route('/get_data_from_table')
@login_required
def get_data_from_table():
    table_type = request.args.get('table')
    
    if table_type == "cadastre_table":
        # Join the CadastreTable with IndustryTable
        data = db.session.query(CadastreTable, IndustryTable).join(
            IndustryTable, CadastreTable.INDUSTRY_ID == IndustryTable.INDUSTRY_ID
        ).all()

        # Return the CADASTRE_NAME, CADASTRE_ID, INDUSTRY_NAME and CAD_GROUP
        return jsonify([
            {
                "CADASTRE_ID": row.CadastreTable.CADASTRE_ID,  # added CADASTRE_ID
                "CADASTRE_NAME": row.CadastreTable.CADASTRE_NAME,
                "CAD_GROUP": row.CadastreTable.CAD_GROUP,
                "INDUSTRY_NAME": row.IndustryTable.INDUSTRY_NAME
            }
            for row in data
        ])
    elif table_type == "contact_table":
        data = db.session.query(ContactTable).all()
        return jsonify([
            {
                "CONTACT_ID": row.CONTACT_ID,  # added CONTACT_ID
                "CONTACT_NAME": row.CONTACT_NAME,
                "CONTACT_EMAIL": row.CONTACT_EMAIL,
                "CONTACT_PHONE": row.CONTACT_PHONE
            }
            for row in data
        ])
    else:
        return jsonify([])

@history_bp.route('/update_original_table', methods=['POST'])
@login_required
def update_original_table():
    try:
        table_type = request.form.get('tableType')
        selected_id = request.form.get('selectedId')
        history_id = request.form.get('ID_UNIQUE')  # Fetch ID_UNIQUE from the request
        
        # Determine the column to update based on the table type
        column_to_update = "ID_OWNER" if table_type == "cadastre_table" else "ID_CONT_OWNER"
        
        # Fetch the old value before updating
        old_value = db.session.query(HistoryTable).filter(HistoryTable.ID_UNIQUE == history_id).first().__getattribute__(column_to_update)
        
        # Update the original table's data using the selected row's ID
        db.session.query(HistoryTable).filter(HistoryTable.ID_UNIQUE == history_id).update({column_to_update: selected_id})
        
        # Determine the name of the table being updated for logging purposes
        if table_type == "cadastre_table":
            table_name = "Cadastre Table"
        else:
            table_name = "Contact Table"

        # Log the update operation
        user = current_user.username
        log = LogsTable(
            table_name=table_name,
            variable_name=column_to_update,
            table_id=history_id,
            old_value=str(old_value),
            new_value=str(selected_id),
            user=user,
            date_update=datetime.now(),
            update_type="Update"
        )
        db.session.add(log)
        
        # Commit the changes
        db.session.commit()
        
        return jsonify(success=True)
    except Exception as e:
        print(str(e))
        return jsonify(success=False, message="An unexpected error occurred.")

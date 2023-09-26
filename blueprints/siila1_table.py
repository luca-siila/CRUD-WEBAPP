# blueprints/siila1_table.py
from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from models import db, Siila1Table, LogsTable  # Include LogsTable if it's being used for logging
from utils import get_menu_context
from models.region_table import RegionTable
from models.market_table import MarketTable
from datetime import datetime  # If you're using datetime

siila1_bp = Blueprint('siila1_table', __name__)

@siila1_bp.route('/siila1_table')  
@login_required
def siila1_table():
    current_table, tables = get_menu_context('Siila1 Table')
    return render_template('group1/siila1_table.html', tables=tables, current_table=current_table)

@siila1_bp.route('/get_siila1_data')
@login_required
def get_siila1_data():
    # Join Siila1Table, RegionTable and MarketTable to retrieve all necessary fields
    siila1_data = db.session.query(
        Siila1Table, 
        RegionTable.REGION_NAME, 
        MarketTable.MARKET_NAME
    ).join(
        RegionTable, Siila1Table.REGION_ID == RegionTable.REGION_ID
    ).join(
        MarketTable, RegionTable.MARKET_ID == MarketTable.MARKET_ID
    ).all()
    # Convert the data to a list of dictionaries to be sent as JSON
    siila1_data = [{
        "SIILA1_ID": row.Siila1Table.SIILA1_ID,
        "PROPERTY_TYPE": row.Siila1Table.PROPERTY_TYPE,
        "SIILA1_NAME": row.Siila1Table.SIILA1_NAME,
        "CLASS": row.Siila1Table.CLASS,
        "REGION_NAME": row.REGION_NAME,
        "MARKET_NAME": row.MARKET_NAME
    } for row in siila1_data]
    return jsonify(siila1_data)
 
@siila1_bp.route('/update_siila1_table', methods=['POST'])
@login_required
def update_siila1_table():
    # extract data from form
    table_id = request.form.get('table_id')
    column_name = request.form.get('column_name')
    new_value = request.form.get('new_value')
    user = current_user.username

    # Fetch the Siila1 row
    siila1_row = db.session.query(Siila1Table).filter(Siila1Table.SIILA1_ID == table_id).first()

    # If the column is REGION_NAME, fetch the corresponding REGION_ID and update it
    if column_name == "REGION_NAME":
        old_region_name = db.session.query(RegionTable).filter(RegionTable.REGION_ID == siila1_row.REGION_ID).first().REGION_NAME
        region = RegionTable.query.filter_by(REGION_NAME=new_value).first()
        if region:
            siila1_row.REGION_ID = region.REGION_ID
        else:
            return jsonify(success=False, message="Invalid region name.")
    else:
        old_value = siila1_row.__getattribute__(column_name)
        setattr(siila1_row, column_name, new_value)

    # log the update operation using REGION_NAME
    log = LogsTable(table_name='Siila1 Table', variable_name="REGION_NAME", table_id=table_id, old_value=old_region_name, new_value=new_value, user=user, date_update=datetime.now(), update_type="Update")
    db.session.add(log)

    # commit the changes
    db.session.commit()

    return jsonify(success=True)


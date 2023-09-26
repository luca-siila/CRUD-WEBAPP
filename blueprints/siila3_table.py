from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from models import db, Siila3Table, Siila1Table, Siila2Table
from utils import get_menu_context
from datetime import datetime
from models.logs_table import LogsTable
from sqlalchemy import cast, String

siila3_bp = Blueprint('siila3_table', __name__)

@siila3_bp.route('/siila3_table')
@login_required
def siila3_table():
    current_table, tables = get_menu_context('Siila3 Table')
    return render_template('group1/siila3_table.html', tables=tables, current_table=current_table)

@siila3_bp.route('/get_siila3_data')
@login_required
def get_siila3_data():
    # Join Siila3Table, Siila1Table, and Siila2Table to retrieve all necessary fields
    siila3_data = db.session.query(
        Siila3Table,
        Siila1Table.SIILA1_NAME,
        Siila2Table.SIILA2_NAME,
        cast(Siila3Table.DELIVERY_DATE, String).label('formatted_date')  # Using CAST to get date as string
    ).join(
        Siila1Table, Siila3Table.SIILA1_ID_INT == Siila1Table.SIILA1_ID_INT
    ).join(
        Siila2Table, Siila3Table.SIILA2_ID_INT == Siila2Table.SIILA2_ID_INT
    ).all()

    # Convert the data to a list of dictionaries to be sent as JSON
    siila3_data = [{
        "SIILA3_ID": row.Siila3Table.SIILA3_ID,
        "SIILA1_NAME": row.SIILA1_NAME,
        "SIILA2_NAME": row.SIILA2_NAME,
        "SIILA3_NAME": row.Siila3Table.SIILA3_NAME,
        "STATUS": row.Siila3Table.STATUS,
        "DELIVERY_DATE": row.formatted_date if row.formatted_date else None,  # Using the formatted date
        "AREA_BOMA": row.Siila3Table.AREA_BOMA,
        "AREA": row.Siila3Table.AREA,
        "REGISTRY": row.Siila3Table.REGISTRY,
        "MODULE_EFFICIENCY": row.Siila3Table.MODULE_EFFICIENCY,
        "DOCKS_MODULE": row.Siila3Table.DOCKS_MODULE
    } for row in siila3_data]
    return jsonify(siila3_data)



@siila3_bp.route('/update_siila3_table', methods=['POST'])
@login_required
def update_siila3_table():
    try:
        # extract data from form
        table_id = request.form.get('table_id')
        column_name = request.form.get('column_name')
        new_value = request.form.get('new_value')
        user = current_user.username

        # Get the old value before updating
        old_value = db.session.query(Siila3Table).filter(Siila3Table.SIILA3_ID == table_id).first().__getattribute__(column_name)

        # perform the update operation
        db.session.query(Siila3Table).filter(Siila3Table.SIILA3_ID == table_id).update({column_name: new_value})

        # log the update operation
        log = LogsTable(table_name='Siila3 Table', variable_name=column_name, table_id=table_id, old_value=old_value, new_value=new_value, user=user, date_update=datetime.now(), update_type="Update")
        db.session.add(log)

        # commit the changes
        db.session.commit()

        return jsonify(success=True)
    except Exception as e:
        # Log the exception for debugging
        print(str(e))
        return jsonify(success=False, message="An unexpected error occurred.")

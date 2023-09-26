from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from models import db, Siila2Table, Siila1Table
from utils import get_menu_context
from datetime import datetime
from models.logs_table import LogsTable

siila2_bp = Blueprint('siila2_table', __name__)

@siila2_bp.route('/siila2_table')
@login_required
def siila2_table():
    current_table, tables = get_menu_context('Siila2 Table')
    return render_template('group1/siila2_table.html', tables=tables, current_table=current_table)

@siila2_bp.route('/get_siila2_data')
@login_required
def get_siila2_data():
    # Join Siila2Table and Siila1Table to retrieve all necessary fields
    siila2_data = db.session.query(
        Siila2Table.SIILA2_ID,
        Siila1Table.SIILA1_NAME,
        Siila2Table.SIILA2_NAME
    ).join(
        Siila1Table, Siila2Table.SIILA1_ID_INT == Siila1Table.SIILA1_ID_INT
    ).all()
    # Convert the data to a list of dictionaries to be sent as JSON
    siila2_data = [{
        "SIILA2_ID": row.SIILA2_ID,
        "SIILA1_NAME": row.SIILA1_NAME,
        "SIILA2_NAME": row.SIILA2_NAME
    } for row in siila2_data]
    return jsonify(siila2_data)

@siila2_bp.route('/update_siila2_table', methods=['POST'])
@login_required
def update_siila2_table():
    try:
        # extract data from form
        table_id = request.form.get('table_id')
        column_name = request.form.get('column_name')
        new_value = request.form.get('new_value')
        user = current_user.username

        # Get the old value before updating
        old_value = db.session.query(Siila2Table).filter(Siila2Table.SIILA2_ID == table_id).first().__getattribute__(column_name)

        # perform the update operation
        db.session.query(Siila2Table).filter(Siila2Table.SIILA2_ID == table_id).update({column_name: new_value})

        # log the update operation
        log = LogsTable(table_name='Siila2 Table', variable_name=column_name, table_id=table_id, old_value=old_value, new_value=new_value, user=user, date_update=datetime.now(), update_type="Update")
        db.session.add(log)

        # commit the changes
        db.session.commit()

        return jsonify(success=True)
    except Exception as e:
        # Log the exception for debugging
        print(str(e))
        return jsonify(success=False, message="An unexpected error occurred.")


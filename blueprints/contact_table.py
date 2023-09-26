from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user # Added current_user here
from models import db, ContactTable, LogsTable
from datetime import datetime

from datetime import datetime

contact_bp = Blueprint('contact_table', __name__, template_folder='../templates/group0')

@contact_bp.route('/contact_table')
@login_required
def contact_table():
    current_table, tables = get_menu_context('Cadastre Table')
    return render_template('group1/contact_table.html', tables=tables, current_table=current_table)

@contact_bp.route('/get_contact_data')
@login_required
def get_contact_data():
    contacts = ContactTable.query.all()
    data = [{'CONTACT_ID': c.CONTACT_ID, 'CONTACT_NAME': c.CONTACT_NAME, 'CONTACT_EMAIL': c.CONTACT_EMAIL, 'CONTACT_PHONE': c.CONTACT_PHONE} for c in contacts]
    return jsonify(data)

@contact_bp.route('/update_contact_table', methods=['POST'])
@login_required
def update_contact_table():
    # extract data from form
    table_id = request.form.get('table_id')  # the ID of the row to be updated
    column_name = request.form.get('column_name')  # the name of the column to be updated
    new_value = request.form.get('new_value')  # the new value for the column
    user = current_user.username  # get current user's username

    # Get the old value before updating
    old_value = db.session.query(ContactTable).filter(ContactTable.CONTACT_ID == table_id).first().__getattribute__(column_name)

    # Perform the update operation
    db.session.query(ContactTable).filter(ContactTable.CONTACT_ID == table_id).update({column_name: new_value})

    # Log the update operation
    log = LogsTable(table_name='Contact Table', variable_name=column_name, table_id=table_id, old_value=old_value, new_value=new_value, user=user, date_update=datetime.now(), update_type="Update")
    db.session.add(log)

    # Commit the changes
    db.session.commit()

    return jsonify(success=True)

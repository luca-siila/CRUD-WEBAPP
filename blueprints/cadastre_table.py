from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from datetime import datetime
from models import db, LogsTable
from models.cadastre_table import CadastreTable
from models.industry_table import IndustryTable
from utils import get_menu_context

cadastre_bp = Blueprint('cadastre_table', __name__)

@cadastre_bp.route('/cadastre_table')
@login_required
def cadastre_table():
    current_table, tables = get_menu_context('Cadastre Table')
    return render_template('group1/cadastre_table.html', tables=tables, current_table=current_table)

@cadastre_bp.route('/get_cadastre_data')
@login_required
def get_cadastre_data():
    cadastre_data = db.session.query(
        CadastreTable,
        IndustryTable.INDUSTRY_NAME
    ).join(
        IndustryTable, CadastreTable.INDUSTRY_ID == IndustryTable.INDUSTRY_ID
    ).all()
    cadastre_data = [{
        "CADASTRE_ID": row.CadastreTable.CADASTRE_ID,
        "CADASTRE_NAME": row.CadastreTable.CADASTRE_NAME,
        "CAD_GROUP": row.CadastreTable.CAD_GROUP,
        "INDUSTRY_NAME": row.INDUSTRY_NAME
    } for row in cadastre_data]
    return jsonify(cadastre_data)

@cadastre_bp.route('/update_cadastre_table', methods=['POST'])
@login_required
def update_cadastre_table():
    # extract data from form
    table_id = request.form.get('table_id')
    column_name = request.form.get('column_name')
    new_value = request.form.get('new_value')
    user = current_user.username

    # Fetch the Cadastre row
    cadastre_row = db.session.query(CadastreTable).filter(CadastreTable.CADASTRE_ID == table_id).first()

    # If the column is INDUSTRY_NAME, fetch the corresponding INDUSTRY_ID and update it
    if column_name == "INDUSTRY_NAME":
        old_industry_name = db.session.query(IndustryTable).filter(IndustryTable.INDUSTRY_ID == cadastre_row.INDUSTRY_ID).first().INDUSTRY_NAME
        industry = IndustryTable.query.filter_by(INDUSTRY_NAME=new_value).first()
        if industry:
            cadastre_row.INDUSTRY_ID = industry.INDUSTRY_ID
        else:
            return jsonify(success=False, message="Invalid industry name.")
    else:
        old_value = cadastre_row.__getattribute__(column_name)
        setattr(cadastre_row, column_name, new_value)

    # log the update operation using INDUSTRY_NAME
    log = LogsTable(table_name='Cadastre Table', variable_name="INDUSTRY_NAME", table_id=table_id, old_value=old_industry_name, new_value=new_value, user=user, date_update=datetime.now(), update_type="Update")
    db.session.add(log)

    # commit the changes
    db.session.commit()

    return jsonify(success=True)


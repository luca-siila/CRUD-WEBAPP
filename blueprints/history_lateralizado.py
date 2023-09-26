from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from models import (db, HistoryLateralizado, Siila1Table, Siila2Table, Siila3Table, 
                    RegionTable, MarketTable, CadastreTable, ContactTable, IndustryTable, DateTable)
from utils import get_menu_context
from datetime import datetime
from models.logs_table import LogsTable
from sqlalchemy import text, or_, asc, desc

history_lateralizado_bp = Blueprint('history_lateralizado', __name__)

@history_lateralizado_bp.route('/')
@login_required
def history_lateralizado():
    current_table, tables = get_menu_context('History Lateralizado')
    return render_template('group1/history_lateralizado.html', tables=tables, current_table=current_table)

def get_datatables_order_query(model, order_column, order_dir):
    if order_column is not None:
        column = model.__table__.columns[order_column]
        if order_dir == 'desc':
            return desc(column)
        else:
            return asc(column)
    return None

def get_datatables_search_query(model, search_value):
    if search_value:
        filters = [
            model.siila3_id.like(f"%{search_value}%"),
            model.market_name.like(f"%{search_value}%"),
            model.region_name.like(f"%{search_value}%"),
            # Add other columns as needed
        ]
        return or_(*filters)
    else:
        return None

@history_lateralizado_bp.route('/get_history_lateralizado_data', methods=['GET', 'POST'])
def get_history_lateralizado_data():
    draw = request.form.get('draw')
    start = request.form.get('start')
    length = request.form.get('length')
    search_value = request.form.get('search[value]')

    # Define the query with necessary joins and columns
    history_data_query = db.session.query(
        HistoryLateralizado.SIILA3_ID,
        HistoryLateralizado.MARKET_NAME,
        HistoryLateralizado.PROPERTY_TYPE,
        HistoryLateralizado.SIILA1_ID,
        HistoryLateralizado.SIILA1_NAME,
        HistoryLateralizado.REGION_NAME,
        Siila1Table.CLASS,
        HistoryLateralizado.DELIVERY_DATE,
        Siila3Table.STATUS,
        HistoryLateralizado.SIILA2_NAME,
        HistoryLateralizado.SIILA3_NAME,
        HistoryLateralizado.AREA,
        HistoryLateralizado._201504,
        HistoryLateralizado._201601,
        HistoryLateralizado._201602,
        HistoryLateralizado._201603,
        HistoryLateralizado._201604,
        HistoryLateralizado._201701,
        HistoryLateralizado._201702,
        HistoryLateralizado._201703,
        HistoryLateralizado._201704,
        HistoryLateralizado._201801,
        HistoryLateralizado._201802,
        HistoryLateralizado._201803,
        HistoryLateralizado._201804,
        HistoryLateralizado._201901,
        HistoryLateralizado._201902,
        HistoryLateralizado._201903,
        HistoryLateralizado._201904,
        HistoryLateralizado._202001,
        HistoryLateralizado._202002,
        HistoryLateralizado._202003,
        HistoryLateralizado._202004,
        HistoryLateralizado._202101,
        HistoryLateralizado._202102,
        HistoryLateralizado._202103,
        HistoryLateralizado._202104,
        HistoryLateralizado._202201,
        HistoryLateralizado._202202,
        HistoryLateralizado._202203,
        HistoryLateralizado._202204,
        HistoryLateralizado._202301,
        HistoryLateralizado._202302,
        HistoryLateralizado._202303,
        HistoryLateralizado._202303_INDUSTRY_NAME,
        Siila3Table.REGISTRY,
        HistoryLateralizado._202303_CONTACT_NAME,
        HistoryLateralizado._202303_CONTACT_PHONE,
        HistoryLateralizado._202303_CONTACT_EMAIL
    ).join(
        Siila1Table, HistoryLateralizado.SIILA1_ID == Siila1Table.SIILA1_ID
    ).join(
        Siila3Table, HistoryLateralizado.SIILA3_ID == Siila3Table.SIILA3_ID
    ).filter(
        Siila3Table.STATUS == 'CONCLUÍDO'
    )

    # Apply ordering and pagination
    if search_value:
        # You can add custom search logic here if needed
        pass
    if start:
        history_data_query = history_data_query.offset(start)
    if length:
        history_data_query = history_data_query.limit(length)

    # Execute the query
    history_data = history_data_query.all()

# Convert the results to a list of dictionaries
    data = [{
        'SIILA3_ID': row.SIILA3_ID,
        'MARKET_NAME': row.MARKET_NAME,
        'PROPERTY_TYPE': row.PROPERTY_TYPE,
        'SIILA1_ID': row.SIILA1_ID,
        'SIILA1_NAME': row.SIILA1_NAME,
        'REGION_NAME': row.REGION_NAME,
        'CLASS': row.CLASS,
        'DELIVERY_DATE': row.DELIVERY_DATE,
        'STATUS': row.STATUS,
        'SIILA2_NAME': row.SIILA2_NAME,
        'SIILA3_NAME': row.SIILA3_NAME,
        'AREA': row.AREA,  
        '201504': row._201504,
        '201601': row._201601,
        '201602': row._201602,
        '201603': row._201603,
        '201604': row._201604,
        '201701': row._201701,
        '201702': row._201702,
        '201703': row._201703,
        '201704': row._201704,
        '201801': row._201801,
        '201802': row._201802,
        '201803': row._201803,
        '201804': row._201804,
        '201901': row._201901,
        '201902': row._201902,
        '201903': row._201903,
        '201904': row._201904,
        '202001': row._202001,
        '202002': row._202002,
        '202003': row._202003,
        '202004': row._202004,
        '202101': row._202101,
        '202102': row._202102,
        '202103': row._202103,
        '202104': row._202104,
        '202201': row._202201,
        '202202': row._202202,
        '202203': row._202203,
        '202204': row._202204,
        '202301': row._202301,
        '202302': row._202302,
        '202303': row._202303,
        '_202303_INDUSTRY_NAME': row._202303_INDUSTRY_NAME,
        'REGISTRY': row.REGISTRY,
        '_202303_CONTACT_NAME': row._202303_CONTACT_NAME,
        '_202303_CONTACT_PHONE': row._202303_CONTACT_PHONE,
        '_202303_CONTACT_EMAIL': row._202303_CONTACT_EMAIL
    } for row in history_data]

    # Query total records and filtered records
    records_total = HistoryLateralizado.query.count()
    records_filtered = history_data_query.count()  # Update this logic if you add search filters

    # Return the data as a JSON object
    output = {
        "draw": draw,
        "recordsTotal": records_total,
        "recordsFiltered": records_filtered,
        "data": data,
    }

    return jsonify(output)


@history_lateralizado_bp.route('/update_history_lateralizado', methods=['POST'])
@login_required
def update_history_lateralizado():
    # Extract data from form
    table_id = request.form.get('table_id')
    column_name = request.form.get('column_name')
    new_value = request.form.get('new_value')
    user = current_user.username

    # Get the old value before updating
    old_value = db.session.query(HistoryLateralizado).filter(HistoryLateralizado.SIILA3_ID == table_id).first().__getattribute__(column_name)

    # Perform the update operation
    db.session.query(HistoryLateralizado).filter(HistoryLateralizado.SIILA3_ID == table_id).update({column_name: new_value})

    # Log the update operation
    log = LogsTable(
        table_name='History Lateralizado', 
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

@history_lateralizado_bp.route('/get_data_from_table', methods=['GET'])
@login_required
def get_data_from_table():
    table_name = request.args.get('table_name')
    column_name = request.args.get('column_name')
    row_id = request.args.get('row_id')

    # Query the appropriate table and filter by ID
    if table_name == 'siila1':
        row = Siila1Table.query.get(row_id)
    elif table_name == 'siila2':
        row = Siila2Table.query.get(row_id)
    elif table_name == 'siila3':
        row = Siila3Table.query.get(row_id)
    else:
        return jsonify(success=False, message="Invalid table name")

    # Check if the row exists and the column is valid
    if row and hasattr(row, column_name):
        return jsonify(success=True, data=getattr(row, column_name))
    else:
        return jsonify(success=False, message="Invalid row ID or column name")

@history_lateralizado_bp.route('/get_cadastre_names', methods=['GET'])
@login_required
def get_cadastre_names():
    # Query all names from the CadastreTable
    names = [cadastre.CADASTRE_NAME for cadastre in CadastreTable.query.all()]
    
    # Return the names as a JSON array
    return jsonify(names)

@history_lateralizado_bp.route('/update_original_table', methods=['POST'])
@login_required
def update_original_table():
    table_name = request.form.get('table_name')
    column_name = request.form.get('column_name')
    row_id = request.form.get('row_id')
    new_value = request.form.get('new_value')
    user = current_user.username

    # Query the appropriate table and filter by ID
    if table_name == 'siila1':
        row = Siila1Table.query.get(row_id)
    elif table_name == 'siila2':
        row = Siila2Table.query.get(row_id)
    elif table_name == 'siila3':
        row = Siila3Table.query.get(row_id)
    else:
        return jsonify(success=False, message="Invalid table name")

    # Check if the row exists and the column is valid
    if row and hasattr(row, column_name):
        old_value = getattr(row, column_name)
        setattr(row, column_name, new_value)
        db.session.commit()

        # Log the update operation
        log = LogsTable(
            table_name=table_name, 
            variable_name=column_name, 
            table_id=row_id, 
            old_value=old_value, 
            new_value=new_value, 
            user=user, 
            date_update=datetime.now(), 
            update_type="Update"
        )
        db.session.add(log)
        db.session.commit()

        return jsonify(success=True)
    else:
        return jsonify(success=False, message="Invalid row ID or column name")

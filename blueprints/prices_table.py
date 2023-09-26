from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from models import db, PricesTable, Siila1Table
from utils import get_menu_context
from datetime import datetime
from models.logs_table import LogsTable
from sqlalchemy import cast, String

prices_bp = Blueprint('prices_table', __name__)

@prices_bp.route('/prices_table')
@login_required
def prices_table():
    current_table, tables = get_menu_context('Prices Table')
    return render_template('group1/prices_table.html', tables=tables, current_table=current_table)

@prices_bp.route('/get_prices_data')
@login_required
def get_prices_data():
    # Join PricesTable and Siila1Table to retrieve all necessary fields
    prices_data = db.session.query(
        PricesTable,
        Siila1Table.SIILA1_NAME
    ).join(
        Siila1Table, PricesTable.SIILA1_ID == Siila1Table.SIILA1_ID
    ).all()

    # Convert the data to a list of dictionaries to be sent as JSON
    prices_data = [{
        "ID_PRICE": row.PricesTable.ID_PRICE,  # Include ID_PRICE
        "SIILA1_NAME": row.SIILA1_NAME,
        "PERIOD": row.PricesTable.PERIOD,
        "PRICE": str(row.PricesTable.PRICE), # Convert to string to handle decimal
        "PRICE_BOMA": str(row.PricesTable.PRICE_BOMA),
        "PRICE_TEXT": row.PricesTable.PRICE_TEXT,
        "COND": str(row.PricesTable.COND),
        "COND_BOMA": str(row.PricesTable.COND_BOMA),
        "COND_TEXT": row.PricesTable.COND_TEXT,
        "TAX": str(row.PricesTable.TAX),
        "TAX_BOMA": str(row.PricesTable.TAX_BOMA),
        "TAX_TEXT": row.PricesTable.TAX_TEXT
    } for row in prices_data]
    return jsonify(prices_data)

@login_required
@prices_bp.route('/update_prices_table', methods=['POST'])
def update_prices_table():
    try:
        # Extract data from form
        table_id = request.form.get('table_id') # This should be ID_PRICE and is a string
        column_name = request.form.get('column_name')
        new_value = request.form.get('new_value')
        user = current_user.username

        # Additional validation to ensure that table_id is not None
        if table_id is None:
            return jsonify(success=False, message="ID_PRICE is missing.")

        # Convert new_value to appropriate type if needed
        if column_name in ["PRICE", "PRICE_BOMA", "COND", "COND_BOMA", "TAX", "TAX_BOMA"]:
            new_value = float(new_value)

        # Get the old value before updating
        old_record = db.session.query(PricesTable).filter(PricesTable.ID_PRICE == table_id).first()
        old_value = getattr(old_record, column_name) if old_record else None

        # Perform the update operation
        db.session.query(PricesTable).filter(PricesTable.ID_PRICE == table_id).update({column_name: new_value})

        # Log the update operation, using ID_PRICE
        log = LogsTable(table_name='Prices Table', variable_name=column_name, table_id=table_id, old_value=str(old_value), new_value=str(new_value), user=user, date_update=datetime.now(), update_type="Update")
        db.session.add(log)

        # Commit the changes
        db.session.commit()

        return jsonify(success=True)
    except Exception as e:
        print(str(e))
        return jsonify(success=False, message="An unexpected error occurred.")
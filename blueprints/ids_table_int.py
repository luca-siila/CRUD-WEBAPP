# blueprints/ids_table_int.py
from flask import Blueprint, render_template
from flask_login import login_required
from models import db, IdsTableInt

ids_int_bp = Blueprint('ids_table_int', __name__)

tables = [
    'Siila1 Table',
    'Siila2 Table',
    'Industry Table',
    'Contact Table',
    'Cadastre Table',
    'Logs Table',
    'Market Table',
    'Siila3 Table',
    'Prices Table',
    'History Table'
]

@ids_int_bp.route('/ids_table_int')  
@login_required
def ids_table_int():
    ids_int_data = IdsTableInt.query.order_by(IdsTableInt.id.desc()).all()
    return render_template('ids_table_int.html', data=ids_int_data, tables=tables, current_table='Ids Table Int')

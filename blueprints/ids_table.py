# blueprints/ids_table.py
from flask import Blueprint, render_template
from flask_login import login_required
from models import db, IdsTable

ids_bp = Blueprint('ids_table', __name__)

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

@ids_bp.route('/ids_table')  
@login_required
def ids_table():
    ids_data = IdsTable.query.order_by(IdsTable.id.desc()).all()
    return render_template('ids_table.html', data=ids_data, tables=tables, current_table='Ids Table')

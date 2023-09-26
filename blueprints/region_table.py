from flask import Blueprint, render_template
from flask_login import login_required
from models import db, RegionTable
from utils import get_menu_context

region_bp = Blueprint('region_table', __name__)

@region_bp.route('/region_table')  
@login_required
def region_table():
    current_table, tables = get_menu_context('Region Table')
    region_data = RegionTable.query.order_by(RegionTable.REGION_ID.desc()).all()
    return render_template('group0/region_table.html', data=region_data, tables=tables, current_table=current_table)

@region_bp.route('/refresh_region_table')  
@login_required
def refresh_region_table():
    current_table, tables = get_menu_context('Region Table')
    # Query the database to get the latest data
    region_data = RegionTable.query.order_by(RegionTable.REGION_ID.desc()).all()
    return render_template('group0/region_table.html', data=region_data, tables=tables, current_table=current_table)

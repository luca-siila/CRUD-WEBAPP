from flask import Blueprint, render_template
from flask_login import login_required
from models import db, IndustryTable
from utils import get_menu_context

industry_bp = Blueprint('industry_table', __name__)

@industry_bp.route('/industry_table')  
@login_required
def industry_table():
    current_table, tables = get_menu_context('Industry Table')
    industry_data = IndustryTable.query.order_by(IndustryTable.INDUSTRY_ID.desc()).all()
    return render_template('group0/industry_table.html', data=industry_data, tables=tables, current_table=current_table)

@industry_bp.route('/refresh_industry_table')  
@login_required
def refresh_industry_table():
    current_table, tables = get_menu_context('Industry Table')
    industry_data = IndustryTable.query.order_by(IndustryTable.INDUSTRY_ID.desc()).all()
    return render_template('group0/industry_table.html', data=industry_data, tables=tables, current_table=current_table)

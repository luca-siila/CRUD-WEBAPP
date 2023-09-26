from flask import Blueprint, render_template
from flask_login import login_required
from models import db, MarketTable
from utils import get_menu_context

market_bp = Blueprint('market_table', __name__)

@market_bp.route('/market_table')  
@login_required
def market_table():
    current_table, tables = get_menu_context('Market Table')
    market_data = MarketTable.query.order_by(MarketTable.MARKET_ID.desc()).all()
    return render_template('group0/market_table.html', data=market_data, tables=tables, current_table=current_table)

@market_bp.route('/refresh_market_table')  
@login_required
def refresh_market_table():
    current_table, tables = get_menu_context('Market Table')
    market_data = MarketTable.query.order_by(MarketTable.MARKET_ID.desc()).all()
    return render_template('group0/market_table.html', data=market_data, tables=tables, current_table=current_table)

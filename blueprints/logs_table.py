from flask import Blueprint, render_template, request
from flask_login import login_required
from models import db, LogsTable
from utils import get_menu_context

logs_bp = Blueprint('logs_table', __name__)


@logs_bp.route('/logs_table')  
@login_required
def logs_table():
    current_table, tables = get_menu_context('Logs Table')
    logs = LogsTable.query.order_by(LogsTable.logs_id.desc()).limit(100).all()  # retrieve last 100 logs
    return render_template('group0/logs_table.html', logs=logs, tables=tables, current_table=current_table)


@logs_bp.route('/refresh_logs_table')  
@login_required
def refresh_logs_table():
    current_table, tables = get_menu_context('Logs Table')
    # Query the database to get the latest data
    logs = LogsTable.query.order_by(LogsTable.logs_id.desc()).limit(100).all()
    return render_template('group0/logs_table.html', logs=logs, tables=tables, current_table=current_table)

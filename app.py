from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_login import LoginManager, login_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import check_password_hash
from config import Config
from models import db, User, LogsTable
from models.siila1_table import Siila1Table
from models.region_table import RegionTable
from models.market_table import MarketTable
from models.industry_table import IndustryTable
from datetime import datetime
from blueprints.contact_table import contact_bp as contact_table_bp
from blueprints.history_lateralizado import history_lateralizado_bp as history_lateralizado_bp
from blueprints.cadastre_table import cadastre_bp as cadastre_table_bp
from blueprints.siila3_table import siila3_bp as siila3_table_bp
from blueprints.region_table import region_bp as region_table_bp
from blueprints.industry_table import industry_bp as industry_table_bp
from blueprints.market_table import market_bp as market_table_bp
from blueprints.history_table import history_bp as history_table_bp
from blueprints.logs_table import logs_bp as logs_table_bp
from blueprints.siila2_table import siila2_bp as siila2_table_bp
from blueprints.siila1_table import siila1_bp as siila1_table_bp
from blueprints.prices_table import prices_bp as prices_table_bp
from utils import get_menu_context

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

app.register_blueprint(contact_table_bp)
app.register_blueprint(history_lateralizado_bp)
app.register_blueprint(cadastre_table_bp)
app.register_blueprint(siila3_table_bp)
app.register_blueprint(region_table_bp)
app.register_blueprint(industry_table_bp)
app.register_blueprint(market_table_bp)
app.register_blueprint(history_table_bp)
app.register_blueprint(siila2_table_bp)
app.register_blueprint(siila1_table_bp)
app.register_blueprint(logs_table_bp)
app.register_blueprint(prices_table_bp)

all_tables = [
    'Logs Table',
    'Siila1 Table',
    'Siila2 Table',
    'Siila3 Table',
    'Region Table',
    'Market Table',
    'Contact Table',
    'Cadastre Table',
    'Industry Table',
    'Prices Table',
    'History Table',
    'History Lateralizado'
]

def get_menu_context(current_table):
    tables = [table for table in all_tables if table != current_table]
    return current_table, tables

@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    return user if user else None

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(password):
            login_user(user)
            return jsonify(success=True)
        else:
            return jsonify(success=False)
    else:
        return render_template('login.html')


@app.route('/under_development')
@login_required
def under_development():
    current_table, tables = get_menu_context('Under Development')
    return render_template('under_development.html', tables=tables, current_table=current_table)


@app.route('/get_region_names')
@login_required
def get_region_names():
    regions = RegionTable.query.with_entities(RegionTable.REGION_NAME).all()
    region_names = [region.REGION_NAME for region in regions]
    return jsonify(region_names=region_names)

if __name__ == '__main__':
    app.run(debug=True)


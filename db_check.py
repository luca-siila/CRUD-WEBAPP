from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db

# Initialize the Flask app
app = Flask(__name__)

# Set the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db.init_app(app)

# Import all models
from models.industry_table import IndustryTable
from models.logs_table import LogsTable
from models.market_table import MarketTable
from models.period_table import PeriodTable
from models.prices_table import PricesTable
from models.region_table import RegionTable
from models.siila1_table import Siila1Table
from models.siila2_table import Siila2Table
from models.siila3_table import Siila3Table
from models.user import User
from models.cadastre_table import CadastreTable
from models.contact_table import ContactTable
from models.date_table import DateTable
from models.history_lateralizado import HistoryLateralizado
from models.history_table import HistoryTable
from models.ids_table import IdsTable
from models.ids_table_int import IdsTableInt

# Create the database
with app.app_context():
    db.create_all()

print("Database created successfully!")

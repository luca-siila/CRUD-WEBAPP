from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .logs_table import LogsTable
from .siila1_table import Siila1Table
from .region_table import RegionTable
from .market_table import MarketTable
from .industry_table import IndustryTable
from .cadastre_table import CadastreTable
from .contact_table import ContactTable
from .period_table import PeriodTable
from .ids_table import IdsTable
from .ids_table_int import IdsTableInt
from .siila2_table import Siila2Table
from .siila3_table import Siila3Table
from .history_table import HistoryTable
from .history_lateralizado import HistoryLateralizado
from .prices_table import PricesTable
from .date_table import DateTable

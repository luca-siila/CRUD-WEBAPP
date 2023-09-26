# utils.py

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

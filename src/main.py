# routes need to be touched by import once to proc the app import/setup
# from src.config.db_config import reset_database
from src.route import *
from src.route import qc_info
from src.config.flask_config import app
from dotenv import dotenv_values
from src.config.database_initialization import populate_table_entire_batch


if __name__ == "__main__":
    dotenv_values("../.env")
    app.run()
    # populate_table_entire_batch('TR-1145')
    # reset_database("src/sql/setup.sql")

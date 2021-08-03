# routes need to be touched by import once to proc the app import/setup
# from src.route import caliber, self_comparison
# from src.config.flask_config import app
from src.config.db_config import reset_database
from dotenv import dotenv_values


if __name__ == "__main__":
    dotenv_values("../.env")
    # app.run()
    reset_database("src/sql/setup.sql")

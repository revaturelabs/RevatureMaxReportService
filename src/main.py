# routes need to be touched by import once to proc the app import/setup
from route import *
from config.flask_config import app

from dotenv import dotenv_values


if __name__ == "__main__":
    dotenv_values("../.env")
    app.run()

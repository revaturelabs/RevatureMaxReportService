# routes need to be touched by import once to proc the app import/setup
from src.route import caliber
from src.route.trainer_associate_grades_view import getTraineeData
from src.config.flask_config import app

from dotenv import dotenv_values


if __name__ == "__main__":
    dotenv_values("../.env")
    app.run()

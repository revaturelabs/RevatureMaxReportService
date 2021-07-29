<<<<<<< HEAD
from src.config.flask_config import app
=======
# routes need to be touched by import once to proc the app import/setup
from route import caliber

from config.flask_config import app
from dotenv import dotenv_values

>>>>>>> 10bf5d926e78f5ba9d17be3c1cda14ef765eda8d

if __name__ == "__main__":
    dotenv_values("../.env")
    app.run()

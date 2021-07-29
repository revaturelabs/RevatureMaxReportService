
from config.flask_config import app
from dotenv import dotenv_values


if __name__ == "__main__":
    dotenv_values("../.env")
    app.run()

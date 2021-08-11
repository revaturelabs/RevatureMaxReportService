# routes need to be touched by import once to proc the app import/setup
from route import *
from config.flask_config import app
from os import environ

if __name__ == "__main__":
    with open(".env") as env:
        for line in env:
            val = line.strip().split("=")
            environ[val[0]] = val[1]
    app.run(host="0.0.0.0")

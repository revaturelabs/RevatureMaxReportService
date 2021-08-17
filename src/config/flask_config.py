from flask import Flask
from os import environ

app = Flask(__name__)
app.debug = environ.get("DEBUG", True)

from flask import make_response, request
from src.config.flask_config import app
from src.util.fetch import fetch_json

URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"

@app.route("/grades/reports/individual/<associate_email>", methods=["GET"])
def getTraineeGradesComparedToBatch(associate_email):
    # localhost:5000/grades/reports/individual/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com
    url = f"{URL_BASE}evaluation/grades/reports/individual/{associate_email}"
    return {"batch_grades": fetch_json(url)}
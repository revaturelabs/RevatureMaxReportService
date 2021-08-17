from config.flask_config import app
from util.fetch import fetch_json

URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"


@app.route("/trainer/individual/grades/<associate_email>", methods=["GET"])
def getTraineeData(associate_email):
    # localhost:5000/trainer/individual/grades/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com
    url = f"{URL_BASE}evaluation/grades/reports/individual/{associate_email}"
    return {"associateGrades": fetch_json(url)['traineeGrades']}

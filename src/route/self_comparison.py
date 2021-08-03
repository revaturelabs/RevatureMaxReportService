# from flask import make_response, request
from src.config.flask_config import app
from src.util.self_comparison import individual_vs_batch_score, score_report_by_week

URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"


@app.route("/reports/<batch_id>/<associate_email>/weekly", methods=["GET"])
def get_trainee_grades_compared_to_batch_all_weeks(batch_id, associate_email):
    # localhost:5000/reports/TR-1190/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com/weekly
    return individual_vs_batch_score(batch_id, associate_email)


@app.route("/reports/<batch_id>/spider/<associate_email>", methods=["GET"])
def spider_on_batch(batch_id, associate_email):
    # localhost:5000/reports/TR-1190/spider/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com
    return score_report_by_week(batch_id, associate_email)

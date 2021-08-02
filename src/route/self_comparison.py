# from flask import make_response, request
from src.config.loggingConfig import controller_log as logger
from src.config.flask_config import app
from src.util.fetch import fetch_json
from src.util.self_comparison import individual_vs_batch_score_formatted, score_report_by_week

URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"


@app.route("/associate/<associate_email>")
def associate_listing(associate_email):
    # localhost:5000/associate/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com
    url = f"{URL_BASE}training/associate/{associate_email}"
    batches = fetch_json(url)
    return {**batches}, 200


@app.route("/associate/<associate_email>/batch")
def associate_batch_listing(associate_email):
    # localhost:5000/associate/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com/batch
    url = f"{URL_BASE}training/associate/{associate_email}/batch"
    batches = fetch_json(url)
    return {**batches}, 200


@app.route("/grades/reports/individual/<associate_email>", methods=["GET"])
def get_trainee_grades_compared_to_batch(associate_email):
    # localhost:5000/grades/reports/individual/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com
    url = f"{URL_BASE}evaluation/grades/reports/individual/{associate_email}"
    return {**fetch_json(url)}


@app.route("/grades/reports/individual/<associate_email>/<int:week>", methods=["GET"])
def get_trainee_grades_compared_to_batch_on_week(associate_email, week):
    # localhost:5000/grades/reports/individual/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com/2
    url = f"{URL_BASE}evaluation/grades/reports/individual/{associate_email}/{week}"
    return {**fetch_json(url)}


@app.route("/reports/<batch_id>/<associate_email>/weekly", methods=["GET"])
def get_trainee_grades_compared_to_batch_all_weeks(batch_id, associate_email):
    # localhost:5000/reports/TR-1190/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com/weekly
    return individual_vs_batch_score_formatted(batch_id, associate_email)


@app.route("/reports/<batch_id>/spider/<associate_email>", methods=["GET"])
def spider_on_batch(batch_id, associate_email):
    # localhost:5000/reports/TR-1190/spider/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com
    return score_report_by_week(batch_id, associate_email)

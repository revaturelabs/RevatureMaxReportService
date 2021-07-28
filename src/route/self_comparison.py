# from flask import make_response, request
# from config.loggingConfig import controller_log as logger
from config.flask_config import app
from util.fetch import fetch_json

URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"


@app.route("/associate/<associate_email>")
def associate_listing(associate_email):
    # localhost:5000/associate/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com
    url = f"{URL_BASE}training/associate/{associate_email}"
    batches = fetch_json(url)
    return {"batches": batches}, 200


@app.route("/associate/<associate_email>/batch")
def associate_batch_listing(associate_email):
    # localhost:5000/associate/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com/batch
    url = f"{URL_BASE}training/associate/{associate_email}/batch"
    batches = fetch_json(url)
    return {"batches": batches}, 200


@app.route("/grades/reports/individual/<associate_email>", methods=["GET"])
def get_trainee_grades_compared_to_batch(associate_email):
    # localhost:5000/grades/reports/individual/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com
    url = f"{URL_BASE}evaluation/grades/reports/individual/{associate_email}"
    return {"batch_grades": fetch_json(url)}


@app.route("/grades/reports/individual/<associate_email>/<int:week>", methods=["GET"])
def get_trainee_grades_compared_to_batch_on_week(associate_email, week):
    # localhost:5000/grades/reports/individual/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com/2
    url = f"{URL_BASE}evaluation/grades/reports/individual/{associate_email}/{week}"
    return {"batch_grades": fetch_json(url)}


@app.route("/grades/reports/individual/<associate_email>/weekly", methods=["GET"])
def get_trainee_grades_compared_to_batch_all_weeks(associate_email):
    # localhost:5000/grades/reports/individual/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com/weekly
    result = {}
    # https://caliber2-mock.revaturelabs.com:443/mock/training/associate/mock1.associatee5c1c02d-531e-404c-9a86-082107ff12bc%40mock.com/batch
    # get batch id
    url = f"{URL_BASE}training/associate/{associate_email}/batch"
    batch_id = fetch_json(url).get("batchId", None)
    # https://caliber2-mock.revaturelabs.com:443/mock/qa/notes/batch/TR-1190
    # get a list of the weeks that the batch existed for
    url = f"{URL_BASE}qa/notes/batch/{batch_id}"
    notes_by_week_for_batch = fetch_json(url)
    weeks = list(map(lambda x: x.get("week", None), notes_by_week_for_batch))

    for week in weeks:
        url = f"{URL_BASE}evaluation/grades/reports/individual/{associate_email}/{week}"
        r1 = fetch_json(url)
        result[week] = r1

    return {**result}

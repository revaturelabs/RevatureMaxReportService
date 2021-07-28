from flask import make_response, request
from config.flask_config import app
from util.fetch import fetch_json

URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"


@app.route("/grades/assessment/<int:assessment_id>", methods=["GET"])
def findGradesByAssessment(assessment_id):
    url = "%s%s%d" % (URL_BASE, "evaluation/grades/assessment/", assessment_id)
    return {"assessments": fetch_json(url)}, 200


@app.route("/grades/average", methods=["GET"])
def findAverageGradeByWeek():
    assessment = request.args.get("assessment", None)
    batch = request.args.get("batch", None)
    week = request.args.get("week", None)
    url_response = None

    if assessment:
        url_response = f"?assessment={assessment}"
    elif batch and week:
        url_response = f"?batch={batch}&week={week}"
    else:
        return make_response("Malformed inputs: You must provide assessment or (batch and week)", 400)

    url = f"{URL_BASE}{'evaluation/grades/average'}{url_response}"
    return {"average": fetch_json(url)}, 200


@app.route("/grades/batch/<batch_id>", methods=["GET"])
def findGradesByBatch(batch_id):
    url = f"{URL_BASE}{'evaluation/'}{'grades/batch/'}{batch_id}"
    return {"batch_grades": fetch_json(url)}


@app.route("/grades/reports/batch/<batch_id>/<int:week>", methods=["GET"])
def getGradeComparisonForBatchOnWeek(batch_id, week):
    url = f"{URL_BASE}{'evaluation/'}{'grades/reports/batch/'}{batch_id}/{week}"
    return {"batch_grades": fetch_json(url)}


@app.route("/grades/reports/individual/<associate_email>", methods=["GET"])
def getTraineeGradesComparedToBatch(associate_email):
    url = f"{URL_BASE}{'evaluation/'}{'grades/reports/individual/'}{associate_email}"
    return {"batch_grades": fetch_json(url)}


@app.route("/grades/reports/individual/<associate_id>/<int:week>", methods=["GET"])
def getTraineeGradesComparedToBatchOnWeek(associate_id, week):
    url = f"{URL_BASE}{'evaluation/'}{'grades/reports/individual/'}{associate_id}/{week}"
    return {"batch_grades": fetch_json(url)}


@app.route("/grades/reports/<batch_id>/overall", methods=["GET"])
def getGradeReportForBatch(batch_id):
    url = f"{URL_BASE}{'evaluation/'}{'grades/reports/'}{batch_id}"
    return {"batch_grades": fetch_json(url)}


@app.route("/grades/reports/<batch_id>/overall/<int:week>", methods=["GET"])
def getWeeklyGradeReportForBatch(batch_id, week):
    url = f"{URL_BASE}{'evaluation/'}{'grades/reports/'}{batch_id}{week}"
    return {"batch_grades": fetch_json(url)}


@app.route("/grades/reports/<batch_id>/spider", methods=["GET"])
def getSpiderGraphDataForBatch(batch_id):
    url = f"{URL_BASE}{'evaluation/'}{'grades/reports/'}{batch_id}"
    return {"batch_grades": fetch_json(url)}


@app.route("/grades/reports/<batch_id>/spider/<associate_email>", methods=["GET"])
def getSpiderGraphDataForTraineeAndBatch(batch_id, associate_email):
    url = f"{URL_BASE}{'evaluation/'}{'grades/reports/'}{batch_id}/spider/{associate_email}"
    return {"batch_grades": fetch_json(url)}

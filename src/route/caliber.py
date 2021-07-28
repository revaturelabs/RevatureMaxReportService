from flask import make_response, request
from config.flask_config import app
from util.fetch import fetch_json
from config.loggingConfig import controller_log as logger


URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"

# @app.route("/report/individual/<associate_email>", methods=["GET"])
# def get_associate_information(associate_email):
#     return "wazzaaa", 200


# @app.route("/report/batch/<batch_id>", methods=["GET"])
# def get_batch_mates(batch_id):
#     return "wazzaaa", 200


# @app.route("/report/qc/<associate_email>", methods=["GET"])
# def get_all_notes(associate_email):
#     return "wazzaaa", 200


# @app.route("/report/grades/<associate_email>", methods=["GET"])
# def get_all_grades(associate_email):
#     return "wazzaaa", 200


@app.route("/grades/assessment/<int:assessment_id>", methods=["GET"])
def findGradesByAssessment(assessment_id):
    url = "%s%s%d" % (URL_BASE, "evaluation/grades/assessment/", assessment_id)
    logger.info(url)
    json = fetch_json(url)
    return {"assessments": json}, 200


@app.route("/grades/average", methods=["GET"])
def findAverageGradeByWeek():
    request.get_data()

    assessment = None
    batch = None
    week = None

    url = "%s%s" % (URL_BASE, "evaluation/grades/average")
    logger.info(url)
    json = fetch_json(url)
    return {"average": json}, 200


@app.route("/grades/batch/<int:batch_id>", methods=["GET"])
def findGradesByBatch(batch_id):
    pass


@app.route("/grades/reports/batch/<batch_id>/<int:week>", methods=["GET"])
def getGradeComparisonForBatchOnWeek(batch_id, week):
    pass


@app.route("/grades/reports/individual/<associate_email>", methods=["GET"])
def getTraineeGradesComparedToBatch(associate_email):
    pass


@app.route("/grades/reports/individual/<associate_id>/<int:week>", methods=["GET"])
def getTraineeGradesComparedToBatchOnWeek(associate_id, week):
    pass


@app.route("/grades/reports/<batch_id>/overall", methods=["GET"])
def getGradeReportForBatch(batch_id):
    pass


@app.route("/grades/reports/<batch_id>/overall/<int:week>", methods=["GET"])
def getWeeklyGradeReportForBatch(batch_id, week):
    pass


@app.route("/grades/reports/<batch_id>/spider", methods=["GET"])
def getSpiderGraphDataForBatch(batch_id):
    pass


@app.route("/grades/reports/<batch_id>/spider/<associate_email>", methods=["GET"])
def getSpiderGraphDataForTraineeAndBatch(batch_id, associate_email):
    pass

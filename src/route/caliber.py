from flask import make_response, request
from src.config.flask_config import app
from src.util.fetch import fetch_json
from src.service import qa_service

URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/grades/assessment/<int:assessment_id>", methods=["GET"])
def findGradesByAssessment(assessment_id):
    # localhost:5000/grades/assessment/2169
    url = "%s%s%d" % (URL_BASE, "evaluation/grades/assessment/", assessment_id)
    return {"assessments": fetch_json(url)}, 200


@app.route("/grades/average", methods=["GET"])
def findAverageGradeByWeek():
    # http://127.0.0.1:5000/grades/average?batch=TR-1190&week=1
    # http://127.0.0.1:5000/grades/average?assessment=2169
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

    url = f"{URL_BASE}evaluation/grades/average{url_response}"
    return {"average": fetch_json(url)}, 200


@app.route("/grades/batch/<batch_id>", methods=["GET"])
def findGradesByBatch(batch_id):
    # localhost:5000/grades/batch/TR-1190
    url = f"{URL_BASE}evaluation/grades/batch/{batch_id}"
    return {"batch_grades": fetch_json(url)}


@app.route("/grades/reports/batch/<batch_id>/<int:week>", methods=["GET"])
def getGradeComparisonForBatchOnWeek(batch_id, week):
    # localhost:5000/grades/reports/batch/TR-1190/1
    url = f"{URL_BASE}evaluation/grades/reports/batch/{batch_id}/{week}"
    return {"batch_grades": fetch_json(url)}


@app.route("/grades/reports/individual/<associate_email>", methods=["GET"])
def getTraineeGradesComparedToBatch(associate_email):
    # localhost:5000/grades/reports/individual/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com
    url = f"{URL_BASE}evaluation/grades/reports/individual/{associate_email}"
    return {"batch_grades": fetch_json(url)}


@app.route("/grades/reports/individual/<associate_email>/<int:week>", methods=["GET"])
def getTraineeGradesComparedToBatchOnWeek(associate_email, week):
    # localhost:5000/grades/reports/individual/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com/2
    url = f"{URL_BASE}evaluation/grades/reports/individual/{associate_email}/{week}"
    return {"batch_grades": fetch_json(url)}


@app.route("/grades/reports/<batch_id>/overall", methods=["GET"])
def getGradeReportForBatch(batch_id):
    # localhost:5000/grades/reports/TR-1190/overall
    url = f"{URL_BASE}evaluation/grades/reports/{batch_id}/overall"
    return {"batch_grades": fetch_json(url)}


@app.route("/grades/reports/<batch_id>/overall/<int:week>", methods=["GET"])
def getWeeklyGradeReportForBatch(batch_id, week):
    # localhost:5000/grades/reports/TR-1190/overall/1
    url = f"{URL_BASE}evaluation/grades/reports/{batch_id}/overall/{week}"
    return {"batch_grades": fetch_json(url)}


@app.route("/grades/reports/<batch_id>/spider", methods=["GET"])
def getSpiderGraphDataForBatch(batch_id):
    # localhost:5000/grades/reports/TR-1190/spider
    url = f"{URL_BASE}evaluation/grades/reports/{batch_id}/spider"
    return {"batch_grades": fetch_json(url)}


@app.route("/grades/reports/<batch_id>/spider/<associate_email>", methods=["GET"])
def getSpiderGraphDataForTraineeAndBatch(batch_id, associate_email):
    # localhost:5000/grades/reports/TR-1190/spider/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com
    url = f"{URL_BASE}evaluation/grades/reports/{batch_id}/spider/{associate_email}"
    return {"batch_grades": fetch_json(url)}


@app.route("/qa/notes/trainee/<associate_id>", methods=["GET"])
def getQANotesForTrainee(associate_id):
    # localhost:5000/qa/notes/trainee/SF-2128
    url_ind = f"{URL_BASE}qa/notes/trainee/{associate_id}"
    qa_json_ind = fetch_json(url_ind)
    batch_id = qa_service.getbatchID(qa_json_ind)
    url_batch = f"{URL_BASE}qa/notes/batch/{batch_id}"
    qa_json_batch = fetch_json(url_batch)

    return qa_service.parseTraineeJson(qa_json_ind, qa_json_batch)


@app.route("/qa/notes/batch/<batch_id>", methods=["GET"])
def getQCNotesForBatchGroup(batch_id):
    # localhost:5000/qa/notes/batch/TR-1131
    url = f"{URL_BASE}qa/notes/batch/{batch_id}"
    qa_json = fetch_json(url)
    return qa_service.parseBatchJson(qa_json)

@app.route("/qa/notes/individual/<batch_id>", methods=["GET"])
def getQCNoteForBatchIndividual(batch_id):
    # localhost:5000/qa/notes/individual/TR-1131
    url_ind = f"{URL_BASE}qa/notes/individual/{batch_id}"

    qa_json = fetch_json(url)
    return qa_service.parseBatchIndividualJson(qa_json)


# from flask import make_response, request
from config.flask_config import app
from service import category_service, assessment_service

URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"


@app.route("/associate/<batch_id>/<associate_email>/weekly", methods=["GET"])
def get_trainee_grades_compared_to_batch_all_weeks(batch_id, associate_email):
    # localhost:5000/associate/TR-1190/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com/weekly
    result = {
        "chartData": {
            **category_service.select_categorical_averages_by_email_weekly(
                associate_email
            ),
            **category_service.select_batch_averages_weekly(batch_id),
        }
    }
    return result


@app.route("/associate/<batch_id>/spider/<associate_email>", methods=["GET"])
def spider_on_batch(batch_id, associate_email):
    # localhost:5000/associate/TR-1190/spider/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com
    return {"data": assessment_service.select_batch_averages(batch_id, associate_email)}

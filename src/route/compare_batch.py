from urllib.error import HTTPError

from flask import make_response, request
from config.flask_config import app
from util.fetch import fetch_json
from datetime import datetime

URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"

@app.route("/batch/<batch_id>/compare")
def compareBatchToPastBatches(batch_id):
    # localhost:5000/batch/TR-1140/compare
    try:
        batch_url = URL_BASE + "training/batch/" + batch_id
        original_batch = fetch_json(batch_url)
        batch_skill = original_batch.get("skill")
        original_batch_id = original_batch.get("batchId")
        original_date = datetime.strptime(original_batch.get("startDate"), "%Y-%m-%d").date()
        original_grades_avg_url = URL_BASE + f"evaluation/grades/reports/{batch_id}/overall"
        avg_grades_in_batch = fetch_json(original_grades_avg_url)
        original_sum = 0
        original_num = 0
        for trainee in avg_grades_in_batch:
            original_sum += int(trainee.get("average"))
            original_num += 1
        avg_original = original_sum/original_num

        batches_url = URL_BASE + "training/batch/current/"
        batches = fetch_json(batches_url)
        similar_batches = [original_batch]
        for batch in batches:
            skill = batch.get("skill")
            prev_batch_id = batch.get("batchId")
            prev_batch_date = datetime.strptime(batch.get("startDate"), "%Y-%m-%d").date()
            if skill == batch_skill and original_batch_id != prev_batch_id:
                if original_date > prev_batch_date:
                    similar_batches.append(batch)
                    avg_grades_url = URL_BASE + f"evaluation/grades/reports/{prev_batch_id}/overall"
                    avg_grades_in_batch = fetch_json(avg_grades_url)
                    sum = 0
                    num = 0
                    for trainee in avg_grades_in_batch:
                        sum += int(trainee.get("average"))
                        num += 1
                    avg_prev = sum/num
                    if avg_original > avg_prev:
                        print("Hooray!")
                    else:
                        print("widepeeposad")
                else:
                    return "No other batches exist that are the same tech stack and before this one."
    except HTTPError:
        return "aight"

    return {"batches":similar_batches}
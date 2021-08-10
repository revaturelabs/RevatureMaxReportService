from urllib.error import HTTPError

from src.config.flask_config import app
from src.util.fetch import fetch_json
from datetime import datetime
from src.service.compare_batch_services import *

URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"

@app.route("/batch/<batch_id>/compare")
def compareBatchToPastBatches(batch_id):
    # localhost:5000/batch/TR-1145/compare
    try:
        # First get the skill and starting date of the batch
        batch_skill, original_date = get_batch_by_id(batch_id)
        # Get the grades for the batch and average them out
        avg_original = batch_total_avg(batch_id)

        data = {batch_id: [], "week":list(range(1, 8))}
        data.get("week").append("Overall")
        chart_data = {batch_id: []}
        for week in range(1, 8):
            weekly_avg = batch_weekly_avg(batch_id, week)
            data[batch_id].append(weekly_avg)
            chart_data[batch_id].append(weekly_avg)
        data[batch_id].append(avg_original)
        chart_data[batch_id].append(avg_original)

        batches = get_batches_with_same_skill(batch_skill, original_date)
        for batch in batches:
            prev_batch_id = batch[0]

            data[prev_batch_id] = []
            chart_data[prev_batch_id] = []
            avg_prev = batch_total_avg(prev_batch_id)

            for week in range(1, 8):
                weekly_avg_prev = batch_weekly_avg(prev_batch_id, week)
                data[prev_batch_id].append(weekly_avg_prev)
                chart_data[prev_batch_id].append(weekly_avg_prev)
            data[prev_batch_id].append(avg_prev)
            chart_data[prev_batch_id].append(avg_prev)

    except TypeError:
        return "Invalid batch ID"

    return {"data": data, "chartData": chart_data}

@app.route("/batch/<batch_id>/compare/<other_batch_id>")
def compareBatchToOtherBatch(batch_id, other_batch_id):
    try:
        # Get the grades for the batch and average them out
        avg_original = batch_total_avg(batch_id)

        data = {batch_id: [], "week": list(range(1, 8))}
        data.get("week").append("Overall")
        chart_data = {batch_id: []}
        for week in range(1, 8):
            weekly_avg = batch_weekly_avg(batch_id, week)
            data[batch_id].append(weekly_avg)
            chart_data[batch_id].append(weekly_avg)
        data[batch_id].append(avg_original)
        chart_data[batch_id].append(avg_original)

        data[other_batch_id] = []
        chart_data[other_batch_id] = []
        avg_prev = batch_total_avg(other_batch_id)

        for week in range(1, 8):
            weekly_avg_prev = batch_weekly_avg(other_batch_id, week)
            data[other_batch_id].append(weekly_avg_prev)
            chart_data[other_batch_id].append(weekly_avg_prev)
        data[other_batch_id].append(avg_prev)
        chart_data[other_batch_id].append(avg_prev)

    except HTTPError:
        return "Invalid batch ID"

    return {"data": data, "chartData": chart_data}
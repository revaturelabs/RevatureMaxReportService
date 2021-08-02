from urllib.error import HTTPError

from config.flask_config import app
from util.fetch import fetch_json
from datetime import datetime

URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"

@app.route("/batch/<batch_id>/compare")
def compareBatchToPastBatches(batch_id):
    # localhost:5000/batch/TR-1145/compare
    try:
        # First get the skill and starting date of the batch
        batch_url = URL_BASE + "training/batch/" + batch_id
        original_batch = fetch_json(batch_url)
        batch_skill = original_batch.get("skill")
        original_date = datetime.strptime(original_batch.get("startDate"), "%Y-%m-%d").date()
        # Get the grades for the batch and average them out
        original_grades_avg_url = URL_BASE + f"evaluation/grades/reports/{batch_id}/overall"
        avg_grades_in_batch = fetch_json(original_grades_avg_url)
        original_sum = 0
        original_num = 0
        for trainee in avg_grades_in_batch:
            original_sum += int(trainee.get("average"))
            original_num += 1
        avg_original = original_sum/original_num

        batches_url = URL_BASE + "training/batch"
        batches = fetch_json(batches_url)
        data = {batch_id: [], "week":list(range(1, 8))}
        data.get("week").append("Overall")
        chart_data = {batch_id: []}
        for week in range(1, 11):
            weekly_avg_url = URL_BASE + "evaluation/grades/reports/{}/overall/{}".format(batch_id, week)
            week_of_batch = fetch_json(weekly_avg_url)
            if week_of_batch[0].get("average") == 0:
                break
            weekly_sum = 0
            weekly_num = 0
            for associate in range(len(week_of_batch)):
                weekly_sum += week_of_batch[associate].get("average")
                weekly_num += 1
            data[batch_id].append(round(weekly_sum / weekly_num, 2))
            chart_data[batch_id].append(round(weekly_sum/weekly_num, 2))
        data[batch_id].append(round(avg_original, 2))
        chart_data[batch_id].append(round(avg_original, 2))
        for batch in batches:
            skill = batch.get("skill")
            prev_batch_id = batch.get("batchId")
            prev_batch_date = datetime.strptime(batch.get("startDate"), "%Y-%m-%d").date()

            if skill == batch_skill:
                if original_date > prev_batch_date:
                    data[prev_batch_id] = []
                    chart_data[prev_batch_id] = []
                    avg_grades_url = URL_BASE + f"evaluation/grades/reports/{prev_batch_id}/overall"
                    avg_grades_in_batch = fetch_json(avg_grades_url)
                    sum = 0
                    num = 0
                    for trainee in avg_grades_in_batch:
                        sum += int(trainee.get("average"))
                        num += 1
                    avg_prev = sum/num

                    for week in range(1, 11):
                        weekly_avg_url = URL_BASE + "evaluation/grades/reports/{}/overall/{}".format(prev_batch_id, week)
                        week_of_batch = fetch_json(weekly_avg_url)
                        if week_of_batch[0].get("average") == 0:
                            break
                        weekly_sum = 0
                        weekly_num = 0
                        for associate in range(len(week_of_batch)):
                            weekly_sum += week_of_batch[associate].get("average")
                            weekly_num += 1
                        data[prev_batch_id].append(round(weekly_sum/weekly_num, 2))
                        chart_data[prev_batch_id].append(round(weekly_sum / weekly_num, 2))
                    data[prev_batch_id].append(round(avg_prev, 2))
                    chart_data[prev_batch_id].append(round(avg_prev, 2))

                else:
                    return "No other batches exist that are the same tech stack and before this one."
    except HTTPError:
        return "Invalid batch ID"

    return {"data": data, "chartData": chart_data}

@app.route("/batch/<batch_id>/compare/<other_batch_id>")
def compareBatchToOtherBatch(batch_id, other_batch_id):
    try:
        # First get the skill and starting date of the batch
        batch_url = URL_BASE + "training/batch/" + batch_id
        original_batch = fetch_json(batch_url)
        original_date = datetime.strptime(original_batch.get("startDate"), "%Y-%m-%d").date()
        # Get the grades for the batch and average them out
        original_grades_avg_url = URL_BASE + f"evaluation/grades/reports/{batch_id}/overall"
        avg_grades_in_batch = fetch_json(original_grades_avg_url)
        original_sum = 0
        original_num = 0
        for trainee in avg_grades_in_batch:
            original_sum += int(trainee.get("average"))
            original_num += 1
        avg_original = original_sum / original_num
        data = {batch_id: [], "week": list(range(1, 8))}
        data.get("week").append("Overall")
        chart_data = {batch_id: []}
        for week in range(1, 11):
            weekly_avg_url = URL_BASE + "evaluation/grades/reports/{}/overall/{}".format(batch_id, week)
            week_of_batch = fetch_json(weekly_avg_url)
            if week_of_batch[0].get("average") == 0:
                break
            weekly_sum = 0
            weekly_num = 0
            for associate in range(len(week_of_batch)):
                weekly_sum += week_of_batch[associate].get("average")
                weekly_num += 1
            data[batch_id].append(round(weekly_sum / weekly_num, 2))
            chart_data[batch_id].append(round(weekly_sum / weekly_num, 2))
        data[batch_id].append(round(avg_original, 2))
        chart_data[batch_id].append(round(avg_original, 2))
        print(other_batch_id)
        other_batch = fetch_json(other_batch_id)
        prev_batch_date = datetime.strptime(other_batch.get("startDate"), "%Y-%m-%d").date()
        if original_date > prev_batch_date:
            data[other_batch_id] = []
            chart_data[other_batch_id] = []
            avg_grades_url = URL_BASE + f"evaluation/grades/reports/{other_batch_id}/overall"
            avg_grades_in_batch = fetch_json(avg_grades_url)
            sum = 0
            num = 0
            for trainee in avg_grades_in_batch:
                sum += int(trainee.get("average"))
                num += 1
            avg_prev = sum / num

            for week in range(1, 11):
                weekly_avg_url = URL_BASE + "evaluation/grades/reports/{}/overall/{}".format(other_batch_id, week)
                week_of_batch = fetch_json(weekly_avg_url)
                if week_of_batch[0].get("average") == 0:
                    break
                weekly_sum = 0
                weekly_num = 0
                for associate in range(len(week_of_batch)):
                    weekly_sum += week_of_batch[associate].get("average")
                    weekly_num += 1
                data[other_batch_id].append(round(weekly_sum / weekly_num, 2))
                chart_data[other_batch_id].append(round(weekly_sum / weekly_num, 2))
            data[other_batch_id].append(round(avg_prev, 2))
            chart_data[other_batch_id].append(round(avg_prev, 2))
        else:
            return "{} starts after {}.".format(other_batch_id, batch_id)

    except HTTPError:
        return "Invalid batch ID"

    return {"data": data, "chartData": chart_data}
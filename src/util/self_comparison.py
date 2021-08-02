from util.fetch import fetch_json

URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"


def score_report_by_week(batch_id, associate_email):
    results = individual_score_by_week_formatted(batch_id, associate_email)
    batch_scores = batch_averages_by_week_formatted(batch_id)

    results["data"]["Batch Averages"] = batch_scores["data"]["Batch Averages"]
    results["chartData"]["Batch Average Score"] = batch_scores["chartData"]["Batch Average Score"]

    return results


def batch_averages_by_week_formatted(batch_id):
    # https://caliber2-mock.revaturelabs.com/mock/evaluation/grades/reports/TR-1190/spider/
    url = f"{URL_BASE}evaluation/grades/reports/{batch_id}/spider"
    batch_average_by_week = fetch_json(url)
    results = {
        "data": {"Batch Averages": []},
        "chartData": {"Batch Average Score": []}
    }
    for avg in batch_average_by_week:
        results["data"]["Batch Averages"].append(avg["score"])
        results["chartData"]["Batch Average Score"].append(avg["score"])
    return results


def individual_score_by_week_formatted(batch_id, associate_email):
    # https://caliber2-mock.revaturelabs.com/mock/evaluation/grades/reports/TR-1190/spider/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com
    url = f"{URL_BASE}evaluation/grades/reports/{batch_id}/spider/{associate_email}"
    individual_score_by_week = fetch_json(url)
    results = {
        "data": {"Assessment Type": [], "My Score": [], " Week #": [], "Weight": []},
        "chartData": {"Associate Score": []}
    }
    for row in individual_score_by_week:
        results["chartData"]["Associate Score"].append(row["score"])
        results["data"]["Assessment Type"].append(row["assessmentType"])
        results["data"]["My Score"].append(row["score"])
        results["data"][" Week #"].append(row["week"])
        results["data"]["Weight"].append(row["weight"])

    return results


def individual_vs_batch_score_formatted(batch_id, associate_email):
    result, categories = individual_vs_batch_score(batch_id, associate_email)

    values = {"data": {}, "chartData": {}}
    for category in categories:
        values["data"] = {**values["data"], **table_data(result, category)}
        values["chartData"] = {**values["chartData"], **chart_data(result, category)}

    return values


def individual_vs_batch_score(batch_id, associate_email):
    # https://caliber2-mock.revaturelabs.com:443/mock/training/associate/mock1.associatee5c1c02d-531e-404c-9a86-082107ff12bc%40mock.com/batch
    url = f"{URL_BASE}qa/notes/batch/{batch_id}"
    notes_by_week_for_batch = fetch_json(url)
    weeks = list(map(lambda x: x.get("week", None), notes_by_week_for_batch))

    result = {}
    categories = set()
    for week in weeks:
        url = f"{URL_BASE}evaluation/grades/reports/individual/{associate_email}/{week}"
        r1 = fetch_json(url)
        for key in r1.keys():
            categories = categories.union(set(r1[key].keys()))

        r1["week"] = week
        result[week] = r1
    return result, categories


def table_data(dataBlock, category):
    # intentional leading space to get this to appear first in an alphabetized grouping
    report = {
        " Week #": [],
        f"Average {category} Score": [],
        f"Associate {category} Score": [],
    }
    # construct the final
    for data in dataBlock.values():
        report[" Week #"].append(data["week"])
        grade = data["traineeGrades"].get(category, "N/A")
        if isinstance(grade, float):
            grade = f"{grade:.2f}"
        report[f"Associate {category} Score"].append(grade)
        grade = data["restOfBatchGrades"].get(category, "N/A")
        if isinstance(grade, float):
            grade = f"{grade:.2f}"
        report[f"Average {category} Score"].append(grade)
    return report


def step_fill(prev_score, score, next_score, multiplier):
    if score != -1 or next_score == -1:
        return score
    return prev_score + (next_score - prev_score) * multiplier


def chart_data(dataBlock, category):
    report = {f"Average {category} Score": [], f"Associate {category} Score": []}
    # construct the final, fill with -1
    for data in dataBlock.values():
        report[f"Associate {category} Score"].append(
            data["traineeGrades"].get(category, -1)
        )
        report[f"Average {category} Score"].append(
            data["restOfBatchGrades"].get(category, -1)
        )

    dat_iter = iter(report[f"Associate {category} Score"])
    next(dat_iter)
    index_from = 0
    index_to = 1

    for index in range(len(report[f"Associate {category} Score"])):
        # interpolate data for the graph for when these values weren't added
        # e.g. week 1 and week 3 had an Exam but week 2 didn't
        if report[f"Associate {category} Score"][index] == -1:
            multiplier = (index - index_from) / (index_to - index_from)

            report[f"Associate {category} Score"][index] = step_fill(
                report[f"Associate {category} Score"][index_from],
                report[f"Associate {category} Score"][index],
                report[f"Associate {category} Score"][index_to],
                multiplier,
            )
            report[f"Average {category} Score"][index] = step_fill(
                report[f"Average {category} Score"][index_from],
                report[f"Average {category} Score"][index],
                report[f"Average {category} Score"][index_to],
                multiplier,
            )

            if index + 1 == index_to:
                index_from = index
        else:
            index_from = index_to = index
            try:
                while True:
                    index_to += 1
                    if next(dat_iter) != -1:
                        break
            except StopIteration:
                for i in range(
                    index_from + 1, len(report[f"Associate {category} Score"])
                ):
                    report[f"Associate {category} Score"][i] = 0
                    report[f"Average {category} Score"][i] = 0
                break  # end outermost for loop

    for index in range(len(report[f"Associate {category} Score"])):
        if report[f"Associate {category} Score"][index] == -1:
            report[f"Associate {category} Score"][index] = 0
            report[f"Average {category} Score"][index] = 0

    return report

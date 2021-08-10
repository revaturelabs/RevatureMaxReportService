from dao import category_dao, associate_dao
from model.category import Category


def create_category(category: Category):
    if category.grade_id == -1:  # category has no valid grade id
        category_dao.create_new(*category.to_tuple()[1:])
    else:  # category refers to something that existed previously
        category_dao.create_existing(*category.to_tuple())


def select_by_email_category_week(associate_email, category_type, week):
    result = category_dao.select_by_email_category_week(associate_email, category_type, week)
    return list(map(lambda x: Category(*x), filter(None, result)))


def select_by_email_category(associate_email, category_type):
    result = category_dao.select_by_email_category(associate_email, category_type)
    return list(map(lambda x: Category(*x), filter(None, result)))


def select_by_email(associate_email):
    result = category_dao.select_by_email(associate_email)
    return list(map(lambda x: Category(*x), filter(None, result)))


def select_by_batch(batch_id):
    result = category_dao.select_by_batch(batch_id)
    return list(map(lambda x: Category(*x), filter(None, result)))


def select_batch_average_weekly(batch_id):
    batch_scores = sorted(category_dao.select_batch_average_weekly(batch_id), key=lambda x: x[2])
    cat = None
    result = {}
    for score in batch_scores:
        if cat is None or score.category != cat:
            cat = score[1]
            result[cat] = []
        result[cat].append(score[0])
    return result


def select_all_categories():
    return [tpl[0] for tpl in filter(None, category_dao.select_all_categories())]


def select_all_by_batch_averages(batch_id):
    categories = select_all_categories()
    associate_scores = {}
    for cat in categories:
        cat = str.lower(cat)
        result_set = select_by_batch_category(batch_id, cat)
        for result in result_set:
            if result.email not in associate_scores.keys():
                associate_scores[result.email] = {}
            if cat not in associate_scores[result.email].keys():
                associate_scores[result.email][cat] = 0
                associate_scores[result.email][f"{cat}_weight"] = 0

            associate_scores[result.email][cat] += result.score * result.grade_weight
            associate_scores[result.email][f"{cat}_weight"] += result.grade_weight

    result = {
        "Associate Name": [],
        "Quiz Score": [],
        "Exam Score": [],
        "Project Score": [],
        "Verbal Score": [],
        "Email": [],
    }
    weighted_score_sum = {
        "quiz": 0,
        "exam": 0,
        "project": 0,
        "verbal": 0,
        "quiz_weight": 1,
        "exam_weight": 1,
        "project_weight": 1,
        "verbal_weight": 1,
    }
    # Associate running total
    for associate_email in associate_scores.keys():
        associate_score = associate_scores[associate_email]
        result["Associate Name"].append(
            associate_dao.select_name_by_email(associate_email)
        )
        result["Quiz Score"].append(
            associate_score.get("quiz", 0) / associate_score.get("quiz_weight", 1)
        )
        weighted_score_sum["quiz"] += associate_score.get("quiz", 0)
        weighted_score_sum["quiz_weight"] += associate_score.get("quiz_weight", 0)
        result["Exam Score"].append(
            associate_score.get("exam", 0) / associate_score.get("exam_weight", 1)
        )
        weighted_score_sum["exam"] += associate_score.get("exam", 0)
        weighted_score_sum["exam_weight"] += associate_score.get("exam_weight", 0)
        result["Project Score"].append(
            associate_score.get("project", 0) / associate_score.get("project_weight", 1)
        )
        weighted_score_sum["project"] += associate_score.get("project", 0)
        weighted_score_sum["project_weight"] += associate_score.get("project_weight", 0)
        result["Verbal Score"].append(
            associate_score.get("verbal", 0) / associate_score.get("verbal_weight", 1)
        )
        weighted_score_sum["verbal"] += associate_score.get("verbal", 0)
        weighted_score_sum["verbal_weight"] += associate_score.get("verbal_weight", 0)
        result["Email"].append(associate_email)
    # Batch running total averages
    result["Associate Name"].insert(0, "-")
    result["Email"].insert(0, "-")
    result["Quiz Score"].insert(
        0, weighted_score_sum["quiz"] / weighted_score_sum["quiz_weight"]
    )
    result["Exam Score"].insert(
        0, weighted_score_sum["exam"] / weighted_score_sum["exam_weight"]
    )
    result["Project Score"].insert(
        0, weighted_score_sum["project"] / weighted_score_sum["project_weight"]
    )
    result["Verbal Score"].insert(
        0, weighted_score_sum["verbal"] / weighted_score_sum["verbal_weight"]
    )
    return result


def select_categorical_averages_by_email_weekly(associate_email):
    values_by_category = category_dao.select_categorical_averages_by_email_weekly(associate_email)
    if values_by_category is None or len(values_by_category) == 0:
        return {}
    values_by_category = filter(None, values_by_category)
    values_by_category = sorted(values_by_category, key=lambda x: x[1])
    category = None
    result = {}

    for score_by_week in sorted(values_by_category, key=lambda res: res[2]):
        if category is None or score_by_week[1] != category:
            category = score_by_week[1]
            result[f"Associate {category} Score"] = []
        result[f"Associate {category} Score"].append(f"{float(score_by_week[0]):.2f}")

    return result


def select_batch_averages_weekly(batch_id):
    values_by_category = category_dao.select_batch_averages_weekly(batch_id)
    if values_by_category is None or len(values_by_category) == 0:
        return {}
    values_by_category = filter(None, values_by_category)
    values_by_category = sorted(values_by_category, key=lambda x: x[1])
    category = None
    result = {}

    for score_by_week in sorted(values_by_category, key=lambda res: res[2]):
        if category is None or score_by_week[1] != category:
            category = score_by_week[1]
            result[f"Average {category} Score"] = []
        result[f"Average {category} Score"].append(f"{float(score_by_week[0]):.2f}")

    return result


def select_by_batch_category(batch_id, category_type):
    result = category_dao.select_by_batch_category(batch_id, category_type)
    return list(map(lambda x: Category(*x), filter(None, result)))


def select_by_batch_max_grade(batch_id, max_grade):
    result = category_dao.select_by_batch_max_grade(batch_id, max_grade)
    return list(map(lambda x: Category(*x), filter(None, result)))

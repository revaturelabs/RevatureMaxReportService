from dao import assessment_dao
from model.assessment import Assessment


def create_assessment(assessment: Assessment):
    tpl = assessment.to_tuple()
    if assessment.grade_id == -1:  # assessment has no valid grade id
        assessment_dao.create_new(*assessment.to_tuple()[1:])
    else:  # assessment refers to something that existed previously
        assessment_dao.create_existing(*assessment.to_tuple())


def select_by_email_assessment_week(associate_email, assessment_type, week):
    result = assessment_dao.select_by_email_assessment_week(
        associate_email, assessment_type, week
    )
    return list(map(lambda x: Assessment(*x), filter(None, result)))


def select_by_email_assessment(associate_email, assessment_type):
    result = assessment_dao.select_by_email_assessment(associate_email, assessment_type)
    return list(map(lambda x: Assessment(*x), filter(None, result)))


def select_by_email(associate_email):
    result = assessment_dao.select_by_email(associate_email)
    return list(map(lambda x: Assessment(*x), filter(None, result)))


def select_by_batch(batch_id):
    result = assessment_dao.select_by_batch(batch_id)
    return list(map(lambda x: Assessment(*x), filter(None, result)))


def select_by_batch_assessment(batch_id, assessment_type):
    result = assessment_dao.select_by_batch_assessment(batch_id, assessment_type)
    return list(map(lambda x: Assessment(*x), filter(None, result)))


def select_by_batch_max_grade(batch_id, max_grade):
    result = assessment_dao.select_by_batch_max_grade(batch_id, max_grade)
    return list(map(lambda x: Assessment(*x), filter(None, result)))


def select_assessment_averages_by_email(associate_email):
    values = assessment_dao.select_assessment_averages_by_email(associate_email)
    return values


def select_batch_averages(batch_id, associate_email):
    result = {"Week #": [], "Assessment Type": [], "My Score": [], "Weight": []}
    values = assessment_dao.select_weekly_categories_by_email(associate_email)
    if values is None:
        return {}

    for value in values:
        # score, assessment_type, week, grade_weight
        result["My Score"].append(f"{float(value[0]):.2f}")
        result["Assessment Type"].append(value[1])
        result["Week #"].append(value[2])
        result["Weight"].append(value[3])

    result["Batch Averages"] = [
        f"{float(x[0]):.2f}" for x in assessment_dao.select_weekly_categories_by_batch(batch_id)
    ]
    return result

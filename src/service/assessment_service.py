from src.dao import assessment_dao as dao
from src.model.assessment import Assessment


def create_assessment(assessment: Assessment):
    if assessment.grade_id == -1:  # assessment has no valid grade id
        dao.create_new(*assessment.to_tuple()[1:])
    else:  # assessment refers to something that existed previously
        dao.create_existing(*assessment)


def select_by_email_assessment_week(associate_email, assessment_type, week):
    result = dao.select_by_email_assessment_week(associate_email, assessment_type, week)
    return list(map(lambda x: Assessment(*x), result))


def select_by_email_assessment(associate_email, assessment_type):
    result = dao.select_by_email_assessment(associate_email, assessment_type)
    return list(map(lambda x: Assessment(*x), result))


def select_by_email(associate_email):
    result = dao.select_by_email(associate_email)
    return list(map(lambda x: Assessment(*x), result))


def select_by_batch(batch_id):
    result = dao.select_by_batch(batch_id)
    return list(map(lambda x: Assessment(*x), result))


def select_by_batch_assessment(batch_id, assessment_type):
    result = dao.select_by_batch_assessment(batch_id, assessment_type)
    return list(map(lambda x: Assessment(*x), result))


def select_by_batch_max_grade(batch_id, max_grade):
    result = dao.select_by_batch_max_grade(batch_id, max_grade)
    return list(map(lambda x: Assessment(*x), result))

from dao.dao_helper import cursor_handler
from util.fetch import fetch_json
from service import assessment_service, category_service
from dao import associate_dao
from model.assessment import Assessment
from model.associate import Associate
from model.category import Category


URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"
batches_considered = ["TR-1145", "TR-1190", "TR-1072", "TR-1021", "TR-1140"]


@cursor_handler
def initialize_batch(batch, cursor):
    cursor.execute("DELETE FROM report_batch WHERE rb_id = %s", (batch["id"],))
    cursor.execute(
        """INSERT INTO report_batch
        VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        (
            batch["batchId"],
            batch["name"],
            batch["skill"],
            batch["location"],
            batch["type"],
            batch["goodGrade"],
            batch["passingGrade"],
            batch["currentWeek"],
            batch["startDate"],
            batch["endDate"],
        ),
    )


@cursor_handler
def initialize_batch_grades(trainee, batch_id, cursor):
    cursor.execute(
        "DELETE FROM batch_grades WHERE batch_id = %s AND traineename = %s",
        (str(batch_id), trainee["traineeName"]),
    )
    cursor.execute(
        """INSERT INTO batch_grades
        VALUES (%s, %s, %s)""",
        (trainee["traineeName"], trainee["average"], str(batch_id)),
    )


@cursor_handler
def initialize_report_on_assessment(report, cursor):
    cursor.execute(
        "DELETE FROM report_on_assessment WHERE associate_id = %s AND week = %s AND assessment_type = %s",
        (report["traineeId"], report["week"], report["assessmentType"]),
    )
    cursor.execute(
        """INSERT INTO report_on_assessment VALUES(DEFAULT, %s, NULL, %s, %s, %s, %s)""",
        (
            report["traineeId"],
            report["assessmentType"],
            str(report["score"]),
            str(report["week"]),
            str(int(report["weight"])),
        ),
    )


@cursor_handler
def get_batch_ids(cursor):
    cursor.execute("SELECT batch_id FROM report_batch ORDER BY batchid")
    return cursor.fetchall()


def populate_batch_table():
    url_batch_current = f"{URL_BASE}training/batch/current"
    url_batch = f"{URL_BASE}training/batch"
    url_batch_1190 = f"{URL_BASE}training/batch/TR-1190"
    current_batch_json = fetch_json(url_batch_current)
    batch_json = fetch_json(url_batch)
    batch_1190_json = fetch_json(url_batch_1190)

    initialize_batch(batch_1190_json)

    for batch in current_batch_json:
        initialize_batch(batch)

    for batch in batch_json:
        initialize_batch(batch)


def selective_populate_batch_table():
    for batch in batches_considered:
        initialize_batch(batch)


def populate_batch_grades_table():
    for batch_id in get_batch_ids():
        url_batch_grade = f"{URL_BASE}evaluation/grades/reports/{batch_id[0]}/overall"
        batch_grade_json = fetch_json(url_batch_grade)
        for trainee in batch_grade_json:
            initialize_batch_grades(trainee, batch_id[0])


def get_list_of_emails(batch_id):
    emails_url = f"{URL_BASE}training/batch/{batch_id}"
    data = fetch_json(emails_url)
    emails = []
    for assoc in data["associateAssignments"]:
        emails.append(assoc["associate"]["email"])
    return emails


def populate_assessment_table():
    for batch in batches_considered:
        batched_emails = get_list_of_emails(batch)
        for email in batched_emails:
            data = fetch_json(
                f"{URL_BASE}evaluation/grades/reports/{batch}/spider/{email}"
            )
            for d in data:
                assess = Assessment(
                    -1,
                    batch,
                    email,
                    d["assessmentType"],
                    d["score"],
                    d["week"],
                    d["weight"],
                )
                assessment_service.create_assessment(assess)


def populate_associate_table():
    for batch in batches_considered:
        batched_emails = get_list_of_emails(batch)
        for email in batched_emails:
            data = fetch_json(f"{URL_BASE}training/associate/{email}")
            a = Associate(
                email, data["salesforceId"], data["firstName"], data["lastName"], batch
            )
            associate_dao.create_new_associate(*a.to_tuple())


@cursor_handler
def get_known_weeks_for_batch(batch_id, cursor):
    cursor.execute("""
        SELECT week FROM report_on_assessment
            WHERE batch_id = %s
            GROUP BY week
            ORDER BY week;
    """, (batch_id,))
    return cursor.fetchall()


def populate_category_table():
    for batch in batches_considered:
        batched_emails = get_list_of_emails(batch)
        for email in batched_emails:
            weeks = get_known_weeks_for_batch(batch)
            for week in weeks:
                data = fetch_json(
                    f"{URL_BASE}evaluation/grades/reports/individual/{email}/{week[0]}"
                )
                if "traineeGrades" in data:
                    for d in data["traineeGrades"]:
                        category = Category(
                            -1,
                            batch,
                            email,
                            d,
                            data["traineeGrades"][d],
                            week,
                            100,
                        )
                        category_service.create_category(category)

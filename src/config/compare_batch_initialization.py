from src.dao.dao_helper import cursor_handler
from src.util.fetch import fetch_json

URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"


@cursor_handler
def initialize_batch(batch, cursor):
    cursor.execute('DELETE FROM report_batch WHERE id = %s', (batch['id'],))
    cursor.execute(
        """INSERT INTO report_batch
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        (batch['id'], batch['batchId'], batch['name'], batch['startDate'], batch['endDate'], batch['skill'], batch['location'], batch['type'], batch['goodGrade'],
         batch['passingGrade'], batch['currentWeek'])
    )

@cursor_handler
def initialize_batch_grades(trainee, batch_id, cursor):
    cursor.execute('DELETE FROM batch_grades WHERE batch_id = %s AND traineename = %s', (str(batch_id), trainee['traineeName']))
    cursor.execute("""INSERT INTO batch_grades
        VALUES (%s, %s, %s)""", (trainee['traineeName'], trainee['average'], str(batch_id)))

@cursor_handler
def initialize_report_on_assessment(report, cursor):
    cursor.execute('DELETE FROM report_on_assessment WHERE traineeid = %s AND week = %s AND assessmenttype = %s', (report['traineeId'], report['week'], report['assessmentType']))
    cursor.execute("""INSERT INTO report_on_assessment VALUES(DEFAULT, %s, NULL, %s, %s, %s, %s)""",
                   (report['traineeId'], report['assessmentType'], str(report['score']), str(report['week']), str(int(report['weight']))))

@cursor_handler
def get_batch_ids(cursor):
    cursor.execute('SELECT batchid FROM report_batch ORDER BY batchid')
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


def populate_batch_grades_table():
    for batch_id in get_batch_ids():
        url_batch_grade = f"{URL_BASE}evaluation/grades/reports/{batch_id[0]}/overall"
        batch_grade_json = fetch_json(url_batch_grade)
        for trainee in batch_grade_json:
            initialize_batch_grades(trainee, batch_id[0])

def populate_report_on_assessments_table():
    for batch_id in get_batch_ids():
        url_spider = f"{URL_BASE}evaluation/grades/reports/{batch_id[0]}/spider"
        spider_json = fetch_json(url_spider)
        for report in spider_json:
            initialize_report_on_assessment(report)
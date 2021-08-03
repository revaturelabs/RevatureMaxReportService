from src.dao.dao_helper import cursor_handler

# -- https://caliber2-mock.revaturelabs.com/mock/evaluation/grades/reports/TR-1190/spider/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com
# CREATE TABLE report_on_assessment (
#   grade_id        BIGSERIAL,    --
#   batch_id        VARCHAR,
#     REFERENCES report_batch(batch_id),
#   associate_id    VARCHAR(40)
#     REFERENCES associate(email),
#   assessment_type  VARCHAR(10), -- assessmentType
#   score           INTEGER
#     CHECK score >= 0,           -- score
#   week            INTEGER
#     CHECK week > 0,             -- week
#   grade_weight    INTEGER
#     CHECK grade_weight >= 0,    -- weight
# );
#


@cursor_handler
def create_existing(grade_id, batch_id, associate_id, assessment_type, score, week, grade_weight, cursor):
    cursor.execute(
        """INSERT INTO report_on_assessment
        VALUES (%s, %s, %s, %s, %s, %s, %s)""",
        (grade_id, batch_id, associate_id, assessment_type, score, week, grade_weight),
    )
    cursor.commit()


@cursor_handler
def create_new(batch_id, associate_id, assessment_type, score, week, grade_weight, cursor):
    cursor.execute(
        """INSERT INTO report_on_assessment
        VALUES (%s, %s, %s, %s, %s, %s)""",
        (batch_id, associate_id, assessment_type, score, week, grade_weight),
    )
    cursor.commit()

# DROP TABLE IF EXISTS report_batch, report_employee, report_evaluation, report_on_assessment CASCADE;
# DROP TABLE IF EXISTS associate_portfolio, employee_portfolio, associate, employee CASCADE;

# create table associate(
#     salesforceId varchar(10) primary key not null, 
#     firstname varchar(20) not null,
#     lastname varchar(20) not null,
#     email varchar(40) UNIQUE,
#     pswrd varchar(40)
# );
from src.model.associate import Associate
associates = [
    Associate("ex0001@example.com", "EX-0001", "ExFirst", "ExLast", ""),
    Associate("ex0002@example.com", "EX-0002", "ExFirst", "ExLast", ""),
    Associate("ex0003@example.com", "EX-0003", "ExFirst", "ExLast", ""),
    Associate("ex0004@example.com", "EX-0004", "ExFirst", "ExLast", ""),
    Associate("ex0005@example.com", "EX-0005", "ExFirst", "ExLast", ""),
    Associate("ex0006@example.com", "EX-0006", "ExFirst", "ExLast", ""),
    Associate("ex0007@example.com", "EX-0007", "ExFirst", "ExLast", ""),
    Associate("ex0008@example.com", "EX-0008", "ExFirst", "ExLast", ""),
    Associate("ex0009@example.com", "EX-0009", "ExFirst", "ExLast", ""),
]

# CREATE TABLE report_batch (
#   rb_id BIGSERIAL PRIMARY KEY,
#   batch_id VARCHAR UNIQUE,       -- batchId
#   rb_name VARCHAR,               -- name
#   skill VARCHAR,                 -- skill
#   rb_location VARCHAR,           -- location
#   rb_type VARCHAR,               -- type
#   good_grade SERIAL,             -- goodGrade
#   passing_grade SERIAL,          -- passingGrade
#   -- for some reason, I've seen test data with negative week numbers
#   current_week INTEGER,          -- currentWeek
#   rb_start_date VARCHAR,         -- startDate
#   rb_end_date VARCHAR            -- endDate
# );
from src.model.batch import Batch
batches = [
    Batch(0, "EX-B01", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(1, "EX-B02", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(2, "EX-B03", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(3, "EX-B04", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(4, "EX-B05", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(5, "EX-B06", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(6, "EX-B07", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(7, "EX-B08", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(8, "EX-B09", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(9, "EX-B10", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(10, "EX-B11", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
]

# -- https://caliber2-mock.revaturelabs.com/mock/evaluation/grades/reports/TR-1190/spider/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com
# CREATE TABLE report_on_assessment (
#   grade_id        BIGSERIAL,    -- 
#   batch_id        VARCHAR
#     REFERENCES report_batch(batch_id),
#   associate_id    VARCHAR(40)
#     REFERENCES associate(email),
#   assessment_type  VARCHAR(10), -- assessmentType
#   score           INTEGER  
#     CHECK (score >= 0),           -- score
#   week            INTEGER
#     CHECK (week > 0),             -- week
#   grade_weight    INTEGER
#     CHECK (grade_weight >= 0)     -- weight
# );
from src.model.assessment import Assessment
assessments = [
    Assessment(0, "EX-B01", "ex0001@example.com", "Score", 60, 1, 100),
    Assessment(1, "EX-B01", "ex0003@example.com", "Score", 60, 1, 100),
    Assessment(2, "EX-B01", "ex0005@example.com", "Score", 60, 1, 100),
    Assessment(3, "EX-B01", "ex0007@example.com", "Score", 60, 1, 100),
    Assessment(4, "EX-B01", "ex0009@example.com", "Score", 60, 1, 100),
    Assessment(5, "EX-B02", "ex0002@example.com", "Score", 60, 1, 100),
    Assessment(6, "EX-B02", "ex0004@example.com", "Score", 60, 1, 100),
    Assessment(7, "EX-B02", "ex0006@example.com", "Score", 60, 1, 100),
    Assessment(8, "EX-B02", "ex0008@example.com", "Score", 60, 1, 100),
    Assessment(9, "EX-B01", "ex0001@example.com", "Score", 60, 1, 100),
    Assessment(10, "EX-B01", "ex0003@example.com", "Score", 70, 2, 100),
    Assessment(11, "EX-B01", "ex0005@example.com", "Score", 70, 2, 100),
    Assessment(12, "EX-B01", "ex0007@example.com", "Score", 70, 2, 100),
    Assessment(13, "EX-B01", "ex0009@example.com", "Score", 70, 2, 100),
    Assessment(14, "EX-B02", "ex0002@example.com", "Score", 70, 2, 100),
    Assessment(15, "EX-B02", "ex0004@example.com", "Score", 70, 2, 100),
    Assessment(16, "EX-B02", "ex0006@example.com", "Score", 70, 2, 100),
    Assessment(17, "EX-B02", "ex0008@example.com", "Score", 70, 2, 100),
    Assessment(20, "EX-B01", "ex0001@example.com", "Score", 60, 3, 100),
    Assessment(21, "EX-B01", "ex0003@example.com", "Score", 60, 3, 100),
    Assessment(22, "EX-B01", "ex0005@example.com", "Score", 60, 3, 100),
    Assessment(23, "EX-B01", "ex0007@example.com", "Score", 60, 3, 100),
    Assessment(24, "EX-B01", "ex0009@example.com", "Score", 60, 3, 100),
    Assessment(25, "EX-B02", "ex0002@example.com", "Score", 60, 3, 100),
    Assessment(26, "EX-B02", "ex0004@example.com", "Score", 60, 3, 100),
    Assessment(27, "EX-B02", "ex0006@example.com", "Score", 60, 3, 100),
    Assessment(28, "EX-B02", "ex0008@example.com", "Score", 60, 3, 100),
    Assessment(29, "EX-B01", "ex0001@example.com", "Score", 60, 3, 100),
    Assessment(210, "EX-B01", "ex0003@example.com", "Score", 70, 4, 100),
    Assessment(211, "EX-B01", "ex0005@example.com", "Score", 70, 4, 100),
    Assessment(212, "EX-B01", "ex0007@example.com", "Score", 70, 4, 100),
    Assessment(213, "EX-B01", "ex0009@example.com", "Score", 70, 4, 100),
    Assessment(214, "EX-B02", "ex0002@example.com", "Score", 70, 4, 100),
    Assessment(215, "EX-B02", "ex0004@example.com", "Score", 70, 4, 100),
    Assessment(216, "EX-B02", "ex0006@example.com", "Score", 70, 4, 100),
    Assessment(217, "EX-B02", "ex0008@example.com", "Score", 70, 4, 100),
]

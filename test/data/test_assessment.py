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

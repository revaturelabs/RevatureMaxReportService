# CREATE TABLE report_on_category (
#   grade_id        BIGSERIAL,      --
#   batch_id        VARCHAR
#     REFERENCES report_batch(batch_id),
#   email           VARCHAR(40)
#     REFERENCES associate(email),
#   category        VARCHAR(10),    -- assessmentType
#   score           INTEGER
#     CHECK (score >= 0),           -- score
#   week            INTEGER
#     CHECK (week > 0),             -- week
#   grade_weight    INTEGER
#     CHECK (grade_weight >= 0)     -- weight
# );
from src.model.category import Category
categories = [
    Category(0, "EX-B01", "ex0001@example.com", "Verbal", 10, 1, 100),
    Category(1, "EX-B01", "ex0003@example.com", "Verbal", 11, 1, 100),
    Category(2, "EX-B01", "ex0005@example.com", "Verbal", 20, 1, 100),
    Category(3, "EX-B01", "ex0007@example.com", "Verbal", 21, 1, 100),
    Category(4, "EX-B01", "ex0009@example.com", "Verbal", 30, 1, 100),
    Category(5, "EX-B02", "ex0002@example.com", "Verbal", 31, 1, 100),
    Category(6, "EX-B02", "ex0004@example.com", "Verbal", 40, 1, 100),
    Category(7, "EX-B02", "ex0006@example.com", "Verbal", 41, 1, 100),
    Category(8, "EX-B02", "ex0008@example.com", "Quiz", 50, 1, 100),
    Category(9, "EX-B01", "ex0001@example.com", "Quiz", 51, 1, 100),
    Category(10, "EX-B01", "ex0003@example.com", "Exam", 60, 2, 100),
    Category(11, "EX-B01", "ex0005@example.com", "Exam", 61, 2, 100),
    Category(12, "EX-B01", "ex0007@example.com", "Exam", 70, 2, 100),
    Category(13, "EX-B01", "ex0009@example.com", "Exam", 71, 2, 100),
    Category(14, "EX-B02", "ex0002@example.com", "Exam", 80, 2, 100),
    Category(15, "EX-B02", "ex0004@example.com", "Exam", 81, 2, 100),
    Category(16, "EX-B02", "ex0006@example.com", "Exam", 90, 2, 100),
    Category(17, "EX-B02", "ex0008@example.com", "Exam", 91, 2, 100),
    Category(20, "EX-B01", "ex0001@example.com", "Exam", 100, 3, 100),
    Category(21, "EX-B01", "ex0003@example.com", "Exam", 19, 3, 100),
    Category(22, "EX-B01", "ex0005@example.com", "Exam", 29, 3, 100),
    Category(23, "EX-B01", "ex0007@example.com", "Exam", 39, 3, 100),
    Category(24, "EX-B01", "ex0009@example.com", "Exam", 49, 3, 100),
    Category(25, "EX-B02", "ex0002@example.com", "Exam", 59, 3, 100),
    Category(26, "EX-B02", "ex0004@example.com", "Exam", 69, 3, 100),
    Category(27, "EX-B02", "ex0006@example.com", "Quiz", 79, 3, 100),
    Category(28, "EX-B02", "ex0008@example.com", "Quiz", 89, 3, 100),
    Category(29, "EX-B01", "ex0001@example.com", "Quiz", 99, 3, 100),
    Category(210, "EX-B01", "ex0003@example.com", "Project", 15, 4, 100),
    Category(211, "EX-B01", "ex0005@example.com", "Project", 25, 4, 100),
    Category(212, "EX-B01", "ex0007@example.com", "Project", 35, 4, 100),
    Category(213, "EX-B01", "ex0009@example.com", "Project", 45, 4, 100),
    Category(214, "EX-B02", "ex0002@example.com", "Project", 55, 4, 100),
    Category(215, "EX-B02", "ex0004@example.com", "Project", 65, 4, 100),
    Category(216, "EX-B02", "ex0006@example.com", "Project", 75, 4, 100),
    Category(217, "EX-B02", "ex0008@example.com", "Project", 85, 4, 100),
]

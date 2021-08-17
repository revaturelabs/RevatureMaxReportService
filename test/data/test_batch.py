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

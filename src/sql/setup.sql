DROP IF EXISTS report_batch, report_employee CASCADE;

-- CREATE TABLE report_role (
--   rr_id BIGSERIAL PRIMARY KEY,
--   role_name VARCHAR,
-- );

CREATE TABLE report_employee (
  re_id BIGSERIAL PRIMARY KEY,    
  -- rr_role_id BIGSERIAL
  --   REFERENCES report_role(rr_id),
  rb_id BIGSERIAL
    REFERENCES report_batch(rb_id),           
  email VARCHAR UNIQUE NOT NULL,  -- email
  first_name VARCHAR NOT NULL,    -- firstName
  last_name VARCHAR NOT NULL,     -- lastName
  associate_id VARCHAR,           -- salesforceId / associateId
  -- flag VARCHAR,                   -- flag
);

CREATE TABLE report_evaluation (
  grade_id BIGSERIAL PRIMARY KEY, -- gradeId
  date_received DATE,             -- dateReceived
  score DECIMAL,                  -- score
  re_id BIGSERIAL,                -- assessmentId note that this is different than the gradeId
  trainee_id VARCHAR,             -- traineeId /mock/qa/notes/trainee/SF-2681
);

--https://caliber2-mock.revaturelabs.com:443/mock/qa/notes/individual/TR-1190
CREATE TABLE report_qc_note (
  note_id BIGSERIAL PRIMARY KEY,  -- "noteId": 3942,
  content VARCHAR,                -- "content": "This is a Qc note on week 6",
  week INTEGER,                   -- "week": 6,
  batch_id VARCHAR,               -- "batchId": "TR-1190",
  associate_id VARCHAR,           -- "associateId": "SF-2681",
  employee_id VARCHAR,            -- "employeeId": "QC-User",
  associate_type VARCHAR,         -- "type": "QC_TRAINEE",
  technical_status VARCHAR,       -- "technicalStatus": "Superstar",
  created_on DATE,                -- "createdOn": null,
  last_updated DATE,              -- "lastUpdated": null
)

CREATE TABLE report_batch (
  rb_id BIGSERIAL PRIMARY KEY,
  batch_id VARCHAR,              -- batchId
  rb_name VARCHAR,               -- name
  skill VARCHAR,                 -- skill
  rb_location VARCHAR,           -- location
  rb_type VARCHAR,               -- type
  good_grade SERIAL,             -- goodGrade
  passing_grade SERIAL,          -- passingGrade
  -- for some reason, I've seen test data with negative week numbers
  current_week INTEGER           -- currentWeek
  rb_start_date VARCHAR,         -- startDate
  rb_end_date VARCHAR,           -- endDate
);
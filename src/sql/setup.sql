DROP TABLE IF EXISTS report_batch, report_qc_note, report_employee, report_evaluation, report_on_assessment CASCADE;
DROP TABLE IF EXISTS associate_portfolio, employee_portfolio, associate, employee CASCADE;

create table associate(
  email varchar(75) UNIQUE,
  salesforceId varchar(10) primary key not null, 
  firstname varchar(20) not null,
  lastname varchar(20) not null,
  batch_id VARCHAR(10) not null
);

create table associate_portfolio(
  bio text,
  favorite_technologies text,
  preference varchar(15),
  salesforceId varchar(10) not null,
  foreign key (salesforceId)
  references associate(salesforceId)
);

create table employee (
  salesforceId varchar(10) primary key not null, 
  firstname varchar(20) not null,
  lastname varchar(20) not null,
  email varchar(40) UNIQUE,
  pswrd varchar(40)
);

create table employee_portfolio(
  bio text,
  technology text,
  trainer_location varchar(25),
  salesforceId varchar(10) not null,
  foreign key (salesforceId)
  references associate(salesforceId)
);

CREATE TABLE report_batch (
  rb_id BIGSERIAL PRIMARY KEY,
  batch_id VARCHAR UNIQUE,       -- batchId
  rb_name VARCHAR,               -- name
  skill VARCHAR,                 -- skill
  rb_location VARCHAR,           -- location
  rb_type VARCHAR,               -- type
  good_grade SERIAL,             -- goodGrade
  passing_grade SERIAL,          -- passingGrade
  -- for some reason, I've seen test data with negative week numbers
  current_week INTEGER,          -- currentWeek
  rb_start_date VARCHAR,         -- startDate
  rb_end_date VARCHAR            -- endDate
);

CREATE TABLE report_evaluation (
  grade_id BIGSERIAL PRIMARY KEY, -- gradeId
  date_received DATE,             -- dateReceived
  score DECIMAL,                  -- score
  re_id BIGSERIAL,                -- assessmentId note that this is different than the gradeId
  trainee_id VARCHAR              -- traineeId /mock/qa/notes/trainee/SF-2681
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
  last_updated DATE               -- "lastUpdated": null
);

-- https://caliber2-mock.revaturelabs.com/mock/evaluation/grades/reports/TR-1190/spider/mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com
CREATE TABLE report_on_assessment (
  grade_id        BIGSERIAL,    -- 
  batch_id        VARCHAR
    REFERENCES report_batch(batch_id),
  associate_id    VARCHAR(40)
    REFERENCES associate(email),
  assessment_type  VARCHAR(10), -- assessmentType
  score           INTEGER  
    CHECK (score >= 0),           -- score
  week            INTEGER
    CHECK (week > 0),             -- week
  grade_weight    INTEGER
    CHECK (grade_weight >= 0)     -- weight
);

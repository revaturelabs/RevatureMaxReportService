from src.model.assessment import Assessment
from src.dao import assessment_dao as dao
from src.config.db_config import get_local_connection
from test.data.test_assessment_data import assessments, batches, associates

from unittest import TestCase


class TestAssessmentGradesDAO(TestCase):
    def setUp(self):
        with get_local_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """TRUNCATE report_batch,
                    report_evaluation,
                    report_qc_note,
                    report_on_assessment,
                    associate CASCADE"""
                )
                for associate in associates:
                    cur.execute(
                        """INSERT INTO associate
                    VALUES (%s,%s,%s,%s,%s)""",
                        associate.to_tuple(),
                    )
                for batch in batches:
                    cur.execute(
                        """INSERT INTO report_batch
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                        batch.to_tuple(),
                    )
                for assess in assessments:
                    cur.execute(
                        """INSERT INTO report_on_assessment
                    VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                        assess.to_tuple(),
                    )
                conn.commit()

    def tearDown(self):
        with get_local_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """TRUNCATE report_batch,
                    report_evaluation,
                    report_qc_note,
                    report_on_assessment,
                    associate CASCADE"""
                )
                conn.commit()

    def test_create_existing(self):
        # def test_create_existing(grade_id, batch_id, email, assessment_type, score, week, grade_weight, cursor):
        examples = [
            Assessment(50, "EX-B01", "ex0001@example.com", "Score", 60, 1, 100),
            Assessment(51, "EX-B01", "ex0003@example.com", "Score", 60, 1, 100),
            Assessment(52, "EX-B01", "ex0005@example.com", "Score", 60, 1, 100),
        ]
        for ex in examples:
            dao.create_existing(*ex.to_tuple())

    def test_create_new(self):
        # def test_create_new(batch_id, email, assessment_type, score, week, grade_weight, cursor):
        examples = [
            Assessment(50, "EX-B01", "ex0001@example.com", "Score", 60, 1, 100),
            Assessment(51, "EX-B01", "ex0003@example.com", "Score", 60, 1, 100),
            Assessment(52, "EX-B01", "ex0005@example.com", "Score", 60, 1, 100),
        ]
        for ex in examples:
            dao.create_existing(*ex.to_tuple())

    def test_select_by_email_assessment_week(self):
        # def test_select_email_assessment_week(email, assessment_type, week, cursor):
        self.assertEqual(len(dao.select_by_email_assessment_week("ex0001@example.com", "Score", 1)), 2)

    def test_select_by_email_assessment(self):
        # def test_select_by_email_assessment(email, assessment_type, cursor):
        self.assertEqual(len(dao.select_by_email_assessment("ex0001@example.com", "Score")), 4)

    def test_select_by_email(self):
        # def test_select_by_email(email, cursor):
        self.assertEqual(len(dao.select_by_email_assessment("ex0001@example.com", "Score")), 4)

    def test_select_by_batch(self):
        # def test_select_by_batch(batch_id, cursor):
        self.assertEqual(len(dao.select_by_batch("EX-B01")), 20)

    def test_select_by_batch_assessment(self):
        # def test_select_by_batch_assessment(batch_id, assessment_type, cursor):
        self.assertEqual(len(dao.select_by_batch_assessment("EX-B01", "Score")), 20)

    def test_select_by_batch_max_grade(self):
        # def test_select_by_batch_max_grade(batch_id, max_grade, cursor):
        self.assertEqual(len(dao.select_by_batch_max_grade("EX-B01", 61)), 12)

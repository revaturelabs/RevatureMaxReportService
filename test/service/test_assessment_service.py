from unittest import TestCase, mock

from src.model.assessment import Assessment
from src.service import assessment_service as service
from test.data import test_assessment, test_associate, test_batch


def add_all(cursor):
    for associate in test_associate.associates:
        cursor.execute(
            """INSERT INTO associate
        VALUES (%s,%s,%s,%s,%s)""",
            associate.to_tuple(),
        )
    for batch in test_batch.batches:
        cursor.execute(
            """INSERT INTO report_batch
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            batch.to_tuple(),
        )
    for assess in test_assessment.assessments:
        cursor.execute(
            """INSERT INTO report_on_assessment
        VALUES (%s,%s,%s,%s,%s,%s,%s)""",
            assess.to_tuple(),
        )


def remove_all(cursor):
    try:
        cursor.execute("""DELETE FROM report_on_assessment WHERE batch_id LIKE 'EX%';""")
        cursor.execute("""DELETE FROM report_batch WHERE batch_id LIKE 'EX-B%';""")
        cursor.execute("""DELETE FROM associate WHERE salesforceid LIKE 'EX%';""")
    except Exception as e:
        print(e)


class TestAssessmentService(TestCase):
    @mock.patch("src.dao.assessment_dao.create_new")
    @mock.patch("src.dao.assessment_dao.create_existing")
    def test_create_assessment(self, m_create_existing, m_create_new):
        # create_assessment(assessment: Assessment):
        assessments = [
            Assessment(-1, "EX-B01", "ex0001@example.com", "Score", 60, 1, 100),
            Assessment(-1, "EX-B01", "ex0003@example.com", "Score", 60, 1, 100),
            Assessment(2, "EX-B01", "ex0005@example.com", "Score", 60, 1, 100),
        ]
        service.create_assessment(assessments[0])
        self.assertTrue(m_create_new.called)
        self.assertFalse(m_create_existing.called)

        service.create_assessment(assessments[1])
        self.assertGreater(m_create_new.call_count, 1)
        self.assertFalse(m_create_existing.called)

        service.create_assessment(assessments[2])
        self.assertTrue(m_create_existing.called)


    @mock.patch("src.dao.assessment_dao.select_by_email_assessment_week")
    def test_select_by_email_assessment_week(self, m_select):
        # select_by_email_assessment_week(associate_email, assessment_type, week):
        m_select.return_value = (tuple(),)
        result = service.select_by_email_assessment_week("", "word", 0)
        self.assertEqual(len(result), 0)

        m_select.return_value = ((0, "EX-B01", "ex0001@example.com", "Score", 60, 1, 100),)
        result = service.select_by_email_assessment_week("", "", 0)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Assessment)

    @mock.patch("src.dao.assessment_dao.select_by_email_assessment")
    def test_select_by_email_assessment(self, m_select):
        # select_by_email_assessment(associate_email, assessment_type):
        m_select.return_value = (tuple(),)
        result = service.select_by_email_assessment("", "")
        self.assertEqual(len(result), 0)

        m_select.return_value = ((0, "EX-B01", "ex0001@example.com", "Score", 60, 1, 100),)
        result = service.select_by_email_assessment("", "")
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Assessment)

    @mock.patch("src.dao.assessment_dao.select_by_email")
    def test_select_by_email(self, m_select):
        # select_by_email(associate_email):
        m_select.return_value = (tuple(),)
        result = service.select_by_email("")
        self.assertEqual(len(result), 0)

        m_select.return_value = ((0, "EX-B01", "ex0001@example.com", "Score", 60, 1, 100),)
        result = service.select_by_email("")
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Assessment)

    @mock.patch("src.dao.assessment_dao.select_by_batch")
    def test_select_by_batch(self, m_select):
        # select_by_batch(batch_id):
        m_select.return_value = (tuple(),)
        result = service.select_by_batch("")
        self.assertEqual(len(result), 0)

        m_select.return_value = ((0, "EX-B01", "ex0001@example.com", "Score", 60, 1, 100),)
        result = service.select_by_batch("")
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Assessment)

    @mock.patch("src.dao.assessment_dao.select_by_batch_assessment")
    def test_select_by_batch_assessment(self, m_select):
        # select_by_batch_assessment(batch_id, assessment_type):
        m_select.return_value = (tuple(),)
        result = service.select_by_batch_assessment("", "")
        self.assertEqual(len(result), 0)

        m_select.return_value = ((0, "EX-B01", "ex0001@example.com", "Score", 60, 1, 100),)
        result = service.select_by_batch_assessment("", "")
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Assessment)

    @mock.patch("src.dao.assessment_dao.select_by_batch_max_grade")
    def test_select_by_batch_max_grade(self, m_select):
        # select_by_batch_max_grade(batch_id, max_grade):
        m_select.return_value = (tuple(),)
        result = service.select_by_batch_max_grade("", 100)
        self.assertEqual(len(result), 0)

        m_select.return_value = ((0, "EX-B01", "ex0001@example.com", "Score", 60, 1, 100),)
        result = service.select_by_batch_max_grade("", 59)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Assessment)

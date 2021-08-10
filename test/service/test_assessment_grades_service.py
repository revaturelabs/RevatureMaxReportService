from test.data.test_assessment_data import assessments, batches, associates
from unittest import TestCase, mock


class TestAssessmentGradesService(TestCase):
    @mock.patch("src.dao.assessment_grades.create_new")
    @mock.patch("src.dao.assessment_grades.create_existing")
    def test_create_assessment(self, m_create_new, m_create_existing):
        # create_assessment(assessment: Assessment):
        pass

    @mock.patch("src.dao.assessment_grades.select_by_email_assessment_week")
    def test_select_by_email_assessment_week(self, m_select):
        # select_by_email_assessment_week(associate_email, assessment_type, week):
        pass

    @mock.patch("src.dao.assessment_grades.select_by_email_assessment")
    def test_select_by_email_assessment(self, m_select):
        # select_by_email_assessment(associate_email, assessment_type):
        pass

    @mock.patch("src.dao.assessment_grades.select_by_email")
    def test_select_by_email(self, m_select):
        # select_by_email(associate_email):
        pass

    @mock.patch("src.dao.assessment_grades.select_by_batch")
    def test_select_by_batch(self, m_select):
        # select_by_batch(batch_id):
        pass

    @mock.patch("src.dao.assessment_grades.select_by_batch_assessment")
    def test_select_by_batch_assessment(self, m_select):
        # select_by_batch_assessment(batch_id, assessment_type):
        pass
    
    @mock.patch("src.dao.assessment_grades.select_by_batch_max_grade")
    def test_select_by_batch_max_grade(self, m_select):
        # select_by_batch_max_grade(batch_id, max_grade):
        pass

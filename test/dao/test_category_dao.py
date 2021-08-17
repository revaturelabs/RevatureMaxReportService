from src.model.category import Category
from src.dao import category_dao as dao
from src.config.db_config import get_local_connection
from test.data import test_batch, test_associate, test_category

from unittest import TestCase


def remove_all(cursor):
    try:
        cursor.execute("""DELETE FROM report_on_category WHERE batch_id LIKE 'EX%';""")
        cursor.execute("""DELETE FROM report_batch WHERE batch_id LIKE 'EX-B%';""")
        cursor.execute("""DELETE FROM associate WHERE salesforceid LIKE 'EX%';""")
    except Exception as e:
        print(e)


class TestCategoryDAO(TestCase):
    def setUp(self):
        with get_local_connection() as conn:
            with conn.cursor() as cur:
                remove_all(cur)
                for associate in test_associate.associates:
                    cur.execute(
                        """INSERT INTO associate
                    VALUES (%s,%s,%s,%s,%s)""",
                        associate.to_tuple(),
                    )
                for batch in test_batch.batches:
                    cur.execute(
                        """INSERT INTO report_batch
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                        batch.to_tuple(),
                    )
                for category in test_category.categories:
                    cur.execute(
                        """INSERT INTO report_on_category
                    VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                        category.to_tuple(),
                    )
                conn.commit()

    def tearDown(self):
        with get_local_connection() as conn:
            with conn.cursor() as cur:
                remove_all(cur)
            conn.commit()

    def test_create_existing(self):
        # def test_create_existing(grade_id, batch_id, email, assessment_type, score, week, grade_weight, cursor):
        examples = [
            Category(50, "EX-B01", "ex0001@example.com", "Score", 60, 1, 100),
            Category(51, "EX-B01", "ex0003@example.com", "Score", 60, 1, 100),
            Category(52, "EX-B01", "ex0005@example.com", "Score", 60, 1, 100),
        ]
        for ex in examples:
            dao.create_existing(*ex.to_tuple())

    def test_create_new(self):
        # def test_create_new(batch_id, email, assessment_type, score, week, grade_weight, cursor):
        examples = [
            Category(50, "EX-B01", "ex0001@example.com", "Score", 60, 1, 100),
            Category(51, "EX-B01", "ex0003@example.com", "Score", 60, 1, 100),
            Category(52, "EX-B01", "ex0005@example.com", "Score", 60, 1, 100),
        ]
        for ex in examples:
            dao.create_existing(*ex.to_tuple())

    def test_select_by_email_category_week(self):
        # def test_select_email_assessment_week(email, assessment_type, week, cursor):
        self.assertEqual(len(dao.select_by_email_category_week("ex0001@example.com", "Quiz", 1)), 1)

    def test_select_by_email_category(self):
        # def test_select_by_email_assessment(email, assessment_type, cursor):
        self.assertEqual(len(dao.select_by_email_category("ex0001@example.com", "Quiz")), 2)
        self.assertEqual(len(dao.select_by_email_category("ex0003@example.com", "Exam")), 2)
        self.assertEqual(len(dao.select_by_email_category("ex0003@example.com", "Project")), 1)
        self.assertEqual(len(dao.select_by_email_category("ex0001@example.com", "Verbal")), 1)

    def test_select_by_email(self):
        # def test_select_by_email(email, cursor):
        self.assertEqual(len(dao.select_by_email("ex0001@example.com")), 4)

    def test_select_by_batch(self):
        # def test_select_by_batch(batch_id, cursor):
        self.assertEqual(len(dao.select_by_batch("EX-B01")), 20)

    def test_select_by_batch_averages(self):
        # select_by_batch_averages(batch_id, cursor):
        self.assertEqual(len(dao.select_by_batch_averages("EX-B01")), 15)

    def test_select_by_batch_assessment(self):
        # def test_select_by_batch_assessment(batch_id, assessment_type, cursor):
        self.assertEqual(len(dao.select_by_batch_assessment("EX-B01", "Quiz")), 2)

    def test_select_by_batch_max_grade(self):
        # def test_select_by_batch_max_grade(batch_id, max_grade, cursor):
        self.assertEqual(len(dao.select_by_batch_max_grade("EX-B01", 61)), 15)

    def test_select_all_categories(self):
        # select_all_categories(cursor)
        self.assertGreaterEqual(len(dao.select_all_categories()), 4)

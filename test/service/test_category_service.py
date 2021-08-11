from unittest import TestCase, mock

from src.model.category import Category
from src.service import category_service as service


class TestCategoryService(TestCase):
    @mock.patch("src.dao.category_dao.create_new")
    @mock.patch("src.dao.category_dao.create_existing")
    def test_create_category(self, m_create_existing, m_create_new):
        # def create_category(category: Category):
        categories = [
            Category(-1, "EX-B01", "ex0001@example.com", "Score", 60, 1, 100),
            Category(2, "EX-B01", "ex0005@example.com", "Score", 60, 1, 100),
        ]
        m_create_new.return_value = categories[0].to_tuple()
        service.create_category(categories[0])
        self.assertTrue(m_create_new.called)

        m_create_existing.return_value = categories[1].to_tuple()
        service.create_category(categories[1])
        self.assertTrue(m_create_existing.called)

    @mock.patch("src.dao.category_dao.select_by_email_category_week")
    def test_select_by_email_category_week(self, m_select):
        # def select_by_email_category_week(associate_email, category_type, week):
        m_select.return_value = [
            (0, "EX-B01", "ex0001@example.com", "Verbal", 10, 1, 100)
        ]
        result = service.select_by_email_category_week("", "", -1)
        self.assertIsInstance(result[0], Category)

    @mock.patch("src.dao.category_dao.select_by_email_category")
    def test_select_by_email_category(self, m_select):
        # def select_by_email_category(associate_email, category_type):
        m_select.return_value = [
            (0, "EX-B01", "ex0001@example.com", "Verbal", 10, 1, 100)
        ]
        result = service.select_by_email_category("", "")
        self.assertIsInstance(result[0], Category)

    @mock.patch("src.dao.category_dao.select_by_email")
    def test_select_by_email(self, m_select):
        # def select_by_email(associate_email):
        m_select.return_value = [
            (0, "EX-B01", "ex0001@example.com", "Verbal", 10, 1, 100)
        ]
        result = service.select_by_email("")
        self.assertIsInstance(result[0], Category)

    @mock.patch("src.dao.category_dao.select_by_batch")
    def test_select_by_batch(self, m_select):
        # def select_by_batch(batch_id):
        m_select.return_value = [
            (0, "EX-B01", "ex0001@example.com", "Verbal", 10, 1, 100)
        ]
        result = service.select_by_batch("")
        self.assertIsInstance(result[0], Category)

    @mock.patch("src.dao.category_dao.select_all_categories")
    def test_select_all_categories(self, m_select):
        # def select_all_categories():
        m_select.return_value = [("Verbal",), ("Exam",), ("Project",), ("Quiz",)]
        result = service.select_all_categories()
        self.assertGreater(len(result), 3)

    @mock.patch("src.dao.category_dao.select_by_batch_category")
    def test_select_by_batch_category(self, m_select):
        # def select_by_batch_category(batch_id, category_type):
        m_select.return_value = [
            (0, "EX-B01", "ex0001@example.com", "Verbal", 10, 1, 100)
        ]
        result = service.select_by_batch_category("", "")
        self.assertIsInstance(result[0], Category)

    @mock.patch("src.dao.category_dao.select_by_batch_max_grade")
    def test_select_by_batch_max_grade(self, m_select):
        # def select_by_batch_max_grade(batch_id, max_grade):
        m_select.return_value = [
            (0, "EX-B01", "ex0001@example.com", "Verbal", 10, 1, 100)
        ]
        result = service.select_by_batch_max_grade("", 71)
        self.assertIsInstance(result[0], Category)

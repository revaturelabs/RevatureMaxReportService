from test.data.test_compare_batch_data import batches, batch_grades, spider_weeks
from unittest import TestCase, mock

class TestCompareBatchService(TestCase):
    @mock.patch("src.dao.compare_batch_dao.get_batch_by_id")
    def test_get_batch_by_id(self, m_select):
        pass

    @mock.patch("src.dao.compare_batch_dao.get_batches_with_same_skill")
    def test_get_batches_same_skill(self, m_select):
        pass

    @mock.patch("src.dao.compare_batch_dao.batch_total_avg")
    def test_batch_total_avg(self, m_select):
        pass

    @mock.patch("src.dao.compare_batch_dao.batch_weekly_avg")
    def test_batch_weekly_avg(self, m_select):
        pass
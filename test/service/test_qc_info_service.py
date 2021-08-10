import unittest
from unittest.mock import Mock
import src.dao.qc_dao as dao
import src.service.qc_service as service


class qc_info_service_test(unittest.TestCase):
    def setUp(self):
        dao.select_qc_info_by_associate_id = Mock(
            return_value=[('This is a Qc note on week 1', 1, 'Superstar', 'TR-1145')])
        dao.select_qc_batch_average_by_week = Mock(return_value=('Average',))

    def test_get_qc_info_trainee(self):
        self.assertEqual(service.get_qc_info_trainee('SF-2274')[1]['score'], 'Superstar')
        self.assertEqual(service.get_qc_info_trainee('SF-2274')[1]['average'], 'Average')

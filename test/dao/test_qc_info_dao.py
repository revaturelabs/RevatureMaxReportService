from src.config.db_config import get_local_connection
from src.dao import qc_dao as dao
import unittest


class qc_info_dao_test(unittest.TestCase):

    def setUp(self):
        with get_local_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """DELETE FROM report_qc_note WHERE note_id = 1337"""
                )
                cur.execute(
                    """DELETE FROM report_qc_batch_note WHERE note_id = 1337"""
                )

                cur.execute("""INSERT INTO report_qc_note VALUES ('1337', 'this is a test', '1', 'TR-404', 'SF-420', 
                'QC-User', 'QC-TRAINEE', 'Superstar', NULL, NULL)""")

                cur.execute("""INSERT INTO report_qc_batch_note VALUES ('1337', 'this is a test', '1', 'TR-404', 'SF-420', 
                                'QC-User', 'QC-TRAINEE', 'Superstar', NULL, NULL)""")

    def tearDown(self):
        with get_local_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """DELETE FROM report_qc_note WHERE note_id = 1337"""
                )
                cur.execute(
                    """DELETE FROM report_qc_batch_note WHERE note_id = 1337"""
                )

    def test_select_qc_info_by_associate_id(self):
        result = dao.select_qc_info_by_associate_id('SF-420')
        self.assertEquals(result[0][2], 'Superstar')

    def test_select_qc_batch_average_by_week(self):
        self.assertEquals(dao.select_qc_batch_average_by_week('TR-404', 1)[0], 'Superstar')

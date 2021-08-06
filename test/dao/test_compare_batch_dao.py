from src.dao import compare_batch_dao as dao
from src.config.db_config import get_local_connection
from test.data.test_compare_batch_data import batches
from unittest import TestCase

class TestCompareBatchDAO(TestCase):
    def setUp(self):
        with get_local_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    TRUNCATE report_batch
                    CASCADE
                """)
                for batch in batches:
                    cur.execute("""
                        INSERT INTO report_batch VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """, batch.to_tuple())
                conn.commit()

    def test_get_batch_by_id(self):
        skill, date = dao.get_batch_by_id("TR-1145", productionDB=False)
        with get_local_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT skill, startdate FROM report_batch WHERE batchid = 'TR-1145'""")
                actual_skill, actual_date = cur.fetchone()
        self.assertEqual(skill, actual_skill)
        self.assertEqual(date, actual_date)

    def test_get_batches_same_skill(self):
        with get_local_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT batchid FROM report_batch WHERE skill = 'PEGA' AND '2021-05-28' > startdate""")
                batch_id, = cur.fetchone()
        self.assertEqual(batch_id, "TR-1140")



    def tearDown(self):
        with get_local_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""TRUNCATE report_batch CASCADE""")
                conn.commit()
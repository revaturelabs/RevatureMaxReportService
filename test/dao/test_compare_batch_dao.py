import datetime

from src.dao import compare_batch_dao as dao
from src.config.db_config import get_local_connection
from test.data.test_compare_batch_data import batches, batch_grades, spider_weeks
from unittest import TestCase

class TestCompareBatchDAO(TestCase):
    def setUp(self):
        with get_local_connection() as conn:
            with conn.cursor() as cur:
                cur.execute('DELETE FROM report_on_assessment CASCADE')
                cur.execute("""
                    DELETE FROM report_batch CASCADE
                """)
                cur.execute('DELETE FROM batch_grades CASCADE')

                for batch in batches:
                    cur.execute("""
                        INSERT INTO report_batch VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """, (batch.rb_id, batch.batch_id, batch.rb_name, batch.rb_start_date, batch.rb_end_date, batch.skill,
                                batch.rb_location, batch.rb_type, batch.good_grade, batch.passing_grade, batch.current_week))

                for grade in batch_grades:
                    cur.execute("""INSERT INTO batch_grades
                        VALUES(%s, %s, %s)
                    """, grade.to_tuple())

                for week in spider_weeks:
                    cur.execute("""INSERT INTO report_on_assessment
                        VALUES(%s, %s, %s, %s, %s, %s, %s)
                    """, week.to_tuple())
                conn.commit()

    def test_get_batch_by_id(self):
        skill, date = dao.get_batch_by_id("TR-1145", productionDB=False)
        with get_local_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT skill, rb_start_date FROM report_batch WHERE batch_id = 'TR-1145'""")
                actual_skill, actual_date = cur.fetchone()
        self.assertEqual(skill, actual_skill)
        self.assertEqual(date, actual_date)

    def test_get_batches_same_skill(self):
        test_batch_ids = dao.get_batches_with_same_skill("PEGA", "2021-05-28", productionDB=False)
        with get_local_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT batch_id FROM report_batch WHERE skill = 'PEGA' AND '2021-05-28' > rb_start_date""")
                actual_batch_ids = cur.fetchall()
        self.assertCountEqual(actual_batch_ids, test_batch_ids)

    def test_batch_total_avg(self):
        test_average = dao.batch_total_avg("TR-1140", productionDB=False)
        with get_local_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT SUM(average)/ COUNT(average) FROM batch_grades WHERE batch_id = 'TR-1140'""")
                average, = cur.fetchone()
        self.assertEqual(test_average[0], average)

    def test_batch_weekly_avg(self):
        test_weekly_avg = dao.batch_weekly_avg("TR-1140", 1, productionDB=False)
        with get_local_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT SUM(score)/COUNT(score) FROM report_on_assessment 
                WHERE batch_id = 'TR-1140' AND week = 1""")
                average, = cur.fetchone()
        self.assertEqual(test_weekly_avg[0], average)

    def tearDown(self):
        with get_local_connection() as conn:
            with conn.cursor() as cur:
                cur.execute('DELETE FROM report_on_assessment CASCADE')
                cur.execute("""
                                    DELETE FROM report_batch CASCADE
                                """)
                cur.execute('DELETE FROM batch_grades CASCADE')
                conn.commit()
from unittest import mock, TestCase
from src.util.self_comparison import (
    batch_averages_by_week,
    score_report_by_week
)
from json import loads


class TestSelfComparison(TestCase):
    @mock.patch("src.util.self_comparison.fetch_json")
    def test_batch_averages_by_week(self, m_fetch):
        with open("test/route/caliber_data/reports_TR-1190_spider.json") as spider_json:
            m_fetch.return_value = loads(spider_json.read())
            result = batch_averages_by_week("TR-1190")
            self.assertEqual(len(result["data"]["Batch Averages"]), 22)
            self.assertEqual(len(result["chartData"]["Batch Average Score"]), 22)

    @mock.patch("src.util.self_comparison.fetch_json")
    def test_score_report_by_week(self, m_fetch):
        with open("test/route/caliber_data/reports_TR-1190_spider_mock8.json") as spider_json:
            m_fetch.return_value = loads(spider_json.read())
            result = score_report_by_week("TR-1190", "mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com")
            self.assertEqual(len(result["data"]), 5)
            self.assertEqual(len(result["chartData"]), 2)

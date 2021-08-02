from unittest import TestCase
from unittest.mock import Mock
from src.util.fetch import fetch_json
from src.route.compare_batch import compareBatchToPastBatches, compareBatchToOtherBatch

class TestCompareBatchRoute(TestCase):
    def setUp(self):
        self.URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"
        self.batch_id = "TR-1145"
        self.batch_url = self.URL_BASE + "training/batch/" + self.batch_id
        self.other_batch_id = "TR-1140"
        self.other_batch_url = self.URL_BASE + "training/batch/" + self.other_batch_id
        pass
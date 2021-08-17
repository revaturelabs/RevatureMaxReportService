import unittest
from unittest import mock
from unittest.mock import Mock
import src.route.trainer_associate_grades_view as trainer_view

import src.util.fetch as fetch



class getTraineeDataTest(unittest.TestCase):
    # mocking the fetch_json to return mock data that we can use to verify
    # that our function is working
    def setUp(self):
        trainer_view.fetch_json = Mock(return_value={
        "restOfBatchGrades": {
          "Exam": 56.13589212473701,
          "Other": 43.95712546741261,
          "Presentation": 58.89518950967228,
          "Project": 61.2712664604187,
          "Verbal": 52.09569162480972
        },
        "traineeGrades": {
          "Exam": 69,
          "Other": 73,
          "Presentation": 88,
          "Project": 2,
          "Verbal": 70
        }
        })
    def test_get_trainee_data_type(self):
        self.assertIsInstance(trainer_view.getTraineeData('mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com'), dict)
    def test_get_trainee_data_return(self):
        self.assertEqual(trainer_view.getTraineeData('mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com')['associateGrades']['Exam'], 69)
    def test_get_trainee_data_length(self):
        self.assertGreater(len(trainer_view.getTraineeData('mock8.associatef4c8d0c5-ecaf-4127-a459-7bf3617118a6@mock.com')), 0)



from src.model.batch import Batch
from src.model.batch_grade import BatchGrade
from src.model.spider_week import SpiderWeek

batches = [
    Batch(69, "TR-1140", "Mock Batch 69", "PEGA", "Savannah", "Type", 90, 100, -13, "2021-05-14", "2021-07-23"),
    Batch(70, "TR-1145", "Mock Batch 70", "PEGA", "Savannah", "Type", 90, 100, -13, "2021-05-28", "2021-08-06"),
    Batch(71, "TR-1072", "Mock Batch 71", "PEGA", "Savannah", "Type", 90, 100, -13, "2020-05-14", "2020-07-23"),
    Batch(72, "TR-1021", "Mock Batch 72", "PEGA", "Savannah", "Type", 90, 100, -13, "2021-04-14", "2021-06-23")
]

batch_grades = [
    BatchGrade("name", 60, "TR-1140"),
    BatchGrade("name", 50, "TR-1140")
]

spider_weeks = [
    SpiderWeek(0, "TR-1140", None, "type", 60, 1, 100),
    SpiderWeek(1, "TR-1140", None, "type", 50, 1, 100),
]
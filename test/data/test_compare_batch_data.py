from src.model.batch import Batch
from src.model.batch_grade import BatchGrade
from src.model.spider_week import SpiderWeek

batches = [
    Batch(69, "TR-1140", "Mock Batch 69", "PEGA", "Savannah", "Type", 90, 100, -13, "2021-05-14", "2021-07-23"),
    Batch(70, "TR-1145", "Mock Batch 70", "PEGA", "Savannah", "Type", 90, 100, -13, "2021-05-28", "2021-08-06")
]

batch_grades = [
    BatchGrade("name", 60, "TR-1140"),
    BatchGrade("name", 50, "TR-1140")
]

spider_weeks = [
    SpiderWeek(0, "TR-1140", None, "type", 60, 1, 100),
    SpiderWeek(1, "TR-1140", None, "type", 50, 1, 100),
]
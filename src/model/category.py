from dataclasses import dataclass


@dataclass
class Category:
    grade_id: int
    batch_id: str
    email: str
    category: str
    score: int
    week: int
    grade_weight: int

    def to_tuple(self):
        return (
            self.grade_id,
            self.batch_id,
            self.email,
            self.category,
            self.score,
            self.week,
            self.grade_weight,
        )

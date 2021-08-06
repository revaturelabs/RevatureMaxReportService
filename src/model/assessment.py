class Assessment:
    def __init__(
        self,
        grade_id,
        batch_id,
        associate_id,
        assessment_type,
        score,
        week,
        grade_weight,
    ):
        self.grade_id = grade_id
        self.batch_id = batch_id
        self.associate_id = associate_id
        self.assessment_type = assessment_type
        self.score = score
        self.week = week
        self.grade_weight = grade_weight

    def __repr__(self):
        return "Assessment(%s, %s, %s, %s, %s, %s, %s)" % (
            self.grade_id,
            self.batch_id,
            self.associate_id,
            self.assessment_type,
            self.score,
            self.week,
            self.grade_weight,
        )

    def to_tuple(self):
        return (
            self.grade_id,
            self.batch_id,
            self.associate_id,
            self.assessment_type,
            self.score,
            self.week,
            self.grade_weight,
        )

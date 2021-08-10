class SpiderWeek:
    def __init__(self, grade_id, trainee_id, associate_id, type, score, week, weight):
        self.grade_id = grade_id
        self.trainee_id = trainee_id
        self.associate_id = associate_id
        self.type = type
        self.score = score
        self.week = week
        self.weight = weight

    def __repr__(self):
        return "SpiderWeek(%s, %s, %s, %s, %s, %s, %s)" % (
            self.grade_id,
            self.trainee_id,
            self.associate_id,
            self.type,
            self.score,
            self.week,
            self.weight
        )

    def to_tuple(self):
        return (
            self.grade_id,
            self.trainee_id,
            self.associate_id,
            self.type,
            self.score,
            self.week,
            self.weight
        )
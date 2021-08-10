class BatchGrade():
    def __init__(self, name, average, batch_id):
        self.name = name
        self.average = average
        self.batch_id = batch_id

    def __repr__(self):
        return "BatchGrade(%s, %s, %s)" % (
            self.name,
            self.average,
            self.batch_id
        )

    def to_tuple(self):
        return (
            self.name,
            self.average,
            self.batch_id
        )
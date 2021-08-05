class Batch:
    def __init__(
        self,
        rb_id,
        batch_id,
        rb_name,
        skill,
        rb_location,
        rb_type,
        good_grade,
        passing_grade,
        current_week,
        rb_start_date,
        rb_end_date,
    ):
        self.rb_id = rb_id
        self.batch_id = batch_id
        self.rb_name = rb_name
        self.skill = skill
        self.rb_location = rb_location
        self.rb_type = rb_type
        self.good_grade = good_grade
        self.passing_grade = passing_grade
        self.current_week = current_week
        self.rb_start_date = rb_start_date
        self.rb_end_date = rb_end_date

    def __repr__(self):
        return "Batch(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (
            self.rb_id,
            self.batch_id,
            self.rb_name,
            self.skill,
            self.rb_location,
            self.rb_type,
            self.good_grade,
            self.passing_grade,
            self.current_week,
            self.rb_start_date,
            self.rb_end_date,
        )

    def to_tuple(self):
        return (
            self.rb_id,
            self.batch_id,
            self.rb_name,
            self.skill,
            self.rb_location,
            self.rb_type,
            self.good_grade,
            self.passing_grade,
            self.current_week,
            self.rb_start_date,
            self.rb_end_date,
        )

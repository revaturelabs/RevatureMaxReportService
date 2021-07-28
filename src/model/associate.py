class Associate:
    def __init__(self, re_id, rr_role_id, rb_id, email, first_name, last_name, associate_id, flag):
        self.re_id = re_id
        self.rr_role_id = rr_role_id
        self.rb_id = rb_id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.associate_id = associate_id
        self.flag = flag

    def __repr__(self):
        return """{re_id: %d, rr_role_id: %d, rb_id: %d,
            email: %s, first_name: %s, last_name: %s,
            associate_id: %s, flag: %s}""" % (
            self.re_id, self.rr_role_id, self.rb_id,
            self.email, self.first_name,
            self.last_name, self.associate_id, self.flag
        )

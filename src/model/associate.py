class Associate:
    def __init__(self, email, salesforceId, firstname, lastname, batch_id):
        self.email = email
        self.salesforceId = salesforceId
        self.firstname = firstname
        self.lastname = lastname
        self.batch_id = batch_id

    def __repr__(self):
        return "Associate(%s, %s, %s, %s, %s)" % (
            self.email,
            self.salesforceId,
            self.firstname,
            self.lastname,
            self.batch_id
        )

    def to_tuple(self):
        return (
            self.email,
            self.salesforceId,
            self.firstname,
            self.lastname,
            self.batch_id
        )

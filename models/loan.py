class Loan:
    def __init__(self, client, duration, interest_rate, status):
        self.client = client
        self.duration = duration
        self.interest_rate = interest_rate
        self.status = status
        self.loan_date = None

    def approve(self):
        self.status = "Approved"
        return

    def reject(self):
        self.status = "Rejected"
        return

    def checking(self):
        if ((self.client.get_annual_income() >= 20000) and (self.client.get_loan_amount() < 19000)):
            self.approve()
        else:
            self.reject()


    def get_status(self):
        return self.status

    def get_amount(self):
        return self.client.get_loan_amount()

    def get_duration(self):
        return self.duration

    def get_interest_rate(self):
        return self.interest_rate

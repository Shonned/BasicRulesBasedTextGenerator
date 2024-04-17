class Loan:
    def __init__(self, client, duration, interest_rate, status):
        self.client = client
        self.duration = duration
        self.interest_rate = interest_rate
        self.status = status
        self.message = None
        self.loan_date = None

    def approve(self):
        self.status = "Approved"
        return self.message

    def reject(self):
        self.status = "Rejected"
        return self.message

    def checking(self):
        if self.client.get_annual_income() < 20000:
            self.reject()
            self.message = "Your annual income is insufficient for any loan amount."
        elif self.client.get_loan_amount() > self.client.get_annual_income() * 0.95:
            self.reject()
            self.message = "The loan amount exceeds the maximum limit of 95% of your annual income."
        else:
            self.message = "Your loan amount has been approved."
            self.approve()


    def get_status(self):
        return self.status

    def get_amount(self):
        return self.client.get_loan_amount()

    def get_duration(self):
        return self.duration

    def get_interest_rate(self):
        return self.interest_rate

    def get_message(self):
        return self.message
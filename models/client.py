from models.user import User


class Client(User):
    def __init__(self, client_id, name, address, phone, employment_status):
        super().__init__(client_id, name, address, phone)
        self.employment_status = employment_status
        self.annual_income = None
        self.loan_amount = None

    def submit_loan_request(self, loan):
        pass

    def get_request_status(self):
        pass

    def get_annual_income(self):
        return self.annual_income

    def get_employment_status(self):
        return self.employment_status

    def get_loan_amount(self):
        return self.loan_amount

    def set_annual_income(self, annual_income):
        self.annual_income = annual_income

    def set_loan_amount(self, loan_amount):
        self.loan_amount = loan_amount

    def set_employment_status(self, employment_status):
        self.employment_status = employment_status

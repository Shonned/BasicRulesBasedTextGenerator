import time

from models.loan import Loan
from models.user import User
import spacy

# Load the model
nlp = spacy.load("en_core_web_sm")


class Advisor(User):
    def __init__(self, advisor_id, name, address, phone, specialization):
        super().__init__(advisor_id, name, address, phone)
        self.specialization = specialization
        self.clients = []

    def add_client(self, client):
        self.clients.append(client)
        print("Hello " + client.get_name() + " I'm " + self.get_name() + " and we will study your loan request.\n")
        time.sleep(3)

    def remove_client(self, client):
        self.clients.remove(client)

    def get_clients(self):
        return self.clients

    def ask_for_loan_amount(self, client):
        loan_amount = input("How much loan do you want? ")
        loan_amount = self.extract_int_with_nlp(loan_amount)
        client.set_loan_amount(loan_amount)
        print("You asking for", loan_amount, "£\n")
        time.sleep(3)

    def ask_for_annual_income(self, client):
        annual_income = input("What is your annual income? ")
        annual_income = self.extract_int_with_nlp(annual_income)
        client.set_annual_income(annual_income)
        print("Your annual income is", annual_income, "£\n")
        time.sleep(3)

    def create_loan(self, client):
        loan = Loan(client, "10 years", "3.3%", "Pending")
        loan.checking()
        time.sleep(3)
        print(loan.get_message())
        print("Thank you for trusting Bank of Aberdeen")

    def extract_int_with_nlp(self, input_text):
        doc = nlp(input_text)
        for token in doc:
            if token.like_num:
                return int(token.text)
        print("I couldn't understand the number. Please enter a valid number.")
        return None

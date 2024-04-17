from models.advisor import Advisor
from models.bank import Bank
from models.client import Client


def main():
    bank_of_aberdeen = Bank("Bank of Aberdeen", "123 Main Street")

    advisor1 = Advisor("ADV001", "John Doe", "456 Oak Avenue", "555-1234", "Investment")
    advisor2 = Advisor("ADV002", "Jane Smith", "789 Elm Street", "555-5678", "Mortgage")
    bank_of_aberdeen.add_advisor(advisor1)
    bank_of_aberdeen.add_advisor(advisor2)

    client1 = Client("CLI001", "Kilian PEYRON", "100 Hillview Rd, AB14 0UB Peterculter", "+33782647212", "employee")
    bank_of_aberdeen.add_client(client1)

    # Notify the client
    bank_of_aberdeen.new_arrival(client1)
    advisor1.add_client(client1)

    advisor1.ask_for_annual_income(client1)
    advisor1.ask_for_loan_amount(client1)
    advisor1.create_loan(client1)


if __name__ == "__main__":
    main()
